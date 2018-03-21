from process.process import Process
from datetime import datetime


class PolitifactProcess(Process):

    def process(self):
        document = super().process()
        document["innerTitle"] = ''.join(document["innerTitle"]).strip()
        document['content'] = document['content'].strip()
        document['date'] = datetime.strptime(document['date'].replace('.',''), 'on %A, %B %dth, %Y at %H:%M %p').strftime('%d-%m-%Y')

        return document
