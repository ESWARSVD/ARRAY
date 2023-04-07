#find Largest Sum Contiguous Subarray

arr=list(map(int,input("Enter array:").split()))  #Enter space separated integers

length=len(arr)

subarry=[]
largest=[]

for num in range(length):
    for num2 in range(num+1,length):
        sub=arr[num:num2]
        total=sum(sub)
        subarry.append(sub)
        largest.append(total)

maximum=max(largest)
index=largest.index(maximum)

print("subarray: %s"%subarry[index])
print("maximum:%s"%maximum)


