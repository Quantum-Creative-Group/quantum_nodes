class Gate:
    def __init__(self, t, n, loc, inp = None, out = None):
        self.type = t
        self.name = n
        self.location = loc
        self.input = inp
        self.output = out