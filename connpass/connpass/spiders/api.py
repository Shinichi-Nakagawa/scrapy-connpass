# -*- coding: utf-8 -*-
import json
import scrapy

from connpass.items import EventItem


class ApiSpider(scrapy.Spider):
    name = 'api'
    allowed_domains = ['connpass.com']
    start_urls = []

    def __init__(self, **kwargs):
        # パラメータにクエリ文字列があれば設定
        if not kwargs:
            self.start_urls.append('https://connpass.com/api/v1/event/')
        else:
            query = '&'.join([ '{k}={v}'.format(k=k, v=v) for k, v in kwargs.items()])
            self.start_urls.append('https://connpass.com/api/v1/event/?{}'.format(query))

    def item_event(self, event: dict)-> EventItem:
        """
        イベント情報
        :param event: イベント情報(APIの戻り)
        :return: Scrapyのイベントアイテム
        """
        i = EventItem()
        i['event_id'] = event.get('event_id')
        i['title'] = event.get('title')
        i['description'] = event.get('description')
        i['catch'] = event.get('catch')
        i['hash_tag'] = event.get('hash_tag')
        i['event_url'] = event.get('event_url')
        i['started_at'] = event.get('started_at')
        i['ended_at'] = event.get('ended_at')
        i['limit'] = event.get('limit')
        i['event_type'] = event.get('event_type')
        i['series'] = json.dumps(event.get('series'), ensure_ascii=False)
        i['address'] = event.get('address')
        i['place'] = event.get('place')
        i['lat'] = event.get('lat')
        i['lon'] = event.get('lon')
        i['owner_id'] = event.get('owner_id')
        i['owner_nickname'] = event.get('owner_nickname')
        i['owner_display_name'] = event.get('owner_display_name')
        i['accepted'] = event.get('accepted')
        i['waiting'] = event.get('waiting')
        i['updated_at'] = event.get('updated_at')
        return i

    def parse(self, response):
        """
        responseを取得
        仕様は以下を参照
        https://connpass.com/about/api/
        """
        body = json.loads(response.body)
        events = body.get('events', [])
        for event in events:
            yield self.item_event(event)
