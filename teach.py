n=int(input("Enter a number :"))

m=str(n)

a=m[:len(m)//2]
b=m[len(m)//2:]

c=int(a)+int(b)

tech=c**2

if(tech==n):
    print(f"{n} The given number is a tech number\n")
else:
    print(f"{n} The given number is not a tech number")
