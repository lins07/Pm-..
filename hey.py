import os
from PIL import Image


def mostrar_imagens(cifras):
    for cifra in cifras.split():
        caminho = os.path.join("imagens", f"{cifra}.png")
        if os.path.exists(caminho):
            print(f"Mostrando imagem de {cifra}...")
            img = Image.open(caminho)
            img.show()
        else:
            print(f"Imagem de {cifra} não encotrada.")


# ---------- Execução ----------
entrada = input("Digite as cifras separadas por espaço (ex: C Dm G7):")
mostrar_imagens(entrada)
