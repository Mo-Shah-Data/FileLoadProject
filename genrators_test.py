import gzip
import json
with gzip.open("k.json.gz","rt") as f:
    x = f.readlines()
    ''.join(x)
    json_data = json.load(x)
    in_net_data = (print(k) for k,v in json_data.items())
    # variable is too big to use json.dumps() also having memeory issues

