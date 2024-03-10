from pathlib import Path
import json

J_FILE = Path(__file__).resolve().parent/"exo"/"test.json"


with open(J_FILE, 'r') as f:
    liste = json.load(f)

liste.append(4)

with open(J_FILE, 'w') as f:
    json.dump(liste,f,indent=4)

