#Write a program to print a table of given n using for loop.
n=int(input("Enter Number:"))
s=n
print("*** A table of given {} number ***".format(n))
for i in range(1,11): 
       x=s*i
       print(s,"*",i,"=",x)
input()
       
