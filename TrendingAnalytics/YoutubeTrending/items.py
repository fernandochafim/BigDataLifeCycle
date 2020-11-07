# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class YoutubeTrendingItem(Item):

    """
    The class defines the item model to store the extracted data from YouTube
    """

    title = Field()
    url = Field()
    views = Field()
    duration = Field()
    likes = Field()
    dislikes = Field()
    channelName = Field()
    subscribers = Field()
    description = Field()
    keywords = Field()
    date_published = Field()
    date_scraped = Field()
    tags = Field()
    #n_comments = Field()
    comments = Field()
    image_urls = Field()
    images = Field()

