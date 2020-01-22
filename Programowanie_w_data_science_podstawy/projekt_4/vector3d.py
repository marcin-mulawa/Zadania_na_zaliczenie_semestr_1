class Vector3d():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "x = {}, y = {}, z = {}".format(self.x, self.y, self.z)

    def modul(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def iloczyn_skalarny(self, x, y, z):
        return self.x * x + self.y * y + self.z * z

    def iloczyn_przez_liczbe(self, number):
        return(Vector3d(self.x * number, self.y * number, self.z * number))

    def zwieksz(self, x, y, z):
        return(Vector3d(self.x + x, self.y + y, self.z + z))

    def zmniejsz(self, x, y, z):
        return(Vector3d(self.x - x, self.y - y, self.z - z))

    def przeciwny(self):
        return(Vector3d(self.x *(-1), self.y *(-1), self.z *(-1)))

    def iloczyn_wektorowy(self, x, y, z):
        return(Vector3d(self.y * z - self.z * y, self.z * x - self.x * z, self.x * y - self.y * x))
