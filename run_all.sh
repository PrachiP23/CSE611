cd rumors_crawl
./spider_runner.sh
cd ..
python documents_process.py
python nlp_start.py
cd twitter
python base.py > logs/output.log
