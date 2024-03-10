from PIL import Image
from pathlib import Path

from _utils import compare


current_file = Path(__file__).resolve()
for im in current_file.glob("*.jpg"):
    Image.open(im)
    im.split[i]