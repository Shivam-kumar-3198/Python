# Write a program using function to print the greatest of three number

a = int(input("Enter the number a : "))
b = int(input("Enter the number b : "))
c = int(input("Enter the number c : "))

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c

print("Greatest of three number")