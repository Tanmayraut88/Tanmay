#Write a program to print nth fibonacci series.
n=int(input("Enter number:"))
a=0
b=1
i=1
print(n,"Fibonacci series")
while (i<n):
    c=a+b
    print(a,"+",b,"=",c)
    a=b
    b=c
    i+=1
input()
