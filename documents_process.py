'''
@author Jose Ayerdis

This script witll allow to process documents gather by the spiders
into more coherent data. It will try to normalize the current data into
sections with less noise that includes extra spaces, line jumps, and
unrelated information.
'''

import os
import hashlib
import json

from process.buzzfeed import BuzzFeedProcess
from process.politifact import PolitifactProcess
from process.snope import SnopeProcess
from process.urbanlegend import UrbanLegendProcess
from pprint import pprint


URBAN_LEGENDS="URBAN_LEGENDS"
SNOPES="SNOPES"
BUZZFEED="BUZZFEED"
POLITIFACT="POLITIFACT"

def get_files():
    basedir = './rumors_crawl/data/'
    documents = ['snopes','buzzfeed','politifact','urbanlegends']

    files = []
    for document in documents:
        objects = os.listdir(basedir+document)
        for file in objects:
            files.append(basedir+document+'/'+file)

    return files

def file_type(file):
    if "urbanlegends" in file:
        return URBAN_LEGENDS
    if "snopes" in file:
        return SNOPES
    if "buzzfeed" in file:
        return BUZZFEED
    if "politifact" in file:
        return POLITIFACT

def normalize(document, file_type):
    #Cleaning document content
    if(file_type == BUZZFEED):
        processor = BuzzFeedProcess(document)
    if(file_type == POLITIFACT):
        processor = PolitifactProcess(document)
    if(file_type == SNOPES):
        processor = SnopeProcess(document)
    if(file_type == URBAN_LEGENDS):
        processor = UrbanLegendProcess(document)

    document['type'] = file_type
    return processor.process()

def compute_hash(content):
    return hashlib.sha1(''.join(content).encode('utf-8')).hexdigest()

def load():
    print("Loading the files to process")
    for file in get_files():
        documents = json.load(open(file))
        yield {'documents':documents,'type':file_type(file)}

def persist(documents):
    print("Preparing for persisting this docs")
    for document in documents:
        if not os.path.exists('cdata/{}/'.format(document["type"].lower())):
            os.makedirs('cdata/{}/'.format(document["type"].lower()))

        #Check if document exist
        doc_name = 'cdata/{}/{}.json'.format(document["type"].lower(),document["id"])
        if not os.path.exists(doc_name):
            print("Creating new document")
            with open(doc_name, 'w') as outfile:
                json.dump(document, outfile)
        else:
            #Check if the document content has changed
            current_document = json.load(open(doc_name))
            current_hash = compute_hash(current_document['content'])
            if current_hash!=compute_hash(document['content']):
                print(document['type'])
        #print(document["type"])
        #print(document["id"])


def process(loaded_docs):
    for meta_doc in loaded_docs:
        file_type = meta_doc['type']
        for document in meta_doc['documents']:
            yield normalize(document,file_type)

if __name__ == '__main__':
    documents = process(load())
    persist(documents)
