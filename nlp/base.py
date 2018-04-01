import random
from nltk import FreqDist
import gensim.downloader as api
from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from gensim.models.ldamodel import LdaModel
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem.snowball import EnglishStemmer
from nltk.corpus import stopwords
import pyLDAvis.gensim
from nltk import ngrams

def get_words(text):
    words = word_tokenize(text)
    #Removing single letter words as they offer no insight
    #Also non numeric information is really not necesary
    english_stopwords = stopwords.words('english')
    english_punkt = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','``','""',"''"]
    news_stopwords = english_stopwords + english_punkt

    words = [word for word in words if len(word) > 1 and not word.isnumeric()]
    words = [word for word in words if word.lower() not in news_stopwords ]
    return words


def gen_ngrams(document, n):
    words = get_words(document["content"])
    ngram_g = ngrams(words,n)
    s = []
    for ngram in ngram_g:
        s.append(' '.join(str(i) for i in ngram))

    print(s)

def word_count(document):
    words = get_words(document["content"])
    stemmer = EnglishStemmer()
    words = [stemmer.stem(word) for word in words]
    fdist = FreqDist(words)
    for word, frequency in fdist.most_common(50):
        print(u'{};{}'.format(word, frequency))

    fdist.plot(30,cumulative=False)

def lda(documents):

    texts = []
    idx = 0
    for file_docs in documents:
        document = file_docs["documents"]
        words = get_words(document["content"])
        if document["claim"]:
            words = words + get_words(document["claim"])
        stemmer = EnglishStemmer()
        words = [stemmer.stem(word) for word in words]
        texts.append(words)
        #print(document["claim"])
        #print(document["claimReviewed"])

    dictionary = Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    ldamodel = LdaModel(corpus, num_topics=10, id2word = dictionary, passes=20)
    print(ldamodel.show_topics())
    data = pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary)
    pyLDAvis.save_html(data,'vis.html')


def run_lda(documents):
    lda(documents)

def run(documents, n_docs):

    #lda(documents)
    random_doc = random.randint(1,n_docs)
    idx = 0
    for file_docs in documents:
        ##We'll get a random document
        if random_doc==idx:
        #    lda(file_docs["documents"])
            #word_count(file_docs["documents"])
            gen_ngrams(file_docs["documents"],5)
            break
        idx = idx + 1
