from PIL import Image
import random

# ============================================
# CONFIG
# ============================================

SIZE = 5000
CENTER = SIZE // 2
RADIUS = 2320

TOTAL_COLORS = 256 * 256 * 256

OUTPUT_FILE = "all_colors_become_gray_full_rgb_circle_white.png"

# ============================================
# COLLECT ALL PIXELS INSIDE CIRCLE
# ============================================

circle_pixels = []

for y in range(SIZE):
    for x in range(SIZE):

        dx = x - CENTER
        dy = y - CENTER

        if dx * dx + dy * dy <= RADIUS * RADIUS:
            circle_pixels.append((x, y))

print("Circle pixels:", len(circle_pixels))
print("Required RGB colors:", TOTAL_COLORS)

if len(circle_pixels) < TOTAL_COLORS:
    raise ValueError(
        "Circle is too small. Increase SIZE or RADIUS."
    )

# ============================================
# SHUFFLE PIXEL POSITIONS
# ============================================

random.seed(2026)

random.shuffle(circle_pixels)

circle_pixels = circle_pixels[:TOTAL_COLORS]

# ============================================
# CREATE ALL RGB COLORS
# ============================================

colors = list(range(TOTAL_COLORS))

random.seed(2026)

random.shuffle(colors)

# ============================================
# CREATE IMAGE
# ============================================

img = Image.new(
    "RGB",
    (SIZE, SIZE),
    (255, 255, 255)
)

pixels = img.load()

# ============================================
# PLACE EVERY RGB COLOR EXACTLY ONCE
# ============================================

for i, (x, y) in enumerate(circle_pixels):

    n = colors[i]

    r = (n >> 16) & 255
    g = (n >> 8) & 255
    b = n & 255

    pixels[x, y] = (r, g, b)

# ============================================
# SAVE IMAGE
# ============================================

img.save(
    OUTPUT_FILE,
    optimize=True,
    compress_level=9
)

print()
print("Saved:", OUTPUT_FILE)
print("Canvas size:", SIZE, "x", SIZE)
print("RGB colors placed:", TOTAL_COLORS)
print("Each RGB color appears exactly once.")