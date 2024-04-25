class Dog:
    def __init__(self, breed, age, color, name): #self is must
        self.breed = breed
        self.age = age
        self.color = color
        self.name = name
    def say_age(self):
        words_to_say = 'I am ' + str(self.age) + ' years old'
        print(words_to_say)

    def intro(self):
        print('Hi')
        print('I am a ' + (self.breed) + ' dog')
        print('I am ' + str(self.age) + ' years old')
        print('I am ' + (self.color) + ' in color')

    def run(self, speed):
        print('I am', self.name)
        print('Okay, i will run in', str(speed), 'km/hr')
        print()

    def bark(self):
        print('woof! woof!')

    def sleep(self):
        print('zzz.....')

    def eat(self):
        print('Nom nom nom')

dog = Dog('Bhutanese', 20, 'black', 'Tomy')
petdog = Dog('pug', 10, 'white', 'puku')
my_friends_dog = Dog('German shephard', 15, 'brown', 'Viki')
dog.sleep()
dog.eat()
dog.bark()

dog.say_age()
petdog.say_age()

dog.intro()
petdog.intro()
my_friends_dog.intro()


print(dog.name)
print(petdog.name)
print(my_friends_dog.name)

how_fast_should_dog_run = 1000
dog.run(10)
dog.run(100)
dog.run(how_fast_should_dog_run)
petdog.run(20)