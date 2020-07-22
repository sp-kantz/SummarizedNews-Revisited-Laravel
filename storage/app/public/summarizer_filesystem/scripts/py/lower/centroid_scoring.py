#!Not Used!

from sklearn.feature_extraction.text import CountVectorizer
from scipy import spatial

from lower.preprocessing import *

#get a score for each sentence
#based on its similarity to the centroid of the cluster
def getCentroidScores(sent_text):

    #vector representation of the cluster's text
    tf = CountVectorizer(input = 'content', stop_words = tokenized_stop_words, decode_error = 'strict',
                         strip_accents = 'unicode', tokenizer = Tokenizer())
    A = tf.fit_transform(sent_text).toarray()

    #centroid of the cluster
    centroid = A.mean(0)

    centroid_scores = {}

    #score each sentence based on its similarity to the centroid
    for i, sentence in enumerate(A):
        centroid_scores[i] = 1 - spatial.distance.cosine(sentence, centroid)
        
    return centroid_scores
