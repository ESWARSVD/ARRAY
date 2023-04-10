# Minimum number of jumps to reach end

#Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
#Output: 3 (1-> 3 -> 9 -> 9)
#Explanation: Jump from 1st element to 2nd element as there is only 1 step.
#Now there are three options 5, 8 or 9. 
#if 8 or 9 is chosen then the end node 9 can be reached. So 3 jumps are made.

#Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
#Output: 10

arr=list(map(int,input("Enter an array: ").split()))   # Enter space separated integers

length=len(arr)

jump=arr[0]
count=1
while jump<length:
    count+=1

    jump=jump+arr[jump]

print(count)

