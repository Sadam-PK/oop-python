class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def like_walk(self):
        return True

    def bark(self):
        return 'Woof'


class GermanShepherd(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)


class Liza(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def fetchability(self):
        return 8


liza = Liza('Liza', 5)
walk = liza.like_walk()
print(liza.name, liza.age, walk, liza.fetchability())


# #------ multiple inheritance --------

class PitBull(Liza, GermanShepherd):
    def __init__(self, n, a):
        super().__init__(n, a)

    def bark(self):
        return 'Arf Arf'


pb = PitBull('PitBull', 1)
print(pb.name, pb.age, pb.like_walk(), pb.fetchability())

# #------- Polymorphism -------------

dog = Dog('Gneric', 10)
print(dog.name, dog.age, dog.bark())

print(pb.name, pb.age, pb.bark())
