import scrapy, re, os, hashlib

dir_path = os.path.dirname(os.path.realpath(__file__))
#path to dataset (raw html format) directory 
dataset = os.path.join(dir_path, '../../../../../files/working/dataset/')
print(dir_path)
class rss_crawler(scrapy.Spider):
	
	name = "rss_crawler"

    #rss feeds [independent, guardian, bbc, rtnews, skynews, ctvnews, nytimes, cbsnews]
	start_urls = [
        'http://www.independent.co.uk/news/world/rss',
        'https://www.theguardian.com/world/rss',
        'http://feeds.bbci.co.uk/news/world/rss.xml',
        'https://www.rt.com/rss/news/',
        'http://feeds.skynews.com/feeds/rss/world.xml',
        'https://www.ctvnews.ca/rss/ctvnews-ca-world-public-rss-1.822289',
        'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
        'https://www.cbsnews.com/latest/rss/world'  
    ]
    
    #parse rss response
	def parse(self, response):
	#extract the urls of the 15 most recent articles and yield new requests for them
		for item in response.xpath('//item')[:15]:
			for url in item.xpath('link/text()').extract():
				yield scrapy.Request(url, self.article_parse)

    #parse article response
	def article_parse(self, response):
	#create filename
		url_hash = hashlib.md5(response.url.encode("utf8")).hexdigest()
		filename = url_hash + '.html'
        

	#save the html to file
		with open(dataset + filename, 'wb') as f:
			f.write(response.body)
