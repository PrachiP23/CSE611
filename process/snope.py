from process.process import Process

class SnopeProcess(Process):

    def process(self):
        document = super().process()
        document["innerTitle"] = ''.join(document["innerTitle"]).strip()
        
        return document
