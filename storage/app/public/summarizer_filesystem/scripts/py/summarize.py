import os, nltk
from time import time

from lower.position_scoring import getPositionScores
#from lower.centroid_scoring import getCentroidScores !Not Used!
from lower.lsa import LSA
from lower.graph import graphMethod
from lower.Summary import Summary
import lower.sentence_selection as sentence_selection
import lower.json_ld as json_ld

#create a summary for the cluster
def summarize(cluster):

    #new summary object
    summary = Summary()
    #list of article titles in the cluster
    art_titles = []
    #list of sentences in the cluster
    sent_text = []
    #used to mark the lenghts of the articles in the cluster
    len_marks = []
    
    #get the data of every article in the cluster
    for article in cluster:
        
        #open json file containing article data
        data = json_ld.get_data('clean', article)

        #add the source
        summary.add_source(data['domain'], data['url'], data['title'])       
        #add title to the list
        art_titles.append(data['title'])
        #add the article's sentences to the cluster's sentences
        sent_text += nltk.sent_tokenize(data['body'])
        #mark the length so far
        len_marks.append(len(sent_text))

    #assign a score to every sentence based on its position in the original article
    position_scores = getPositionScores(sent_text, len_marks)

    #set the summary title (random)
    summary.set_title(art_titles)

    #set reduction rate for LSA
    if len(cluster) < 2:
        reduction_rate = len(sent_text)
    else:
        #dimensions to keep r = n * 25%
        reduction_rate = int(len(sent_text)*0.20)


    method = 'LSA'
    
    #perform LSA. return a sorted list of the sentences and their scores
    ranked_sentences = LSA(sent_text, reduction_rate, position_scores)
    #create summary (rerank, select, order)
    summary_text_LSA = sentence_selection.create_summary(ranked_sentences, sent_text, len_marks, method)
    #set the LSA summary text
    summary.set_summary_LSA(summary_text_LSA)

    method = 'graph'
    
    #rank sentences with a graph-based method. return a sorted list of the sentences and their scores
    ranked_sentences = graphMethod(sent_text)
    #create summary (rerank, select, order)
    summary_text_graph = sentence_selection.create_summary(ranked_sentences, sent_text, len_marks, method)
    #set the graph summary text
    summary.set_summary_graph(summary_text_graph)
    
    #set the summary id (hash of summary text)
    summary.set_id()

    #return the summary and its info as a dictionary
    return summary.get_dict()

################################### Start Here
t0 = time()

#read clusters from cluster mapping json file
clusters = json_ld.get_data('mapping', 'clusters.json')

#list of summary filenames
#will be saved in json file and used by the server
summary_mapping = []

#for every cluster
for c in clusters:
    #create a summary for the cluster
    summary_dict = summarize(clusters[c])

    #save the summmary to a json file
    json_ld.store_data('summaries', summary_dict['summary_id'], summary_dict)

    #add summary's filename to mapping list
    summary_mapping.append(summary_dict['summary_id'])
      
#save mapping list to file
json_ld.store_data('mapping', 'summaries', summary_mapping)

print('Total Summarization Time:', time() - t0)
