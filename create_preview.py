from PIL import Image

SOURCE = "all_colors_become_gray_full_rgb_circle_white.png"

OUTPUT = "all_colors_become_gray_preview.png"

PREVIEW_SIZE = 2000

img = Image.open(SOURCE)

img.thumbnail((PREVIEW_SIZE, PREVIEW_SIZE))

img.save(
    OUTPUT,
    optimize=True,
    compress_level=9
)

print("Preview image saved:", OUTPUT)