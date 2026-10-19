
from pathlib import Path

dossier = Path(__file__).parent / "test_files"

for fichier in dossier.iterdir():
    if fichier.is_file():
        print(fichier.name)
