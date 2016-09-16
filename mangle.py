import sys
import os
import json
import pprint
from model import Network
                                
if __name__ == '__main__':
    network = Network()
    foo = network.load_it()
    # output = network.traverse()