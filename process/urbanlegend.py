from process.process import Process
from datetime import datetime
import re

class UrbanLegendProcess(Process):

    def process(self):
        document = super().process()
        document["innerTitle"] = ''.join(document["innerTitle"]).strip()

        if document["description"] is not None:
            document["description"] = filter(None,document["description"])
            document["description"] = ''.join(document["description"])

        document["content"] = document["content"].strip()

        if document["claim"] is not None:
            document["claim"] = filter(None,document["claim"])
            document["claim"] = ''.join(document["claim"])

        claimReviewed = re.search('\w+:(.+)\(', document["claimReviewed"], re.IGNORECASE)
        if claimReviewed is not None:
            document["claimReviewed"] = claimReviewed.group(1).strip()
        else:
            document["claimReviewed"] = "N/A"

        document["date"] = ''.join(document["date"]).strip()
        document["date"] = datetime.strptime(document["date"], 'Updated %B %d, %Y').strftime('%d-%m-%Y')

        # date = scrapy.Field()
        # claimReviewed = scrapy.Field()
        # referredUrl = scrapy.Field()


        return document
