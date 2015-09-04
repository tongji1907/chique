from scrapy import Spider, signals
from scrapy.exceptions import DontCloseSpider
from scrapy.exceptions import CloseSpider
from scrapy.http.request import Request
import pickle
import  redis



class RedisMixin(object):
    """Mixin class to implement reading urls from a redis queue."""
    redis_key = None  # use default '<spider>:start_urls'

    def setup_redis(self):
        """Setup redis connection and idle signal.
        This should be called after the spider has set its scrapy object.
        """
        if not self.redis_key:
            self.redis_key = '%s:start_urls' % self.name

        self.server = redis.Redis('120.25.216.93','6379')
        # idle signal is called when the spider has no requests left,
        # that's when we will schedule new requests from redis queue
        self.crawler.signals.connect(self.spider_idle, signal=signals.spider_idle)
        self.crawler.signals.connect(self.item_scraped, signal=signals.item_scraped)
        #self.scrapy.signals.connect(self.spider_closed, signal=signals.spider_closed)
        self.log("Reading URLs from redis list '%s'" % self.redis_key)
        self.paused = False

    def next_request(self):
        """Returns a request to be scheduled or none."""
        use_set = self.settings.getbool('REDIS_SET')

        if use_set:
            url = self.server.spop(self.redis_key)
        else:
            url = self.server.lpop(self.redis_key)

        if url:
            t =pickle.loads(url)
            #print t['cookies']
            print t['link_hash']
            print t['product_code']
            cookie = ''
            if t['cookies'] is not None:
                print t['cookies']
                if t['cookies'] != '':
                    cookie = eval((t['cookies']))


            return Request(t['url'],cookies=cookie,meta={'product_code':t['product_code'], 'link_hash': t['link_hash']},dont_filter=True)
            #return self.make_requests_from_url(t['url'])

    def schedule_next_request(self):
        """Schedules a request if available"""
        req = self.next_request()
        if req:
            self.crawler.engine.crawl(req, spider=self)

    def spider_idle(self):
        """Schedules a request if available, otherwise waits."""
        #if self.paused==False:
        if not self.crawler.engine.paused:
            self.schedule_next_request()
        raise DontCloseSpider

    def item_scraped(self, *args, **kwargs):
        """Avoids waiting for the spider to  idle before scheduling the next request"""
        self.schedule_next_request()


    def spider_pause(self):
        self.paused = True

    def spider_resume(self):
        self.paused = False

class RedisSpider(RedisMixin, Spider):
    """Spider that reads urls from redis queue when idle."""

    def _set_crawler(self, crawler):
        super(RedisSpider, self)._set_crawler(crawler)
        self.setup_redis()