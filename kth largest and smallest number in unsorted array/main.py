# k'th largest and smallest number in unordered list

k=int(input("Enter number:"))

un_list=list(map(int,input("Enter unorderd list of numbers:\n").split())) #enter space seperated numbers
unique_set=set(un_list)
unique_list=list(unique_set)
unique_list.sort()
#kth largest
print("kth largest number: %s"% unique_list[-k])

#kth smallest

print("kth smallest number: %s"% unique_list[k-1])