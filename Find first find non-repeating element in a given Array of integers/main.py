#Find first non-repeating element in a given Array of integers

arr=input("Enter array:").split(",")  #enter "," separated integers

result=True

for num in arr:
    if arr.count(num)==1:
        print(num)
        result=False
        break 
    else:
        continue
if result:
    print("No non-repeating element in the given array")
    