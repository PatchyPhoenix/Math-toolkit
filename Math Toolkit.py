import math
import time

q = input("Math Toolkit\nWhat do you want to do?\n1 - Check if a word or number is a palindrome\n2 - Check if a number is a prime number\n3 - Find the square root of a number\n4 - Find the cube root of a number\n5 - Find the square of a number\n6 - Find the cube of a number\n")

if q == "1":
    
    n1 = input("Enter a word or a number : ")
    n = n1.lower()
    if n == n[::-1]:
        print(n1, " is palindrome")
        time.sleep(1)
        print("\nRestart program to use it again")
    else:
        print(n1, " is not palindrome")
        time.sleep(1)
        print("\nRestart program to use it again")

elif q == "2":
    
    num = int(input("Enter a number : "))
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                 flag = True
                 break
    if flag:
        print(num, "is not a prime number")
        time.sleep(1)
        print("\nRestart program to use it again")
    else:
        print(num, "is a prime number")
        time.sleep(1)
        print("\nRestart program to use it again")

elif q == "3":

    n = float(input("Enter a Number : "))
    root = float(math.sqrt(n))
    print("The square root is ",root)
    time.sleep(1)
    print("\nRestart program to use it again")

elif q == "4":

    n = float(input("Enter a number : "))
    def is_cube(n):
        guess = n**(1.0/3.0)
        print("The cube root is ", guess)
    is_cube(n)
    time.sleep(1)
    print("\nRestart program to use it again")

elif q == "5":
    n = float(input("Enter a number : "))
    square = n*n
    print(square," is the square of ",n)
    time.sleep(1)
    print("\nRestart program to use it again")
        
elif q == "6":
    n = float(input("Enter a number : "))
    cube = n*n*n
    print(cube," is the cube of ",n)
    time.sleep(1)
    print("\nRestart program to use it again")

else:
    print("Choose a valid option!")
    time.sleep(1)
    print("\nRestart program to use it again")
