## ADDED Requirements

### Requirement: Skip Existing Precomputed Chunks

The precompute application SHALL skip processing for a split (train/validation) if NPZ chunk files already exist in the output directory.

#### Scenario: Chunks already exist

- **WHEN** running precompute with existing chunks in `parquet_chunks/train/`
- **THEN** the train split processing is skipped
- **AND** a message is printed indicating the split was skipped with chunk count

#### Scenario: No existing chunks

- **WHEN** running precompute with no existing chunks for a split
- **THEN** the split is processed normally and chunks are created

#### Scenario: Partial chunks exist

- **WHEN** only train chunks exist but not validation chunks
- **THEN** train processing is skipped
- **AND** validation is processed normally
