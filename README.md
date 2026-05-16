# All Colors Become Gray

![All Colors Become Gray](all_colors_become_gray_preview.png)

[View Full RGB Archival Version](https://github.com/kimikhoi/all-colors-become-gray/blob/main/all_colors_become_gray_full_rgb_circle_white.png)

A generative artwork containing every possible RGB color exactly once within a circular perceptual field.

## Concept

This artwork contains every possible RGB color combination exactly once.

Each pixel represents a unique and irreducible color identity.  
However, when all colors coexist simultaneously at sufficient density, the human eye perceives the image as an almost uniform gray field.

The work explores a paradox of perception:

> Extreme diversity may converge into perceptual uniformity.

Rather than rejecting diversity itself, the artwork examines the limits of human perception, consensus, averaging, entropy, and distinction within highly heterogeneous systems.

The circular composition symbolizes a closed perceptual universe in which objective diversity exists physically, while subjective uniformity emerges perceptually.

---

## Technical Structure

- Canvas size: 5000 × 5000
- Shape: Circular RGB field
- Total RGB colors:
  
  16,777,216

- RGB usage rule:
  
  Every possible RGB color appears exactly once.

- Background:
  
  White

---

## Files

| File | Description |
|---|---|
| `all_colors_become_gray_full_rgb_circle_white.png` | Full-resolution archival artwork |
| `generate_full_rgb_circle.py` | Artwork generation code |
| `check_full_rgb.py` | RGB completeness verification script |
| `ARTIST_STATEMENT.md` | Extended conceptual statement |
| `LICENSE` | Copyright and usage restrictions |

---

## Verification

The included verification script confirms that the artwork contains all possible RGB colors exactly once.

Expected verification result:

```text
unique colors: 16777216
SUCCESS
Every possible RGB color exists exactly once.
