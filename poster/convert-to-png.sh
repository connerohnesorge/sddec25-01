#!/usr/bin/env bash
# Convert poster PDF to PNG at 300 DPI
# Requires ImageMagick or pdftoppm

set -e

POSTER_PDF="poster.pdf"
POSTER_PNG="poster.png"
DPI=300

if [ ! -f "$POSTER_PDF" ]; then
    echo "Error: $POSTER_PDF not found. Please compile the poster first."
    exit 1
fi

echo "Converting $POSTER_PDF to $POSTER_PNG at ${DPI} DPI..."

# Try pdftoppm first (usually faster and better quality)
if command -v pdftoppm &> /dev/null; then
    echo "Using pdftoppm..."
    pdftoppm -png -r $DPI -singlefile "$POSTER_PDF" poster_temp
    mv poster_temp.png "$POSTER_PNG"
# Fallback to ImageMagick convert
elif command -v convert &> /dev/null; then
    echo "Using ImageMagick convert..."
    convert -density $DPI "$POSTER_PDF" -quality 100 "$POSTER_PNG"
else
    echo "Error: Neither pdftoppm nor ImageMagick convert found."
    echo "Please install poppler-utils or ImageMagick."
    exit 1
fi

echo "Successfully created $POSTER_PNG"
echo "Verifying dimensions..."
if command -v identify &> /dev/null; then
    identify "$POSTER_PNG"
fi
