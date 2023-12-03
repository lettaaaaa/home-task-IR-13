from enum import Enum


class Pet:

    def __init__(self, name, breed, age, greeting, mass, kind):
        self.name = name
        self.breed = breed
        self.age = age
        self.greeting = greeting
        self.mass = mass
        self.kind = kind

    def politeness_test(self):
        """визначає вічлива тварина, чи ні"""
        if self.greeting == "Hello":
            return True
        else:
            return False


class Kind(Enum):
    """зберігає числове значення для кожного виду тварин"""
    DOG = 1
    CAT = 2
    BIRD = 3


class Home:

    def __init__(self):
        self.list_pets = []

    def addPet(self, pet):
        self.list_pets.append(pet)


def identifying_pairs_of_friends(*pet):
    """визначає пари друзів серед тварин, тварини друзі - якщо візниця віку меше 2 років"""
    for i in pet:
        for j in pet[pet.index(i)+1:]:
            if abs(i.age - j.age) < 2:
                print(f'{i.name} дружить з {j.name}')


def sortPetsByAge(pets):
    """сортує тварин за віком"""
    pets.sort(key=lambda x: x.age)


if __name__ == "__main__":
    dog = Pet('Арчі', "лабрадор", 2, "Hello", 30, Kind.DOG)
    cat1 = Pet('Тоша', "мейкун", 1, "Мяу", 5, Kind.CAT)
    cat2 = Pet('Кузя', "персідський", 1.5, "Hello", 4, Kind.CAT)
    bird = Pet('Кєша', "хвилястий", 7, "хочу їсти", 10, Kind.BIRD)

    home = Home()
    home.addPet(dog)
    home.addPet(cat1)
    home.addPet(cat2)
    home.addPet(bird)

    print("сортування тварин за віком")
    sortPetsByAge(home.list_pets)
    for i in home.list_pets:
        print(f'{i.name}, {i.age}')
    print()

    print(dog.politeness_test())
    print(cat1.politeness_test())
    print(cat2.politeness_test())
    print(bird.politeness_test())

    print()
    print("чи друзі тварини?")
    identifying_pairs_of_friends(dog, cat1, cat2, bird)
