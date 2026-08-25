# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python", "tqdm"]
# ///

from typing import TypedDict
from dataclasses import dataclass
import sys

from tqdm.contrib.concurrent import process_map, thread_map

from cv2.typing import MatLike
import numpy as np
import cv2

from pathlib import Path

SIZE = (3626, 2040)

from bg import Colors, colors, light, dark

def get_img(file) -> MatLike:
    img = cv2.imread(file, cv2.IMREAD_COLOR_RGB)
    assert img is not None, f"Failed to load image: {file}"
    return img[:,:,:]/255

def hex(color: str):
    color = color.lstrip("#")
    return np.array(tuple(int(color[i:i+2], 16)/255 for i in (0, 2, 4)))


def blend(a, b, alpha):
    return b * (1 - alpha) + a * alpha

def multiply(a, b, alpha):
    return blend(
        (a * b),
        a, alpha,
    )

def add(a, b, alpha):
    return blend(
        np.clip(a + b, 0, 1),
        a, alpha
    )

def screen(a, b, alpha):
    return blend(
        1 - (1-a) * (1-b),
        a, alpha
    )

def soft_light(a, b, alpha):
    return blend(
        (1 - 2*b)*a*a + 2*b*a,
        a, alpha
    )


img_paths = sorted(Path("./out/").rglob("*.png"))

imgs_vals = thread_map(get_img, img_paths)
imgs = dict(zip(img_paths, imgs_vals))

layers = {path: img for path, img in imgs.items() if "layers" in str(path)}

def generate(imgs, c: Colors):
    res = np.zeros((SIZE[1], SIZE[0], 3), dtype=np.float32)
    res[:,:,:] = c.dark

    for file, alpha in layers.items():
        print(f"Processing {file.name}")

        color_name = file.stem.split("-")[1]
        color = getattr(c, color_name, None)
        assert color is not None, f"Color {color_name} not found in Colors class"

        res = alpha * color + (1 - alpha) * res

    res = multiply(res, c.shadow, imgs[Path("./out/fx/18-shadows.png")] * 0.35)
    res = soft_light(res, c.yellow, imgs[Path("./out/fx/19-window-hl.png")] * 1)
    res = multiply(res, c.shadow, imgs[Path("./out/fx/20-ao.png")] * 0.25)
    res = screen(res, c.blue, imgs[Path("./out/fx/21-screen.png")] * 0.12)
    res = soft_light(res, c.yellow, imgs[Path("./out/fx/22-bloom-yellow.png")] * 0.6)
    res = soft_light(res, c.blue, imgs[Path("./out/fx/23-bloom-blue.png")] * 0.8)
    # res = soft_light(res, c.blue, imgs[Path("./out/fx/23-bloom-blue.png")]*8)

    la = add(hex("#000000"), c.lightest, imgs[Path("./out/fx/25-lineart-hl.png")])
    res = blend(la, res, imgs[Path("./out/fx/24-lineart.png")])
    return res

theme = sys.argv[1]

out = generate(imgs, colors[theme])
cv2.imwrite("out.png", cv2.cvtColor((out*255).astype(np.uint8), cv2.COLOR_BGR2RGB))
