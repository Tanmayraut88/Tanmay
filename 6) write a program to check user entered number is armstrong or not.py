##6) write a program to check user entered number is armstrong or not
N=int(input("Enter Number:"))
X=str(N)
Y=len(X)
M=N
S=0
print("User enter number is:",N)
while(N>0):
    A=N%10
    S=S+(A**Y)
    N=N//10
print("Sum of indiviual digit:",S)
if(M==S):
    print("Number is armstrong")
else:
    print("Number is not armstrong")
input()
