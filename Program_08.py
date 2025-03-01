#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
numbers = []
odd_count = 0
for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)
