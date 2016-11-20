#coding:utf-8
__author__ = 'jiliwei'

class UrlManager(object):
    def __init__(self):
        # 待爬取的url列表
        self.new_urls = set()
        # 爬取过的url列表
        self.old_urls = set()

    # 添加单个url到url管理器
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 批量添加url到url管理器
    def add_new_urls(self,urls):
      if urls is None or len(urls)==0:
          return
      for url in urls:
          self.add_new_url(url)

    # 判断管理器中是否有新的待爬取的URL
    def has_new_url(self):
        return len(self.new_urls)!=0
    # 获取待爬取的URL
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return  new_url

