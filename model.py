import json

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
            if "subnets" in networks_dict:
                for network_dict in networks_dict:
                    print("doing something")
                    network = Network()
                    network.name = network_dict["name"]
                    network.cidr = network_dict["cidr"]
                    network.subnets = self.__class__().traverse(network_dict)
                    network.subnets.append(network)

                return network
