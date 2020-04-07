# -*- coding: utf-8 -*-

# import csv
#
# from .items import Book
#
#
# class FilterDuplicateItemsPipeline(object):
#     skip_headers = False
#     csvwriter = csv.writer(open('file.csv', 'w', newline=''))
#
#     def open_spider(self, spider):
#         if not self.skip_headers:
#             header_keys = Book.fields.keys()
#             self.csvwriter.writerow(header_keys)
#             self.skip_headers = True
#
