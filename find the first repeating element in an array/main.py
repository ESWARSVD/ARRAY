#find the first repeating element in an array

arr=list(map(int,input("Enter array:").split()))  #enter space separated integers

dict_=dict()

for num in arr:
    if num in dict_:
        dict_[num]=dict_[num]+1
        if dict_[num]==2:
            print(num)
            break 
        else:
            continue 
    else:
        dict_[num]=1

