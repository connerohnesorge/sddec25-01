"""Memory-efficient HuggingFace dataset creation from NPZ chunks."""

import gc
from pathlib import Path
from typing import Callable

import numpy as np
from datasets import Dataset, DatasetDict, Features, Value, Array2D, Array3D


def create_hf_dataset_from_npz(
    output_dir: Path,
    image_height: int = 400,
    image_width: int = 640,
    verbose: bool = True,
) -> DatasetDict:
    """
    Create HuggingFace Dataset from saved npz chunk files using streaming.

    Uses generator-based loading to avoid OOM errors on large datasets.
    Memory usage is constant regardless of dataset size.

    Args:
        output_dir: Directory containing train/ and validation/ npz chunks
        image_height: Height of images (default: 400)
        image_width: Width of images (default: 640)
        verbose: Whether to print progress messages

    Returns:
        HuggingFace DatasetDict with train and validation splits
    """
    if verbose:
        print("Creating datasets from npz files (streaming mode)...", flush=True)

    features = Features({
        "image": Array2D(shape=(image_height, image_width), dtype="uint8"),
        "label": Array2D(shape=(image_height, image_width), dtype="uint8"),
        "spatial_weights": Array2D(shape=(image_height, image_width), dtype="float32"),
        "dist_map": Array3D(shape=(2, image_height, image_width), dtype="float32"),
        "cx": Value("float32"),
        "cy": Value("float32"),
        "rx": Value("float32"),
        "ry": Value("float32"),
        "filename": Value("string"),
        "preprocessed": Value("bool"),
    })

    def make_generator(split_name: str) -> Callable:
        """Create a generator function for the given split."""
        def sample_generator():
            split_dir = output_dir / split_name
            chunk_files = sorted(split_dir.glob("chunk_*.npz"))

            for chunk_file in chunk_files:
                # Load chunk with mmap for memory efficiency
                data = np.load(chunk_file, mmap_mode="r")
                n_samples = len(data["cx"])

                for i in range(n_samples):
                    yield {
                        "image": np.array(data["images"][i]),
                        "label": np.array(data["labels"][i]),
                        "spatial_weights": np.array(data["spatial_weights"][i]),
                        "dist_map": np.array(data["dist_maps"][i]),
                        "cx": float(data["cx"][i]),
                        "cy": float(data["cy"][i]),
                        "rx": float(data["rx"][i]),
                        "ry": float(data["ry"][i]),
                        "filename": str(data["filenames"][i]),
                        "preprocessed": True,
                    }

                # Explicit cleanup after each chunk
                del data
                gc.collect()

        return sample_generator

    train_dataset = Dataset.from_generator(make_generator("train"), features=features)
    gc.collect()

    val_dataset = Dataset.from_generator(make_generator("validation"), features=features)
    gc.collect()

    return DatasetDict({"train": train_dataset, "validation": val_dataset})
