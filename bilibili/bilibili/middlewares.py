# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from selenium import webdriver
from scrapy.http import HtmlResponse
from fake_useragent import UserAgent

class WebDriverMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # 加载驱动
        print('================process_request WebDriverMiddleware================')
        browser = webdriver.PhantomJS()
        browser.get(request.url)  # 加载网页
        data = browser.page_source  # 获取网页文本
        data = data.encode('utf-8')
        browser.quit()
        return HtmlResponse(request.url, body=data, encoding='utf-8', request=request)

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

import  base64
class ProxyIpMiddleware(object):
    def __init__(self, user_agent=''):
        self.ip_ls = [
            {'ip_port': '111.8.60.9:8123'},
            {'ip_port': '101.71.27.120:80'},
            {'ip_port': '122.96.59.104:80', 'user_passwd': 'user3:pass3'},
            {'ip_port': '122.224.249.122:8088', 'user_passwd': 'user4:pass4'},
        ]

    def process_request(self, request, spider):
        print('===ProxyIpMiddleware process_request==')
        # 显示当前使用的useragent
        print("********Current UserAgent:%s************")
        proxy = random.choice(self.ip_ls)
        print(proxy)
        if proxy['user_passwd'] is None:
            # 没有代理账户验证的代理使用方式
            request.meta['proxy'] = "http://" + proxy['ip_port']
        else:
            # 对账户密码进行 base64 编码转换
            base64_userpasswd = base64.b64encode(proxy['user_passwd'])
            # 对应到代理服务器的信令格式里
            request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd
            request.meta['proxy'] = "http://" + proxy['ip_port']


class UserAgentMiddleware(object):
    def __init__(self, user_agent=''):
        self.ua = UserAgent(verify_ssl=False)

    def process_request(self, request, spider):
        print('===UserAgentMiddleware process_request==')
        if self.ua:
            # 显示当前使用的useragent
            print("********Current UserAgent:%s************")
            custom_ua = self.ua.random
            print(custom_ua)
            request.headers.setdefault('User-Agent', custom_ua)
