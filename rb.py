print("Hello, welcome to Adrian's Coffee!!!!!!!!!")

name = input("What is your name?\n")

if name == "Ben":
     evil_status = input("Are you evil\n?")
     if evil_status == "Yes":
         print("You're not welcome here Ben!! Get out!!")
         exit()
else:
    print("Hello " + name + ", thank you so much for coming in today!!\n\n\n")    

menu = ("Black Coffee, Espresso, Cappuccino, Frappuccino, Latte")

print ("Here's your menu " + name + "\n" + menu)

order = input("What would you like from it " + name + " ?\n") 
 
quantity = input("How many coffee's would you like " + name + " ?\n")

price = 0

if order == "Frappuccino":
    price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    price = 9
elif order == "Cappuccino":
    price = 10
else:
    print("We dont have that here. Sorry!")

total = price * int(quantity)

print("Sound good " + name + ", we'll have your " + order + " ready for you in a moment.")

print("Thanks for the order. Your total is " + str(total))


