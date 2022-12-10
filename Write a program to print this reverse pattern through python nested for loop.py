#Write a program to print this pattern through python nested for loop.
i=6
print("To print this pattern through python nested for loop.")
while (i>1):
    j=1
    while(j<i):
        print("*",end="")
        j+=1
    print()
    i-=1
input()
