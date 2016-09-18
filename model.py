
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