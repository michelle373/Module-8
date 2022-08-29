# Michelle Patlan
# 8/28/2022
# Write a function that takes a list and prints if the value 5 is in that list

def check_five(lst):  # Define function
    if 5 in lst:  # Iterate through list
        print('Number 5 is present in the list')  # print to console
        print(lst)
    else:
        print('Number 5 is not present on list')


check_five(lst=[4, 5, 10])
