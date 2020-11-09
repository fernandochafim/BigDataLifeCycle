<img src=https://github.com/fernandochafim/BigDataLifeCycle/raw/main/img/ProjectName.png width=560/>
===========

Esta práctica se inició en el marco de la asignatura **Tipología y ciclo de vida de los datos**, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya (UOC).

## Goal

**Creation of a dataset from the data contained in a web.**
It means apply web scraping as data collection. Web scrapers are computer programs that extract information from web sites. The structure and content of a web page are encoded in Hypertext Markup Language (HTML), which you can see using your browser’s ‘view source’ or ‘inspect element’ function. A scraper understands HTML, and is able to parse and extract information from it. 

**Creación de un dataset a partir de los datos contenidos en una web**.
Esto significa aplicar web scraping como recopilación de datos. Los web scrapers son programas informáticos que extraen información de sitios web. La estructura y el contenido de una página web están codificados en lenguaje de marcado de hipertexto (HTML), que se puede ver utilizando la función "ver fuente" o "inspeccionar elemento" de su navegador. Un raspador comprende HTML y es capaz de analizar y extraer información de él.

### 1. Contexto

La primera parte de cualquier proyecto de Inteligencia Artificial (Visión computacional y Procesamiento del Lenguaje Natural) es obtener una base de datos. De hecho, tener todo el conjunto de datos limpio y etiquetado solo se aplica en Kaggle, no en la vida real. Youtube tiene imágenes, videos, comentarios e información como likes, dislikes, número de visualizaciones y otras informaciones representan una gran fuente de datos infrautilizada.

Sabiendo todo esto, este proyecto tiene como objetivo comenzar a desarrollar una muestra de este conjunto de datos para ser explorado para diseñar aplicaciones de inteligencia artificial.

### 2- Título del dataset

[**SampleYoutubeTrendingPT**](https://zenodo.org/record/4256746#.X6bRkmhKiUk)

### 3 - Descripción

YouTube (el sitio web de fama mundial para compartir videos) mantiene una lista de los videos más populares de la plataforma. Según la [revista Variety] (http://variety.com/2017/digital/news/youtube-2017-top-trending-videos-music-videos-1202631416/), "Para determinar los videos de mayor tendencia del año, YouTube utiliza una combinación de factores que incluyen la medición de las interacciones de los usuarios (número de vistas, acciones, comentarios y me gusta)
El dataset que resulta de nuestro web scraping se compone de dos secuencias de archivos extraídos diariamente llamados 'youtubetrending_tabular_YYYYMMDD.csv'
y 'youtubetrending_YYYYMMDD.csv'. El primero contiene 18 columnas de características fundamentales de video; el segundo contiene 3 columnas sobre imágenes en miniatura de videos de YouTube.

Usamos scrapy porque es la biblioteca de código abierto más poderosa para recopilar datos web y Selenium. Después de todo, youtube tiene mucho javascript en su página, y esto hace con que Selenium sea interesante para recopilar información correctamente. El Selenium es considerablemente lento y será reemplazado en una versión futura para slash.

Nuestro algoritmo va a la página de tendencias en portugués de Portugal para recopilar la URL de los videos enumerados. Después de eso, va a cada página para recopilar la información relevante de cada video.

### 4 - Contenido

#### 4A - Dataset tabular 

Attribute Information:

* title = título del video de Youtube
* url = URL del video de Youtube
* views = vistas de videos de Youtube
* duration = duración del video de Youtube
* likes = "Me gusta" de videos de Youtube
* dislikes = "No me gusta" el video de Youtube
* channelName = nombre del canal
* suscribers = número de suscriptores
* description = descripción del video de Youtube
* keywords = palabras clave
* date_published = Fecha de publicación del video de Youtube
* date_scraped = fecha en que se recopiló la información
* tags = etiquetas
* comments = comentarios
* image_urls = URL de la imagen del video de Youtube
* path = ruta relativa a donde se almacenaron los datos jpg de la imagen
* checksum = un hash MD5 del contenido de la imagen
* status = la indicación del estado del archivo.


#### 4B - Dataset de Imágenes

Es una colección de imágenes en miniatura de videos de YouTube. Cada imagen del conjunto de datos se serializó como una cadena Base64 y, por lo tanto, se representó en un archivo csv separado por tabulaciones, que consta de tres valores:

* El [Identificador único universal] (https://en.wikipedia.org/wiki/Universally_unique_identifier) (UUID) de la imagen.
* La ruta original a la imagen en el disco.
* La propia imagen serializada como una cadena Base64.

El archivo es más grande que las imagenes pero es útil para accesar a esta información de manera rápida y eficiente en nuestro Data Lake Hadoop. También mantenemos las imágenes en formato jpg.

#### 4C - Dataset de Texto

**TODO**

Esta parte se desarrollará pronto. Por ahora, eliminamos solo el primer comentario con fines de prueba.

### 5 - Representación gráfica

![](img/out.png?raw=true)

### 6 - Reconocimiento

Me gustaría extender mi más sincero agradecimiento a:

[the Video Understanding group within Google Research](https://research.google.com/youtube8m/people.html).

[Karan Murthy](https://github.com/karanmurthy7/youtube-tag-recommender)

### 7 - Inspiration

Este conjunto de datos tiene como objetivo ser útil para análisis de Inteligencia Artificial como Predicciones de Series de Tiempo (número esperado de vistas en N días), Regresión (predecir la mejor duración) y tareas de Clasificación (automatizar etiquetas), ... Combinar imagen, texto y Los datos tabulares en el mismo modelo son una de las principales fuentes de inspiración para iniciar esta recopilación de datos.

Solo con las imágenes podemos:

* Faces detection
![](img/faces_detection.png?raw=true)

* Label detection
![](img/label_detection.png?raw=true)

* Object detection
![](img/object_detection.png?raw=true)

* Subject detection
![](img/subject_detection.png?raw=true)

* Text detection
![](img/text_detection.png?raw=true)

### 8 - Licencia

<div style="float: left; margin-right: 1em;">
  <img src="https://i.creativecommons.org/p/zero/1.0/88x31.png" alt="CC0">
</div>

**Released Under CC0: Public Domain License**

Elegimos esta licencia porque CC0 no impone ninguna obligación legal de proporcionar atribución, cortesía, buenas prácticas, normas y las expectativas de la comunidad a menudo significan que debe dar crédito de todos modos. Dar el crédito adecuado ayuda a otros a comprender el origen del texto para que puedan aprender más e identificar cualquier cambio que se haya realizado.

### Steps

Estos pasos se realizaron manualmente con fines de prueba, pero se automatizarán mediante Apache Airflow /dags/youtube_dag.py

```bash
source /home/fernandovcb/virtualenvs/scrapy/bin/activate
```

```bash
(scrapy) fernandovcb@DESKTOP-5A84P9I:/mnt/d/BigDataLifeCycle/TrendingAnalytics$ scrapy list
YoutubeTrending
```

```bash
(scrapy) fernandovcb@DESKTOP-5A84P9I:/mnt/d/BigDataLifeCycle/TrendingAnalytics$ scrapy list
YoutubeTrending
```

```bash
(scrapy) fernandovcb@DESKTOP-5A84P9I:/mnt/d/BigDataLifeCycle/TrendingAnalytics$ scrapy crawl YoutubeTrending -o /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/json/youtubetrending_$(date +"%Y%m%d").json
```

```bash
(scrapy) fernandovcb@DESKTOP-5A84P9I:/mnt/d/BigDataLifeCycle$ mkdir /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/images/$(date +"%Y%m%d")
```

```bash
(scrapy) fernandovcb@DESKTOP-5A84P9I:/mnt/d/BigDataLifeCycle$ mv -v /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/full/* /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/images/$(date +"%Y%m%d")
```

```bash
(scrapy) fernandovcb@DESKTOP-5A84P9I:/mnt/d/BigDataLifeCycle$ /home/fernandovcb/virtualenvs/scrapy/bin/python /mnt/d/BigDataLifeCycle/dags/dataprocessing/prepare_image_dataset.py -d /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/images/$(date +"%Y%m%d") -o /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/img_encoded/youtubetrending_$(date +"%Y%m%d").csv
```

```bash
(scrapy) fernandovcb@DESKTOP-5A84P9I:/mnt/d/BigDataLifeCycle$ /home/fernandovcb/virtualenvs/scrapy/bin/python /mnt/d/BigDataLifeCycle/dags/dataprocessing/prepare_tabular_dataset.py -d /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/json/youtubetrending_$(date +"%Y%m%d").json -o /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/csv/youtubetrending_tabular_$(date +"%Y%m%d").csv
```

```bash
(scrapy) fernandovcb@DESKTOP-5A84P9I:/mnt/d/BigDataLifeCycle$ /home/fernandovcb/virtualenvs/scrapy/bin/python /mnt/d/BigDataLifeCycle/dags/dataprocessing/prepare_tabular_profiling.py -d /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/csv/youtubetrending_tabular_$(date +"%Y%m%d").csv -o /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/data_profiling/tabular_report_$(date +"%Y%m%d").html
```

|        Contribuciones       | Firma            |
|:---------------------------:|------------------|
|     Investigación previa    | Fernando Chafim  |
| Redacción de las respuestas | Fernando Chafim  |
|      Desarrollo código      | Fernando Chafim  |

### DOI 

