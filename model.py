import json
import pprint

class Network(object):
    def __init__(self):
        self.name = ""
        self.cidr = ""
        self.subnets = []

    def __repr__(self):
        return "Network(name={}, cidr={}, subnets={})".format(
            self.name,
            self.cidr,
            self.subnets,
        )

    def load_it(self, **kwargs):
        with open("mangle.json", "r") as network_file:
            networks_dict = json.load(network_file)
            self.traverse(networks_dict)
            return(networks_dict)

    def traverse(self, networks_dict):
        for network_dict in networks_dict:

            self.name = network_dict['name']
            self.cidr = network_dict['cidr']
            self.subnets = self.__class__(network_dict).traverse()

        print(self)