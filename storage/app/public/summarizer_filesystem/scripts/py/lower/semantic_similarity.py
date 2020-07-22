#!Not Used!

import nltk, re
from time import time
from nltk import word_tokenize
from nltk.corpus import wordnet as wn
import numpy as np

stopwords = nltk.corpus.stopwords.words('english')

#for every word in the sentence
#find the best sense (synset) of the word for the sentence
#by calculating the overlap in the definitions of the different senses of the words
#return the sentence as a list of the best synsets
def words_to_synsets(lex):

    overlaps = {}

    #for every word in the sentence
    for i in range(len(lex)):
        words = list(lex.keys())
        first = ''
        best = 0
        #for every possible sense of the word
        for sense in lex[words[i]]:
            #save the first sense
            if first == '':
                first = sense
            #for every other word in the sentence
            for j in range(len(words)):
                if i == j:
                    continue
                #for every sense of the other words
                for other in lex[words[j]]:
                    #overlap in their definitions
                    ov = len(list(set(lex[words[i]][sense]).intersection(lex[words[j]][other])))
                    #save the sense of the word with the maximum overlap with the others
                    if ov > best:
                        best = ov
                        overlaps[words[i]] = sense
        #if no overlap is found, store the first sense
        if words[i] not in overlaps:
            overlaps[words[i]] = first
    #return the sentence as a list of the best senses
    return list(overlaps.values())

#calculate semantic similarity of two sentences
def semantic_similarity(sent1, sent2):
    #vector for each sentence
    s1 = np.zeros(len(sent1))
    s2 = np.zeros(len(sent2))
    #for every word of sentence 1
    for i in sent1:
        max_sim = 0
        sim_sum = 0
        #for every word of sentence 2
        for j in sent2:
            #path similarity
            sim1 = wn.path_similarity(wn.synset(i), wn.synset(j))
            #wup similarity
            sim2 = wn.wup_similarity(wn.synset(i), wn.synset(j))
            
            if sim1 == None:
                sim1 = 0
            if sim2 == None:
                sim2 = 0
            #average of path and wup
            av = sim1 + sim2
            #save best max similarity of the words
            if av > max_sim:
                max_sim = av
                fi = sent1.index(i)
                fj = sent2.index(j)
                s2[fj] = max_sim
                s1[fi] = max_sim

    if float(len(sent1) + len(sent2)) == 0.0:
        return 0.0

    #overall similarity of two sentences
    overall = (sum(s1) + sum(s2)) / 2 * float(len(sent1) + len(sent2))

    return(overall)

#sentences as input
#keep only verbs, nouns and adjectives
#represent sentences as a list of the best synsets of their words
#calculate semantic similarity for every sentence pair
#return similarity matrix
def sem_sim_matrix(sent_text):
    #stores the sentences as lists of best synsets
    syns_text = []
    t1 = time()
    #for every sentence
    for i in range(len(sent_text)):
        #clean sentence
        regex = re.compile('([^\s\w]|_)+')
        sentence = regex.sub('', sent_text[i]).lower()
        sentence = sentence.split(" ")

        for word in list(sentence):
            if word in stopwords:
                sentence.remove(word)

        sentence = " ".join(sentence)

        #tokenize
        tokens = word_tokenize(sentence)
        #pos_tag
        tokens = nltk.pos_tag(tokens)

        #lexicon for the sentence
        lex = {}
        #for every word in the sentence
        for j, word in enumerate(tokens):
            #keep only nouns, verbs, adjectives
            if 'NN' in word[1] or 'VB' in word[1]:
                #store the word in the lexicon with a dictionary of its senses and their tokenized definitions
                if word[0] not in lex:
                    #get senses
                    senses = wn.synsets(word[0].lower())
                    #if senses are not found, continue
                    if senses == []:
                        continue
                    #if found
                    else:
                        #store the word in the lexicon
                        lex[word[0]] = {}
                        #store every sense and its tokenized definition
                        for s in senses:
                            lex[word[0]][s.name()] = []
                        for s in senses:                
                            lex[word[0]][s.name()] +=  [t for t in word_tokenize(s.definition()) if t not in stopwords]

        #find the best synsets for the words of the sentence
        sent = words_to_synsets(lex)
        #store the synset representation of the sentence
        syns_text.append(sent)

    #similarity matrix
    A = np.eye(len(syns_text), len(syns_text))

    #for every sentence pair
    for i in range(len(syns_text) - 1):
        for j in range(i + 1, len(syns_text)):
            #calculate similarity of the pair
            if len(syns_text[i]) == 0 or len(syns_text[j]) == 0:
                sim = 0
            else:
                sim = semantic_similarity(syns_text[i], syns_text[j])
            #store it in the similarity matrix
            A[i, j] = sim
            A[j, i] = sim

    print(time() - t1)
    #return the similarity matrix
    return A
