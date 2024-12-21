a=int(input("Enter the value : "))
temp=0
rem=0
b=a
while(0<a):
    tem=a%10
    rem=(rem*10)+tem
    a=a//10
    print(a)
if(rem==b):
    print(f"{rem} is amstrong number....")
else:
    print(f"{rem} is not amstrong....")