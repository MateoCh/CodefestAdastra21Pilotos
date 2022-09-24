# neccesary libraries
import rasterio
import quantumrandom
import affine
import time

# start ofuscate method


def ofuscateImage(originalFile, newFile, min, max):

    startTime = time.time()
    # Randomizer para escojer aleatoriamente como mover la imagen
    # Para mantenerse dentro de Colombia, se recomienda min = 50000 y max = 500000

    transX = quantumrandom.randint(50000, 500000)
    transY = quantumrandom.randint(50000, 500000)

    # Se lee la imagen original
    originalImg = rasterio.open(originalFile)

    # Translada la imagen dejandola con el tamaño y orientación original
    nTransform = originalImg.meta['transform'] * \
        affine.Affine.translation(transX, transY)

    # Escribe la imagen en un nuevo archivo
    with rasterio.open(newFile, mode="w",
                       driver=originalImg.meta['driver'],
                       height=originalImg.height,
                       width=originalImg.width,
                       count=originalImg.count,
                       dtype=originalImg.meta['dtype'],
                       crs=originalImg.crs,
                       transform=nTransform) as new_dataset:
        for i in range(1, originalImg.count+1):
            print(f'Procesando banda: {i}...')
            new_dataset.write(originalImg.read(i), i)
    endTime = time.time()
    duration = endTime - startTime
