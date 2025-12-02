#test
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")
Animal("Leo", "Lion").make_sound()
