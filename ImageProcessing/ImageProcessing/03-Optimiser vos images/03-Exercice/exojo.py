from PIL import Image
from pathlib import Path

SOURCE_DIR = Path(__file__).resolve().parent
images = SOURCE_DIR.glob("*.jpg")

facteurs = [2, 4]

for image in images:
    im = Image.open(image)
    nom = image.stem
    suffix = image.suffix

    for facteur in facteurs:
        x, y = im.size
        new_x, new_y = (round(x * facteur), round(y * facteur))
        im.resize((new_x, new_y))

        new_dir = (Path(__file__).parent/"vign")
        new_dir.mkdir(exist_ok=True)

        im.save(f"{new_dir}/{nom}-{new_x}x{new_y}{suffix}")
