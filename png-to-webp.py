import os
from PIL import Image

def convert_png_to_webp(directory):
    # Vérifie si le dossier existe
    if not os.path.exists(directory):
        print(f"Erreur : Le dossier {directory} n'existe pas.")
        return

    # Parcourt tous les fichiers du dossier
    for filename in os.listdir(directory):
        if filename.lower().endswith(".png"):
            png_path = os.path.join(directory, filename)
            
            # Définit le nouveau nom (ex: image.png -> image.webp)
            webp_path = os.path.splitext(png_path)[0] + ".webp"

            try:
                # Ouvre l'image et sauvegarde en webp
                with Image.open(png_path) as img:
                    img.save(webp_path, "WEBP", quality=85) # Qualité à 85% (excellent compromis)
                
                print(f"Converti : {filename} -> {os.path.basename(webp_path)}")
                
                # OPTIONNEL : Supprime le fichier PNG original après conversion
                os.remove(png_path)
                
            except Exception as e:
                print(f"Erreur lors de la conversion de {filename} : {e}")

# Lancer la conversion dans ton dossier d'images
if __name__ == "__main__":
    # Ajuste le chemin selon ton architecture
    target_dir = "assets/scenes"
    convert_png_to_webp(target_dir)