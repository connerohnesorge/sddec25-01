## 1. Create New Package Structure

- [ ] 1.1 Create `packages/effvit/` directory structure
- [ ] 1.2 Create `packages/effvit/pyproject.toml` (mirror `ellipse` package config)
- [ ] 1.3 Create `packages/effvit/README.md` with package description

## 2. Extract and Organize Model Components

- [ ] 2.1 Create `effvit/layers.py` with `TinyConvNorm`, `TinyPatchEmbedding`, `TinyMLP`
- [ ] 2.2 Create `effvit/attention.py` with `TinyCascadedGroupAttention`, `TinyLocalWindowAttention`
- [ ] 2.3 Create `effvit/encoder.py` with `TinyEfficientVitBlock`, `TinyEfficientVitStage`, `TinyEfficientVitEncoder`
- [ ] 2.4 Create `effvit/decoder.py` with `TinySegmentationDecoder`
- [ ] 2.5 Create `effvit/model.py` with `TinyEfficientViTSeg` (imports from other modules)
- [ ] 2.6 Create `effvit/__init__.py` with clean exports for all public classes

## 3. Update Workspace Configuration

- [ ] 3.1 Add `packages/effvit` to workspace members in root `pyproject.toml`
- [ ] 3.2 Remove `packages/tiny_effvit` from workspace members

## 4. Update Dependent Applications

- [ ] 4.1 Update `apps/demo_tiny_effvit/pyproject.toml` to depend on `effvit`
- [ ] 4.2 Update `apps/demo_tiny_effvit/demo_tiny_effvit/main.py` imports
- [ ] 4.3 Update `apps/train_tiny_effvit/pyproject.toml` to depend on `effvit`
- [ ] 4.4 Update `apps/train_tiny_effvit/train_tiny_effvit/main.py` imports
- [ ] 4.5 Update `apps/train_tiny_effvit_inf/pyproject.toml` to depend on `effvit`
- [ ] 4.6 Update `apps/train_tiny_effvit_inf/train_tiny_effvit_inf/main.py` imports

## 5. Cleanup and Validation

- [ ] 5.1 Remove `packages/tiny_effvit/` directory
- [ ] 5.2 Run `uv sync` to verify workspace resolves correctly
- [ ] 5.3 Verify `from effvit import TinyEfficientViTSeg` works
- [ ] 5.4 Verify all dependent apps can import and run
