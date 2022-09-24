# Databricks notebook source


# COMMAND ----------



# COMMAND ----------

from osgeo import gdal
gdal.UseExceptions()

input_file = gdal.Open('/dbfs/mnt/prueba1/type2/tif/recorte_1_m120_l4_20181228_rgbnn.tif')
output = 'output/test1.tif'

topts = gdal.TranslateOptions(creationOptions=['COMPRESS=LZW', 'QUALITY=10', 'PREDICTOR=2', 'BIGTIFF=YES'])
ds = gdal.Translate(output, input_file, options=topts)

from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobClient # también en ASINC
connection_string = "DefaultEndpointsProtocol=https;AccountName=los21pilotosdatabase;AccountKey=fzRp4YPNvJsywbSJkiyhLQpfb1UycCbVEwKJWJ04Zso8RpNXqRa1b46EHqvtcFWvgPzzGmRmcTg9+AStsY2VIA==;EndpointSuffix=core.windows.net"
# Importante, STR conexión, el nombre del contenedor, nombre del archivo como va a quedar guardado
service = BlobServiceClient.from_connection_string(conn_str=connection_string)
blob = BlobClient.from_connection_string(conn_str=connection_string,container_name="container", blob_name = 'prueba1.tif')

with open("/databricks/driver/output/test1.tif", "rb") as data:
    blob.upload_blob(data)

# COMMAND ----------

# MAGIC %sh 
# MAGIC pwd
# MAGIC cd output
# MAGIC ls -lh

# COMMAND ----------

# Ejemplo de conexión


# COMMAND ----------



# COMMAND ----------


