# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter


class PriceRunnerSpidyPipeline:

    def __init__(self):
        print("jelly bean")
        self.connection = sqlite3.connect("products.db")
        self.cur = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Products (
            product_id TEXT PRIMARY KEY NOT NULL,
            product_name TEXT NOT NULL,
            product_sub_title TEXT NOT NULL,
            product_description TEXT NOT NULL,
            main_category TEXT NOT NULL,
            sub_category TEXT NOT NULL,
            price REAL NOT NULL,
            link TEXT NOT NULL,
            overall_rating REAL NOT NULL
             )
        ;""")

    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO products VALUES (
            ?,?,?,?,?,?,?,?,?
        )""",
                         (item["product_id"], item["product_name"], item["product_sub_title"],
                          item["product_description"], item["main_category"], item["sub_category"],
                          item["price"], item["link"], item["overall_rating"]), )
        self.connection.commit()
        return item
