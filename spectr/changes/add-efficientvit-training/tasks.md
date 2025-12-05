## 1. Model Implementation

- [ ] 1.1 Implement TinyConvNorm layer (conv + batchnorm, parameter-efficient)
- [ ] 1.2 Implement TinyPatchEmbedding (2-layer, stride 4)
- [ ] 1.3 Implement TinyCascadedGroupAttention (1-2 heads, small key_dim)
- [ ] 1.4 Implement TinyLocalWindowAttention wrapper
- [ ] 1.5 Implement TinyEfficientVitBlock (dw conv + attention + mlp)
- [ ] 1.6 Implement TinyEfficientVitStage with optional downsampling
- [ ] 1.7 Implement TinyEfficientVitEncoder (combines stages)
- [ ] 1.8 Implement lightweight segmentation decoder with skip connections
- [ ] 1.9 Implement TinyEfficientViTSeg (full model combining encoder + decoder)
- [ ] 1.10 Add parameter counting and verify <60k total parameters

## 2. Training Script

- [ ] 2.1 Create `train_efficientvit.py` with Modal app setup
- [ ] 2.2 Copy dataset loading from train.py (IrisDataset, augmentations)
- [ ] 2.3 Copy loss functions (CombinedLoss) and metrics (IoU computation)
- [ ] 2.4 Copy visualization utilities (plots, predictions)
- [ ] 2.5 Instantiate TinyEfficientViTSeg model with config
- [ ] 2.6 Setup MLflow tracking with distinct experiment/run tags
- [ ] 2.7 Implement training loop with AMP support
- [ ] 2.8 Implement validation loop
- [ ] 2.9 Add ONNX export for best model
- [ ] 2.10 Add checkpoint saving at intervals

## 3. Validation

- [ ] 3.1 Verify model parameter count is <60k
- [ ] 3.2 Verify model forward pass on 640x400 input produces 640x400 output
- [ ] 3.3 Verify ONNX export succeeds without errors
- [ ] 3.4 Test training script runs locally (CPU, 1 epoch, small batch)
- [ ] 3.5 Run full training on Modal and verify MLflow logging
