#Write a program to print this pattern through python nested for loop.
i=0
print("To print this pattern through python nested for loop.")
while (i<7):
    j=1
    while(j<i):
        print(j,end="")
        j+=1
    print()
    i+=1
input()
