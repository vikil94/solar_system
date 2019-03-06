class System:


    bodies = []

    def add(self, body):
        self.bodies.append(body)

    def total_mass(self):
        total = 0
        for body in self.bodies:
            total += body.mass
        return total


class Body():


    def __init__(self, name, mass):
        self.name = name
        self.mass = mass


class Planet(Body):

    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year


class Star(Body):


    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type


class Moon(Body):


    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet
