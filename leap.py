# Which year do you want to check?
year = int(input())
#Logic
if year % 4 == 0:
  if year % 100 != 0:
    print("Leap year")
  elif year % 100 ==0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Not leap Year")
else:
  print("Not leap year")
