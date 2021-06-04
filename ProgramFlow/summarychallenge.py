choice = "-"
while choice != "0":
  if choice in "12345":
    print("You choose {}".format(choice))
  else:
    print("Please choose your option form the list below:")
    print("1:\tLearn Python")
    print("2:\tLearn Java")
    print("3:\tLearn JavaScript")
    print("4:\tRead a book")
    print("5:\tGet a Job")
    print("0:\tExit")
  choice = input()
