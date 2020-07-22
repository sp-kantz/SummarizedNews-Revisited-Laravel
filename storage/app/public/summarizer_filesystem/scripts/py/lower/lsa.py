from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import randomized_svd
from scipy.linalg import diagsvd
from numpy.linalg import norm
import numpy as np

from lower.preprocessing import *

#LSA
def LSA(sent_text, reduction_rate, position_scores):

    #vector representation of the text, returns terms-sentences matrix using pure frequency for weights
    tfidf = TfidfVectorizer(input = 'content', stop_words = tokenized_stop_words, decode_error = 'strict',
                            strip_accents = 'unicode', tokenizer = Tokenizer(), binary = True)
    A = tfidf.fit_transform(sent_text).T.toarray()

    #SVD on A matrix. dimensionality reduction (topics)
    U, s, Vh = randomized_svd(A, reduction_rate)

    #singular values to full matrix
    S = diagsvd(s, reduction_rate, reduction_rate)

    #scoring method from
    #Steinberger, J. and Jezek, K. 2004.
    #Using Latent Semantic Analysis in Text Summarization and Summary Evaluation.
    #Proceedings of ISIM '04, pages 93-100
    #B=S^2*Vh -> matrix used to find sentences with greatest combined weight across all topics 
    B = (S*S@Vh).T
    sc = []
    #score for every sentence is its norm in B
    for i in range(len(B)):
        sc.append(norm(B[i]))

    #add scores according to positions
    for i, score in enumerate(sc):
        sc[i] += position_scores[i]
        
    #score vector
    scores = np.array(sc)
    scores = 10 * scores
    #get the top scored sentences in the cluster
    ranking = scores.argsort()[:-len(sent_text)-1:-1][:reduction_rate]

    #dictionary with sentences (pos in cluster) and their score
    ranked_sentences = {}

    #fill the dictionary
    for i in ranking:
        ranked_sentences[i] = scores[i]

    return ranked_sentences
