# VisionAssist (SDDEC25-01) Context

## Purpose

VisionAssist is an Iowa State University Computer Engineering senior design project focused on optimizing AI-powered eye tracking systems for real-time medical monitoring and assistive technology.

**Application Domain**: Medical assistive technology for individuals with mobility impairments (particularly wheelchair users with conditions like cerebral palsy or epilepsy) to:
- Detect early warning signs of medical episodes through eye movement and posture analysis
- Autonomously respond to medical distress by repositioning the wheelchair to a safer position
- Provide proactive safety monitoring without compromising user independence

**Target Hardware**: AMD Kria KV260 Development Board (Zynq UltraScale+ MPSoC, 4GB DDR, DPU for neural network acceleration). The embedded C++ implementation lives in a separate repository.

This repository contains:
1. **Documentation**: LaTeX design documents and A0 poster for academic presentation
2. **Training Pipeline**: Python scripts for training neural network models (TinyEfficientViT, EllipseRegressionNet)
3. **Demo Applications**: Webcam-based real-time pupil segmentation demos for presentations

## Tech Stack

### Documentation
- **LaTeX**: TeX Live Full distribution with pdflatex/latexmk
- **Bibliography**: biblatex with biber backend (IEEE style)
- **Document Class**: Custom `isusdd.cls` (Iowa State Senior Design Document)
- **Poster**: tikzposter class for A0 portrait format

### ML Training Pipeline
- **Language**: Python 3.10+
- **Framework**: PyTorch 2.0+ with CUDA support
- **Cloud Compute**: Modal (serverless GPU)
- **Experiment Tracking**: MLflow (Databricks-hosted)
- **Model Export**: ONNX for edge deployment
- **Dataset**: OpenEDS from HuggingFace (`Conner/openeds-precomputed`)
- **Package Manager**: uv

### Demo Applications
- **Vision**: OpenCV, MediaPipe Face Mesh
- **Inference**: PyTorch (CUDA/MPS/CPU) or ONNX Runtime
- **UI**: OpenCV window with overlays

### Development Environment
- **Nix/NixOS**: Reproducible development via `flake.nix`
- **direnv**: Automatic environment loading
- **CI/CD**: GitHub Actions for LaTeX compilation and releases
- **Spec-Driven Development**: Spectr

## Project Conventions

### Code Style

**Python (training/, demo/)**:
- **Formatter/Linter**: Ruff (format + lint)
- **Type Hints**: Optional but encouraged
- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Docstrings**: Google style for public functions

**LaTeX (main.tex, poster/)**:
- **Indentation**: 2 spaces
- **Line Length**: <100 characters for readability
- **Labels**: Prefix with type (`chap:`, `sec:`, `fig:`, `tab:`)
- **Validation**: Run `nix develop -c lint` before committing

### Architecture Patterns

**Neural Network Models**:
- TinyEfficientViT: <60k parameters for edge deployment
- Semantic segmentation with U-Net style decoder
- Input: grayscale 640x400, Output: 2-class segmentation mask

**Training Pipeline**:
- Preprocessing: gamma correction -> CLAHE -> resize -> normalize
- Loss: Cross-entropy + Dice + Surface loss
- Metrics: mIoU (mean Intersection over Union)

**Demo Applications**:
- MediaPipe for face/eye detection
- Preprocessing must match training pipeline exactly
- Multi-device support: CUDA > MPS > CPU fallback

### Testing Strategy

**Python Code**: Manual testing only (no automated test suite)
- Training validated via MLflow metrics (loss curves, mIoU)
- Demo validated via visual inspection during presentations
- Model parameter counts verified programmatically

**LaTeX Documentation**:
- Compilation testing with `nix develop -c ltx-compile`
- Visual inspection after significant changes
- CI validates successful PDF generation

### Git Workflow

**Branching**:
- `main`: Production-ready documentation
- Feature branches: `feature/`, `fix/`, `docs/`, `refactor/`
- Short-lived branches, merge within 1-2 weeks

**Commit Conventions** (Conventional Commits):
- `docs:` - Documentation/LaTeX changes
- `feat:` - New features or sections
- `fix:` - Bug fixes
- `style:` - Formatting only
- `refactor:` - Restructuring without content change
- `chore:` - Maintenance tasks

**Example**: `docs(training): add EfficientViT architecture section`

## Domain Context

**Medical Assistive Technology**:
- Primary users: Wheelchair users with cerebral palsy, epilepsy, or similar conditions
- Safety-critical: System must detect medical distress and respond autonomously
- Privacy-preserving: All processing on-device (no cloud data transmission)
- Real-time: <100ms latency for emergency detection

**Eye Tracking for Medical Monitoring**:
- Pupil segmentation enables gaze tracking and attention monitoring
- Abnormal eye movements can indicate seizure onset or loss of consciousness
- Combined with posture analysis for comprehensive distress detection

## Important Constraints

**Model Size**: <60,000 parameters for TinyEfficientViT (edge deployment constraint)
**Accuracy Target**: 99.8% IoU for semantic segmentation
**Latency Target**: 60 FPS (4 frames in <33.2ms total)
**Memory Budget**: <4GB on Kria KV260

**IEEE Standards Compliance**:
- IEEE 3129-2023: AI image recognition robustness
- IEEE 2802-2022: AI medical device evaluation
- IEEE 7002-2022: Data privacy process
- IEEE 2952-2023: Trusted execution environment

## External Dependencies

**Cloud Services**:
- **Modal**: Serverless GPU compute for training (modal.com)
- **Databricks MLflow**: Experiment tracking and model registry
- **HuggingFace**: Dataset hosting (`Conner/openeds-precomputed`)
- **GitHub Actions**: CI/CD for documentation builds

**Local Requirements**:
- NVIDIA GPU with CUDA 12.4+ (for local training)
- 1080p webcam (for demo applications)
- Nix package manager (for reproducible builds)
