#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

num_01 = input("Enter your first number: ")
num_02 = input("Enter your second number: ")
if num_01 > num_02:
    print(f"\nThe first number, {num_01}, is larger!")
elif num_01 < num_02:
    print(f"\nThe second number, {num_02}, is larger!")
