#coding:utf-8
__author__ = 'jiliwei'

import urllib2

class Downloader(object):
    def download(self,url):
        if url is None:
            return
        response = urllib2.urlopen(url)
        # print response.getcode()
        # print response.read()
        if response.getcode()!=200:
            return
        return response.read()