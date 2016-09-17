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
            network.subnets = list()
            pprint.pprint("####")
            pprint.pprint(network)
            if "subnets" in network_dict:
                for subnet_dict_1 in network_dict["subnets"]:
                    subnet_1 = Network(subnet_dict_1["name"])
                    subnet_1.cidr = subnet_dict_1["cidr"]
                    subnet_1.subnets = list()
                    pprint.pprint("#### ####")
                    pprint.pprint(subnet_1)
                    if "subnets" in subnet_dict_1:
                        for subnet_dict_2 in subnet_dict_1["subnets"]:
                            pprint.pprint(subnet_dict_2)
                            subnet_2 = Network(subnet_dict_2["name"])
                            subnet_2.cidr = subnet_dict_2["cidr"]
                            subnet_2.subnets = list()
                            pprint.pprint("#### #### ####")
                            pprint.pprint(subnet_2)
                            subnets.subnets.append(subnet_2)
                    # network_list.subnets.append(subnet_1)
                    # pprint.pprint(subnet)
            network_list.append(network)
        return network_list

if __name__ == '__main__':
    json_file = open_file()
    foo = load_networks(json_file)
    # pprint.pprint(foo)
    # output = network.traverse()