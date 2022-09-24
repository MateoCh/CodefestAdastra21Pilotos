# Databricks notebook source
# Segunda y version mas optima

# COMMAND ----------

import rasterio as rio
from rasterio import windows

# Mediante este método se hace una búsqueda e investigación de como funcionan las ventanas haciendo uso de la librerio rasterio
def overlapping_blocks(src, overlap=0, band=1):
    nols, nrows = src.meta['width'], src.meta['height']
    big_window = windows.Window(col_off=0, row_off=0, width=nols, height=nrows)
    for ji, window in src.block_windows(band):

        if overlap == 0:
            yield ji, window

        else:
            col_off = window.col_off - overlap
            row_off = window.row_off - overlap
            width = window.width + overlap * 2
            height = window.height + overlap * 2
            yield ji, windows.Window(col_off, row_off, width, height).intersection(big_window)

# COMMAND ----------

import numpy as np
import rasterio
from rasterio.windows import get_data_window

# mediante este metodo se hace una exploracion de las ventanas mediante el uso de profile, para determinar el algoritmo de compresion por lzw
#
with rasterio.open('/dbfs/mnt/prueba1/type2/tif/recorte_1_m120_l4_20181228_rgbnn.tif') as src:
    window = get_data_window(src.read(1, masked=True))
#     r, g, b = src.read()

# # Combine arrays in place. Expecting that the sum will
# # temporarily exceed the 8-bit integer range, initialize it as
# # a 64-bit float (the numpy default) array. Adding other
# # arrays to it in-place converts those arrays "up" and
# # preserves the type of the total array.
# total = np.zeros(r.shape)

# for band in r, g, b:
#     total += band

# total /= 3

# Write the product as a raster band to a new 8-bit file. For
# the new file's profile, we start with the meta attributes of
# the source file, but then change the band count to 1, set the
# dtype to uint8, and specify LZW compression.
profile = src.profile
profile.update(dtype=rasterio.uint8, count=1, compress='lzw')

# with rasterio.open('example-total.tif', 'w', **profile) as dst:
#     dst.write(total.astype(rasterio.uint8), 1)

# COMMAND ----------

# En esta seccion se vuelve a intentar lo mismo, sin embargo, se obtiene un problema de MissingRequired:TIFF directory is missing required "StripOffsets" field.
# Una vez solucionado esto, se planteaba una solucion de separacion por ventanas mas el metodo de gdal, esto permite que la compresion se pueda hacer mas especifica y mejor, reduciendo el riesgo de que se pierda la calidad y tamaño de los pixeles.
with rasterio.open('/dbfs/mnt/prueba1/type2/tif/recorte_1_m120_l4_20181228_rgbnn.tif') as src:

    # Write an array as a raster band to a new 8-bit file. For
    # the new file's profile, we start with the profile of the source
    profile = src.profile

    # And then change the band count to 1, set the
    # dtype to uint8, and specify LZW compression.
    profile.update(
        dtype=rasterio.uint8,
        count=1,
        compress='lzw')

    with rasterio.open('/databricks/driver/output/test1.tif', 'w', **profile) as dst:
        dst.write(array.astype(rasterio.uint8), 1)
