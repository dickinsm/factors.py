#Author: Makaliah Dickinson
#Date: 7/5/2020
#Description: Write a program that asks the user to enter a positive integer, then prints a list of all positive integers
#            that divide that number evenly, including itself and 1, in ascending order.
num=int(input("Please enter a positive integer:"))
print("The factors of",num,"are:")
for k in range (1,num):
    if(num % k==0):
        print(k)
