class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Голос собаки: Гав-гав!")

class Cat(Animal):
    def make_sound(self):
        print("Голос кошки: Мяу-мяу!")

class Cow(Animal):
    def make_sound(self):
        print("Голос коровы: Му-му!")

dog=Dog()
cat=Cat()
cow=Cow()

dog.make_sound()
cat.make_sound()
cow.make_sound()