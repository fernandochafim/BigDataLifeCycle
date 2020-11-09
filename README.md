<img src=https://github.com/fernandochafim/BigDataLifeCycle/raw/main/img/ProjectName.png width=560/>
===========
This practice was started under the context of the course "**Data Typology and Lifecycle**" (**Tipología y ciclo de vida de los datos**), belonging to the Master in Data Science of the Open University of Catalonia (UOC).

<span class="get-badge" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Get the DOI badge!">
    <img data-toggle="modal" data-target="[data-modal='10.5281-zenodo.4256746']" src="https://zenodo.org/badge/310364287.svg" alt="10.5281/zenodo.4256746">
  </span>

## Goal

**Creation of a dataset from the data contained in a web.**
It means apply web scraping as data collection. Web scrapers are computer programs that extract information from web sites. The structure and content of a web page are encoded in Hypertext Markup Language (HTML), which you can see using your browser’s ‘view source’ or ‘inspect element’ function. A scraper understands HTML, and is able to parse and extract information from it. 

### 1. Context 

The first part of any Artificial Intelligence (Computer Vision and Natural Language Processing) project is to get a database. Indeed, having the whole dataset cleaned and labeled only applies on Kaggle, not in real life. Youtube cover images, videos, comments, and information such as likes, dislikes, views, and others represent a great and underused source of data.

Knowing all this, this project aims to start developing a sample of this dataset to be explored to design artificial intelligence applications.

### 2- Dataset Title

[**SampleYoutubeTrendingPT**](https://zenodo.org/record/4256746#.X6bRkmhKiUk)

### 3 - Abstract / Description

YouTube (the world-famous video sharing website) maintains a list of the top trending videos on the platform. According to [Variety magazine](http://variety.com/2017/digital/news/youtube-2017-top-trending-videos-music-videos-1202631416/), “To determine the year’s top-trending videos, YouTube uses a combination of factors including measuring users interactions (number of views, shares, comments, and likes).
The presented dataset is composed of two sequences of files scraped daily named 'youtubetrending_tabular_YYYYMMDD.csv'
and 'youtubetrending_YYYYMMDD.csv'. The first contains 18 columns of fundamental video characteristics; the second contains 3 columns about youTube video thumbnail images.

We used scrapy because it's the most powerful open source library to collect web data and selenium. After all, youtube there is a lot of javascript on its page, and selenium is interesting to gather information correctly from this kind of web. Selenium is considerably slow and will be replaced in a future version to splash.

Our algorithm goes to the trending page in Portuguese from Portugal to gather the URL of the videos listed. After that, it goes to each page to collect the relevant information from each video.

### 4 - Content

#### 4A - Tabular set 

Attribute Information:

* title = Youtube video title
* url = Youtube video URL
* views = Youtube video views
* duration = Youtube video duration
* likes = Youtube video likes
* dislikes = Youtube video dislikes
* channelName = channel name
* subscribers = number of subscribers
* description = Youtube video description
* keywords = keywords
* date_published = Youtube video published date
* date_scraped = date when the information was collected
* tags = tags
* comments = comments
* image_urls = Youtube video image url
* path = relative path to where the image jpg data was stored
* checksum = a MD5 hash of the image contents
* status = the file status indication.

#### 4B - Image set

It's a collection of YouTube Video thumbnail images. Each image in the dataset was serialized as a Base64 string and therefore represented in a tab-separated csv file, consisting of three values:

* The  [Universally Unique Identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) (UUID) of the image.
* The original path to the image on disk.
* The image itself serialized as a Base64 string.

#### 4C - Text set

**TODO**

This part will be developed soon. For now, we scraped only the first comment for testing purposes.

### 5 - Graphic Representation / Profiling of dataset

![](img/out.png?raw=true)

### 6 - Acknowledgment

I would like to extend my sincere thanks to:

[the Video Understanding group within Google Research](https://research.google.com/youtube8m/people.html).

[Karan Murthy](https://github.com/karanmurthy7/youtube-tag-recommender)

### 7 - Inspiration

This dataset aims to be useful for Artificial Intelligence analytics such as Time Series Forecastings (expected number of views in N days), Regression (predict the best duration), and Classification tasks (automatize tags),... Combine image, text, and tabular data in the same model is one of the main sources of inspiration to start this data collection.

Just with the image set, we can apply:

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

### 8 - License

<div style="float: left; margin-right: 1em;">
  <img src="https://i.creativecommons.org/p/zero/1.0/88x31.png" alt="CC0">
</div>

**Released Under CC0: Public Domain License**

We choose this license because CC0 imposes no legal obligation to provide attribution, courtesy, good practice, norms, and community expectations often mean that you should give credit anyway. Giving proper credit helps others understand the origin of the text so they can learn more and identify any changes that have been made.

### Manual Steps

These steps were done manually for testing purposes but it will be automated using Apache Airflow /dags/youtube_dag.py

Activate my virtual enviroment

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

#### Data Lake - Hadoop

**TODO**

Hadoop is an open-source framework used for storing large bulks of data and running applications on this data across clusters of commodity hardware machines. The Hadoop framework ships with everything you need to develop full-fledged, end-to-end applications, including programs and tools to load data into HDFS (the Hadoop filesystem), execute MapReduce jobs, and monitor the jobs as they run.

**Hadoop Distributed File System (HDFS)**: HDFS is the Java-based filesystem for Hadoop. Using HDFS, we can store data across multiple machines.

![](img/HDFS.png?raw=true)

```bash
fernandovcb@DESKTOP-5A84P9I:~/hadoop/hadoop-3.2.0$ jps
1136 NameNode
3090 ResourceManager
3282 NodeManager
3714 Jps
1620 SecondaryNameNode
1322 DataNode
```

```bash
fernandovcb@DESKTOP-5A84P9I:~/hadoop/hadoop-3.2.0$ hadoop fs -ls /user
Found 1 items
drwxr-xr-x   - fernandovcb supergroup          0 2020-10-11 22:12 /user/hive
```

```bash
fernandovcb@DESKTOP-5A84P9I:~/hadoop/hadoop-3.2.0$ hdfs dfs -mkdir /user/trending_analytics
fernandovcb@DESKTOP-5A84P9I:~/hadoop/hadoop-3.2.0$ hdfs dfs -mkdir /user/trending_analytics/raw_data
```


```bash
hdfs dfs -ls /user/guru/faces/input
```
