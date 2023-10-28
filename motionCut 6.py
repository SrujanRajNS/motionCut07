import time

def introduction():
    print("Welcome to the Treasure Hunt Adventure!")
    print("You are on a quest to find a hidden treasure.")
    print("Your journey begins now...\n")

def choose_path():
    print("You come to a crossroads. Do you want to go left or right?")
    choice = input("Enter 'left' or 'right': ").lower()
    if choice == "left":
        return "left"
    elif choice == "right":
        return "right"
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        return choose_path()

def left_path():
    print("\nYou chose the left path.")
    time.sleep(1)
    print("You encounter a deep forest.")
    time.sleep(1)
    print("Do you want to 'explore' the forest or 'turn back'?")
    choice = input("Enter 'explore' or 'turn back': ").lower()
    if choice == "explore":
        return "forest"
    elif choice == "turn back":
        return "start"
    else:
        print("Invalid choice. Please enter 'explore' or 'turn back'.")
        return left_path()

def right_path():
    print("\nYou chose the right path.")
    time.sleep(1)
    print("You reach a riverbank.")
    time.sleep(1)
    print("Do you want to 'follow' the river or 'cross' it?")
    choice = input("Enter 'follow' or 'cross': ").lower()
    if choice == "follow":
        return "river"
    elif choice == "cross":
        return "start"
    else:
        print("Invalid choice. Please enter 'follow' or 'cross'.")
        return right_path()

def forest_path():
    print("\nYou explore the forest and find an old map.")
    time.sleep(1)
    print("The map leads you to the hidden treasure!")
    print("Congratulations! You have found the treasure.")
    print("You win!\n")

def river_path():
    print("\nYou follow the river for a while, but it leads to a dead end.")
    time.sleep(1)
    print("You realize you should have taken another path.")
    print("You lose.\n")

def start_game():
    introduction()
    while True:
        choice = choose_path()
        if choice == "left":
            choice = left_path()
            if choice == "forest":
                forest_path()
                break
        elif choice == "right":
            choice = right_path()
            if choice == "river":
                river_path()
                break

if __name__ == "__main__":
    start_game()
