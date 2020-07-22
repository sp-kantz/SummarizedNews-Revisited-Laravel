import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk import word_tokenize

#stopwords
stopwords = nltk.corpus.stopwords.words('english')
tokenized_stop_words = nltk.word_tokenize(' '.join(stopwords))

#Lemmatize
class Tokenizer(object):
    
    def __init__(self):
        #self.stemmer = nltk.stem.PorterStemmer() -> for stemming
        self.wnl = WordNetLemmatizer()
        
    #lemmatize
    def _lemm(self, token):
        # Solves UserWarning about inconsistent stopwords in preprocessing."
        if (token in stopwords):
            return token

        #return self.stemmer.stem(token) -> for stemming
        return self.wnl.lemmatize(token)        
        
    def __call__(self, line):
        tokens = word_tokenize(line)
        tokens = (self._lemm(token) for token in tokens)
        
        return list(tokens)
