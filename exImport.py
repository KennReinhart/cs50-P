#trying import from lecture4
import sys
from lecture4 import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])