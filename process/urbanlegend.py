from process.process import Process

class UrbanLegendProcess(Process):

    def process(self):
        document = super().process()
        document["innerTitle"] = ''.join(document["innerTitle"]).strip()
        
        return document
