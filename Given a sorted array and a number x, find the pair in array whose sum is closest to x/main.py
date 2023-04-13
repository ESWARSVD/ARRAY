#Given a sorted array and a number x, find the pair in array whose sum is closest to x
'''
Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10
'''

arr=list(map(int,input("Enter an array:").split()))    # Enter space separated numbers

x=int(input("Enter sum number:"))  #Enter number

pairs=[]
for num in range(len(arr)-1):
    for num1 in range(num+1,len(arr)):
        pairs.append([arr[num],arr[num1]])

index=0
diff=x

for pair in range(len(pairs)):
    difference=x-(sum(pairs[pair]))
    if difference<0:
        difference=-difference
    if diff<difference:
        diff=diff
        index=index 
    else:
        diff=difference
        index=pair 

print("closest pair:",pairs[index][0],"and",pairs[index][1])