#find maximum product Contiguous Subarray

arr=list(map(int,input("Enter array:").split()))  #Enter space separated integers

length=len(arr)

subarry=[]
product=[]

for num in range(length):
    for num1 in range(num+1,length):
        sub=arr[num:num1]
        total=1
        subarry.append(sub)
        for num2 in sub:
            total=total*num2
        product.append(total)


maximum=max(product)
index=product.index(maximum)

print("subarray: %s"%subarry[index])
print("maximum:%s"%maximum)


