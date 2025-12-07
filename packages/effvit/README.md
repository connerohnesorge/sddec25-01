# EffVit

EfficientViT model for semantic segmentation.

This package provides a lightweight, modular implementation of the TinyEfficientViT architecture
designed for efficient semantic segmentation tasks with minimal parameters (<10k).

## Installation

```bash
pip install -e .
```

## Usage

```python
from effvit import TinyEfficientViTSeg

# Create model for binary segmentation
model = TinyEfficientViTSeg(
    in_channels=1,
    num_classes=2,
)

# Forward pass
output = model(input_tensor)  # [B, num_classes, H, W]
```

## Architecture

The package is organized into the following modules:

- `layers.py` - Basic building blocks (TinyConvNorm, TinyPatchEmbedding, TinyMLP)
- `attention.py` - Attention mechanisms (TinyCascadedGroupAttention, TinyLocalWindowAttention)
- `encoder.py` - Encoder components (TinyEfficientVitBlock, TinyEfficientVitStage, TinyEfficientVitEncoder)
- `decoder.py` - Segmentation decoder (TinySegmentationDecoder)
- `model.py` - Complete model (TinyEfficientViTSeg)
