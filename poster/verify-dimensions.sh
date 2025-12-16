#!/usr/bin/env bash
# Verify poster dimensions from LaTeX source

set -e

POSTER_TEX="poster.tex"

if [ ! -f "$POSTER_TEX" ]; then
    echo "Error: $POSTER_TEX not found"
    exit 1
fi

echo "Verifying poster dimensions from $POSTER_TEX..."
echo ""

# Extract paper dimensions from geometry package
WIDTH=$(grep -o 'paperwidth=[0-9.]*in' "$POSTER_TEX" | grep -o '[0-9.]*')
HEIGHT=$(grep -o 'paperheight=[0-9.]*in' "$POSTER_TEX" | grep -o '[0-9.]*')

if [ -z "$WIDTH" ] || [ -z "$HEIGHT" ]; then
    echo "Error: Could not extract dimensions from $POSTER_TEX"
    exit 1
fi

echo "Extracted dimensions:"
echo "  Width:  $WIDTH inches"
echo "  Height: $HEIGHT inches"
echo ""

# Check if they match requirements
EXPECTED_WIDTH="20.75"
EXPECTED_HEIGHT="37"

if [ "$WIDTH" = "$EXPECTED_WIDTH" ] && [ "$HEIGHT" = "$EXPECTED_HEIGHT" ]; then
    echo "✓ Dimensions match requirements: ${WIDTH}\" x ${HEIGHT}\""
    echo ""
    
    # Calculate aspect ratio
    python3 << EOF
width = float('$WIDTH')
height = float('$HEIGHT')
ratio = width / height
target_ratio = 9/16

print(f"Aspect ratio: {ratio:.6f}")
print(f"Target 9:16: {target_ratio:.6f}")
print(f"Difference: {abs(ratio - target_ratio):.6f} ({abs((ratio - target_ratio)/target_ratio * 100):.2f}%)")

if abs(ratio - target_ratio) < 0.01:
    print("\n✓ Aspect ratio is within acceptable tolerance of 9:16")
else:
    print(f"\n⚠ Aspect ratio differs from 9:16 by more than 1%")
    print(f"  For true 9:16 with width {width}\", height should be {width * 16/9:.4f}\"")
EOF
    exit 0
else
    echo "✗ Dimensions do NOT match requirements"
    echo "  Expected: ${EXPECTED_WIDTH}\" x ${EXPECTED_HEIGHT}\""
    echo "  Found:    ${WIDTH}\" x ${HEIGHT}\""
    exit 1
fi
