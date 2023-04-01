#find the least missing number

num_list=list(map(int,input("numbers: \n").split())) #enter space separated list of numbers

num_list.sort()
start=num_list[0]
end=num_list[-1]

missing_num=[]

for num in range(start,end):
    if num in num_list:
        continue
    else:
        missing_num.append(num)

if len(missing_num)<1:
    print(end+1)
else:
    print(missing_num[0])