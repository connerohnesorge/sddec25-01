# VisionAssist - Assistive Eye Tracking System

## Real-Time Semantic Segmentation Optimization for Medical Assistance Applications

**Iowa State University Computer Engineering Senior Design Project (SDDEC25-01)**

This repository contains comprehensive LaTeX documentation for VisionAssist, an AI-powered eye tracking system designed for real-time medical monitoring and assistive technology. The project optimizes semantic segmentation algorithms for deployment on AMD Kria KV260 edge computing platforms to assist individuals with mobility impairments.

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [Building Documentation](#building-documentation)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

VisionAssist addresses the critical need for real-time eye tracking in medical assistive technology, particularly for wheelchair users with conditions like cerebral palsy or epilepsy. The system:

- **Detects** early warning signs of medical episodes through eye movement analysis
- **Responds** autonomously by safely repositioning wheelchairs during distress
- **Maintains** user privacy through on-device processing (no cloud connectivity)
- **Achieves** 60 FPS processing with 99.8% accuracy (IoU metric)

### Technical Stack

**Documentation (This Repository)**:
- LaTeX (TeX Live) with custom `isusdd.cls` document class
- BibLaTeX with Biber backend (IEEE citation style)
- Nix/NixOS for reproducible development environments

**Implementation (Separate Repository)**:
- AMD Kria KV260 Development Board (Zynq UltraScale+ MPSoC)
- C++17/C++20 with Vitis-AI framework
- U-Net semantic segmentation model (ONNX format)

## Key Features

- **High Performance**: 60 FPS (4 frames in <33.2ms)
- **Medical-Grade Accuracy**: 99.8% Intersection over Union (IoU)
- **Low Latency**: <100ms emergency response time
- **Privacy-Preserving**: All processing on-device
- **IEEE Standards Compliant**: Follows IEEE 3129-2023, 2802-2022, 7002-2022, 2952-2023

## Getting Started

### Prerequisites

- **Nix Package Manager** (recommended) or
- **Full TeX Live Distribution** (2023 or newer)

### Quick Start with Nix

```bash
# Clone the repository
git clone https://github.com/conneroisu/sddec25-01.git
cd sddec25-01

# Enter development environment (automatically loads with direnv)
nix develop

# Compile the main document
ltx-compile

# Watch for changes and auto-recompile
ltx-watch main.tex
```

### Without Nix

Ensure you have a full TeX Live installation with the following packages:
- pdflatex, latexmk
- biblatex, biber
- geometry, hyperref, microtype, ragged2e
- listings, xcolor, amsmath, graphicx, subcaption

```bash
# Compile the document
latexmk -pdf main.tex

# Or use pdflatex with biber
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

## Building Documentation

### Available Commands (Nix Environment)

```bash
ltx-compile         # Compile main.tex to PDF
ltx-watch main.tex  # Auto-recompile on file changes
ltx-wordcount       # Get word count statistics
lint                # Run spell check and validation
```

### Output

The compiled PDF will be generated as `main.pdf` in the project root.

## Project Structure

```
.
├── documents/              # Semester deliverables (PDFs)
│   ├── DesignDocSemester1.pdf
│   ├── Report*Semester*.pdf
│   └── ...
├── sections/              # Modular LaTeX chapters
│   ├── abstract.tex
│   ├── 01-introduction.tex
│   ├── 02-requirements.tex
│   ├── 03-project-plan.tex
│   ├── 04-design.tex
│   ├── 05-testing.tex
│   ├── 06-implementation.tex
│   └── 07-conclusion.tex
├── main.tex              # Main document entry point
├── isusdd.cls           # Custom ISU Senior Design document class
├── references.bib       # Bibliography (IEEE format)
├── flake.nix           # Nix development environment
├── VERSION             # Auto-generated version (DO NOT EDIT)
├── README.md           # This file
├── CLAUDE.md           # Project conventions and AI agent instructions
└── AGENTS.md           # Detailed project context
```

## Development Workflow

### Branching Strategy

- `main` - Production-ready documentation (protected)
- `feature/*` - New features or significant changes
- `fix/*` - Bug fixes and corrections
- `docs/*` - Documentation improvements

### Commit Conventions

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```bash
docs(requirements): add functional requirements for eye tracking
fix(build): correct latexmk configuration for bibliography
style(formatting): fix table alignment in testing chapter
feat(testing): add comprehensive user testing plan
```

### Before Committing

```bash
# Verify compilation succeeds
ltx-compile

# Run spell check
lint

# Check word count (if length requirements exist)
ltx-wordcount
```

### Making Changes

1. Create a feature branch: `git checkout -b feature/my-improvement`
2. Make your changes to relevant `.tex` files in `sections/`
3. Verify compilation: `ltx-compile`
4. Commit with conventional commit message
5. Push and create pull request
6. Request review from team member

## Contributing

We welcome contributions! Please follow these guidelines:

1. **Read** `CLAUDE.md` for detailed project conventions
2. **Follow** LaTeX formatting standards (2-space indentation, <100 char lines)
3. **Use** IEEE citation style for all references
4. **Test** compilation before committing
5. **Write** clear, descriptive commit messages
6. **Request** review before merging to main

### Code Style

- **Indentation**: 2 spaces (no tabs)
- **Line Length**: <100 characters for readability
- **Comments**: Use `%` for explanatory comments
- **Labels**: Prefix with type (`chap:`, `sec:`, `fig:`, `tab:`)
- **Citations**: Use `\cite{}` or `\parencite{}`

## Documentation

For comprehensive project documentation, see:
- **CLAUDE.md**: Project conventions, tech stack, and development practices
- **AGENTS.md**: Detailed project context and domain information
- **sections/*.tex**: Individual chapters of the design document

## Team

**Iowa State University - Department of Computer Engineering**

- Conner Ohnesorge
- Tyler Schaefer
- Aidan Perry
- Joey Metzen

**Course**: Senior Design (SDDEC25-01)
**Semester**: Spring 2025

## License

This project is academic work for Iowa State University. All rights reserved.

## Acknowledgments

Special thanks to our project advisors and the Computer Engineering department at Iowa State University for their support and guidance.

---

For questions or issues, please contact the team through the course instructors or open an issue in this repository.
