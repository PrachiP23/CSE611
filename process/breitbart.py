from process.process import Process
from datetime import datetime
import re

class BreitbartProcess(Process):
    def process(self):
        document = super().process()
        document["title"] = document["title"].strip()
        document["content"] = re.sub(r'\s+', ' ',document["content"])
        document["date"] = datetime.strptime(document["date"].strip(), '%B %d, %Y, %H:%M GMT').strftime('%d-%m-%Y')

        return document
