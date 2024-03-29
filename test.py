import gzip
from functools import partial
import time
import json

RECORD_SIZE = 4096
start_time_1 = time.time()

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
end_time_1 = time.time()
#alternative


import gzip

all_data = ""
start_time_2 = time.time()
with gzip.open("k.json.gz","rt") as f:
    for _ in range(1):
        # Read a chunk of data
        chunk = f.read(4096)  # Adjust the chunk size as needed

        # Check if the chunk is empty, indicating end of file
        if not chunk:
            break

        all_data += chunk
end_time_2 = time.time()

# Next Alternative

import gzip
import time
all_data = ""
start_time_3 = time.time()

with gzip.open("k.json.gz","rt") as f:
    for _ in range(10):
        # Read a chunk of data
        chunk = f.read(4096)  # Adjust the chunk size as needed

        # Check if the chunk is empty, indicating end of file
        if not chunk:
            break

        all_data += chunk

end_time_3 = time.time()

exec_time_1 = end_time_1 - start_time_1
exec_time_2 = end_time_2 - start_time_2
exec_time_3 = end_time_3 - start_time_3

print(exec_time_1)
print(exec_time_2)
print(exec_time_3) # seems to be the quickest


## Next step we need to get some of the json data into a dict format for examination

import json

all_data = all_data.encode("utf-8")
resp = json.loads()

# the above didn't work hence need to try incrementally until complete json doc is found

import json
with gzip.open("k.json.gz","rt") as f:
    json_doc_stream = ""
    doc_count = 0
    while doc_count <= 2:
        json_data = f.read(4096)
        if not json_data:
            break
        json_doc_stream += json_data


        try:
            json_complete_doc = json.loads(json_doc_stream)
            print("complete json doc ")
            print(json_complete_doc)
            doc_count += 1
        except json.JSONDecodeError:
            continue


## still unable to get a complete json doc



