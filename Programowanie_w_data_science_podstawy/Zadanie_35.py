class Kwadrat():
    def __init__(self, bok):
        self.bok = bok

    def __repr__(self):
        return "bok = {}".format(self.bok)

    def pole(self):
        self.pole = self.bok ** 2
        return self.pole

    def obwod(self):
        self.obwod = self.bok * 4
        return self.obwod