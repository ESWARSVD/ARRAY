#Maximum sum of iarr[i] among all rotations of a given array
#Explanation: Lets look at all the rotations,
#{8, 3, 1, 2} = 8*0 + 3*1 + 1*2 + 2*3 = 11
#{3, 1, 2, 8} = 3*0 + 1*1 + 2*2 + 8*3 = 29
#{1, 2, 8, 3} = 1*0 + 2*1 + 8*2 + 3*3 = 27
#{2, 8, 3, 1} = 2*0 + 8*1 + 3*2 + 1*3 = 17
#output=29


arr=list(map(int,input("Enter array:").split()))   #enter space separeted integers


list_arr=[]
for number in range(len(arr)):
    num=len(arr)%number
    first=arr[num:]
    second=arr[:num]
    first.extend(second)
    list_arr.append(first)

maximum=[]
for rot_num in list_arr:
    max_=0
    for i in range(len(rot_num)):
        number=rot_num[i]
        count_=i*number
        max_=max_+count_
    maximum.append(max_)
print(max(maximum))