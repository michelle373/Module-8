# Michelle Patlan
# 8/28/2022
# Write a function that takes two inputs from a user and prints whether the sum is
# greater than 10, less than 10, or equal to 10.

def sunOfNum():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a + b
    x = 10
    if c == x:
        print("Number is equal to 10")
    elif c < x:
        print("Number is less than 10")
    elif c > x:
        print("Number is greater than 10")

sunOfNum()