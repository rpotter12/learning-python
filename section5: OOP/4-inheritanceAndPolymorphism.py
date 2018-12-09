class Animal():
    def __init__(self):
        print('animal created')
    def who_am_i(self):
        print('I am animal')
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
    def who_am_i(self):
        print('I am a dog')
my_dog=Dog()
my_dog.who_am_i()

