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
            if "subnets" in network_dict:
                for subnet_dict_1 in network_dict["subnets"]:
                    subnet_1 = Network(subnet_dict_1["name"])
                    subnet_1.cidr = subnet_dict_1["cidr"]
                    subnet_1.subnets = list()

                    if "subnets" in subnet_dict_1:
                        for subnet_dict_2 in subnet_dict_1["subnets"]:
                            subnet_2 = Network(subnet_dict_2["name"])
                            subnet_2.cidr = subnet_dict_2["cidr"]
                            subnet_2.subnets = list()

                            #network.subnets.subnets.append(subnet_2)

                            #######################
                            #pprint.pprint("2############")
                            #pprint.pprint(subnet_2)
                            #######################

                    network.subnets.append(subnet_1)

                    #######################
                    #pprint.pprint("1######")
                    #pprint.pprint(subnet_1)
                    #######################

            network_list.append(network)

            pprint.pprint(network_list)
            #######################
            #pprint.pprint("0###")
            #pprint.pprint(network)
            #######################

        return network_list

if __name__ == '__main__':
    json_file = open_file()
    foo = load_networks(json_file)
    pprint.pprint("##########################")
    pprint.pprint("#######  RESULT  #########")
    pprint.pprint("##########################")
    pprint.pprint(foo)
    # output = network.traverse()