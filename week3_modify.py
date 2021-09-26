from random import randrange

user_pets = []


class Pet:
    hunger_threshold = 5
    hunger_decrement = 3
    boredom_threshold = 5
    boredom_decrement = 3
    sounds = ["Hi", "Hello"]

    def __init__(self, name):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]

    def clock_tick(self):
        self.hunger = self.hunger + 1
        self.boredom = self.boredom + 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "Happy"
        elif self.hunger >= self.hunger_threshold and self.boredom >= self.boredom_threshold:
            return "Hungry and Bored"
        elif self.hunger >= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "Hungry"
        else:
            return "Bored"

    def __str__(self):
        return "I'm " + self.name + "and I am" + self.mood()

    def teach(self, word):
        self.sounds.append(word)
        self.word = word
        print("I learned the word " + self.word)
        self.reduce_boredom()

    def hi(self):
        print("I'm " + self.name)
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def feed(self):
        print("Delicious!")
        self.reduce_hunger()

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)


class Dog1(Pet):
    def __init__(self):
        print("Dog1 created")


class Dog2(Pet):
    def __init__(self):
        print("Dog2 Created")


class Dog3(Dog1, Dog2):
    def __init__(self):
        print("Dog 3 Created")


class Cat(Pet):
    def __init__(self):
        print("Cat class Created")


def display_user_pets():
    print("Your Pets")
    for pet in user_pets:
        print(f"\n{pet}")

d1 = Dog1()
d2 = Dog2()
d3 = Dog3()
c1 = Cat()
ch = " "
while ch != 0:
    display_user_pets()
    print("\n 1.Adopt\n 2.Feed\n 3.Greet\n 4.Teach")
    ch = int(input("Enter the choice:"))
    if ch == 1:
        print('\nAdopt a new pet!')
        pet_name = input('Enter the pet name: ')
        user_pets.append(Pet(pet_name))
    elif ch in range(2, 5):
        name = input('Enter pet name to interact: ')
        p1 = Pet(name)
        for i in range(len(user_pets)):
            if user_pets[i] == name:
                if ch == 2:
                    p1.feed()
                    p1.clock_tick()
                elif ch == 3:
                    p1.hi()
                    p1.clock_tick()
                elif ch == 4:
                    word = input("Enter the word to learn the pet:")
                    p1.teach(word)
                    p1.clock_tick()
    else:
        exit()
