# game.py

import random
import getpass
import time
print('hey there Welcome to our project i.e. Rock-Paper-Scissors made by Archi, Khushi, Vaishnav, Vishu, Arjun, Maaran')
time.sleep(3)
print('do you want to read winning rules and instructions')
print('press 1 to read\npress 2 to skip')
insc = int(input('enter your choice between 1 or 2 : '))
if insc == 1:
    print("************************")
    print("Winning Rules for Rock-Paper-Scissors : ")
    time.sleep(3)
    print("************************")
    print("Rock crushes Scissors")
    time.sleep(3)
    print("Scissors cuts Paper")
    time.sleep(3)
    print("Paper covers Rock")
    time.sleep(3)
    print("************************")
    print("Instructions for Rock-Paper-Scissors : ")
    time.sleep(3)
    print("************************")
    print('enter R for Rock')
    time.sleep(3)
    print('enter S for Scissors')
    time.sleep(3)
    print('enter P for Paper')
    print("************************")
elif insc == 2:
    print("************************")
    print("Winning Rules for Rock-Paper-Scissors : ")
    print("************************")
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print("************************")
    print("Instructions for Rock-Paper-Scissors : ")
    print("************************")
    print('enter R for Rock')
    print('enter S for Scissors')
    print('enter P for Paper')
    print("************************")
else:
    print('wrong choice')
print('enter 1 to play with computer')
time.sleep(3)
print('enter 2 to pass n play')
time.sleep(3)
print("************************")
gamec = int(input('enter how you want to play : '))
act = ['R','P','S']
n1 = 0
ypts = 0
p1_pts = 0
try:
    n0 = int(input('enter number of times you want to play Rock-Paper-Scissors : '))
    if gamec == 1:
        print('you chose to play with computer')
        a = input('enter your first name : ')
        ac = a.capitalize()
        while(True):
            choic = random.choice (act)
            choice = choic.upper()
            n1 = n1 + 1
            if n0 >= n1:
                playe = input('enter your choice between RPS: ')
                player = playe.upper()
                if player == 'R':
                    if choice == 'R':
                        print('you both did rock, so you got 1 point')
                        ypts = ypts + 1
                    elif choice == 'P':
                        print('paper covers the rock, so you got 0 points')
                        ypts = ypts + 0
                    elif choice == 'S':
                        print('rock breaks the scissors, so you got 2 points')
                        ypts = ypts + 2
                    else:
                        print('enter the correct value you entered', player)
                elif player == 'S':
                    if choice == 'S':
                        print('you both did scissors, so you got 1 point')
                        ypts = ypts + 1
                    elif choice == 'R':
                        print('Rock breaks the scissors, so you got 0 points')
                        ypts = ypts + 0
                    elif choice == 'P':
                        print('scissors cuts paper, so you got 2 points')
                        ypts = ypts + 2
                    else:
                        print('enter the correct value you entered', player)
                elif player == 'P':
                    if choice == 'P':
                        print('you both did paper, so you got 1 point')
                        ypts = ypts + 1
                    elif choice == 'S':
                        print('scissors cuts the paper, so you got 0 points')
                        ypts = ypts + 0
                    elif choice == 'R':
                        print('paper covers rock, so you got 2 points')
                        ypts = ypts + 2
                    else:
                        print('enter the correct value you entered', player)
                else:
                    print('you didn\'t entered the correct value you entered', player)
                    n1 = n1 - 1
            else:
                print('you ran out of moves')
                tpts = n0*2
                cpts = tpts - ypts
                cwpts = cpts - ypts
                ywpts = ypts - cpts
                ywper = ypts*100/tpts
                print("\n\t******ScoreBoard******")
                print(f"\tYou: {ypts} | Computer: {cpts}")
                print("your winning percentage was", str(ywper) +'%')
                if ypts < cpts:
                    print("Sorry You lost the game\n computer won the game by", cwpts, 'points')
                elif ypts == cpts:
                    print("Game is Tie Play Again")
                else:
                    print("You Won the Game by", ywpts,'points')
                print('\npress 1 to check your rank in game')
                print('press 2 to skip checking the rank')
                ra = int(input('enter your choice : '))
                if ra == 1:
                    if ypts == tpts:
                        print('you are a legend')
                    elif ypts == tpts/2:
                        print('that\'s a good score')
                    elif ypts >= tpts*3/4:
                        print('you are master of the game')
                    elif ypts >= tpts/2:
                        print('that\'s a good score')
                    else:
                        print('you need to practice some more')
                elif ra == 2:
                    print('you skipped checking the rank')
                else:
                    print('enter choice only between 1 and 2 but you gave', ra)
                cr = input('please rate our game out of 10 : ')
                time.sleep(3)
                with open("result.txt",mode='a') as my_file:
                    my_file.write("Name : ")
                    my_file.write(ac)
                    my_file.write("\nScore : ")
                    my_file.write(str(ypts))
                    my_file.write(" out of ")
                    my_file.write(str(tpts))
                    my_file.write("\nPoints given : ")
                    my_file.write(str(cr))
                    my_file.write("\n--------------------------------------------------------------------\n")
                    print('response submitted successfully')
                time.sleep(3)
                print('thanks for playing our game',ac)
                time.sleep(3)
                print('\nHeartiest congratulations to team, your project has been rated',cr,'out of 10 by',ac)
                time.sleep(3)
                break
    if gamec == 2:
        print('you chose to play pass n play')
        p1_nam = input('enter player 1 name')
        p1_name = p1_nam.capitalize()
        p2_nam = input('enter player 2 name')
        p2_name = p2_nam.capitalize()
        print(p1_name,'is assigned as player 1 and',p2_name,'is assigned as player 2')
        while(True):
            player1 = getpass.getpass('enter your choice between RPS: ')
            player_1 = player1.upper()
            b_1 = len(player_1)* '*'
            print(b_1)
            player2 = getpass.getpass('enter your choice between RPS: ')
            player_2 = player2.upper()
            b_2 = len(player_2)* '*'
            print(b_2)
            print('player 1 chose',player_1,'and player_2',player_2)
            n1 = n1 + 1
            if n0 >= n1:
                if player_1 == 'R':
                    if player_2 == 'R':
                        print('you both did rock, so player 1 and player 2 both got 1 point')
                        p1_pts = p1_pts + 1
                    elif player_2 == 'P':
                        print('paper covers the rock, so player 1 got 0 points player 2 got 2 points')
                        p1_pts = p1_pts + 0
                    elif player_2 == 'S':
                        print('rock breaks the scissors, so player 1 got 2 points player 2 got 0 points')
                        p1_pts = p1_pts + 2
                    else:
                        print('value you entered is incorrect')
                elif player_1 == 'S':
                    if player_2 == 'S':
                        print('you both did scissors, so player 1 and player 2 both got 1 point')
                        p1_pts = p1_pts + 1
                    elif player_2 == 'R':
                        print('Rock breaks the scissors player 1 got 0 points player 2 got 2 points')
                        p1_pts = p1_pts + 0
                    elif player_2 == 'P':
                        print('scissors cuts paper player 1 got 2 points player 2 got 0 points')
                        p1_pts = p1_pts + 2
                    else:
                        print('value you entered is incorrect')
                elif player_1 == 'P':
                    if player_2 == 'P':
                        print('you both did paper, so player 1 and player 2 both got 1 point')
                        p1_pts = p1_pts + 1
                    elif player_2 == 'S':
                        print('scissors cuts the paper player 1 got 2 points player 2 got 0 points')
                        p1_pts = p1_pts + 0
                    elif player_2 == 'R':
                        print('paper covers rock player 1 got 0 points player 2 got 2 points')
                        p1_pts = p1_pts + 2
                    else:
                        print('value you entered is incorrect')
                else:
                    print('you didn\'t entered the correct value you entered')
                    n1 = n1 - 1
            else:
                print('you ran out of moves')
                to_pts = n0*2
                p2_pts = to_pts - p1_pts
                p2_wpts = p2_pts - p1_pts
                p1_wpts = p1_pts - p2_pts
                p1_wper = p1_pts*100/to_pts
                p2_wper = 100 - p1_wper
                print("\n\t******ScoreBoard******")
                print(f"\t {p1_name} : {p1_pts} | {p2_name} : {p2_pts}")
                print(p1_name,"your winning percentage is", str(p1_wper) +'%')
                print(p2_name,'your winning percentage is', str(p2_wper) +'%')
                if p1_pts < p2_pts:
                    print("congratulations",p2_name,'won the game by',p2_wpts, 'points')
                elif p1_pts == p2_pts:
                    print("Game is Tie Play Again")
                else:
                    print("congratulations",p1_name,'won the game by',p1_wpts, 'points')
                time.sleep(3)
                cr_1 = input('player 1 please rate our game out of 10 : ')
                with open("result.txt   ",mode='a') as my_files1:
                    my_files1.write("Name : ")
                    my_files1.write(p1_name)
                    my_files1.write("\nScore : ")
                    my_files1.write(str(p1_pts))
                    my_files1.write(' out of ')
                    my_files1.write(str(to_pts))
                    my_files1.write("\nPoints given : ")
                    my_files1.write(str(cr_1))
                    my_files1.write("\n--------------------------------------------------------------------\n")
                    print('response submitted successfully')
                time.sleep(3)
                print('thanks for playing our game',p1_name)
                time.sleep(3)
                print('\nHeartiest congratulations to team, your project has been rated',cr_1,'out of 10 by',p1_name,)
                time.sleep(3)
                cr_2 = input('player 2 please rate our game out of 10 : ')
                with open("result.txt",mode='a') as my_files2:
                    my_files2.write("Name : ")
                    my_files2.write(p2_name)
                    my_files2.write("\nScore : ")
                    my_files2.write(str(p2_pts))
                    my_files2.write(' out of ')
                    my_files2.write(str(to_pts))
                    my_files2.write("\nPoints given : ")
                    my_files2.write(str(cr_2))
                    my_files2.write("\n--------------------------------------------------------------------\n")
                    print('response submitted successfully')
                time.sleep(3)
                print('thanks for playing our game',p2_name)
                time.sleep(3)
                print('\nHeartiest congratulations to team, your project has been rated',cr_2,'out of 10 by',p2_name)
                break
    else:
        print('no operation as ',gamec)
except ValueError:
    print('value error, please check the entered value once again')
