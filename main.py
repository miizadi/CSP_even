numbers = []
def num_calc(times):
  for i in range(times):
    num = input("input an integer: ")
    if num == "stop":
      print("here are the evens: ", numbers)
    elif int(num) % 2 == 0:
      numbers.append(num)
amount = int(input("how many times do you want to play? (1-5 times): "))
num_calc(amount)
if amount > 0:
  print("here are the evens: ", numbers)
  amount2 = input("do you want to keep playing (yes/no)? ")
  num_calc((len(amount2)-2)*5)
  print("here are the evens: ", numbers)
elif amount <= 0:
  print("bruh, come on")