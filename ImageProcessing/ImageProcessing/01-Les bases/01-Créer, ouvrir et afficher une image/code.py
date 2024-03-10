from PIL import Image
from pathlib import Path
# Création d'une nouvelle image
im = Image.new("RGBA", (1920, 1080), "#ff0000")
# im.show()
SOURCE_FILE = Path(__file__).resolve()
SOURCE_DIR = SOURCE_FILE.parent.parent.parent

image = Image.open(Path(f"{SOURCE_DIR}/_images/rose.jpg"))
image.show()
