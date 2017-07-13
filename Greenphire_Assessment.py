#Powerball story;
#   As a Greenphire employee I would like to add my favorite 6 numbers to consider for a Powerball entry ticket so that I can win 1 billion dollars.
#    -Capture the name of the employees entering the number.
#    -The first 5 favorite numbers will need to be in the range of 1 to 69 and unique (remember that this is a drawing so there cannot be duplicates in this range of 5 numbers)
#    -6th favorite number will need to be in the range of 1 to 26 and flagged as the 6th Powerball number
#    -Keep count of each individual favorite number provided to determine which numbers to use in our final winning number. (i.e. count the duplicates)
#    -Retrieve the max count of each unique duplicate number and use them as the Powerball numbers
#    -If there is a tie based on the max counts randomly select the tied number
#    -Display all employees with their corresponding number entries
#    -Display the final Powerball number based on the requirements above

import random

print('\nWelcome to the Greenphire Powerball!!')
print('\nPlease follow the instructions to play:\nChoose 5 unique numbers between 1 and 69 (inclusive) followed by a sixth number between 1 and 26 (inclusive).\nGood luck!')
#include a print output with an explanation of how the Powerball works

pball = []
player_count = raw_input('How many players are there today? ')

#Cyclce through user inputs
for player in range(int(player_count)):
  first_name = raw_input('Enter your first name: ')
  last_name = raw_input('Enter your last name: ')
  name = first_name+' '+last_name
  print('\n'+name+', thanks for playing!')
  
  pball.append(name)
  
  a = False
  while a is False:
    num1 = int(raw_input('Please select your first number: '))
    if (num1 > 0 and num1 < 70):
      if num1 in pball[7*player:7*(player+1)]:
        print('Try again (1).')
      else:
        pball.append(num1)
        a = True
    else:
      print('Try again (2).')
 
  b = False
  while b is False:
    num2 = int(raw_input('Please select your second number: '))
    if (num2 > 0 and num2 < 70):
      if num2 in pball[7*player:7*(player+1)]:
        print('Try again (1).')
      else:
        pball.append(num2)
        b = True
    else:
      print('Try again (2).')

  c = False
  while c is False:
    num3 = int(raw_input('Please select your third number: '))
    if (num3 > 0 and num3 < 70):
      if num3 in pball[7*player:7*(player+1)]:
        print('Try again(1).')
      else:
        pball.append(num3)
        c = True
    else:
      print('Try again.')

  d = False
  while d is False:
    num4 = int(raw_input('Please select your fourth number: '))
    if (num4 > 0 and num4 < 70):
      if num4 in pball[7*player:7*(player+1)]:
        print('Try again.')
      else:
        pball.append(num4)
        d = True
    else:
      print('Try again.')

  e = False
  while e is False:
    num5 = int(raw_input('Please select your fifth number: '))
    if (num5 > 0 and num5 < 70):
      if num5 in pball[7*player:7*(player+1)]:
        print('Try again.')
      else:
        pball.append(num5)
        e = True
    else:
      print('Try again.')

  f = False
  while f is False:
    num6 = int(raw_input('Please select your Powerball: '))
    if (num6 > 0 and num6 < 27):
      pball.append(num6)
      f = True
    else:
      print('Try again.')

  if player in range(int(player_count)):
    print('\nNext player, you\'re up!\n')


#Prints player names and corresponding numbers (in order of selection)
for player in range(int(player_count)):
  print(pball[7*player]+': '+' '.join(str(x) for x in pball[(7*player)+1:7*(player+1)-1]) + ' Powerball: '+str(pball[7*(player)+6]))



#Randomly generates powerball numbers
def show_powerball():
  first_five = range(69)
  random.shuffle(first_five)
  final_ball = range(26)
  random.shuffle(final_ball)
  powerball_nums = first_five[0:5]
  powerball_nums.extend(final_ball[0:1])
  #print (powerball_nums)
  return powerball_nums

#Prints randomly generated Powerball
powerball = show_powerball()
print('Powerball Winning Numbers: ')
print(' '.join(str(x) for x in powerball[0:5])+' Powerball: '+str(powerball[5]))





