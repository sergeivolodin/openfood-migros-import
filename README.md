# openfood-migros-import

## Usage

```bash
# Get the IDs of all food products of Migros
$ ./get_migros_ids.sh > migros_ids.txt

# Retrieve and save a JSON dump in infofiles/ for each food product
# (These contain the barcodes that we need)
$ ./get_products_infos_from_ids.sh < migros_ids.txt

# Run python file to obtain barcode-category mapping:
$ cd infofiles/scripts
$ virtualenv -p $(which python3) venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python migros-barcode-category.py
# migros-barcode-category.csv must appear
```
