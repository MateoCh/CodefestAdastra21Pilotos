import rasterio
import numpy as np
import affine
import time
import sys

from rasterio.enums import Resampling


def previsualize(originalFile, newFile):
    # Inicia el temporizador para medir rendimiento del algoritmo
    start = time.time()
    # Se lee la imagen original
    originalImg = rasterio.open(originalFile)

    # Se reescala la iamgen para reducir su resolución
    # Factor de escalamiento
    scale = 1/95
    # Para mantener rotación y translación se usa el original y sobre ese se escala
    transform = originalImg.meta['transform']*affine.Affine.scale(1/scale)
    height = originalImg.height * scale
    width = originalImg.width * scale

    # Se obtiene la metadata original ya que se va a usar la misma a excepción del tamaño y transfrm
    profile = originalImg.profile
    profile.update(transform=transform,
                   driver=originalImg.meta['driver'],
                   height=height, width=width,
                   crs=originalImg.crs)

    # Se usa la función read de rasterio junto a la clase Resampling para aplicar la reducción en la resolución
    data = originalImg.read(
        out_shape=(int(originalImg.count), int(height), int(width)),
        resampling=Resampling.cubic)

    # Ya teniendo la imagen con menor resolución se guarda en archivo
    with rasterio.open(newFile, 'w', **profile) as destination:
        destination.write(data)
    # Se calcula el tiempo total que duró el algoritmo ejecutandose y se imprime
    end = time.time()
    time = end - start
    print(f'El programa tomó {time}')


if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
