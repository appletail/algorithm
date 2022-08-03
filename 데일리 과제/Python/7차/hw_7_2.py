class Doggy():

    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, dog_name, dog_breed):
        self.dog_name = dog_name
        self.dog_breed = dog_breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def bark(self):
        print('bark')

    def __del__(self):
        Doggy.num_of_dogs -= 1
    
    def get_status(self):
        print(f'출생수: {Doggy.birth_of_dogs}, 견수: {Doggy.num_of_dogs}')

dog1 = Doggy('쫑이', '웰시코기')
dog2 = Doggy('덕구', '진돗개')
dog3 = Doggy('존', '보더콜리')
del dog2

dog1.bark()
dog1.get_status()