from PIL import Image
from pathlib import Path
import shutil

SOURCE_FILE = Path(__file__).resolve().parent
image_dir = SOURCE_FILE / "images"


for f in image_dir.glob("*.*"):
    largeur = Image.open(f).size[0]
    if largeur < 250:
        destination = (image_dir/"small")
    elif largeur < 500:
        destination = (image_dir/"medium")
    elif largeur < 1000:
        destination = (image_dir/"large")
    else :
        destination = (image_dir/"extra-large")
    f.rename(destination/f.name)