##1) Write a program to reverse user entered number  
##      n= 123 
##      rev=321
N=int(input("Enter number:"))
X=N
R=0
while(N>0):
    Y=N%10
    R=R*10+Y
    N=N//10
print("User enter number is:",X)
print("Reverse user entered number is:",R)
input()
    
