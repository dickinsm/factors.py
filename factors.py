#Author: Makaliah Dickinson
#Date: 7/5/2020
#Description: Write a program that asks the user to enter a positive integer, then prints a list of all positive integers
#            that divide that number evenly, including itself and 1, in ascending order.
n=int(input("Please enter a positive integer: "))
print("The factors of",n,"are:")
for i in range (2,n):
    if(n % i==0):
        print(i)
