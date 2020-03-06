class Pet():
    def __init__(self):
        self.__name = 'None'
        self.__animal_type = 'None'
        self.__age = 'None'

    def setname(self, name):
        self.__name = name

    def setnanimal_type(self, animal_type):
        self.__animal_type = animal_type

    def setage(self, age):
        self.__age = age
    
    def getname(self):
        return self.__name

    def getanimal_type(self):
        return self.__animal_type

    def getage(self):
        return self.__age

    def __str__(self):
        return f'name :{self.__name}, animal_type : {self.__animal_type} and age : {self.__age} '

pet = Pet()
pet.setname('bruno')
pet.setnanimal_type('Dog')
pet.setage(20)


print(pet)

    