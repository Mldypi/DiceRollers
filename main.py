from random import randint

#x is number of sides, y is number of dice. Adder is a list that the die rolls get written to, and printed by the last line of the Roller.
def Roller(x,y):
  Adder = []
  for x in range(1,x+1):
    z = randint(1,y)
    Adder.append(z)
  print(Adder)

Do_roll = input('Do you want to roll? y/n\n')
while Do_roll == "y":
  #attempting to write an exception handler
  try:
    Size_Dice = int(input('How many sides do the dice have?\n'))
  except ValueError:
    print("Sorry, I didn't understand that. Please enter a whole number.")
    continue
  if Size_Dice < 1:
    print("Sorry, number of sides must not be negative")
    continue    
  
  try:
    Num_Dice = int(input('How many dice would you like to roll?\n'))
  except ValueError:
    print("Sorry, I didn't understand that. Please enter a whole number.")
    continue
  if Num_Dice < 1:
    print ("Sorry, number of dice must not be negative")
    continue

  Roller(Num_Dice, Size_Dice)

  Roll_again = input('Roll again? y/n\n')
  if Roll_again == "y":
    #don't remove 36, it must be Roller, the code breaks without it. No idea why.
    Roller
  else:
    print('Okay, bye!')
    break
else:
  print('Okay, bye!')