## Libraries
import random

## Modules
coin = random.choice(["heads", "tails"])

print(coin)

prize = random.randint(10000,10000000)

print(prize)

cards = ["Jack", "Queen", "King", "Ace"]

random.shuffle(cards)

for card in cards:
    print(card)

## Statistic
import statistics

print("Mean of 90-100 is",statistics.mean([100, 90]))

## CMD line arguments

# sys, docs.python.org/3/library/sys.html
import sys

# print("Hello, my name is", sys.argv[1])
'''
py lecture4.py Ken!
output would be "Hello, my name is Ken"
'''
# Check for errors
if len((sys.argv[1])) < 2:
    sys.exit("Too few arguments")

# to avoid argv[0] which is the file name
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)

## Packages
# PyPI, python package index, pypi.org

#46.37, pip install cowsay

import cowsay
import sys

if len(sys.argv) == 2:
    #cow, trex,
    cowsay.trex("Hello, " + sys.argv[1])

# API (Application rogramming interface), requests, JSON (javascript object notation)
import json
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search/entity=song&limit=1&term=" + sys.argv[1])
# dumps, dump string
# print(json.dumps(response.json()))

o = response.json()
for result in o["results"]:
    print(result["artistName"])

# Custom libraries
def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

def main():
    hello("World")
    goodbye("World")

if __name__ == '__main__':
    main()