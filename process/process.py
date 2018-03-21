import re

class Process:
    def __init__(self,document):
        self.document = document

    def process(self):
        self.document["content"] = re.sub(r"[\n\t]", "", ''.join(self.document["content"]))
        return self.document
