#Find the missing and repeating number

'''
input: arr[] = {3, 1, 3}
Output: Missing = 2, Repeating = 3
Explanation: In the array, 2 is missing and 3 occurs twice 

Input: arr[] = {4, 3, 6, 2, 1, 1}
Output: Missing = 5, Repeating = 1   '''


arr=list(map(int,input("Enter an array:").split()))  #Enter space separated numbers

arr.sort()

for num in range(len(arr)):
    if num+1==arr[num]:
        continue
    else:
        print("Missing number:",num+1)
        break 
for num in range(len(arr)):
    if arr.count(arr[num])>1:
        print("Repeating number:",arr[num])
        break

