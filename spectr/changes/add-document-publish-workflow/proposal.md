# Change: Add Manually Triggerable Document Publish Workflow

## Why
The project needs a streamlined way to update the website's document directory (`www/documents/`) with the latest compiled Design Document and Poster PDFs without going through a full release. This enables quick updates when document content changes but a formal version release is not required.

## What Changes
- Add new GitHub Action workflow (`publish-docs.yml`) that is manually triggerable via `workflow_dispatch`
- Workflow compiles both main design document (`main.tex`) and poster (`poster/poster.tex`)
- Workflow copies compiled PDFs to `www/documents/` with standardized names:
  - `DesignDoc.pdf` - Latest compiled design document
  - `Poster.pdf` - Latest compiled poster
- Workflow commits and pushes the updated PDFs to the repository
- **Note**: LaTeX files already use relative paths correctly; no path fixes needed

## Technical Decisions

### Authentication
- Use GitHub App token (consistent with `release.yml`) via `actions/create-github-app-token@v2`
- Requires `SDDEC2501_PRIVATE_KEY` secret and app-id `2280081`
- This ensures commits bypass branch protection rules and maintain consistent authorship

### Concurrency Control
- Add `concurrency` block to prevent race conditions on parallel triggers
- Use `cancel-in-progress: true` to abort stale runs

### Output File Naming
- `DesignDoc.pdf` and `Poster.pdf` are **new "latest" files**, separate from versioned semester documents
- Existing files like `DesignDocSemester1.pdf` remain unchanged
- This allows the website to link to always-current versions

## Impact
- Affected specs: `build-system`
- Affected code: `.github/workflows/publish-docs.yml` (new file), `www/documents/` (updated PDFs)
- No changes to existing workflows - this is additive
- Enables website to serve latest document versions without manual intervention
