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

    return processor.process()


def load():
    print("Loading the files to process")

    for file in get_files():
        yield json.load(open(file))

def persist(documents):
    print("Preparing for persisting this docs")

def process(documents):
    for document in documents:
        yield normalize(document,file_type(file))

if __name__ == '__main__':
    documents = process(load())
    persist(documents)
