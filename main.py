#formating
# chai="Leman chai "
# quantity=2
# order="i order {} cups of {}"
# print(order.format(quantity,chai))
from calendar import day_abbr

#convert list into string
# city=["islamabad","lahor","karachi","peshawar"]
# print(" ".join(city))


#convert string into list
# city="islamabad,lahor,karachi,peshawar"
# print(city.split())
# city="islamabad,lahor,karachi,peshawar"
# print(len(city))
# print()


#list
# city=["islamabad","lahor","karachi","peshawar","Quetta","Rawalpindi","multan"]
# print(city[0:6:2])
# city[3]="Sialkot"
# print(city)
# city.append("Kohat")
# print(city)


#conditional satement
# age=int(input("enter your age"))
# if age < 13:
#  print("child")
# elif age < 18:
#  print("teenager")
# elif age < 30:
#  print("adult")
# elif age > 55:
#  print("senior citizen")
#
# ages = [10, 15, 25, 60, 35, 12, 16, 58]
#

# age_categories = [
#     "child" if age < 13 else
#     "teenager" if age < 18 else
#     "adult" if age < 30 else
#     "senior citizen" if age > 55 else
#     "middle-aged"  
#     for age in ages
# ]
#
# print(age_categories)

age = int(input("Enter your age: "))
day = input("Enter day: ")
price_for_child = 12
price_for_adult = 15
if age < 18:
    print("The ticket price for a child is", price_for_child)
else:
    print("The ticket price for an adult is", price_for_adult)
if day == "wednesday":
    if age < 18:
        discount_price_for_child = price_for_child - 2
        print("But today is Wednesday, so the special discount price for a child is", discount_price_for_child)
    else:
        discount_price_for_adult = price_for_adult - 2
        print("But today is Wednesday, so the special discount price for an adult is", discount_price_for_adult)
else:
    print("The discount price is only available on Wednesday. You will be charged the regular price.")
