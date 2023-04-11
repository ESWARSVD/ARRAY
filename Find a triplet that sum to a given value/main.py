# Find a triplet that sum to a given value
'''
input: array = {12, 3, 4, 1, 6, 9}, sum = 24; 
Output: 12, 3, 9 
Explanation: There is a triplet (12, 3 and 9) present 
in the array whose sum is 24. 
Input: array = {1, 2, 3, 4, 5}, sum = 9 
Output: 5, 3, 1 
'''

arr=list(map(int,input("enter the array:").split()))   # Enter space separated integers
sum_=int(input("Enter sum:"))

for num in range(len(arr)-2):
    for num1 in range(num+1,len(arr)-1):
        for num2 in range(num1+1,len(arr)):
            if arr[num]+arr[num1]+arr[num2]==sum_:
                 print("Triplet is", arr[num],", ", arr[num1], ", ", arr[num2])




