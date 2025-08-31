# Write code below 💖

guess = 0
tries =0

while guess != 6 and tries <3:
  guess = int(input("Guess the number:  "))

  tries+=1 #Code wont stop giving tries if this is missing


if guess ==6:
  print("You got it!")

else:
  print ("Out of tries")

