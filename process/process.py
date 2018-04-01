import re
import hashlib
import difflib

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

    def merge(self, new_document):
        print("Mergin with new document {}".format(new_document["id"]))

        if new_document["date"] != self.document["date"]:

            if new_document["claimReviewed"]!=self.document["claimReviewed"]:
                self.document["claimReviewed"] = new_document["claimReviewed"]
            output_list = [li for li in list(difflib.ndiff(self.document["claimReviewed"],new_document["claimReviewed"])) if li[0] != ' ']
