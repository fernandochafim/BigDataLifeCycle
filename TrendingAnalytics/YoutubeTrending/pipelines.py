# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter
import os

#class ImageCrawlerPipeline(object):
#    def process_item(self, item, spider):
#        os.chdir('/mnt/d/BigDataLifeCycle/TrendingAnalytics/output')
#
#        if item['images'][0]['path']:
#            new_image_name = item['title'][0] + '.jpg'
#            new_image_path = 'full/' + new_image_name
#
#            os.rename(item['images'][0]['path'], new_image_path)

class YoutubeTrendingPipeline(object):

    #TODO
    def process_item(self, item, spider):
        return item
