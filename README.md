# P21 -  Procesamiento de imagenes satelitales

P21 es una libreria open-source que ofrece funcionalidades para el procesamiento de imagenes aéreas y satelitales. Especificamente, la libreria ofrece las siguientes funciones: 

1. Alterar las coordenadas geográficas de una imagen. 

2. Reducir el tamaño de una imagen a hasta un 5% de la imagen inicial, teniendo en cuenta que la imagen se pueda previsualizar y sea útil aún cuando se pierda el tamaño del pixel.

3. Comprimir una imagen en relación 1/10 manteniendo al calidad y tamaño del pixel.

Primero, se debe clonar o descargar el repositorio para usar las funcionalidades. 

Para utilizar la libreria, el usuario debe instalar las dependencias que se usan en el proyecto. Entre estas encontramos, rasterio, quantumrandom, entre otras. Si no posee alguna en su entorno de trabajo, se debe instalar usando el siguiente comando o equivalentes donde **** corresponde al nombre de la dependencia a descargar:

```
pip install ****
```

Luego, se debe localizar cual de los tres archivos corresponde con la funcionalidad deseada para el proyecto. 

1. ofuscate-image.py: Se encuentra la funcionalidad de alterar las coordenadas geográficas de una imagen para evitar accesos indeseados de información. El método debe recibir por parámetro los siguientes valores: 

   - originalFile: String con ubicación de la imagen satelital que a procesar. 
   - newFile: String con ubicación que tendrá el nuevo archivo con las coordenadas ofuscadas.
   - min: Límite inferior donde se ofuscarán las coordenadas de la imagen dada.
   - max: Límite superior donde se ofuscarán las coordenadas de la imagen dada.
   
   Al finalizar el método, debe quedar la imagen con coordenadas ofuscadas en la ubicación indicada por parámetro.
   
   Para convocarlo, debe ubicar el archivo donde desee ejecutarlo y usar el siguiente comando: 
   ```
   python ofuscate-image.py ofuscateImage <originalFile> <newFile> <min> <max>  
   ```
   
2. previsualize-image.py: Se encuentra la funcionalidad de reducir el tamaño de una imagen a hasta un 5% de la imagen inicial, teniendo en cuenta que la imagen se pueda previsualizar. El método debe recibir por parámetro los siguientes valores: 

   - originalFile: String con ubicación de la imagen satelital que a procesar. 
   - newFile: String con ubicación que tendrá el nuevo archivo con las coordenadas ofuscadas.
   
   Al finalizar el método, debe quedar la imagen procesada en la ubicación indicada por parámetro.
   
   Para convocarlo, debe ubicar el archivo donde desee ejecutarlo y usar el siguiente comando: 
   ```
   python previsualize-image.py previsualize <originalFile> <newFile>
   ```

3.1. compress-image-30.py: Se encuentra la funcionalidad de comprimir sin pérdida de calidad pero en una razón de compresión menor a la esperada en el reto, siendo actualmente 3/10 y no 1/10. Por esta razón y porque consideramos que aún puede ser mejorada a nivel de optimización (como se verá en el segundo archivo "compress-image-window.py") no es funcional ni generica.

3.2. compress-image-window.py: En este archivo se verá un proceso de compresión analizando los archivos origen en forma de ventana para hacer el proceso más óptimo pero debido a falta de tiempo para el desarrollo consideramos que esta funcionalidad se encuentra en desarrollo por lo que no es accesible como funci{on.
