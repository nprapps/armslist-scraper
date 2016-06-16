#!/usr/bin/env python
"""
Dedupe index csv.
"""

import csv


def dedupe_index():
    ids = []
    deduped_rows = []
    with open('cache/index.csv') as index_file:
        reader = csv.reader(index_file)
        for row in reader:
            if row[0] not in ids:
                ids.append(row[0])
                deduped_rows.append(row)

    with open('cache/index-deduped.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(deduped_rows)


if __name__ == '__main__':
    dedupe_index()
