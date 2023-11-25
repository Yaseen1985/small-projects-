import random

print("welcome to age gusseing game")
print("please enter your name")
name = input()

lower_limit = 9
upper_limit = 60
random_no = random.randint(lower_limit, upper_limit)

print("I think your age is", random_no)
print("1: I am older than", random_no)
print("2: I am younger than", random_no)
print("3: This is my age")
print(name, "Please select one option from these options")
first_select = input()

while first_select != "3":
  if first_select == "1":
    lower_limit = random_no
    random_no = random.randint(lower_limit, upper_limit)
    print("I think your age is", random_no)
    print("1: I am older than", random_no)
    print("2: I am younger than", random_no)
    print("3: This is my age")
  elif first_select == "2":
    upper_limit = random_no
    random_no = random.randint(lower_limit, upper_limit)
    print("I think your age is", random_no)
    print("1: I am older than", random_no)
    print("2: I am younger than", random_no)
    print("3: This is my age")
  elif first_select == "3":
    print("Thanks for playing with us!")
  else:
    print("You entered a wrong number. Please try again.")
  first_select = input()