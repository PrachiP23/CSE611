from process.process import Process
from datetime import datetime



class SnopeProcess(Process):

    def process(self):
        document = super().process()
        document["innerTitle"] = ''.join(document["innerTitle"]).strip()

        if document["claim"] is not None:
            document["claim"] = document["claim"].strip()

        document["date"] = datetime.strptime(document["date"], '%d %B %Y').strftime('%d-%m-%Y')

        #missing the step to create an unique id per class

        return document
