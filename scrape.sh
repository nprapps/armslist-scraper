#!/bin/bash

./states.py | parallel --results cache/states ./scrape_index.py {} > cache/index.csv
