class Gate:
    def __init__(self, t, n, i, loc, inp=None, out=None):
        self.type = t
        self.name = n
        self.index = i
        self.location = loc
        self.input = inp
        self.output = out

    def __str__(self):
        ostream = "TYPE : " + self.type + "\n"
        ostream += "NAME : " + self.name + "\n"
        ostream += "INDEX : " + str(self.index) + "\n"
        ostream += "LOCATION : " + str(self.location) + "\n"
        ostream += "INPUT : " + str(self.input) + "\n"
        ostream += "OUTPUT : " + str(self.output)
        return ostream
