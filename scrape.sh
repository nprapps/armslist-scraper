#!/bin/bash

parallel ./scrape_index.py ::: `./states.py` > cache/index.csv
