class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError()

    def eat(self):
        print(f"{self.name} кушает.")


class Bird(Animal):
    def make_sound(self):
        print("Курлык")


class Mammal(Animal):
    def make_sound(self):
        print("Мур, мур")


class Reptile(Animal):
    def make_sound(self):
        print("Шшшшшшшш")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


bird = Bird("Воробей", 1)
mammal = Mammal("Кот", 2)
reptile = Reptile("Змея", 3)

animals = [bird, mammal, reptile]
print(animal_sound(animals))
print(f"{bird.name} - {bird.age}, {mammal.name} - {mammal.age}, {reptile.name} - {reptile.age}")
animal_sound(animals)


class Staff:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        print(f"{self.name} работает как {self.position}")

    def worker(self):
        raise NotImplementedError()


class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "Укратитель")

    def feed_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} кормит {animal.name}.")
            animal.eat()
        else:
            print("Это не животное!")


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} лечит {animal.name}.")
        else:
            print("Это не животное!")


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staffs = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"Животное {animal.name} добавлено в зоопарк.")
        else:
            print("Это не животное!")

    def add_staff(self, staff):
        if isinstance(staff, Staff):
            self.staffs.append(staff)
            print(f"Сотрудник {staff.name} добавлен в зоопарк.")
        else:
            print("Это не сотрудник!")

    def show_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"{animal.name}, Возраст: {animal.age}")

    def show_staff(self):
        print("Сотрудники зоопарка:")
        for staff in self.staffs:
            print(f"{staff.name}, Должность: {staff.position}")


zoo = Zoo("Зоопарк 'Сафари'")

bird = Bird("Воробей", 1)
mammal = Mammal("Кот", 2)
reptile = Reptile("Змея", 3)

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zookeeper = ZooKeeper("Иван")
veterinarian = Veterinarian("Анна")

zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

zoo.show_animals()
zoo.show_staff()
