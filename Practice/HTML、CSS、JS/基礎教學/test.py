class Animal:
    category="動物"

    def __init__(self,species):
        self.species=species

dog=Animal("狗")
print(f'{dog.species}是{dog.category}')