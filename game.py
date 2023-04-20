#print("This is my first try at a text adventure game in python. So if it is trash it's because it's my first real text adventure game in python.")

inventory = []

choice = input("Do you want to play this text adventure game??\n(y/n)")

if choice == "y":
    print("I see that you want to try out my game.")
else:
    exit()


name = input("What do you wan the name of your character to be?\n>")

print("Hello " + name + ". Are you ready to play this text adventure game?")


