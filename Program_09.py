#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
even_numbers = []
for i in range (101):
    if i % 2 == 0:
        even_numbers.append(i)
print("The following are all even numbers starting from 0 to 100:\n")
for j in even_numbers:
    print(j)
