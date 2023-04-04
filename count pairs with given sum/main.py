# count pairs with given sum


arr=list(map(int,input("Enter number list:").split())) #Enter numbers with space separated

sum_num=int(input("Enter sum number:")) #Enter single integer

pair_count=0

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[i]+arr[j])==sum_num:
            pair_count+=1

#print pair count

print(pair_count)