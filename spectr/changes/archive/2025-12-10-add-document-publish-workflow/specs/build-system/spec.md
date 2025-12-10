## ADDED Requirements

### Requirement: Manual Document Publish Workflow
The system SHALL provide a manually triggerable GitHub Actions workflow that compiles the design document and poster, then publishes them to the website documents directory for public access.

#### Scenario: Manual workflow trigger available
- **WHEN** maintainer navigates to Actions tab in GitHub repository
- **THEN** "Publish Documents" workflow is listed
- **AND** workflow has "Run workflow" button available
- **AND** workflow can be triggered from the `main` branch

#### Scenario: Compile design document
- **WHEN** publish workflow is triggered
- **THEN** workflow compiles `main.tex` using `xu-cheng/latex-action@v4`
- **AND** compilation uses latexmk with biber for bibliography
- **AND** `main.pdf` is generated successfully

#### Scenario: Compile poster
- **WHEN** publish workflow is triggered
- **THEN** workflow compiles `poster/poster.tex` using `xu-cheng/latex-action@v4`
- **AND** `working_directory` is set to `poster`
- **AND** `poster/poster.pdf` is generated successfully

#### Scenario: Copy PDFs to website documents
- **WHEN** both compilations succeed
- **THEN** `main.pdf` is copied to `www/documents/DesignDoc.pdf`
- **AND** `poster/poster.pdf` is copied to `www/documents/Poster.pdf`
- **AND** existing files at those paths are overwritten

#### Scenario: Commit and push changes
- **WHEN** PDFs are copied to `www/documents/`
- **THEN** workflow stages the changed PDF files
- **AND** workflow creates a commit with message "docs: update published documents [skip ci]"
- **AND** workflow pushes commit to `main` branch
- **AND** `[skip ci]` prevents recursive workflow triggering

#### Scenario: Workflow permissions and authentication
- **WHEN** workflow runs
- **THEN** workflow has `contents: write` permission
- **AND** workflow creates GitHub App installation token using `actions/create-github-app-token@v2`
- **AND** workflow uses app-id `2280081` with `SDDEC2501_PRIVATE_KEY` secret
- **AND** checkout uses the installation token for git operations
- **AND** workflow can push commits to the repository bypassing branch protection

#### Scenario: Concurrency control
- **WHEN** workflow is triggered while another instance is running
- **THEN** the in-progress run is cancelled
- **AND** only the latest triggered run completes
- **AND** concurrency group is set to `publish-docs`

#### Scenario: Git configuration
- **WHEN** workflow prepares to commit changes
- **THEN** git user.name is configured as `github-actions[bot]`
- **AND** git user.email is configured as `github-actions[bot]@users.noreply.github.com`

#### Scenario: Workflow summary
- **WHEN** workflow completes successfully
- **THEN** workflow writes summary to `$GITHUB_STEP_SUMMARY`
- **AND** summary includes confirmation of updated files
- **AND** summary includes links to the published documents

#### Scenario: Workflow failure handling
- **WHEN** document compilation fails
- **THEN** workflow reports failure status
- **AND** no partial commits are made to repository
- **AND** error logs are available in workflow output
