import hashlib
from random import choice

#class representing a summary and its info (id, title, sources)
class Summary(object):

    summary_id = None
    summary_title = None
    summary_LSA = None
    summary_graph = None
    summary_sources = []

    def __init__(self):
        self.summary_id = None
        self.summary_title = None
        self.summary = None
        self.summary_sources = []

    #set the summary id
    def set_id(self):
        #id is the hash of the summary
        summary_id = hashlib.md5(self.summary_LSA.encode("utf8")).hexdigest()
        self.summary_id = summary_id

    #set the summary title
    def set_title(self, titles):
        self.summary_title = choice(titles)

    #set the LSA summary
    def set_summary_LSA(self, summary):
        self.summary_LSA = summary

    #set the graph summary
    def set_summary_graph(self, summary):
        self.summary_graph = summary

    #add a source as a dictionary containing domain, url and title
    def add_source(self, domain, url, title):
        source = dict(domain = domain, url = url, title = title)
        self.summary_sources.append(source)

    #return a dictionay of the summary and its info
    def get_dict(self):

        return {
            'summary_id': self.summary_id,
            'summary_title': self.summary_title,
            'summary_LSA': self.summary_LSA,
            'summary_graph': self.summary_graph,
            'summary_sources': self.summary_sources
        }
