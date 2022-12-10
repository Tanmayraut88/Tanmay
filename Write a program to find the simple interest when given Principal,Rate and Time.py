#Write a program to find the simple interest when given Principal,Rate and Time.
Pr=float(input("Enter the principal amount(Rs.):"))
Ra=float(input("Enter the rate of interest(%):"))
Ti=float(input("Enter number of years (No.):"))
Si=(Pr*Ra*Ti)/100
print("Principal amount (Rs.):",Pr)
print("Rate of interest (%): ",Ra)
print("Number of years (No.): ",Ti)
print("Simple interest(Rs.): ({}*{}*{})/100 = {}".format(Pr,Ra,Ti,Si))
#Enter any key to exit
Exit=input("Enter any key to exit:")
