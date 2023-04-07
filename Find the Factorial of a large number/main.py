# Find the Factorial of a large number

given_number=int(input("Enter number:"))  #enter a number

total=1

for fact in range(1,given_number+1):
    total=total*fact

#print factorial

print(total)
