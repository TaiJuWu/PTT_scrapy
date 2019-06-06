# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from PTT.items import PttItem



class GossipingSpider(CrawlSpider):
    name = 'Grad-ProbAsk'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Grad-ProbAsk/index.html']
    key_userid = ['q79236' ,'skyHuan' ,'magic83v' ,'TEPLUN']

    rules = (
        Rule(LinkExtractor(allow=r'.*/bbs/Grad-ProbAsk/index\d+.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'.*/bbs/Grad-ProbAsk/M\..+.html'), callback='parse_article', follow=False)
    )

    def parse_item(self, response):
        pass

    def parse_article(self ,response):
        push_userids = response.xpath('//span[contains(@class ,"push-userid")]/text()').getall()
        push_contents = response.xpath('//span[contains(@class ,"push-content")]/text()').getall()
        content = response.xpath('//span[@class="article-meta-value"]/text()').getall()
        article_title = content[2] 
        time = content[3]
        for push_userid,push_content in zip(push_userids,push_contents):
            # print(article_title,time ,push_userid , push_content)
            if push_userid in self.key_userid:
                #會自動打印到螢幕上
               yield PttItem(push_userid=push_userid ,push_content=push_content ,article_title=article_title ,time=time)
