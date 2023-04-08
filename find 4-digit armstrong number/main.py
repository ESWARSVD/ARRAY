#find 4-digit armstrong number


num=input("Enter a 4-digit number:")
a1=(int(num[0]))**4
a2=(int(num[1]))**4
a3=(int(num[2]))**4
a4=(int(num[3]))**4
if (a1+a2+a3+a4)==int(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")