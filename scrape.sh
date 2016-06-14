#!/bin/bash

./states.py | parallel --results cache/states ./scrape_index.py {} > cache/index.csv

csvcut -c 1 cache/index.csv | parallel ./scrape_listing.py {} > cache/listings.csv
