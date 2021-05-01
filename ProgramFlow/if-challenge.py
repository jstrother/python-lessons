name = input("What is your name? ")
age = int(input("How old are you? "))

if 18 <= age <= 30:
  print("Welcome on the trip, {}!".format(name))
else:
  print("Sorry, {}, this trip is only for those between 18 and 30".format(name))