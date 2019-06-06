# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os

class PttPipeline(object):
    def __init__(self):
        self.path = os.path.join(os.getcwd(),'data')
        self.check_path()

    def process_item(self, item, spider):
        data = []
        for key,val in item.items():
            data.append(val)

        with open(os.path.join(self.path ,item['push_userid'] + '.csv' ),'a+' ,encoding='utf8' ,newline='') as fp:
            writer = csv.writer(fp)
            writer.writerow(data)

        return item

    def check_path(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
