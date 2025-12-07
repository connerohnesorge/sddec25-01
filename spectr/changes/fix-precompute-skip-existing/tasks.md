## 1. Implementation

- [ ] 1.1 Add `has_existing_chunks(split_dir: Path) -> bool` helper function to check if any `.npz` files exist
- [ ] 1.2 Modify `main()` to check for existing chunks before calling `process_and_save_split()`
- [ ] 1.3 Print skip message with chunk count when skipping a split
- [ ] 1.4 Return existing sample count from skipped splits for summary

## 2. Verification

- [ ] 2.1 Test that first run processes all files normally
- [ ] 2.2 Test that second run skips processing and completes quickly
- [ ] 2.3 Verify HuggingFace dataset creation still works with existing chunks
