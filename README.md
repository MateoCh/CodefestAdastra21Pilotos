# P21 -  Procesamiento de imagenes satelitales

P21 es una libreria open-source que ofrece funcionalidades para el procesamiento de imagenes aéreas y satelitales. Especificamente, la libreria ofrece las siguientes funciones: 

1. Alterar las coordenadas geográficas de una imagen. 

2. Reducir el tamaño de una imagen a hasta un 5% de la imagen inicial, teniendo en cuenta que la imagen se pueda previsualizar y sea útil aún cuando se pierda el tamaño del pixel.

3. Comprimir una imagen en relación 1/10 manteniendo al calidad y tamaño del pixel.

Primero, se debe clonar o descargar el repositorio para usar las funcionalidades. 

Para utilizar la libreria, el usuario debe instalar las dependencias que se encuentran en requirements.txt utilizando el comando: 

```
pip install requirements.txt
```
Luego, se debe localizar cual de los tres archivos corresponde con la funcionalidad deseada para el proyecto. 

1. ofuscate-image.py: Se encuentra la funcionalidad de alterar las coordenadas geográficas de una imagen para evitar accesos indeseados de información. El método debe recibir por parámetro los siguientes valores: 

  1.1. originalFile: String con ubicación de la imagen satelital que a procesar.
  1.2. newFile: String con ubicación que tendrá el nuevo archivo con las coordenadas ofuscadas.
  1.3. min: Límite inferior donde se ofuscarán las coordenadas de la imagen dada.
  1.4. max: Límite superior donde se ofuscarán las coordenadas de la imagen dada.
  
Al finalizar el método, debe quedar la imagen con coordenadas ofuscadas en la ubicación indicada por parámetro.

2. 

3. 

