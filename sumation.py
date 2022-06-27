#2.Write a Python program to sum  two given integers. However, if the sum is between 15 to 20 it will return 20 else it returns the actual sum
number = float (input("Enter a number : "))
numba = float (input("Enter a number : "))


def sum(number,numba):
    add = number + numba
    if add > 15 and add < 21:
        print (20)
    else:
        print ("The sum is: ",add)

sum(number,numba) 