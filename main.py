from random import randint
n=randint(1,100)
a=0
while(a != n):
    a=int(input("enter number: "))
    if(a>n):
        print("Enter lower number")
    else:
        print("Enter higher number")    

print("Yor number right match with random number:")        