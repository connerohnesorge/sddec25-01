# VisionAssist Training

Training scripts for the TinyEfficientViT semantic segmentation and ellipse regression models used in the VisionAssist project.

## Usage

```bash
uv run train_efficientvit.py      # Modal cloud training
python train_efficientvit_local.py # Local training
python train_ellipse_local.py      # Ellipse regression training
```

This runs the training on Modal with GPU acceleration or locally.

## Dataset Precomputation

The `precompute.py` script downloads the raw OpenEDS dataset from Kaggle, applies all deterministic preprocessing, and pushes to HuggingFace. This eliminates CPU-bound preprocessing during training for faster iteration.

### Prerequisites

**Kaggle API credentials:**
1. Go to https://www.kaggle.com/settings
2. Click "Create New API Token" to download `kaggle.json`
3. Place `kaggle.json` in `~/.kaggle/kaggle.json`
4. Set permissions: `chmod 600 ~/.kaggle/kaggle.json`

**HuggingFace authentication (for push):**
```bash
huggingface-cli login
```

### Usage

**Full preprocessing and push to HuggingFace:**
```bash
python precompute.py --hf-repo Conner/sddec25-01
```

**Local preprocessing only (no HuggingFace push):**
```bash
python precompute.py --no-push --output-dir ./my_dataset
```

**Validate existing dataset:**
```bash
python precompute.py --validate --hf-repo Conner/sddec25-01
```

**Skip Kaggle download (use existing files):**
```bash
python precompute.py --skip-download --output-dir ./existing_data
```

### CLI Options

| Option | Default | Description |
|--------|---------|-------------|
| `--hf-repo` | `Conner/sddec25-01` | HuggingFace repo to push to |
| `--output-dir` | `./precompute_output` | Local directory for intermediate files |
| `--no-push` | - | Skip pushing to HuggingFace |
| `--validate` | - | Validate existing dataset preprocessing |
| `--skip-download` | - | Skip Kaggle download (use existing files) |

### Preprocessing Pipeline

1. **Download**: Fetches OpenEDS train/validation from Kaggle (`soumicksarker/openeds-dataset`)
2. **Label binarization**: Converts 4-class labels to binary (0=background, 1=pupil)
3. **Skip empty masks**: Excludes samples with no pupil pixels
4. **Gamma correction**: Applies LUT with gamma=0.8
5. **CLAHE**: Adaptive histogram equalization (clipLimit=1.5, tileGridSize=8x8)
6. **Ellipse extraction**: Fits ellipse to pupil contour using cv2.fitEllipse
7. **Spatial weights**: Computes boundary weights using morphological gradient
8. **Distance maps**: Signed distance transform per class (normalized)
9. **Push**: Uploads to HuggingFace with chunked parquet upload

### Output Schema

The preprocessed HuggingFace dataset (`Conner/sddec25-01`) contains:
- `image`: uint8[400, 640] - preprocessed grayscale (gamma + CLAHE applied)
- `label`: uint8[400, 640] - binarized segmentation mask (0=background, 1=pupil)
- `spatial_weights`: float32[400, 640] - boundary weights for loss
- `dist_map`: float32[2, 400, 640] - signed distance per class (normalized)
- `cx`: float32 - normalized ellipse center x (0-1)
- `cy`: float32 - normalized ellipse center y (0-1)
- `rx`: float32 - normalized ellipse radius x
- `ry`: float32 - normalized ellipse radius y
- `filename`: string - original filename for traceability
- `preprocessed`: bool - always True for this dataset

Training scripts automatically detect the `preprocessed` flag and skip runtime gamma/CLAHE. Ellipse training scripts use precomputed cx, cy, rx, ry parameters when available.
