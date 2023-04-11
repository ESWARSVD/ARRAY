#Find the smallest positive integer value that cannot be represented as sum of any subset of a given array


#Input:  arr[] = {1, 10, 3, 11, 6, 15};
#Output: 2

#Input:  arr[] = {1, 1, 1, 1};
#Output: 5

arr=list(map(int,input("Enter array:").split()))  #Enter space separated integers

sum_array=1

for num in range(len(arr)):
    if arr[num]<=sum_array:
        sum_array=sum_array+arr[num]
    else:
        break 

print(sum_array)