from process.process import Process
from datetime import datetime
import re

class PolitifactProcess(Process):

    def process(self):
        document = super().process()
        document["innerTitle"] = ''.join(document["innerTitle"]).strip()
        document['content'] = document['content'].strip()

        #note: one coule apply a more complex regexp but for
        # now we just want to clean this
        preffix = "th"

        if re.search(r"[\d\d]st",document['date']):
            preffix = "st"
        elif re.search(r"[\d\d]nd",document['date']):
            preffix = "nd"

        pattern = 'on %A, %B %d{}, %Y at %H:%M %p'.format(preffix)
        document['date'] = datetime.strptime(document['date'].replace('.',''), pattern).strftime('%d-%m-%Y')

        return document
