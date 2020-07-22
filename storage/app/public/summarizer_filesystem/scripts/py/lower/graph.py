from time import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise
import networkx as nx

from lower.preprocessing import *
#from lower.semantic_similarity import sem_sim_matrix !Not Used!

#graph based method
def graphMethod(sent_text):

    #term-sentences tf matrix
    tfidf_vectorizer = TfidfVectorizer(input = 'content', stop_words = tokenized_stop_words, decode_error = 'strict',
                            strip_accents = 'unicode', tokenizer = Tokenizer(), binary = True)

    #articles' text as input
    tfidf = tfidf_vectorizer.fit_transform(sent_text).toarray()

    #create (cosine) similarity matrix for the sentences
    A = pairwise.cosine_similarity(tfidf)

    #create graph from similarity matrix
    G = nx.from_numpy_matrix(A)
    #remove selfloop edges
    G.remove_edges_from(nx.selfloop_edges(G))
    
    #calculate pagerank scores
    pr = nx.pagerank(G)

    #sort sentences by pagerank score
    sentences = sorted(pr, key=pr.get, reverse=True)

    ranked_sentences = {}

    #return the sentences with their scores
    for i in sentences:
        ranked_sentences[i] = 100 * pr[i]

    return ranked_sentences

