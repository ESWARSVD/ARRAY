#Find duplicates in array

arr=input("Enter array:").split()    #enter space separated numbers

duplicate_num=[]

for num in arr:
    if arr.count(num)>1:
        if num in duplicate_num:
            continue
        else:
            duplicate_num.append(num)
    else:
        continue

#print duplicate numbers
print("Duplicate numbers:")
print(*duplicate_num)