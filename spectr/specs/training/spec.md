# Training Specification

## Purpose

Define requirements for training scripts that train neural network models for eye pupil segmentation on the OpenEDS dataset, including model architectures, loss functions, and MLflow integration.

## Requirements

### Requirement: EfficientViT Training Script
The system SHALL provide a training script `train_efficientvit.py` that trains a TinyEfficientViT model for eye pupil segmentation on the OpenEDS dataset.

#### Scenario: Training script execution
- **WHEN** user runs `modal run training/train_efficientvit.py`
- **THEN** training completes and logs metrics to MLflow
- **AND** best model is exported to ONNX format

#### Scenario: Model parameter constraint
- **WHEN** TinyEfficientViTSeg model is instantiated
- **THEN** total trainable parameters SHALL be less than 60,000

### Requirement: TinyEfficientViT Model Architecture
The system SHALL implement a TinyEfficientViTSeg model based on EfficientViT-MSRA architecture with drastically reduced dimensions to meet the <60k parameter constraint.

#### Scenario: Model configuration
- **WHEN** TinyEfficientViTSeg is created with default config
- **THEN** embed_dim SHALL be approximately (8, 16, 24)
- **AND** depth SHALL be (1, 1, 1)
- **AND** num_heads SHALL be (1, 1, 2)

#### Scenario: Forward pass
- **WHEN** model receives input tensor of shape (B, 1, 400, 640)
- **THEN** output tensor SHALL have shape (B, 2, 400, 640)

### Requirement: Segmentation Decoder
The system SHALL implement a lightweight decoder that produces dense predictions from multi-scale encoder features.

#### Scenario: Decoder with skip connections
- **WHEN** encoder produces features at multiple scales
- **THEN** decoder SHALL upsample and combine features to produce full-resolution output

### Requirement: MLflow Integration
The system SHALL log training metrics, parameters, and artifacts to MLflow.

#### Scenario: Metric logging
- **WHEN** each epoch completes
- **THEN** train_loss, valid_loss, train_iou, valid_iou SHALL be logged
- **AND** loss components (ce_loss, dice_loss, surface_loss) SHALL be logged

#### Scenario: Model tagging
- **WHEN** MLflow run is created
- **THEN** model_type tag SHALL be "TinyEfficientViT"
- **AND** architecture tag SHALL distinguish from ShallowNet runs

### Requirement: Ellipse Model PyTorch Checkpoint Export
The system SHALL export the trained ellipse regression model to PyTorch checkpoint format compatible with edge deployment and fine-tuning.

#### Scenario: PyTorch checkpoint export
- **WHEN** training completes with best validation mIoU
- **THEN** best model SHALL be saved to `best_ellipse_model.pt`
- **AND** checkpoint SHALL contain model `state_dict()`
- **AND** model SHALL be in contiguous memory format for portability

#### Scenario: Epoch checkpoints
- **WHEN** training reaches checkpoint epochs (every 10 epochs or final epoch)
- **THEN** checkpoint SHALL be saved as `ellipse_model_epoch_{n}.pt`
- **AND** all checkpoints SHALL be uploaded to MLflow as artifacts

#### Scenario: Compiled model handling
- **WHEN** model is wrapped with `torch.compile()`
- **THEN** export function SHALL unwrap to `_orig_mod` before saving
- **AND** checkpoint SHALL contain unwrapped model weights

### Requirement: Ellipse Regression Colab Notebook
The system SHALL provide a Jupyter notebook `train_ellipse.ipynb` that trains an EllipseRegressionNet model for pupil ellipse parameter prediction, runnable in Google Colab with free GPU.

#### Scenario: Notebook execution in Colab
- **WHEN** user opens `training/train_ellipse.ipynb` in Google Colab
- **AND** user selects GPU runtime
- **AND** user runs all cells
- **THEN** training completes successfully
- **AND** trained model is exported to ONNX format

#### Scenario: Dataset loading from HuggingFace
- **WHEN** notebook executes dataset loading cells
- **THEN** OpenEDS dataset SHALL be downloaded from `Conner/openeds-precomputed`
- **AND** train and validation splits SHALL be available

#### Scenario: Model architecture consistency
- **WHEN** EllipseRegressionNet is instantiated in notebook
- **THEN** model architecture SHALL match `train_ellipse.py` Modal version
- **AND** model SHALL output 4 parameters (cx, cy, rx, ry)

#### Scenario: Training visualization
- **WHEN** training completes
- **THEN** notebook SHALL display loss curves
- **AND** notebook SHALL display sample prediction visualizations
- **AND** notebook SHALL report final mIoU and error metrics

### Requirement: Colab Runtime Configuration
The notebook SHALL include setup cells that configure the Colab environment for GPU training.

#### Scenario: GPU availability check
- **WHEN** user runs the setup cells
- **THEN** notebook SHALL verify GPU is available
- **AND** notebook SHALL print GPU name and memory

#### Scenario: Dependency installation
- **WHEN** user runs the pip install cell
- **THEN** required packages SHALL be installed (torch, torchvision, opencv-python, datasets, pillow, scikit-learn, tqdm, matplotlib, onnx)

### Requirement: Model Export from Colab
The notebook SHALL provide functionality to export and download the trained model.

#### Scenario: ONNX export
- **WHEN** training completes with best validation mIoU
- **THEN** notebook SHALL export model to `best_ellipse_model.onnx`
- **AND** notebook SHALL display file size

#### Scenario: Model download
- **WHEN** user runs the download cell
- **THEN** trained ONNX model SHALL be downloadable from Colab
