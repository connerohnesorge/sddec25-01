# hf_dataset

Memory-efficient HuggingFace dataset creation from NPZ chunks.

## Usage

```python
from pathlib import Path
from hf_dataset import create_hf_dataset_from_npz

dataset = create_hf_dataset_from_npz(
    output_dir=Path("./precompute_output"),
    image_height=400,
    image_width=640,
)
```

## Features

- Generator-based loading to avoid OOM errors
- Memory-mapped NPZ file reading
- Automatic garbage collection between chunks
- Configurable image dimensions
