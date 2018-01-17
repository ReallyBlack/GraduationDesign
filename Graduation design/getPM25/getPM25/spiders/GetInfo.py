import scrapy
from scrapy.linkextractors import LinkExtractor
import time
from ..items import CityPM25InfoItem


class GetInfoSpider(scrapy.Spider):
    # 网络爬虫名称
    name = "getInfo"
    # 定义不被过滤的域名，避免爬取错误信息
    allowed_domains = ["www.pm25.in"]
    # 定义爬虫的起始页面
    start_urls = ['http://www.pm25.in/']

    # 定义爬取网页函数
    def parse(self, response):
        le = LinkExtractor(restrict_css='div.all a')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_getinfo)
            time.sleep(0.1)
        pass

    # 定义获得每个城市信息的函数
    def parse_getinfo(self, response):
        city_info = CityPM25InfoItem()
        city_info['name'] = response.css('div.city_name h2')\
            .xpath('./text()').extract_first()  # 城市名称
        ls = response.css('tbody tr')  # 数据位置的父标签处剪切全部数据
        for l in ls:
            p = l.xpath('./td/text()').extract()  # 得到每一组数据信息
            if p[1] != '_':
                city_info['MonitoringStations'] = p[0]
                city_info['AQI'] = p[1]  # AQI指数
                city_info['AirQuality'] = p[2]  # 空气质量指数类别
                if p[3] == p[-10]:
                    p3 = p[3].replace('\n', '')
                    p3 = p3.replace(' ', '')
                    p4 = p[4].replace('\n', '')
                    p4 = p4.replace(' ', '')
                    city_info['pollutants'] = p3 + '\n' + p4  # 主要污染物
                else:
                    city_info['pollutants'] = p[3]  # 主要污染物
                city_info['PM25'] = p[-7]  # PM2.5细颗粒物
                city_info['PM10'] = p[-6]  # PM10可吸入颗粒物
                city_info['CO'] = p[-5]  # 一氧化碳
                city_info['NO2'] = p[-4]  # 二氧化氮
                city_info['O31'] = p[-3]  # 臭氧一小时平均
                city_info['O38'] = p[-2]  # 臭氧八小时平均
                city_info['SO2'] = p[-1]  # 二氧化硫
                yield city_info
        pass
