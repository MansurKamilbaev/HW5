class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

person=Person("Abigneyl","22")
person2=Person("Price","21")
person3=Person("Simon","24")

print("Инормация о объектах: ")
print(f'Имя: {person.name}, Возраст: {person.age}')
print(f'Имя: {person2.name}, Возраст: {person2.age}')
print(f'Имя: {person3.name}, Возраст: {person3.age}')