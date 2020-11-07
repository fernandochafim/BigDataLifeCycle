# -*- coding: utf utf-8 -*-
from re import sub
from time import sleep, strptime
from datetime import timedelta, datetime
from scrapy import Spider
from scrapy.loader import ItemLoader
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from YoutubeTrending.items import YoutubeTrendingItem

class YoutubeTrendingSpider(Spider):
    name = 'YoutubeTrending'
    allowed_domains = ['youtube.com']

    def start_requests(self):
        self.driver = webdriver.Chrome('/mnt/d/BigDataLifeCycle/TrendingAnalytics/webdrivers/chromedriver.exe')
        self.driver.get('https://www.youtube.com/feed/trending?gl=PT&hl=pt')

        sel = Selector(text=self.driver.page_source)
        videos = sel.xpath('//*[@id="thumbnail"]/@href').extract()

        for video in videos:
            url = 'https://www.youtube.com{}'.format(video)
            sleep(10)
            yield Request(url, callback=self.parse)
        
        self.driver.quit()
    
    def parse(self, response):
        l = ItemLoader(item=YoutubeTrendingItem(), response=response)
        self.driver.get(response.url)
        self.driver.execute_script('window.scrollTo(1, 500);')
        sleep(5)
        self.driver.execute_script('window.scrollTo(1, 3000);')
        
        sel = Selector(text=self.driver.page_source)

        title = self.get_title(sel), #title,
        url = self.get_url(response), #url,
        views = self.get_views(sel), #views,
        duration = self.get_duration(sel), #duration,
        likes = self.get_likes(sel), #likes,
        dislikes = self.get_dislikes(sel), #dislikes,
        channelName = self.get_channel_name(sel), #channelName,
        subscribers = self.get_subscribers(sel), #subscribers,
        description = self.get_description(sel), #description,
        keywords = self.get_keywords(sel), #keywords,
        date_published = self.get_date_published(sel) , #date_published,
        date_scraped = self.get_date_scraped()
        tags = self.get_tags(sel), #tags,
        #n_comments = self.get_number_of_comments(sel), #n_comments,
        comments = self.get_comments(sel), #comments,
        image_urls = self.get_image_url(response), #[imageURL]

        l.add_value('title', title)
        l.add_value('url', url)
        l.add_value('views', views)        
        l.add_value('duration', duration)       
        l.add_value('likes', likes)
        l.add_value('dislikes', dislikes)
        l.add_value('channelName', channelName)
        l.add_value('subscribers', subscribers)
        l.add_value('description', description)        
        l.add_value('keywords', keywords)
        l.add_value('date_published', date_published)
        l.add_value('date_scraped', date_scraped)
        l.add_value('tags', tags)
        #l.add_value('n_comments', n_comments)
        l.add_value('comments', comments)
        l.add_value('image_urls', image_urls)

        yield l.load_item() #return l.load_item() 

    def get_title(self, selector):
        """
        Returns the Youtube page title, empty is not found.
        :param selector: Scrapy Selector of Fetched Page
        :return: title of page, empty if invalid entry
        """
        return selector.xpath('//meta[@name="title"]/@content').extract_first()
    
    def get_url(self, response):
        """
        Returns the Youtube page title, empty is not found.
        :param response: Fetched Page
        :return: title of page, empty if invalid entry
        """
        return response.request.url
    
    def get_views(self, selector):
        """
        Returns the number of views for a given YouTube url.
        :param selector: Scrapy Selector of Fetched Page
        :return: number of views, empty if not found
        """
        raw = selector.xpath('//*[@id="metadata-line"]/span[1]/text()').extract_first() #//yt-view-count-renderer/span[1]
        return int(sub('[^0-9]','', str(raw)))
    
    def get_duration(self, selector):
        """
        Returns the video's duration in seconds.
        :param selector: Scrapy Selector of Fetched Page
        :return: number of views, empty if not found
        """
        raw = selector.xpath('//span[@class="ytp-time-duration"]/text()').extract_first()
        x = strptime(raw, '%M:%S')
        duration_sec = timedelta(minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
        return duration_sec

    def get_likes(self, selector):
        """
        Returns the number of video's like.
        :param selector: Scrapy Selector of Fetched Page
        :return: number of views, empty if not found
        """
        raw = selector.xpath('//ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/*[@id="text"]/text()').extract_first()
        return int(sub('[^0-9]','', str(raw)))

    def get_dislikes(self, selector):
        """
        Returns the number of video's dislike.
        :param selector: Scrapy Selector of Fetched Page
        :return: number of views, empty if not found
        """
        raw = selector.xpath('//ytd-menu-renderer/div/ytd-toggle-button-renderer[2]/a/*[@id="text"]/text()').extract_first()
        return int(sub('[^0-9]','', str(raw)))
    
    def get_channel_name(self, selector):
        """
        Returns the youtube channel's name.
        :param selector: Scrapy Selector of Fetched Page
        :return: number of views, empty if not found
        """
        return selector.xpath('//ytd-channel-name/div/div/yt-formatted-string/a/text()').extract_first()
    
    def get_subscribers(self, selector):
        """
        Returns the channel's number of subscribers.
        :param selector: Scrapy Selector of Fetched Page
        :return: number of views, empty if not found
        """
        raw = selector.xpath('//*[@id="owner-sub-count"]/text()').extract_first()
        return int(sub('[^0-9]','', str(raw)))

    def get_description(self, selector):
        """
        Returns the video's description.
        :param selector: Scrapy Selector of Fetched Page
        :return: number of views, empty if not found
        """
        return selector.xpath("//meta[@name='description']/@content").extract_first()

    def get_keywords(self, selector):
        """
        Returns the video's keywords.
        :param selector: Scrapy Selector of Fetched Page
        :return: number of views, empty if not found
        """
        return selector.xpath("//meta[@name='keywords']/@content").get()

    def get_date_published(self, selector):
        """
        Returns the video's published date.
        :param selector: Scrapy Selector of Fetched Page
        :return: number of views, empty if not found
        """
        return selector.xpath("//meta[@itemprop='datePublished']/@content").get()
    
    def get_date_scraped(self):
        """
        Returns the scraped date time.
        :return: string representing date time in %d/%m/%Y %H:%M:%S format
        """
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def get_tags(self, selector):
        """
        Returns the video's tags.
        :param selector: Scrapy Selector of Fetched Page
        :return: number of views, empty if not found
        """
        return selector.xpath("//meta[@property='og:video:tag']/@content").getall()

    #def get_number_of_comments(self, selector):
    #    """
    #    Returns the number of comments.
    #    :param selector: Scrapy Selector of Fetched Page
    #    :return: number of views, empty if not found
    #    """
    #    raw = selector.xpath('//*[@id="count"]/yt-formatted-string/text()').extract_first()
    #    return int(sub('[^0-9]','', str(raw)))

    def get_comments(self, selector):
        """
        Returns a sample of most relevant comments.
        :param selector: Scrapy Selector of Fetched Page
        :return: string with comments
        """
        raw = selector.xpath('//*[@id="contents"]').xpath('//*[@id="content-text"]/text()').getall()
        return str(list(dict.fromkeys(raw)))

    def get_image_url(self, response):
        """
        Returns the image url.
        :param response: Fetched Page
        :return: number of views, empty if not found
        """
        url = response.request.url
        video_code = url[32:]
        return 'http://i4.ytimg.com/vi/{}/hqdefault.jpg'.format(video_code)
        #return ['http://i4.ytimg.com/vi/{}/hqdefault.jpg'.format(video_code)]
