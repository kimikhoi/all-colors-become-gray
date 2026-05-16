from PIL import Image

FILE = "all_colors_become_gray_full_rgb_circle_white.png"

img = Image.open(FILE)

print("size:", img.size)

total_pixels = img.size[0] * img.size[1]

print("total pixels:", total_pixels)

colors = set(img.getdata())

print("unique colors:", len(colors))

expected = 256 * 256 * 256

print("expected RGB colors:", expected)

if len(colors) == expected:
    print()
    print("SUCCESS")
    print("Every possible RGB color exists exactly once.")
else:
    print()
    print("WARNING")
    print("RGB set is incomplete.")