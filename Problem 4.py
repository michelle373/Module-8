# Michelle Patlan
# 8/28/2022
# Write a function that takes a year as a parameter and returns True if the year is a
# leap year, False if it is otherwise.

def leap_year(year):
  if (year % 4) == 0:
    if (year % 100) == 0:
      if (year % 400) == 0:
        print(f"{year} is a leap year")
      else:
        print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
  else:
    print(f"{year} is not a leap year")


leap_year(year=2020)