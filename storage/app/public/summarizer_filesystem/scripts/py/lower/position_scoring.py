#for every sentence in the cluster
#find the article position of the sentence
#assign a score according to its position, highest score = 1 for the first sentence of an article
#score = (article length - sentence position) / article length
def getPositionScores(sent_text, len_marks):

    #stores the score for each sentence based on its position in the original article
    position_scores = {}

    #for every sentence in the cluster
    for pos_in_cl in range(len(sent_text)):
        #check the marks
        for mark in len_marks:
            #if the cluster position is higher than the current mark, continue
            if pos_in_cl > mark - 1:
                continue
            #the sentence came from the article corresponding to this mark
            else:
                #get the index the previous length mark
                lm_i = len_marks.index(mark) - 1
                #if it's negative it means the sentence comes from the first article in the cluster
                if lm_i < 0:
                    pos_val = (mark - pos_in_cl) / mark
                    #score
                    pos_in_art = pos_in_cl + 1
                    break
                #calculate the article's length
                art_len = mark - len_marks[lm_i]
                #distance from the end
                end_d = mark - pos_in_cl
                #position in the article
                pos_in_art = art_len - end_d + 1
                #score
                pos_val = (art_len - pos_in_art + 1) / art_len
                break
        #store score
        position_scores[pos_in_cl] = pos_val

    return position_scores
