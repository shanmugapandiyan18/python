num=int(input("Enter the number :"))
Sum=0
rem=1
temp=num
if(num>1):
    for i in range (1,num):
        
      rem=num%10
      Sum+=rem*rem*rem
      num=num//10
      
    print("Revers of a number :",Sum)


