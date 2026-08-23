# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python"]
# ///

from pathlib import Path
import cv2

output_dir = Path("./out")
output_dir.mkdir(exist_ok=True)

for path in Path("./transass").iterdir():
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    assert img is not None, f"Failed to read image: {path}"
    alpha = img[:, :, 3]
    cv2.imwrite(output_dir / path.name, alpha)


