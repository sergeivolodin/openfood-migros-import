from os import listdir
from os.path import isfile, join
import json
from tqdm import tqdm
import pandas as pd
from copy import deepcopy

# Loading file list
path = '..'
files = listdir(path)
extension = '.json'
files = filter(lambda f: len(f) > len(extension), files)
files = map(lambda f: join(path, f), files)
files = list(filter(lambda pf: extension in pf and isfile(pf), files))

# Reading all files, storing data to rows
header = ['idx', 'name', 'eans', 'slug']
rows = []
for f in tqdm(files):
    product = json.load(open(f, 'r'))
    
    row = product['_product']['id'], product['_source']['name'], \
        product['_source']['eans'], product['_source']['categories'][0]['slug']
    for item in row:
        assert(len(item) > 0)
    
    eans_idx = header.index('eans')
    
    for ean in row[eans_idx]:
        r = list(deepcopy(row))
        r[eans_idx] = ean
        rows.append(r)

# Creating a dataframe
df = pd.DataFrame(rows, columns = header)

# Saving data to csv file
df.to_csv('migros-barcode-category.csv')
