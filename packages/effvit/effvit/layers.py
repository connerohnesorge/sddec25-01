"""
Basic building block layers for TinyEfficientViT.

This module contains the fundamental layers used throughout the architecture:
- TinyConvNorm: Convolution + BatchNorm layer
- TinyPatchEmbedding: Lightweight patch embedding with stride 4
- TinyMLP: Simple MLP with expansion ratio
"""

import torch
import torch.nn as nn


class TinyConvNorm(nn.Module):
    """Convolution + BatchNorm layer (parameter-efficient)."""

    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size=3,
        stride=1,
        padding=1,
        groups=1,
        bias=False,
    ):
        super().__init__()
        self.conv = nn.Conv2d(
            in_channels,
            out_channels,
            kernel_size=kernel_size,
            stride=stride,
            padding=padding,
            groups=groups,
            bias=bias,
        )
        self.bn = nn.BatchNorm2d(out_channels)

    def forward(self, x):
        return self.bn(self.conv(x))


class TinyPatchEmbedding(nn.Module):
    """
    Lightweight patch embedding with 2 conv layers and stride 4.
    Reduces spatial resolution by 4x while embedding to initial dim.
    """

    def __init__(self, in_channels=1, embed_dim=8):
        super().__init__()
        mid_dim = embed_dim // 2 if embed_dim >= 4 else 2
        self.conv1 = TinyConvNorm(
            in_channels,
            mid_dim,
            kernel_size=3,
            stride=2,
            padding=1,
        )
        self.act1 = nn.GELU()
        self.conv2 = TinyConvNorm(
            mid_dim,
            embed_dim,
            kernel_size=3,
            stride=2,
            padding=1,
        )
        self.act2 = nn.GELU()

    def forward(self, x):
        x = self.act1(self.conv1(x))
        x = self.act2(self.conv2(x))
        return x


class TinyMLP(nn.Module):
    """Tiny MLP with expansion ratio."""

    def __init__(self, dim, expansion_ratio=2):
        super().__init__()
        hidden_dim = int(dim * expansion_ratio)
        self.fc1 = nn.Linear(dim, hidden_dim)
        self.act = nn.GELU()
        self.fc2 = nn.Linear(hidden_dim, dim)

    def forward(self, x):
        return self.fc2(self.act(self.fc1(x)))
