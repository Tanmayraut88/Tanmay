#Write a Program to find sum of 1st and last digit of 4 digit number.
while True:
    n=int(input("Enter 4 digit number:"))
    x=str(n)
    y=len(x)
    if(y<=4):
        if (y==4):
            sum=int(x[0])+int(x[-1])
            print("Sum of 1st and last digit of 4 digit number: {} + {} = {}".format(int(x[0]),int(x[-1]),sum))
            break    
        else:
            print("Enter number is invalid")
        
    else:
        print("Please enter 4 digit number.")
       
input()
