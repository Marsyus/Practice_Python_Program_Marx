#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
numbers = []
odd_count = 0
for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)
for j in numbers:
    if j % 2:
        odd += 1
print(f"The count of odd numbers from all the 10 numbers is {odd_count}!")
