#Partition problem  DP-18

'''
Input: arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

Input: arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.

'''

from itertools import combinations




arr=list(map(int,input("Enter an array:").split()))  #Enter space separated numbers

sub_sum=[]
sub_sets=[]
length=len(arr)

arr.sort()
for num in range(1,len(arr)+1):
    com=combinations(arr,num)
    subsets=set(com)
    subsets=list(subsets)
    subsets.sort()
    for item in subsets:
        sub_sets.append(item)
        sub_sum.append(sum(item))

res=0
for number in sub_sum:
    if sub_sum.count(number)>1:
        res=number
        break 
if res==0:
    print(False)
else:
    print(True)