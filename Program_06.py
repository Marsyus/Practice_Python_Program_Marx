#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
num_01 = int(input("Enter your first number: "))
num_02 = int(input("Enter your second number: "))
power = num_01 ** num_02
print(f"When {num_01} is raised to {num_02}, the result is {power}!")
