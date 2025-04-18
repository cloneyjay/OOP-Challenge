class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting at middle value
        self.energy = 10  # Starting with full energy
        self.happiness = 5  # Starting at middle value
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Reduce hunger but not below 0
        self.happiness = min(10, self.happiness + 1)  # Increase happiness but not above 10
        print(f"{self.name} is eating... 🍽️")

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Increase energy but not above 10
        print(f"{self.name} is sleeping... 😴")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play! 😫")
            return
        
        self.energy = max(0, self.energy - 2)  # Decrease energy but not below 0
        self.happiness = min(10, self.happiness + 2)  # Increase happiness but not above 10
        self.hunger = min(10, self.hunger + 1)  # Increase hunger but not above 10
        print(f"{self.name} is playing... 🎾")

    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger} {'🟥' * self.hunger}{'⬜' * (10-self.hunger)}")
        print(f"Energy: {self.energy} {'🟦' * self.energy}{'⬜' * (10-self.energy)}")
        print(f"Happiness: {self.happiness} {'🟨' * self.happiness}{'⬜' * (10-self.happiness)}")
        if self.tricks:
            print(f"Tricks known: {', '.join(self.tricks)} 🎯")
        else:
            print("No tricks learned yet! 📚")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.energy = max(0, self.energy - 1)  # Training takes some energy
            self.happiness = min(10, self.happiness + 1)  # Learning makes pet happy
            print(f"{self.name} learned {trick}! 🌟")
        else:
            print(f"{self.name} already knows {trick}! 😊")

    def show_tricks(self):
        if self.tricks:
            print(f"\n{self.name}'s tricks:")
            for trick in self.tricks:
                print(f"- {trick} ✨")
        else:
            print(f"{self.name} doesn't know any tricks yet! 📚")