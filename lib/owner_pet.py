class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner = ""):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        # breakpoint()

    @property
    def pet_type(self):
        return self._pet_type 

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise TypeError ("wrong dog dawg")
        self._pet_type = pet_type

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # breakpoint()
        return [pet for pet in Pet.all if pet.owner == self] 
    
    def add_pet(self, pet):
        if not isinstance(pet,Pet):
            raise TypeError("wrong pet")
        pet.owner = self    

    def get_sorted_pets(self):
        # breakpoint()
        return sorted([pet for pet in self.pets()], key = lambda pet : pet.name)