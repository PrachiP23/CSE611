from process.process import Process
from datetime import datetime

datetime.strptime('on Tuesday, March 6th, 2018 at 11:39 a.m.', 'on %A, %B %dth, %Y at %H:%M %p').strftime('%d-%m-%Y')


class PolitifactProcess(Process):

    def process(self):
        document = super().process()
        document["innerTitle"] = ''.join(document["innerTitle"]).strip()

        document['content'] = document['content'].strip()

        document['date'] = datetime.strptime(document['date'], 'on %A, %B %dth, %Y at %H:%M %p').strftime('%d-%m-%Y')
        
        return document
