from crawler.core import Cralwer
from db_tools import Curls
class Runner():
    def __init__(self,logger=None):
        self.logger = logger
        self.cralwer = Cralwer()
    def get_urls(self):
        iurls = Curls()
        urls = []
        for inst in iurls.query(setting=1):
            urls.append(inst.url)
        return urls
    def run(self):
        urls = self.get_urls()
        self.cralwer.crawl(start_urls=urls, logger=self.logger)

    def set_goods_name(self,urls):
        self.cralwer.crawl(start_urls=urls,spider= 'crawler.spiders.' + 'GoodsSpider',
                           pipeline= 'crawler.pipeline.'+ 'GoodsPipe')
