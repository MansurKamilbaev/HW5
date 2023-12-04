class Pet:
    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed

pet=Pet(name="Marazm",age="2",breed="Volkodav")
print(pet.name, pet.age,pet.breed)