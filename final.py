import gzip
from functools import partial
import time
import json
from collections import deque

pattern = """{"rep"""

# Testing
# out = search(character="""{"rep""", pattern="""{"rep""", history=5)

def search(character, pattern, history=5):
    previous_chars = deque(maxlen=history)
    if character in pattern:
        previous_chars.append(character)
        if pattern in ''.join(previous_chars):
            yield pattern

RECORD_SIZE = 1

with gzip.open("k.json.gz","rt") as f:
    record = iter(partial(f.read, RECORD_SIZE), b'')
    # text = f.read()
    for _ in range(25):
        try:
            character = next(record)
            #print(character)
            output = ''.join(search(character,pattern,history=5))
            if output == pattern:
                print(output)

        except StopIteration:
            print("End of iterable reached")
            break


# previous_chars = deque(maxlen=history)
# previous_chars.append("5")
# print(''.join(previous_chars))
# pattern = """{"rep"""
# character = "u"
#
# previous_chars = deque(maxlen=5)
# previous_chars.append("u")
#
# if 'tu' in ''.join(previous_chars):
#     print(True)