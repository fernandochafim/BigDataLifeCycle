#!/usr/bin/env bash

source /home/fernandovcb/virtualenvs/scrapy/bin/activate

scrapy crawl YoutubeTrending -o /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/json/youtubetrending_$(date +"%Y%m%d").json