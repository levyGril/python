#coding:utf-8
__author__ = 'jiliwei'

import url_manager,html_downloader,html_parser,html_outputer


class SpiderMain(object):
    def __init__(self):
        # 初始化URL管理器，下载器，解析器，输出器
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.Downloader()
        self.parser = html_parser.Htmlparser()
        self.outputer = html_outputer.Htmloutputer()

    def craw(self,root_url):
        # 计数器
        count =1
        # url添加进url管理器
        self.urls.add_new_url(root_url)
        # 判断url管理器中是否有待爬取得URL
        while self.urls.has_new_url():
            try:
                # 从 URL管理器中获取url
                new_url = self.urls.get_new_url()
                print 'craw %d:%s'%(count,new_url)
                # 页面下载器下载该url的静态html
                html_cont = self.downloader.download(new_url)
                # print html_cont
               # 解析器解析
                new_urls, new_data = self.parser.parse(new_url,html_cont)

                # print new_urls

                #新的url再次添加到url管理器
                self.urls.add_new_urls(new_urls)
                # 将获取的数据加载到输出器
                self.outputer.collect_data(new_data)
                if count==1000:
                    break
                count = count+1
            except:
                print 'craw fail'
        # 输出收集好的数据
        self.outputer.output_html()

if __name__=='__main__':

    root_url="http://baike.baidu.com/view/21087.htm"

    obj_spider = SpiderMain() #爬虫总调度函数
    obj_spider.craw(root_url)

