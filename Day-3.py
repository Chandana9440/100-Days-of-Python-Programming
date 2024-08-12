print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
input1= input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ")
if input1=="left":
    input2= input("Type swim or wait")
    if input2=="wait":
        input3=input("Which door? Red, blue or yellow")
        if(input3=="red"):
            print("Burned by fire, Game over")
        elif(input3=="blue"):
            print("Eaten by beasts, Game Over")
        elif(input3=="yellow"):
            print("You win!")
        else:
            print("Game Over")
    else:
         print("Game over")
else:
    print("Game over")
    