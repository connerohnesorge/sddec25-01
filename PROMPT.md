

# Do-this checklist (copy/paste-ready)

## 1) CI: build the PDF on every push/PR

Add **.github/workflows/latex.yml**:

```yaml
name: LaTeX CI
on:
  push:
    branches: [main]
  pull_request: {}

permissions:
  contents: read

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Compile LaTeX (latexmk)
        uses: xu-cheng/latex-action@v4
        with:
          root_file: main.tex
          # set one of these if needed:
          # latexmk_use_xelatex: true
          # latexmk_use_lualatex: true
          # latexmk_shell_escape: true
      - name: Upload PDF artifact
        uses: actions/upload-artifact@v4
        with:
          name: sddec25-01
          path: |
            main.pdf
            references.bib
```

*`latex-action` is the most-used LaTeX builder on Actions and supports latexmk, XeLaTeX/LuaLaTeX, caching, etc.* ([GitHub][1])

> Prefer **Tectonic** if you want a smaller, reproducible toolchain: swap the build step for `setup-tectonic` + `tectonic main.tex`. ([GitHub][2])

---

## 2) Publish the PDF to GitHub Pages (pretty URL)

Enable **Settings → Pages → Build with Actions**, then add **.github/workflows/pages.yml**:

```yaml
name: Publish PDF to Pages
on:
  workflow_run:
    workflows: ["LaTeX CI"]
    types: [completed]
permissions:
  pages: write
  id-token: write
  contents: read
concurrency:
  group: "pages"
  cancel-in-progress: true
jobs:
  deploy:
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: sddec25-01
          path: ./public
      - name: Add index for direct viewing
        run: |
          echo '<meta http-equiv="refresh" content="0; url=main.pdf">' > public/index.html
      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./public
      - name: Deploy to Pages
        uses: actions/deploy-pages@v4
```

*Official Pages actions, supported flow: upload → deploy.* ([GitHub Docs][3])

---

## 3) PR review bots: LaTeX lint + typos + prose checks

Add **.github/workflows/reviewdog.yml**:

```yaml
name: Review (LaTeX + typos)
on:
  pull_request:
permissions:
  pull-requests: write
  contents: read
jobs:
  chktex:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: ChkTeX
        uses: j2kun/chktex-action@v1
      - name: Typos (reviewdog)
        uses: reviewdog/action-typos@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          reporter: github-pr-review
```

*`chktex` catches common TeX issues; `reviewdog` annotates PRs with typos—use pinned versions/tags and avoid deprecated `reviewdog/action-setup@v1` due to the 2025 supply-chain incident.* ([GitHub][4])

> Tip: add a `.chktexrc` to tune warnings (e.g., ignoring your custom class).

---

## 4) Releases that attach the PDF

Add **.github/workflows/release.yml** to cut a tag like `v0.3.0` and upload the PDF:

```yaml
name: Release PDF
on:
  push:
    tags: ["v*.*.*"]
permissions:
  contents: write
jobs:
  build-and-release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: xu-cheng/latex-action@v4
        with: { root_file: main.tex }
      - uses: actions/upload-artifact@v4
        with: { name: pdf, path: main.pdf }
      - name: Create GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          files: main.pdf
```

*Attach built artifacts to a GitHub Release for versioned citing.* ([GitHub][1])

---

## 5) Repo hygiene & contributor UX

Add these lightweight bits:

* **.github/ISSUE_TEMPLATE/** (bug, doc request, enhancement), **PULL_REQUEST_TEMPLATE.md**, **CODEOWNERS**
  Improves triage and review routing. (GitHub’s defaults are fine to start.) ([GitHub][5])
* **.github/dependabot.yml** to auto-update Actions:

  ```yaml
  version: 2
  updates:
    - package-ecosystem: "github-actions"
      directory: "/"
      schedule: { interval: "weekly" }
  ```

  Keeps CI secure and fresh. (Useful with Pages + latex-action.) ([GitHub Docs][3])
* **Badges** in `README.md`: CI, Pages, Release.
* **Makefile** (optional) mapping `make pdf`, `make watch` → `latexmk -pdf -interaction=nonstopmode -synctex=1 main.tex`.

---

## 6) Dev environments (optional but nice)

* **.devcontainer/** for Codespaces nix preinstalled so teammates can build instantly.
* Since your repo already has a **Nix flake**, consider a second CI job that validates `nix build` to ensure devshell stays green on Linux runners. (Keep the LaTeX build independent so contributors without Nix still get artifacts.)
