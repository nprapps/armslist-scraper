#!/bin/bash

./states.py
./scrape_index.py wyoming
csvcut -c 1 cache/index-deduped.csv | head
./scrape_listing http://www.armslist.com/posts/5887276/chicago-illinois-handguns-for-sale--sw--mp-40---vtac
