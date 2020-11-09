#!/usr/bin/env bash

mkdir /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/images/$(date +"%Y%m%d")

mv -v /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/full/* /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/images/$(date +"%Y%m%d")

/home/fernandovcb/virtualenvs/scrapy/bin/python /mnt/d/BigDataLifeCycle/dags/dataprocessing/prepare_image_dataset.py -d /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/images/$(date +"%Y%m%d") -o /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/img_encoded/youtubetrending_$(date +"%Y%m%d").csv

/home/fernandovcb/virtualenvs/scrapy/bin/python /mnt/d/BigDataLifeCycle/dags/dataprocessing/prepare_tabular_dataset.py -d /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/json/youtubetrending_$(date +"%Y%m%d").json -o /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/csv/youtubetrending_tabular_$(date +"%Y%m%d").csv

/home/fernandovcb/virtualenvs/scrapy/bin/python /mnt/d/BigDataLifeCycle/dags/dataprocessing/prepare_tabular_profiling.py -d /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/csv/youtubetrending_tabular_$(date +"%Y%m%d").csv -o /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/data_profiling/tabular_report_$(date +"%Y%m%d").html