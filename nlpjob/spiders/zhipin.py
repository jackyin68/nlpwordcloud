# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse

class ZhipinSpider(scrapy.Spider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=nlp&city=101020100&industry=&position=']

    def parse(self, response):
        urls = response.xpath('//div[@class="job-list"]//div[@class="primary-box"]/@href').getall()
        for url in urls:
            url = response.urljoin(url)
            yield Request(url=parse.urljoin(response.url, url), callback=self.parse_details)

        next_page = response.xpath('//div[@class="page"]//a[@class="next"]/@href').get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield Request(url=next_page, callback=self.parse)

    def parse_details(self, response):
        job_description = list(response.xpath('//div[@class="detail-content"]//div[@class="job-sec"][1]').getall())[0].strip()
        print(job_description)

