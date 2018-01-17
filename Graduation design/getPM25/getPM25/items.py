# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class Getpm25Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 用于封装城市PM2.5信息的Item
class CityPM25InfoItem(Item):
    name = Field()  # 城市名称
    MonitoringStations = Field()  # 监测站
    AQI = Field()  # AQI指数
    AirQuality = Field()  # 空气质量指数类别
    pollutants = Field()  # 主要污染物
    PM25 = Field()  # PM2.5细颗粒物
    PM10 = Field()  # PM10可吸入颗粒物
    CO = Field()  # 一氧化碳
    NO2 = Field()  # 二氧化氮
    O31 = Field()  # 臭氧一小时平均
    O38 = Field()  # 臭氧八小时平均
    SO2 = Field()  # 二氧化硫
    Predict_list = [[0 for col in range(24)]for row in range(2)]

