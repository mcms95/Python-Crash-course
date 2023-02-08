class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting!")

    def bark(self):
        """Simulate a dog barking in response to a command."""
        print(f"{self.name.title()} is barking!!")


my_dog = Dog('simba', 12)
second_dog = Dog('Preto', 6)

print(f"My dog's name is {my_dog.name.title()}")
print(f"And {my_dog.name.title()} is {my_dog.age} years old")
my_dog.sit()
my_dog.bark()
print("\n")

print(f"Your dog's name is {second_dog.name.title()}")
print(f"And {second_dog.name.title()} is {second_dog.age} years old")
second_dog.sit()
second_dog.bark()
