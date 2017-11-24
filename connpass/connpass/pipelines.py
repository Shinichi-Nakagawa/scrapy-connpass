# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from scrapy.exceptions import DropItem


class ConnpassPipeline(object):

    CREATE_TABLE_EVENT ="""
    CREATE TABLE event (
      event_id integer primary key,
      title text ,
      catch text ,
      description text ,
      event_url text,
      hash_tag text ,
      started_at date ,
      ended_at date ,
      _limit integer ,
      event_type text ,
      series text ,
      address text ,
      place text ,
      lat real ,
      lon real ,
      owner_id integer ,
      owner_nickname text ,
      owner_display_name text ,
      accepted integer ,
      waiting integer ,
      updated_at date ,
      create_date date,
      update_date date
    )
    """

    INSERT_EVENT = """
    insert into event(
    event_id, 
    title, 
    catch, 
    description, 
    event_url, 
    hash_tag, 
    started_at, 
    ended_at, 
    _limit, 
    event_type, 
    series, 
    address, 
    place, 
    lat, 
    lon, 
    owner_id, 
    owner_nickname, 
    owner_display_name, 
    accepted,
    waiting,
    updated_at,
    create_date,
    update_date
    ) 
    values(
    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
    datetime('now', 'localtime'), 
    datetime('now', 'localtime')
    )
    """

    DATABASE_NAME = 'connpass.db'
    conn = None

    def __init__(self):
        """
        Tableの有無をチェック,無ければ作る
        """
        conn = sqlite3.connect(self.DATABASE_NAME)
        if conn.execute("select count(*) from sqlite_master where name='event'").fetchone()[0] == 0:
            conn.execute(self.CREATE_TABLE_EVENT)
        conn.close()

    def open_spider(self, spider):
        """
        初期処理(DBを開く)
        :param spider: ScrapyのSpiderオブジェクト
        """
        self.conn = sqlite3.connect(self.DATABASE_NAME)

    def process_item(self, item, spider):
        """
        成績をSQLite3に保存
        :param item: Itemの名前
        :param spider: ScrapyのSpiderオブジェクト
        :return: Item
        """
        # Spiderの名前で投入先のテーブルを判断
        if spider.name == 'api':
            # ひたすらイベントを投入
            self.conn.execute(
                self.INSERT_EVENT,(
                    item['event_id'],
                    item['title'],
                    item['description'],
                    item['catch'],
                    item['event_url'],
                    item['hash_tag'],
                    item['started_at'],
                    item['ended_at'],
                    item['limit'],
                    item['event_type'],
                    item['series'],
                    item['address'],
                    item['place'],
                    item['lat'],
                    item['lon'],
                    item['owner_id'],
                    item['owner_nickname'],
                    item['owner_display_name'],
                    item['accepted'],
                    item['waiting'],
                    item['updated_at'],
                )
            )
            self.conn.commit()
        else:
            raise DropItem('spider not found')
        return item

    def close_spider(self, spider):
        """
        終了処理(DBを閉じる)
        :param spider: ScrapyのSpiderオブジェクト
        """
        self.conn.close()