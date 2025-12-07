"""
Attention mechanisms for TinyEfficientViT.

This module contains the attention layers:
- TinyCascadedGroupAttention: Efficient multi-head attention with cascaded groups
- TinyLocalWindowAttention: Window-based local attention wrapper
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class TinyCascadedGroupAttention(nn.Module):
    """
    Tiny version of Cascaded Group Attention.
    Uses minimal heads and key dimensions for efficiency.
    """

    def __init__(
        self,
        dim,
        num_heads=1,
        key_dim=4,
        attn_ratio=2,
    ):
        super().__init__()
        self.num_heads = num_heads
        self.key_dim = key_dim
        self.scale = key_dim**-0.5
        self.d = int(attn_ratio * key_dim)
        self.attn_ratio = attn_ratio

        qkv_dim = (num_heads * key_dim * 2) + (num_heads * self.d)
        self.qkv = nn.Linear(dim, qkv_dim)
        self.proj = nn.Linear(num_heads * self.d, dim)

    def forward(self, x):
        B, N, C = x.shape
        qkv = self.qkv(x)

        q_total = self.num_heads * self.key_dim
        k_total = self.num_heads * self.key_dim
        v_total = self.num_heads * self.d

        q = (
            qkv[:, :, :q_total]
            .reshape(B, N, self.num_heads, self.key_dim)
            .permute(0, 2, 1, 3)
        )
        k = (
            qkv[:, :, q_total : q_total + k_total]
            .reshape(B, N, self.num_heads, self.key_dim)
            .permute(0, 2, 1, 3)
        )
        v = (
            qkv[:, :, q_total + k_total :]
            .reshape(B, N, self.num_heads, self.d)
            .permute(0, 2, 1, 3)
        )

        attn = (q @ k.transpose(-2, -1)) * self.scale
        attn = attn.softmax(dim=-1)
        x = (attn @ v).transpose(1, 2).reshape(B, N, self.num_heads * self.d)
        x = self.proj(x)
        return x


class TinyLocalWindowAttention(nn.Module):
    """
    Local window attention wrapper.
    Partitions input into windows and applies attention within each window.
    """

    def __init__(
        self,
        dim,
        num_heads=1,
        key_dim=4,
        attn_ratio=2,
        window_size=7,
    ):
        super().__init__()
        self.window_size = window_size
        self.attn = TinyCascadedGroupAttention(
            dim=dim,
            num_heads=num_heads,
            key_dim=key_dim,
            attn_ratio=attn_ratio,
        )

    def forward(self, x):
        B, C, H, W = x.shape
        ws = self.window_size

        pad_h = (ws - H % ws) % ws
        pad_w = (ws - W % ws) % ws
        if pad_h > 0 or pad_w > 0:
            x = F.pad(x, (0, pad_w, 0, pad_h))
        _, _, Hp, Wp = x.shape

        x = x.view(B, C, Hp // ws, ws, Wp // ws, ws)
        x = x.permute(0, 2, 4, 3, 5, 1).contiguous()
        x = x.view(B * (Hp // ws) * (Wp // ws), ws * ws, C)

        x = self.attn(x)

        x = x.view(B, Hp // ws, Wp // ws, ws, ws, C)
        x = x.permute(0, 5, 1, 3, 2, 4).contiguous()
        x = x.view(B, C, Hp, Wp)

        if pad_h > 0 or pad_w > 0:
            x = x[:, :, :H, :W]

        return x
