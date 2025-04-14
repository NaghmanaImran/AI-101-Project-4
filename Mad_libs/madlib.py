def madlib():
    print("Let's create a fun Mad Libs story!\n")
    
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")

    print("\n📖 Your Mad Libs story:")
    print(f"One day, {name} went to {place}. There, they saw a {adjective} {animal}.")
    print(f"Then, {name} {verb} with the {adjective} {animal}. Everyone was amazed!")

# Run the function only if this file is executed directly
if __name__ == "__main__":
    madlib()
