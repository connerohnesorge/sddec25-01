# Tasks: Convert ShallowNet Demo to PyTorch

## 1. Model Setup

- [x] 1.1 Add ShallowNet model class to `demo/demo.py` (copy from `training/train.py`)
- [x] 1.2 Add device detection function (CUDA > MPS > CPU)
- [x] 1.3 Add `--device` CLI argument

## 2. Inference Conversion

- [x] 2.1 Replace ONNX model loading with PyTorch state dict loading
- [x] 2.2 Replace `_run_inference()` with PyTorch forward pass using `torch.no_grad()`
- [x] 2.3 Update device display text ("CUDA"/"MPS"/"CPU")

## 3. Cleanup

- [x] 3.1 Remove ONNX Runtime imports and IO binding code
- [x] 3.2 Update `demo/requirements.txt` (remove onnxruntime, add torch)
- [x] 3.3 Update README with new model format and MPS instructions

## 4. Validation

- [x] 4.1 Test on MPS (Apple Silicon) - N/A on this machine, code verified
- [x] 4.2 Test on CUDA (if available) - N/A on this machine, code verified
- [x] 4.3 Test CPU fallback - PASSED
