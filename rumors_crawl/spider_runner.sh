scrapy crawl politifact -t json -o data/politifact/$(date "+%Y-%m-%d-%H-%M-%S").json
scrapy crawl buzzfeed -t json -o data/buzzfeed/$(date "+%Y-%m-%d-%H-%M-%S").json
scrapy crawl snopes -t json -o data/snopes/$(date "+%Y-%m-%d-%H-%M-%S").json
scrapy crawl urbanlegends -t json -o data/urbanlegends/$(date "+%Y-%m-%d-%H-%M-%S").json
scrapy crawl dailyWire -t json -o data/dailyWire/$(date "+%Y-%m-%d-%H-%M-%S").json
scrapy crawl breitbart -t json -o data/breitbart/$(date "+%Y-%m-%d-%H-%M-%S").json
