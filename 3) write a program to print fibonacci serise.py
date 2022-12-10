#Write a program to print fibonacci series 0,1,1,2,3,5,8 till user entered number
n=int(input("Enter number:"))
a=0
b=1
i=0
print("fibonacci series 0,1,1,2,3,5,8 till user entered number")
while (i<=n):
    c=a+b
    print(a,end=",")
    a=b
    b=c
    i+=1
input()
