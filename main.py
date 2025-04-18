from pet import Pet
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\n=== Pet Care Menu ===")
    print("1. Feed pet 🍽️")
    print("2. Play with pet 🎾")
    print("3. Let pet sleep 😴")
    print("4. Check pet status 📊")
    print("5. Teach new trick 🎯")
    print("6. Show tricks 📝")
    print("7. Exit 👋")
    print("==================")

def main():
    clear_screen()
    print("Welcome to Virtual Pet Simulator! 🐾")
    name = input("What would you like to name your pet? ")
    pet = Pet(name)
    print(f"\nMeet {name}! Take good care of them!")
    time.sleep(2)

    while True:
        clear_screen()
        pet.get_status()
        display_menu()
        
        choice = input("\nWhat would you like to do? (1-7): ")
        
        if choice == "1":
            pet.eat()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            pet.get_status()
        elif choice == "5":
            trick = input("What trick would you like to teach? ")
            pet.train(trick)
        elif choice == "6":
            pet.show_tricks()
        elif choice == "7":
            print(f"\nGoodbye! Thanks for taking care of {pet.name}! 👋")
            break
        else:
            print("Invalid choice! Please select 1-7")
        
        time.sleep(5)

if __name__ == "__main__":
    main()