# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EventItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    event_id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    catch = scrapy.Field()
    event_url = scrapy.Field()
    hash_tag = scrapy.Field()
    started_at = scrapy.Field()
    ended_at = scrapy.Field()
    limit = scrapy.Field()
    event_type = scrapy.Field()
    series = scrapy.Field()
    address = scrapy.Field()
    place = scrapy.Field()
    lat = scrapy.Field()
    lon = scrapy.Field()
    owner_id = scrapy.Field()
    owner_nickname = scrapy.Field()
    owner_display_name = scrapy.Field()
    accepted = scrapy.Field()
    waiting = scrapy.Field()
    updated_at = scrapy.Field()
