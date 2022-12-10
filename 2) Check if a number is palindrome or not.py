##2) Check if a number is palindrome or not
##n = 121
##rev = 121
##n = rev
N=int(input("Enter number:"))
X=N
R=0
while(N>0):
    Y=N%10
    R=R*10+Y
    N=N//10
print("User enter number is:",X)
print("Reverse user entered number is:",R)
if(X==R):
    print("Enter number is palindrome.")
else:
    print("Enter number is not palindrome.")
input()
    
