"""import random
ax = random.choice(['0', '1'])

#or

from random import choice
ax = choice(['0', '1'])

bx = random.randint(1, 100)

import random
n = [1,2,3,4,5,6,7,8,9,0]

random.shuffle(n)

for N in n:
    print(N, end='')
print()

import statistics
x = [20,22,24,25,27]

y = statistics.mean(x)

print(y)"""

#########################################2

import sys

"""print('my program name is', sys.argv[0], 'and', 'my program name is', sys.argv[1])"""
"""
if len(sys.argv) < 2:
    sys.exit('Too Few Arguments')

for arg in sys.argv:
    print('My name is', arg)
"""
# the problem with it is that it print [0]

"""n = [1,2,3,4,5,6,7,8,9]

print(n[3:6])"""

"""if len(sys.argv) < 2:
    sys.exit('Too Few Arguments')

for arg in sys.argv[1:]:
    print('My name is', arg)

if len(sys.argv) < 2:
    sys.exit('Too Few Arguments')

for arg in sys.argv[1:-1]:
    print('My name is', arg)

import cowsay

cowsay.cow('Hii ' + sys.argv[1])"""


"""import cowsay

cowsay.trex('Hii ' + sys.argv[1])"""


import json
import requests

if len(sys.argv) != 2:
    sys.exit()

o = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]
)

"""print(json.dumps(o.json(), indent=2))"""

oo = o.json()

for res in oo["results"]:
    print(res["trackName"])
