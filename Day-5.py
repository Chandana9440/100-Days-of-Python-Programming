# Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
list1=[]
for i in range(1,nr_letters+1):
    list1.append(random.choice(letters))
for i in range(1,nr_symbols+1):
    list1.append(random.choice(symbols))
for i in range(1,nr_numbers+1):
    list1.append(random.choice(numbers))
print(list1)
random.shuffle(list1) # random.shuffle function does not work with string so, first you are shuffling list and then converting to string.
print(list1)

passwrd=""
for i in list1:
    passwrd+=i
print(passwrd)
