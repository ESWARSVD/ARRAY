# Chocolate Distribution Problem
'''
Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , students= 3 
Output: Minimum Difference is 2 
Explanation:
We have seven packets of chocolates and we need to pick three packets for 3 students 
If we pick 2, 3 and 4, we get the minimum difference between maximum and minimum packet sizes.

Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , students = 5 
Output: Minimum Difference is 6 
'''

arr=list(map(int,input("Enter an array:").split(",")))  # Enter , separated numbers

students=int(input("Enter number of students:"))   #Enter a number

length=len(arr)


#sort the array
arr.sort()

if (length==0 or students==0):
    print("difference=",0)
elif (length<students):
    print("difference="-1)
else:

    min_diff=arr[-1]-arr[0]

    for num in range(length-students+1):
        diff=(arr[num]+students-1)-arr[num]
        min_diff=min(min_diff,diff)
    

    print("difference=",min_diff)




