class Pet:
    all=[]

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception ("Invalid pet type!")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        if owner:
            owner.add_pet(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
            self.pets_list.append(pet)
        else:
            raise Exception ("Invalid pet type!")

    def pets(self):
        return self.pets_list

    def sort_pets_by_name(self):
        self.pets_list.sort(key=lambda pet: pet.name)
        
    
    def get_sorted_pets(self):
        self.sort_pets_by_name()
        return self.pets_list