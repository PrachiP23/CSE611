from process.process import Process
from datetime import datetime
import re

class BuzzFeedProcess(Process):
    def process(self):
        document = super().process()
        document['content'] = re.sub(r'\s+', ' ',document['content'])
        document['content_alt'] = re.sub(r'\s+', ' ',document['content_alt'])

        document["date"] = document["date"].strip()
        document["date2"] = document["date2"].strip()
        document["date"] = datetime.strptime(document["date"], '%B %d, %Y, %H:%M GMT').strftime('%d-%m-%Y')
        document["date2"] = datetime.strptime(document["date2"], '%B %d, %Y, %H:%M GMT').strftime('%d-%m-%Y')

        return document
