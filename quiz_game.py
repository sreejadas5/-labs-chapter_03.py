question1 = ("How many NBA championships did Kobe Bryant win? ")
question2 = ("Which boxer was known as “The Greatest” and “The People’s Champion? ")
question3 = ("Which Jamaican runner is an 11-time world champion and holds the record in the 100 and 200-meter race? ")
question4 = (" Which hockey team did Wayne Gretzky play for in the ‘80s?")
question5 = ("Which Williams sister has won more Grand Slam titles? ")
question6 = ("How many soccer players should each team have on the field at the start of each match? ")
question7 = ("Who is the captain of the Toronto Raptors?")
question8 = ("What was the first sport created? ")
questions = [question1, question2, question3, question4, question5, question6, question7, question8]

answer1 = ("5")
answer2 = ("Muhammad Ali")
answer3 = ("Usain Bolt")
answer4 = ("Edmonton Oilers")
answer5 = ("Serena")
answer6 = ("11")
answer7 = ("Kyle Lowry")
answer8 = ("Wrestling")

answers = [answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8]

points = 0
name = None
yes = ['Yes', 'yes', 'YES']
no = ['No', 'no', 'NO']

def game_reset():
    '''
    Reset all variables of the whole game for a new play
    '''

    global points
    global name

    points = 0
    name = None

def game_intro():
    '''
    Welcome the player and ask him for his name as long as he thinks is correct.
    '''
    print("\n       ------ !! Welcome to the QuizGame !! ------\n")
    
    global name
    while name == None:
        name = input("What's your name? ")
        print("Your name is", name)
        correct = input("Is that correct? ")
        if yes.count(correct) == True: 
            print("Good, let's go on!\n")
        else:
            print("Try again and confirm with Yes!")
            name = None

def print_play_status(x):
    '''
    just print out the current score and the current challenge number.
    '''

    global points
    print("At the moment your total points are", points)
    print("Challenge", x+1, "\n")

def play_quest(x):
    '''int -> int
    this functions asks the player question X, checks if player's answer is right and eventually changes the variable points.
    no examples needed
    '''

    global points
    answerPlayer = input(questions[x])
    if answerPlayer == answers[x]:
        print("Well done,", name + ", 10 points gained! Let's move to the next question.\n")
        points +=10
    else:
        print("Wrong! 0 points gained, the correct answer was:", answers[x], ". Next question...\n")

def game_play():
    '''
    first : tell the player his current score and the current challenge number
    second: tell the play_quest-function how many and which questions it must asks the player.
    '''
    
    for x in range(len(questions)):
        print_play_status(x)
        play_quest(x)

def game_end():
    '''
    first : tell the player his finish score.
    second: ask the player if wants to play again and fullfil his wish.
    '''
    print("\nYou finished the game with a total of", points, "points! \n")

    again = None
    
    while again == None:
        again = input("Once again? ")
        if yes.count(again) == True:
            print("\nEnjoy :)\n")
            game_control()
        elif no.count(again) == True:
            
            print("Thanks for playing!")
        else:
            print("oh, just yes or no!")
            again = None

def game_control():
    '''
    Control the whole game with the single steps.
    '''
    game_reset()
    game_intro()
    game_play()
    game_end()

game_control()
