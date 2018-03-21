'''
@author Jose Ayerdis

This script witll allow to process documents gather by the spiders
into more coherent data. It will try to normalize the current data into
sections with less noise that includes extra spaces, line jumps, and
unrelated information.
'''

import os
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

def process(document, file_type):
    #Cleaning document content

    if(file_type == BUZZFEED):
        processor = BuzzFeedProcess(document)
    if(file_type == POLITIFACT):
        processor = PolitifactProcess(document)
    if(file_type == SNOPES):
        processor = SnopeProcess(document)
    if(file_type == URBAN_LEGENDS):
        processor = UrbanLegendProcess(document)

    #if file_type != BUZZFEED:
    #    document["innerTitle"] = ''.join(document["innerTitle"]).strip()
    #    print(document["innerTitle"])
    document = processor.process()
    
    #document["title"] = document["title"].strip()
    #print(document["title"].strip())

def load():
    print("Loading the files to process")

    for file in get_files():
        documents = json.load(open(file))

        for document in documents:
            document = process(document,file_type(file))

def preprocess():
    print("Preprocessing the data ")

if __name__ == '__main__':
    load()
