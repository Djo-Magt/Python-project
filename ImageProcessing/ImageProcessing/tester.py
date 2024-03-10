from PIL import Image
from pathlib import Path

SOURCE_FILE = Path(__file__).resolve()
SOURCE_DIR = SOURCE_FILE.parent
source_im = SOURCE_DIR/"01-Les bases"/"05-Exercices"

homme = Image.open(Path(f'{source_im}/homme.png'))
homme_new = Image.new("RGB", homme.size, "green")
homme_new.paste(homme, homme)
homme_new.save(Path(f"{source_im}/homme_vert.jpg"))

# rose = Image.open(Path(f"{source_im}/rose.jpg"))
# rose.transpose(Image.ROTATE_90).save(Path(f"{source_im}/rose-rotate.jpg"))
# rose.show()