#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
numbers = []
for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)
add = sum(numbers)
print(f"The summation of all the 10 numbers is {add}!")
