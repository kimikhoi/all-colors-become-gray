import random
from PIL import Image, ImageDraw

# Canvas size
SIZE = 4096
CENTER = SIZE // 2
RADIUS = SIZE // 2 - 50

# Create black background
image = Image.new("RGB", (SIZE, SIZE), (0, 0, 0))
pixels = image.load()

# Generate all RGB color combinations
colors = []

STEP = 16  # 16 x 16 x 16 = 4096 representative RGB combinations

for r in range(0, 256, STEP):
    for g in range(0, 256, STEP):
        for b in range(0, 256, STEP):
            colors.append((r, g, b))

random.shuffle(colors)

# Draw colors inside circular region
i = 0
for y in range(SIZE):
    for x in range(SIZE):

        dx = x - CENTER
        dy = y - CENTER

        if dx * dx + dy * dy <= RADIUS * RADIUS:

            color = colors[i % len(colors)]
            pixels[x, y] = color
            i += 1

# Save image
image.save("all_colors_become_gray.png")

print("Artwork generated.")
