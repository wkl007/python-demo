class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


animal = Animal()
dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

print(isinstance(dog, Dog), isinstance(dog, Animal), isinstance(cat, Cat), isinstance(animal, Dog))
