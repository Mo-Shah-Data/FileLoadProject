import gzip
from functools import partial

RECORD_SIZE = 250

with gzip.open("k.json.gz","rt") as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    # text = f.read()
    for _ in range(200):
        try:
            element = next(records)
            print(element)
        except StopIteration:
            print("End of iterable reached")
            break

#alternative


import gzip

all_data = ""

with gzip.open("k.json.gz","rt") as f:
    for _ in range(10):
        # Read a chunk of data
        chunk = f.read(4096)  # Adjust the chunk size as needed

        # Check if the chunk is empty, indicating end of file
        if not chunk:
            break

        all_data += chunk


# Next Alternative

import gzip

all_data = ""

with gzip.open("k.json.gz","rt") as f:
    for _ in range(10):
        # Read a chunk of data
        chunk = f.read(4096)  # Adjust the chunk size as needed

        # Check if the chunk is empty, indicating end of file
        if not chunk:
            break

        all_data += chunk