# Poster Dimensions Documentation

## Current Specifications

- **Width**: 20.75 inches
- **Height**: 37 inches
- **Aspect Ratio**: ~9:16 (0.3% deviation from exact 9:16)
- **Format**: PNG (preferred) or PDF
- **Resolution**: 300 DPI for PNG export

## Implementation Details

The poster dimensions are defined in `poster.tex` using the geometry package:

```latex
\documentclass[25pt, portrait]{tikzposter}
\usepackage[paperwidth=20.75in, paperheight=37in]{geometry}
```

### Aspect Ratio Notes

The specified dimensions (20.75" × 37") result in an aspect ratio of approximately 0.560811, which is very close to the 9:16 target (0.562500). The deviation is only 0.3%, which is within acceptable printing tolerances.

For a perfect 9:16 aspect ratio:
- With width 20.75": height would be 36.8889"
- With height 37": width would be 20.8125"

The provided dimensions prioritize the specified physical size over mathematical precision.

## Verification

To verify the dimensions are correctly set in the LaTeX source:

```bash
cd poster
./verify-dimensions.sh
```

Expected output:
```
✓ Dimensions match requirements: 20.75" x 37"
✓ Aspect ratio is within acceptable tolerance of 9:16
```

## Compilation and Export

### Generate PDF

```bash
cd poster
nix develop ../ -c latexmk -pdf poster.tex
```

This creates `poster.pdf` with the specified dimensions.

### Convert to PNG

```bash
cd poster
./convert-to-png.sh
```

This converts the PDF to PNG at 300 DPI, creating `poster.png`.

The script uses:
- `pdftoppm` (preferred, from poppler-utils package)
- Falls back to ImageMagick's `convert` if pdftoppm is unavailable

### Expected PNG Dimensions

At 300 DPI:
- Width: 20.75" × 300 = 6225 pixels
- Height: 37" × 300 = 11100 pixels

## Historical Context

The poster was previously sized to A0 portrait format (841mm × 1189mm or 33.1" × 46.8"). This was updated to the current dimensions to meet specific conference or presentation requirements.

## File Outputs

- `poster.pdf` - Generated PDF (ignored by git)
- `poster.png` - Generated PNG (ignored by git)

Both output files are in `.gitignore` and should not be committed to the repository.
