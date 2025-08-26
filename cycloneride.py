

height=float(input("Input height in cm: "))
credits=int(input("Input credits balance: "))

if height>=137 and credits>=10:
  print("Enjoy the ride")
elif height <137 and credits>=10:
  print("Not tall enough for the ride")
elif height>=137 and credits<10:
  print("Not enough credits")
else:
  print("No requirement  met")
