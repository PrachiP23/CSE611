import os
import json
import datetime
from documents_process import load
from nlp.base import run,run_lda, run_tfidf

URBAN_LEGENDS="URBAN_LEGENDS"
SNOPES="SNOPES"
BUZZFEED="BUZZFEED"
POLITIFACT="POLITIFACT"

def file_type(file):
    if "urban_legends" in file:
        return URBAN_LEGENDS
    if "snopes" in file:
        return SNOPES
    if "buzzfeed" in file:
        return BUZZFEED
    if "politifact" in file:
        return POLITIFACT

def build_processor(document, file_type):
    if(file_type == BUZZFEED):
        return BuzzFeedProcess(document)
    if(file_type == POLITIFACT):
        return PolitifactProcess(document)
    if(file_type == SNOPES):
        return SnopeProcess(document)
    if(file_type == URBAN_LEGENDS):
        return UrbanLegendProcess(document)

def get_files():
    basedir = './cdata/'
    documents = ['snopes','buzzfeed','politifact','urban_legends']

    files = []
    for document in documents:
        objects = os.listdir(basedir+document)
        for file in objects:
            files.append(basedir+document+'/'+file)

    return files

def load(type=None):
    today = datetime.date.today()
    margin = datetime.timedelta(days = 5)

    #datetime.strptime("03-03-2018",'%d-%m-%Y')
    #print("Loading the files to apply NLP")
    for file in get_files():
        documents = json.load(open(file))
        if not type or type == documents["type"]:

            document_date = datetime.datetime.strptime(documents["date"],'%d-%m-%Y')
            if today - margin <= document_date.date() <= today + margin :
                yield {'documents':documents,'type':file_type(file)}

if __name__ == '__main__':
    #run_lda(documents)
    # run_tfidf(load(type=SNOPES))
    # run_tfidf(load(type=BUZZFEED))
    # run_tfidf(load(type=POLITIFACT))
    run_tfidf(load(type=URBAN_LEGENDS))
