a=int(input("Enter the number : "))
c=0
if (a==1 or a==2):
    print("It is prime number.")
if (2<a):
  for i in range(2,a+1):
      if (a%i==0):
          c+=1
if (c==1):
    print("It isPrime number ")
else:
    print("It not isPrime number ")2