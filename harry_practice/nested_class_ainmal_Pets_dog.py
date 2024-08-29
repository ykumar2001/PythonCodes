# create a class Pets from a class Animals and furter create class Dog from pets.Add a method bark to class Dog.
class Animal:
    def __init__(self,species):
        self.species=species
class Pets(Animal):
    def __init__(self,category,species):
        super(). __init__(species)
        self.category=category
class dog(Pets):
    def __init__(self,category):
        super(). __init__("dog",category)
    def bark(self):
        return "woof"
dg=dog("tinggu")    
print(f"my dog name is {dg.category}.he is from {dg.species}") 
print(f"he says {dg.bark()}")   


class animal:
    def __init__(self,species):
        self.species=species
class pet(animal):
    def __init__(self,category):            
        self.category=category
class dog(pet):
    def __init__(self,name):
        self.name=name
    def bark(self):
        return "bhauuuu!"
dgg=dog("chotu badmas")
print(f"my dog name is {dgg.name}")
print(f"he says {dgg.bark()}")                

class Animal :
    def __init__(self,species):
        self.species=species

    class Pets:
        def __init__(self,category):
            self.category=category

        class Dog:
            def __init__(self,name):
                self.name=name

            def bark(self):
                return "bhauu bhau!!"
dgg=Animal.Pets.Dog("billu badmas")
print(f"my dog name is {dgg.name}")
print(f"he says {dgg.bark()}")