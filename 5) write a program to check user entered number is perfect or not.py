##5) write a program to check user entered number is perfect or not 
##n=6 
####1+2+3 all diviser sum is also 6 so 6 is perfect number 
N=int(input("Enter number:"))
R=0
while(N>0):
    A=N%10
    R=R+A
    print(A,"+",end="")
    N=N//10
print("all diviser sum:",R)
X=R%6
if(R==6 and X==0):
    print("User entered number is perfect")
else:
    print("User entered number is not perfect")
    
input()    
    
