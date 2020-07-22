import os, json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering
from time import time

import lower.json_ld as json_ld
from lower.preprocessing import *

#############################################################################################
dir_path = os.path.dirname(__file__)

clean = os.path.join(dir_path, '../../files/working/clean_articles/')

#perform hierarhical agglomerative clustering on article set
#return a dictionary describing the clusters of articles 
def clustering():
    
    #list to be filled with every article text
    article_text = []

    #list for the articles' filenames
    article_list = os.listdir(clean)

    #for every article name
    for article in article_list:

        #read the article data
        data = json_ld.get_data('clean', article)

        #add the article's text to the list
        article_text.append(data['body'])

    #create term-document tfidf matrix
    #ignore stop words, strip unicode accents, lemmatize
    tfidf_vectorizer = TfidfVectorizer(input = 'content', stop_words = tokenized_stop_words, decode_error = 'strict',
                                       strip_accents = 'unicode', tokenizer = Tokenizer())
    #articles' text as input
    tfidf = tfidf_vectorizer.fit_transform(article_text).toarray()

    #perform agglomerative clustering algorithm to get clusters of articles 
    #:unknown number of clusters, cosine affinity (similarity), average linkage, threshold 0.60
    clustering = AgglomerativeClustering(n_clusters = None, affinity = 'cosine', compute_full_tree = 'True',
                                         linkage = 'average', distance_threshold = 0.62)
    #tfidf matrix as input
    clustering.fit_predict(tfidf)

    #dictionary for the clusters: {cluster number: list of documents in the cluster}
    clusters = {}
    #for every cluster in the list, add it in the dictionary
    for i in range(0, len(clustering.labels_)):
        cid = int(clustering.labels_[i])
        #if the cluster is already in the dictionary
        if cid in clusters:
            #add the corresponding document in the cluster    
            clusters[cid].append(article_list[i])
        #if the cluster is not in the dictionary (first time)
        else:
            #create the entry and add the document's name
            clusters[cid] = [article_list[i]]

    return clusters

#######Start Here

t0 = time()

#find clusters of articles
clusters = clustering()

#save clusters to mapping file
json_ld.store_data('mapping', 'clusters', clusters)

print('Clustering Time:', time() - t0)
