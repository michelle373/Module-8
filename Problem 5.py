# Michelle Patlan
# 8/28/2022
# Write a function that checks whether your game character has picked up all the
# items needed to perform certain tasks and checks against any status debuffs. Confirm checks
# with print statements.

def character(mountain, meal, book):
    print("Checks function")
    task = input("What task the character are going to perform(Write,climb,cook)")

    # for climbing a mountain
    if task == "climb":
        if "slow" == mountain:
            print("The character can not climb the mountain")

        elif ('rope' in mountain) and ('coat' in mountain) and ('first aid kit' in mountain):
            print("The character can climb")

        else:
            print("The character will not climb a mountain")
    # For cooking
    elif task == 'cook':
        if meal == "small":
            print("The character can not cook")

        elif ('pan' in meal) and ('groceries' in meal):
            print("The character can cook")

        else:
            print("The character will not Cook")

    # For writing
    elif task == "write":
        if 'confusion' == book:
            print("The character can not write a book")

        elif ('pen' in book) and ('paper' in book) and ('idea' in book):
            print("The character can a write a book")

        else:
            print("The character will not write a book")


character(mountain=['rope', 'coat', 'first aid kit'], meal=['pan', 'groceries'], book=['pen', 'paper', 'idea'])
