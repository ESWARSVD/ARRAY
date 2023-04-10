#The Stock Span Problem

#example: Input: N = 7, price[] = [100 80 60 70 60 75 85]
#Output: 1 1 1 2 1 4 6
#Explanation: Traversing the given input span for 100 will be 1, 80 is smaller than 100 so the span is 1, 60 is smaller than 80 so the span is 1, 70 is greater than 60 so the span is 2 and so on. Hence the output will be 1 1 1 2 1 4 6.
#Input: N = 6, price[] = [10 4 5 90 120 80]
#Output:1 1 2 4 5 1


arr=list(map(int,input("Enter an array:").split()))   #enter space separated numbers

lenght=len(arr)
span_list=[]
span_list.append(1)
for i in range(1,lenght):
    span=1

    j=i-1
    while (j>=0) and (arr[i]>=arr[j]):
        span+=1
        j-=1
    span_list.append(span)


print(*span_list)