import sys
import os
import json
import pprint
from model import Network
import sys
sys.setrecursionlimit(100)


def open_file():
    with open("mangle.json", "r") as network_file:
        return json.load(network_file)

def load_networks(networks_dict):
        network_list = []
        for network_dict in networks_dict:
            network = Network(network_dict["name"])
            network.cidr = network_dict["cidr"]
            if "subnets" in network_dict:
                for subnet_dict in network_dict["subnets"]:
                    # pprint.pprint(subnet_dict)
                    subnet = Network(subnet_dict["name"])
                    subnet.cidr = subnet_dict["cidr"]

                    # pprint.pprint(subnet)
            network_list.append(network)
        return network_list

if __name__ == '__main__':
    json_file = open_file()
    foo = load_networks(json_file)
    pprint.pprint(foo)
    # output = network.traverse()