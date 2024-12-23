class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []  # Track all pets created, changed from `all_pets` to `all` to match the test
    
    def __init__(self, name, pet_type, owner=None):
        """Initialize a Pet instance with a name, pet type, and optional owner"""
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"{pet_type} is not a valid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner  # Store the pet's owner, if provided
        if owner:
            owner.add_pet(self)  # Automatically add pet to the owner's list if an owner is provided
        Pet.all.append(self)  # Add pet to the class-level list


class Owner:
    def __init__(self, name):
        """Initialize an Owner with a name and an empty list of pets"""
        self.name = name
        self._pets = []  # Renamed the attribute to _pets to avoid shadowing pets() method
    
    def pets(self):
        """Return the list of pets owned by this owner"""
        return self._pets
    
    def add_pet(self, pet):
        """Add a pet to the owner's collection of pets if it is a valid Pet instance"""
        if isinstance(pet, Pet):
            self._pets.append(pet)
            pet.owner = self  # Set the owner of the pet
        else:
            raise ValueError("Only instances of Pet can be added.")
    
    def get_sorted_pets(self):
        """Return the owner's pets sorted by name"""
        return sorted(self._pets, key=lambda pet: pet.name)


