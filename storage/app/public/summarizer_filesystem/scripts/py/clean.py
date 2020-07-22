import re, os, hashlib
from time import time
from scrapy.selector import Selector

import lower.json_ld as json_ld

dir_path = os.path.dirname(__file__)

#path to dataset (raw html format) directory
dataset = os.path.join(dir_path, '../../files/working/dataset/')

#regular expressions for HTML markup leftovers (e.g. links), and unicode replacements
cleanup = {'<.*?>': '',
            '“|”': '"',
            '‘|’': "'",
            '…|\.\.\.': '.',
            '–|—': '-',
           '&amp;': '&',
           '\n': ' ',
           '\ufeff': ' ',
            '\u00a0': ' '}

t0 = time()

doc_list = os.listdir(dataset)

#open every html doc and get important data
#save to json
for doc in doc_list:

    f = open(dataset + doc, encoding = "UTF-8")
    #read file
    raw = f.read()
    #close file
    f.close()

    page = Selector(text = raw, type = "html")

##get domain, url, title from meta
##text from each page

    domain = page.xpath('//meta[contains(@property, "og:site_name")]').css('meta::attr(content)').get()
    url = page.xpath('//meta[contains(@property, "og:url")]').css('meta::attr(content)').get()
    title = page.xpath('//meta[contains(@property, "og:title")]').css('meta::attr(content)').get()

###----------independent

    text = page.xpath('//div[@class = "body-content"]/p').getall()

###------------guardian      
    
    if len(text) == 0:
        text = page.xpath('//div[has-class("content__article-body")]/p').getall()
		
	#regex to remove the <p><em>Follow , share, like</em> at the end of the guardian articles
        r = '<p><em>.*?</em></p>'
        
        for t in text:
            i = text.index(t)
            text[i] = re.compile(r).sub("", text[i])
        
###--------------bbc

    if len(text) == 0:
        text = page.xpath('//div[has-class("story-body__inner")]/p').getall()

###------------RTnews    

    if len(text) == 0:     
        text = page.xpath('//div[has-class("article__text")]/p').getall()

        #regex to remove the <p><strong>share, like</strong> at the end of the RT articles
        r = '<p><strong>.*?</strong></p>'
        
        for t in text:
            i = text.index(t)
            text[i] = re.compile(r).sub("", text[i])

###------------SkyNews

    if len(text) == 0:
        text = page.xpath('//div[has-class("sdc-article-body")]/p').getall()

        #regex to remove the <p><strong>listen, follow, share, like</strong> at the end of the sky articles
        r = '<p><strong>.*?</strong></p>'

        for t in text:
            i = text.index(t)
            text[i] = re.compile(r).sub("", text[i])
        
###--------------ctv

    if len(text) == 0:
        text = page.xpath('//div[has-class("articleBody")]/p').getall()

###-----------new york times

    if len(text) == 0:
        text = page.xpath('//section[contains(@name,"articleBody")]/div/div/p').getall()
        if len(text) != 0:
            domain = 'The New York Times'
            brf = page.xpath('//meta[contains(@property, "article:section")]').css('meta::attr(content)').get()
            if brf == "Briefing":
                text = []
                
###------------CBS

    if len(text) == 0:
        text = page.xpath('//article/section/p').getall()
        if len(text) != 0:
            domain = 'CBS News'
	
    #alternativve for cbs morning articles
    if len(text) == 0:
        text = page.xpath('//*[@id="article-entry"]/div/p').getall()
        if len(text) != 0:
            domain = 'CBS News'
       
    if len(text) == 0:
        print("-====--ERROR? [", doc, "] ---===---\n")
    else:

        body = '\n'.join(i for i in text if i)

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in body.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        body = '\n'.join(chunk for chunk in chunks if chunk)

        #remove html markup leftovers and replace some unicode characters
        for i in cleanup:
            body = re.compile(i).sub(cleanup[i], body)

        #hash of url used as json filename, and article id
        fid = hashlib.md5(url.encode("utf8")).hexdigest()

        #dictionary with all the info
        data_dict = dict(article_id = fid, domain = domain, url = url, title = title, body = body)

        #save to json file
        json_ld.store_data('clean', doc, data_dict)

print('Cleanup Time:', time() - t0)
