import time, sys, os

time_lost = 0
my_money = 10
inventory = 0
message = (r"""
 _____  _                ___                               
(_   _)( )              (  _`\                    _        
  | |  | |__     __     | ( (_)   _     ___ ___  (_)   ___ 
  | |  |  _ `\ /'__`\   | |  _  /'_`\ /' _ ` _ `\| | /'___)
  | |  | | | |(  ___/   | (_( )( (_) )| ( ) ( ) || |( (___ 
  (_)  (_) (_)`\____)   (____/'`\___/'(_) (_) (_)(_)`\____)                                                      
 ___                  _     
(  _`\               ( )    
| (_) )   _      _   | |/') 
|  _ <' /'_`\  /'_`\ | , <  
| (_) )( (_) )( (_) )| |\`\ 
(____/'`\___/'`\___/'(_) (_)                             
 ___    _                      
(  _`\ ( )_                    
| (_(_)| ,_)   _    _ __   __  
`\__ \ | |   /'_`\ ( '__)/'__`\
( )_) || |_ ( (_) )| |  (  ___/
`\____)`\__)`\___/'(_)  `\____)
""")
def anything(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.1)
def start_game():
    global time_lost
    global my_money
    global inventory
    anything('Your name is Max, \nyou’re an 11 year-old comic book fan \nwho has to spend way too much of his time \ndoing things other than reading comics… \nThis is your journey to..')
    time.sleep(1)
    print(message)
    time.sleep(3)
    anything('You have to get to The Comic Book Store within 60 minutes \nYou might leave school early...')
    time.sleep(2)
    response = input('\nShould you sneak out of school? \nif you do front or back[F/B/D]?>')
    if response.lower() == 'f':
        time_lost += 30
        anything('You got caught! Detention after school! \nYou lost {} minutes due to detention.'.format(time_lost))
    elif response.lower() == 'b':
        anything('YES!!! You got away with it!')
    elif response.lower() == 'd':
        anything('You stayed at school until the bell.')
        time_lost += 15
        anything('You need to hurry if you want to make it in time!')
    else:
        anything('Invalid character') 
        start_game()
start_game()
def take_bus():
    global time_lost
    global my_money
    anything('\nYou could walk and save the money, or get the bus and save time...')
    time.sleep(2)
    response = input('\nWalk or bus [W/B]?>')
    if response.lower() == 'w':
        time_lost += 10
        anything('You walk, this makes you {} minutes behind schedule'.format(time_lost))
    elif response.lower() == 'b':
        my_money -= 5
        anything('You got the bus... for an extortionate 5 pounds! \nYou have {} pounds left '.format(my_money))
    else:
        anything('Invalid input')
        take_bus()
take_bus()
def home_():
    global time_lost
    global my_money
    time.sleep(2)
    anything('\nNow you are home, should you ask your Mum or \nDad for some money?')
    time.sleep(2)
    response = input('\nMum or Dad? [M/D]?>')
    if response.lower() == 'm':
        time.sleep(2)
        anything('\nYour Mum asks you to do housework for 10 pounds extra pocket money')
        response = input('\nAre you going to do housework [Y/N]?>')
        if response.lower() == 'y':
            my_money += 20 
            time_lost += 10
            time.sleep(2)
            anything('\nThis added 10 minutes to your journey... \nThis made you {} minutes behind schedule! \nYou now have {} pounds'.format(time_lost, my_money))
        elif response.lower() == 'n':
            time.sleep(2)
            my_money += 10
            anything('\nYou get 10 pounds pocket money')
        else:
            anything('\ninvalid input')
            home_()
    elif response.lower() == 'd':
        time.sleep(2)
        my_money += 10 
        anything('\nYou ask your dad and get your pocket money \nYou now have {} pounds'.format(my_money))
    else:
        anything('\nInvalid input')
home_()
def take_bike():
    global time_lost
    global my_money
    anything('\nWalking down the street, \nyou see a person, he has a bike you could borrow. \nTime is of the esscence! Will you walk into town or steal his bike?')
    response = input('\nWalk or steal [W/S]?>')
    if response.lower() == 'w':
        time_lost += 10
        anything('You walk \nYou are {} minutes behind schedule'.format(time_lost))
    elif response.lower() == 's':
        time_lost -= 10 
        anything('You stole the bike \nYou still have {} pounds left '.format(my_money))
    elif anything:
        print('You took too long. \n{} minutes \nGAME OVER'.format(time_lost))
        take_bike()
    else:
        anything('Invalid input')
take_bike()
def sweet_shop():
    global time_lost
    global my_money
    global inventory
    inventory = 0
    anything('\nYou are about to pass by the sweet shop... \nwill you stop to buy some sweets?')
    time.sleep(2)
    response = input('\nGo straight to The Comic Book Shop \nor buy sweets [G/B]?>')
    if response.lower() == 'g':
        time_lost -= 5
        anything('\nYou hurry you are {} minutes behind schedule'.format(time_lost))
    elif time_lost >= 60:
        print('You took too long. \n{} minutes \nGAME OVER'.format(time_lost))
        sweet_shop()
    elif response.lower() == 'b':
        anything('\nWhich sweets would you like?')
        time.sleep(2)
        time_lost += 10
        response = input('\nKitkat, Haribo, Skittles [K/H/S]?>')
        if  response.lower() == 'k':
            anything('\nYou bought a Kitkat for 5 pound')
            my_money -= 5 
            inventory += 1
            anything('\nYou have {} pounds left \nyou are {} beind schedule {} item in inventory'.format(my_money, time_lost, inventory))
        elif response.lower() == 'h':
            anything('\nYou bought a bag of Haribo for 5 pound')
            my_money -= 5
            inventory += 1
            anything('\nYou have {} pounds left \nYou have {} item in inventory'.format(my_money, inventory))
        elif response.lower() == 's':
            anything('\nYou bought a bag of Skittles for 5 pound')
            my_money -= 5
            inventory += 1
            anything('\nYou have {} pounds left \nYou have {} item in inventory'.format(my_money, inventory))
        else:
            anything('\nInvalid input')
            sweet_shop()
sweet_shop()
def encounter_bully():
    global my_money
    global time_lost
    global inventory
    anything("\nJust outside The Comic Book Store theres a bully \njumps out in front of you and waves his fist menacingly...")
    time.sleep(2)
    anything("\nIf you don't buy him off he might beat you up!")
    time.sleep(2)
    response = input('\nMoney, sweets or fight the bully  [M/S/F]?>')
    if response.lower() == "f":
        time.sleep(2)
        time_lost += 20
        anything('\nThe bully beats you up. It takes you 20 minutes to get the wedgie out \nYou have now lost {} minutes in total'.format(time_lost))
    elif inventory >= 0:
        anything('You didn\'t buy any sweets \nTry again!')
        encounter_bully()
    elif response.lower() == 's':
        time.sleep(2)
        inventory -= 1
        anything('\nHe takes your sweets and leaves you alone... \n Inventory has {} items in it'.format(inventory))
    elif response.lower() == 'm':
        time.sleep(2)
        my_money -= 30
        anything('\nHe takes 10 pounds from you \nYou {} pounds left')
    elif time_lost >= 60:
        print('You took too long. \n{} minutes \nGAME OVER'.format(time_lost))
        encounter_bully()
    else:
        anything('\nInvalid Input')
        encounter_bully()  
encounter_bully()
def arrive_store():
    anything("\nFinally! You have arrived at The Comic Book Store!")
    time.sleep(2)
    if time_lost >= 60:
        print('You took too long. \n{} minutes late \nThe Comic Book Store \nis closed \nGAME OVER'.format(time_lost))
        start_game()
    elif my_money >= 80:
        anything("\nYou bought the No.1 Comic Book of All Time!")
        time.sleep(2)
        anything('\nWell done! This is the best possible result. message, \n GAME OVER')
        start_game()
    elif my_money >= 50:
        anything('\nYou bought a Spiderman comic! \nWell done! But maybe you could have done better. {} \n GAME OVER'.format(message))
        start_game()
    elif my_money >= 25:
        anything("\nYou bought a Peppa Pig comic...")
        time.sleep(2)
        anything("\nMaybe you could give it to your little sister?")
        time.sleep(2)
        anything('\nSurely you could have done better. {} \n GAME OVER'.format(message))
        start_game()
    else:
        my_money >= 0
        anything("\nBut you don't have enough to buy anything.")
        time.sleep(2)
        anything('\nThat sucks, doesn\'t it? {} \n GAME OVER'.format(message))
        start_game()
        
arrive_store()
