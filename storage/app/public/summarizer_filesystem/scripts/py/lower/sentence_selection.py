import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from scipy import spatial
from nltk import word_tokenize

from lower.preprocessing import *

#summary size in words
size_in_words = 220

#remove redundancy by reranking
#[1].choose the top scoring sentence
#[2].penalty on the scores of the ones similar to the chosen
#[3].sort by score
#[4].repeat until all sentences are reranked
def remove_redundancy(sent_text, ranked_sentences, method):
    
    #store the new top sentences and their scores
    new_ranked = {}

    #vector representation of cluster's text, creates a sentences-terms matrix,
    #used to find cosine similarity of the sentences
    if method == 'LSA':
        ##raw frequency for LSA method
        tf = CountVectorizer(input = 'content', stop_words = tokenized_stop_words, decode_error = 'strict',
                             strip_accents = 'unicode', tokenizer = Tokenizer())
    else:
        #TFIDF for graph method
        tf = TfidfVectorizer(input = 'content', stop_words = tokenized_stop_words, decode_error = 'strict',
                             strip_accents = 'unicode', tokenizer = Tokenizer())

    A = tf.fit_transform(sent_text).toarray()

    #for every sentence
    for i in range(len(ranked_sentences)):

        #get the sentences' position in the cluster text
        keys = list(ranked_sentences.keys())

        #[1].choose the top scoring sentence and add it with its score to the new list 
        new_ranked[keys[i]] = ranked_sentences[keys[i]]

        #[2].rerank every remaining sentence after the chosen one
        for j in range(i + 1, len(keys)):
            #calculate similarity with the chosen
            sim = 1 - spatial.distance.cosine(A[keys[i]], A[keys[j]])
            #reduce its score according to the similarity
            ranked_sentences[keys[j]] = ranked_sentences[keys[j]] - 0.5 * sim * ranked_sentences[keys[j]]

        #[3].sort the remaining sentences
        ranked_sentences = dict(sorted(ranked_sentences.items(), key=lambda k: k[1], reverse=True))

    return new_ranked

#select the top sentences to include in the summary
#as long as the summary size is under the limit size_in_words (= 220 words)
def select(ranked_sentences, sent_text):

    #total size of selected sentencces
    size = 0
    #selected sentences
    selection = {}
    
    #for every sentence
    for i in range(len(ranked_sentences)):
        #get the sentences' position in the cluster text
        keys = list(ranked_sentences.keys())
        s1 = sent_text[keys[i]]
        s1 = re.sub(r'[^\w\s]', '', s1)
        #get sentence's length in words
        sent_len = len(word_tokenize(s1))
        #check the difference from the limit
        diff = size_in_words - size - sent_len
        #if there is enough space
        if diff > - 1:
            #add the sentence in the summary
            selection[keys[i]] = sent_len
            #add its length to the total
            size += sent_len
        #if there is not enough space
        else:
            if i + 1 < len(ranked_sentences):
                #one more chance with the next sencence
                s1 = sent_text[keys[i + 1]]
                s1 = re.sub(r'[^\w\s]', '', s1)
                sent_len = len(word_tokenize(s1))
                diff = size_in_words - size - sent_len
                if diff > - 1:
                    selection[keys[i]] = sent_len
                    size += sent_len
                #if the next one does not fit either, return the selection
                else:
                    break
            break

    return selection

#get the position of every line in the article it came from
#using the position in the cluster from the ranked list
#and the the length marks of the articles
def getArticlePositions(ranked_sentences, len_marks):

    #stores the article position for every cluster position
    article_positions = {}
    
    for pos_in_cl in ranked_sentences:
        #check the marks
        for mark in len_marks:
            #if the cluster position is higher than the current mark, continue
            if pos_in_cl > mark - 1:
                continue
            #the sentence came from the article corresponding to this mark
            else:
                #get the index the previous length mark
                lm_i = len_marks.index(mark) - 1
                #if it's negative it means the sentence comes
                #from the first article in the cluster
                if lm_i < 0:
                    pos_in_art = pos_in_cl + 1
                    break
                #calculate the article's length
                art_len = mark - len_marks[lm_i]
                #distance from the end
                end_d = mark - pos_in_cl
                #position in the article
                pos_in_art = art_len - end_d + 1
                break
            
        article_positions[pos_in_cl] = pos_in_art

    return article_positions

#remove redundancy, select and order the ranked sentences
#return summary sentences as text
def create_summary(ranked_sentences, sent_text, len_marks, method):

    #remove redundancy. rerank sentences based on similarity
    ranked_sentences = remove_redundancy(sent_text, ranked_sentences, method)

    #from the top scoring, select the sentences to create a summary with total length size_in_words = 205
    selection = select(ranked_sentences, sent_text)
    
    #get the original article positition of the selected sentences
    article_positions = getArticlePositions(selection, len_marks)
    
    #order the selection of sentences by their original postition in their respective articles
    summary_in_order = dict(sorted(article_positions.items(), key = lambda k: k[1]))

    #final summary text. join the top scoring and ordered sentences
    summary_text = '\n'.join(sent_text[i] for i in summary_in_order)

    return summary_text
