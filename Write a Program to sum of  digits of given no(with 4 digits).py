#Write a Program to sum of  digits of given no(with 4 digits)
N=int(input("Enter Number:"))
X=str(N)
Y=len(X)
S=0
if Y<=4:
    if(Y==4):
        while N>0:
            A=N%10
            S=S+A
            N=N//10
        print("sum of  digits of given no(with 4 digits)=",S)
    else:
        print("Given number is less than 4 digit.")
else:
    print("Given number is greater than 4 digit.")
input()   
            
        
            
   

            
