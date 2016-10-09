#!/bin/bash

# Parallelize index scraping over list of states
./states.py | parallel --results cache/states ./scrape_index.py {} > cache/index.csv

# Deduplicate listing URLs
./dedupe_index.py

# Make the listings csv with parallel scrape of URL list
echo "url,...,<all headers>" > cache/listings.csv
csvcut -c 1 cache/index-deduped.csv | parallel ./scrape_listing.py {} >> cache/listings.csv
