#THIS IS THE SNAKE WATER GAME DEVELOPED BY SHUBHAJIT SARKAR DATE 25/07/2020
#FOR THE GAME INSTRUCTIONS PLEASE READ THE README FILE ATTACHED WITH THE GIT PROFILE
import random as ran
print(' Welcome to the GAME.!!\n\n','Please Enter Your Name')
print()
user=input('Your Name:- ')
bot= 'XARVICE'
print('Enter s for the SNAKE\n'
      'Enter w for the WATER\n'
      'Enter g for the GUN')
print('YOU HAVE TOTAL 5 CHANCES ')
user_score = 0
computer_score = 0
lst = ['snake', 'water', 'gun']
print()
for i in range (5):
      user_choose = input('Enter your choice:- ')
      if user_choose =='s'or'w'or'g':
            # for the SNAKE
            if user_choose == 's':  # WHEN THE USER CHOOSE THE SNAKE
                  comp_choice = ran.choice(lst)
                  print(f'Computer choose the :- {comp_choice}')
                  if comp_choice == 's':  # if the computer also choose the snake
                        print(f'{user} and {bot} socre is Tied')
                        print(f'{user} score is = 0,{bot} score is = 0')
                  elif comp_choice == 'g':  # if the computer choose the gun
                        print(f'{bot} wins')
                        computer_score += 1
                        print(f'{user} score is = 0,{bot} score is = 1')
                  else:  # if the computer choose  the water
                        print(f'{user} wins')
                        user_score += 1
                        print(f'{user} score is = 1,{bot} score is = 0')
            # For the WATER
            elif user_choose == 'w':  # WHEN THE USER CHOOSE THE WATER
                  comp_choice = ran.choice(lst)
                  print(f'computer choose the :-{comp_choice}')
                  if comp_choice == 'w':  # if the computer also choose the water
                        print(f'{user} and {bot} socre is tied')
                        print(f'{user} score is = 0,{bot} score is =0 ')
                  elif comp_choice == 'g':  # if the computer choose the gun
                        print(f'{user} wins')
                        user_score += 1
                        print(f'{user} score is = 1,{bot} score is = 0')
                  else:  # if the computer choose  the snake
                        print(f'{bot} wins')
                        computer_score += 1
                        print(f'{user} score is = 0,{bot} score is = 1')
            # For the gun
            elif user_choose == 'g':
                  comp_choice = ran.choice(lst)
                  print(f'computer choose the :-{comp_choice}')
                  if comp_choice == 'g':  # if the computer also choose the gun
                        print(f'{user} and {bot} socre is tied')
                        print(f'{user} score is = 0,{bot} score is =0 ')
                  elif comp_choice == 's':  # if the computer choose the gun
                        print(f'{user} wins')
                        user_score += 1
                        print(f'{user} score is = 1,{bot} score is = 0')
                  else:  # if the computer choose  the water
                        print(f'{bot} wins')
                        computer_score += 1
                        print(f'{user} score is = 0,{bot} score is = 1')


            else:
                  print(f'Invalid user input {user}, Please try Again..!')
            print(f'{user} your chances left {4 - i}')



print(f'Results of the Game is = \n {user} score is {user_score}\n {bot} score is {computer_score}')
print()
print(f'THANK YOU {user} for playing ,HOPE YOU LIKE IT ..!')

