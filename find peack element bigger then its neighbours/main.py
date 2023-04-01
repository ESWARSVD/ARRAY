# find a peack element which is not smaller then its neighbours

#taking space separated numbers as input from user

input=list(map(int,input("Enter list of numbers : ").split()))

num_list=[]

#itarate the input and check the peak element

for num in range(1,(len(input)-1)):
    if input[num-1]<input[num] and input[num+1]<input[num]:
        num_list.append(input[num])

#print the output
print("output:")
print(*num_list)