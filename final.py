import gzip
from functools import partial
import time
import json
from collections import deque

pattern = """{"provider"""
# pattern2 = """{"rep"""
# Testing
# out = search(character="""{"r""", pattern="""{"rep""", history=5)
# ''.join(out) # success

def initial_search(character, pattern):
    if character in pattern:
        previous_chars.append(character)
        if pattern in ''.join(previous_chars):
            yield pattern

# previous_chars = deque(maxlen=5)
# for item in pattern2:
#     out = search(character=item, pattern="""{"rep""")

# def post_initial_search():
#     continue

RECORD_SIZE = 1

with gzip.open("k.json.gz","rt") as f:
    record = iter(partial(f.read, RECORD_SIZE), b'')
    previous_chars = deque(maxlen=10) # unbound with no maxlen

    for _ in range(2500):
        try:
            character = next(record)
            #print(character)
            output = ''.join(initial_search(character,pattern))
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