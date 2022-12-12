
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3


class PriceRunnerSpidyPipeline:

    def __int__(self):
        self.connection = sqlite3.connect("products.db")
        self.curser = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.curser.execute("""CREATE TABLE IF NOT EXIST products (
            id TEXT PRIMARY KEY NOT NULL, 
            name TEXT NOT NULL, 
            sub_title TEXT NOT NULL, 
            description TEXT NOT NULL, 
            category TEXT NOT NULL, 
            sub_category TEXT NOT NULL, 
            price REAL NOT NULL, 
            link TEXT NOT NULL, 
            overall_rank REAL NOT NULL
             )
        ;""")

    def process_item(self, item, spider):
        print("//////////////////////")
        print(item)
        print("//////////////////////")
        # self.curser.execute("""INSERT OR IGNORE INTO products VALUES (
        #     ?,?,?,?,?,?,?,?,?
        # );
        # """)
        return item
