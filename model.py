
class Network(object):
    def __init__(self, name):
        self.name = name
        self.cidr = ""
        self.subnets = []

    def __repr__(self):
        return "Network(name={}, cidr={}, subnets={})".format(
            self.name,
            self.cidr,
            self.subnets,
        )
    """
    def load_it(self, networks_dict):
        self.name = networks_dict["name"]
        self.cidr = networks_dict["cidr"]
        try:
            for network in networks_dict["subnet"]:
                if "subnets" in network:
                    self.traverse(network)
        except TypeError:
            pass

    def traverse(self, networks_dict):
        #pprint.pprint(networks_dict)
        network = Network()
        self.name = networks_dict["name"]
        self.cidr = networks_dict["cidr"]
        self.subnet = network.traverse(networks_dict)
        pprint.pprint(self)
    """