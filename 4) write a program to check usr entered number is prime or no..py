##4) write a program to check usr entered number is prime or no.
N=int(input("Enter Number:"))
X=N%2
if(N>=2):
    if(X>0):
        print("Enter number {} is prime.".format(N))
    else:
        print("Enter number {} is not prime.".format(N))
else:
    print("Enter number {} is not prime.".format(N))
input()        
