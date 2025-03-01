#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
print("The following are all numbers except numbers ending in 0:\n")
for i in range (101):
    if i % 10:
        print(i)
