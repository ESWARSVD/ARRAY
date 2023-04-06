#Rearrange array in alternating positive & negative items with O(1) extra space

arr=input("Enter array:").split() #enter space separated negitive and positive

positive=[]
negitive=[]

for num in arr:
    if (int(num))<0:
        negitive.append(num)
    else:
        positive.append(num)

result=[]

for number in range(len(negitive)):
    result.append(negitive[number])
    result.append(positive[number])

result.extend(positive[len(negitive):])

print(*result)
