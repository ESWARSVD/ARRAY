# find the common elements in three sorted arrays


arr1=input("Enter first array:").split()  #enter space separated numbers

arr2=input("Enter second array:").split()   #enter space separated numbers

arr3=input("Enter third array:").split()  #enter space separated numbers

for num in arr1:
    if num in arr2 and num in arr3:
        print(num)
        arr2.remove(num)
        arr3.remove(num)
    else:
        continue 
