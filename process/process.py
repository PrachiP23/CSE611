import re
import hashlib

class Process:
    def __init__(self,document):
        self.document = document

    def process(self):
        self.document["content"] = re.sub(r"[\n\t]", "", ''.join(self.document["content"]))

        if 'referredUrl' in self.document.keys():
            url = self.document['referredUrl']
        else:
            url = self.document['referred_url']

        url = ''.join(url).encode('utf-8')
        uid = hashlib.sha1(url).hexdigest()

        self.document['id']=uid


        return self.document
