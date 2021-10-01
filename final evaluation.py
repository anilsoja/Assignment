D = {}


class Pet:
    def __init__(self, species=None, name=""):
        if species not in ['Dog', 'Cat', 'Horse', 'Hamster']:
            print("Species is not a dog, cat, horse or hamster!")
        self.species = species
        self.name = name

    def __str__(self):
        if len(self.name) == 0:
            print(f"Species of: {self.species}, unnamed")
        else:
            print(f"Species of: {self.species}, named {self.name}")


class Dog(Pet):
    def __init__(self, name="", chases="Cats"):
        Pet.__init__(self, "Dog", name)
        self.chases = chases

    def __str__(self):
        if len(self.name) == 0:
            print(f"Species of: {self.species}, unnamed, chases {self.chases}")
        else:
            print(f"Species of: {self.species}, named {self.name}, chases {self.chases}")


class Cat(Pet):
    def __init__(self, name="", hates="Dogs"):
        Pet.__init__(self, "Cat", name)
        self.hates = hates

    def __str__(self):
        if len(self.name) == 0:
            print(f"Species of: {self.species}, unnamed, hates {self.hates}")
        else:
            print(f"Species of: {self.species}, named {self.name}, hates {self.hates}")


D["Dog"] = []


