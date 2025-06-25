# Class for animals
class Animal:
    
    # initialize the animal with name and species
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # method to make an animal sound (overwritten later)
    def make_sound(self):
        return "generic animal sound"
    
    # method to return info about the animal
    def info(self):
        return f"{self.name} is a {self.species} that makes a '{self.make_sound()}' sound."

# Bear class that inherits from Animal
class Bear(Animal):

    # initialize the bear with name, species, and fur color
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    # method to overwrite with bear sound
    def make_sound(self):
        return "roar"

    # method to return info about the bear
    def info(self):
        return f"{self.name} is a bear of the {self.species} species with {self.fur_color} fur and makes a '{self.make_sound()}' sound."

# Elephant class that inherits from Animal
class Elephant(Animal):

    # initialize the elephant with name, species, and weight
    def __init__(self, name, species, weight):
        super().__init__(name, species)
        self.weight = weight

    # method to overwrite with elephant sound
    def make_sound(self):
        return "trumpet"

    # method to return info about the elephant
    def info(self):
        return f"{self.name} is an elephant of the {self.species} species weighing {self.weight} kg and makes a '{self.make_sound()}' sound."

# Penguin class that inherits from Animal
class Penguin(Animal):
    # initialize the penguin with name, species, and height
    def __init__(self, name, species, height):
        super().__init__(name, species)
        self.height = height

    # method to overwrite with penguin sound
    def make_sound(self):
        return "squawk"

    # method to return info about the penguin
    def info(self):
        return f"{self.name} is a penguin of the {self.species} species and stands at a height of {self.height}ft and makes a '{self.make_sound()}' sound."

# extra: Monkey class that inherits from Animal
class Monkey(Animal):
    # initialize the monkey with name, species, and swing distance
    def __init__(self, name, species, swing_distance):
        super().__init__(name, species)
        self.swing_distance = swing_distance

    # method to overwrite with monkey sound
    def make_sound(self):
        return "ooh-ooh aah-aah"

    # method to return info about the monkey
    def info(self):
        return f"{self.name} is a monkey of the {self.species} species that can swing {self.swing_distance}ft and makes an '{self.make_sound()}' sound."

# creating the menu functions
def show_main_menu():
    print("\n===Zoo Menu===")
    print("1) Add animals")
    print("2) Print all")
    print("3) Print specific")
    print("0) Exit")
    print("===============")

# creating the menu functions
def show_add_menu():
    print("\n===Add Menu===")
    print("1) Add Bear")
    print("2) Add Elephant")
    print("3) Add Penguin")
    print("4) Add Monkey")
    print("===============")

# creating the menu functions
def show_print_menu():
    print("\n===Print Menu===")
    print("1) Print Bears")
    print("2) Print Elephants")
    print("3) Print Penguins")
    print("4) Print Monkeys")
    print("===============")

# create the main function
def main():
    
    # list for all animals in the zoo
    zoo = []

    while True:
        show_main_menu()
        choice = input("User Input: ")

        # handles user input for adding an animal
        if choice == "1":
            show_add_menu()
            animal_type = input("Input Animal Type: ")
            name = input("Input Name: ")
            species = input("User Input Species: ")

            # shorter as this does not need float validation/error handling
            if animal_type == "1":
                fur = input("User Input Fur Color: ")
                zoo.append(Bear(name, species, fur))
                print("Bear added to zoo.")

            # these include a check to insure the user enters a number
            elif animal_type == "2":
                while True:
                    weight_input = input("User Input Weight (in kg): ")
                    try:
                        weight = float(weight_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value for weight.")
                zoo.append(Elephant(name, species, weight))
                print("Elephant added to zoo.")

            elif animal_type == "3":
                while True:
                    height_input = input("User Input Height (in ft): ")
                    try:
                        height = float(height_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value for height.")
                zoo.append(Penguin(name, species, height))
                print("Penguin added to zoo.")

            elif animal_type == "4":
                while True:
                    distance_input = input("User Input Swing Distance (in ft): ")
                    try:
                        distance = float(distance_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value for swing distance.")
                zoo.append(Monkey(name, species, distance))
                print("Monkey added to zoo.")

            else:
                print("Invalid animal selection.")

        # handles user input for printing animals
        elif choice == "2":
            if not zoo:
                print("Zoo is empty.")
            for animal in zoo:
                print(animal.info())

        # handles user input for printing specific animal types
        elif choice == "3":
            show_print_menu()
            type_choice = input("User Input: ")

            if type_choice == "1":
                for animal in zoo:
                    if isinstance(animal, Bear):
                        print(animal.info())

            elif type_choice == "2":
                for animal in zoo:
                    if isinstance(animal, Elephant):
                        print(animal.info())

            elif type_choice == "3":
                for animal in zoo:
                    if isinstance(animal, Penguin):
                        print(animal.info())

            elif type_choice == "4":
                for animal in zoo:
                    if isinstance(animal, Monkey):
                        print(animal.info())

            else:
                print("Invalid selection.")


        elif choice == "0":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()