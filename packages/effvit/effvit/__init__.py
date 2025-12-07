"""
EffVit - EfficientViT model for semantic segmentation.

This package provides a lightweight, modular implementation of the TinyEfficientViT
architecture designed for efficient semantic segmentation tasks.
"""

from .layers import TinyConvNorm, TinyPatchEmbedding, TinyMLP
from .attention import TinyCascadedGroupAttention, TinyLocalWindowAttention
from .encoder import TinyEfficientVitBlock, TinyEfficientVitStage, TinyEfficientVitEncoder
from .decoder import TinySegmentationDecoder
from .model import TinyEfficientViTSeg

__all__ = [
    "TinyConvNorm",
    "TinyPatchEmbedding",
    "TinyMLP",
    "TinyCascadedGroupAttention",
    "TinyLocalWindowAttention",
    "TinyEfficientVitBlock",
    "TinyEfficientVitStage",
    "TinyEfficientVitEncoder",
    "TinySegmentationDecoder",
    "TinyEfficientViTSeg",
]
