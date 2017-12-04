''' HANGMAN PROJECT: This program asks a user to choose to play hangman on either
easy, medium or hard difficulty with either names, town names, or animals. A point
system is in place so that if the user misses three letters, two points are deducted,
and for every two extra letters missed, two more points are deducted. Simultaneously
a body part is added each time points are deducted. After the end of the program
a message is given to the user to rank how they did in retrospect to the difficulty
of the program. 

'''
from graphics import *

import random

win = GraphWin('person', 250, 400)
win.yUp()

line = Line(Point(0, 25), Point(250, 25))
line.draw(win)
line2 = Line(Point(200, 25), Point(200, 350))
line2.draw(win)
line3 = Line(Point(200, 350), Point(100, 350))
line3.draw(win)
line4 = Line(Point(100, 350), Point(100, 300))
line4.draw(win)

head = Circle(Point(100, 275), 25)
body = Line(Point(100, 250), Point(100, 150))
arm = Line(Point(100, 240), Point(150, 200))
arm2 = Line(Point(100,240), Point(50, 200))
leg = Line(Point(100, 150), Point(150, 50))
leg2 = Line(Point(100, 150), Point(50, 50))

bodyParts = [head, body, arm, arm2, leg, leg2]

s = input('Would you like to guess a NAME, PLACE, or ANIMAL?: ')
e = input('Would you like to play EASY, MEDIUM, or HARD?: ')

if s == 'NAME' and e == 'EASY':
    wordList = ['christopher', 'gianna', 'steven', 'samuel', 'nicholas']
elif s == 'NAME' and e == 'MEDIUM':
    wordList = ['bryson', 'jasper', 'roald', 'morrison', 'harper']
elif s == 'NAME' and e == 'HARD':
    wordList = ['zadie', 'krishna', 'nikhila', 'tamal', 'shreyas']
elif s == 'PLACE' and e == 'EASY':
    wordList = ['london', 'paris', 'munich', 'geneva', 'moscow']
elif s == 'PLACE' and e == 'MEDIUM':
    wordList = ['lahaina', 'manchester', 'seoul', 'bozeman', 'sedona']
elif s == 'PLACE' and e == 'HARD':
    wordList = ['galena', 'ypsilanti', 'wallawalla', 'eureka', 'munster']
elif s == 'ANIMAL' and e == 'EASY':
    wordList = ['elephant', 'giraffe', 'hippo', 'dolphin', 'tiger']
elif s == 'ANIMAL' and e == 'MEDIUM':
    wordList = ['okapi', 'tapir', 'salmon', 'seahorse', 'oyster']
elif s == 'ANIMAL' and e == 'HARD':
    wordList = ['dugong', 'lamprey', 'babirasu', 'markhor', 'duiker']
    




def game():
    points = 0
    for i in range(5):
        random.shuffle(wordList)
        word = wordList.pop()
        a = len(word)
        base = a * '_'
        lines = a * '_ '
        print('WORDLENGTH: ', a)
        print(lines)
        print('')
        letters = []
        cletters = []
        print('CURRENT GAME POINTS: ', points)
        if len(letters) < 13:
            while word != base:
                
                print('Previously incorrectly guessed letters: ', letters)
                print('Previously correctly guessed letters: ', cletters)
                print('')
                letter = input('Please guess a lowercase letter: ')
                if len(letter) is 1:
                    if letter in word:
                        for i in range(len(word)):
                            if word[i] == letter:
                                base = base[:i] + word[i] + base[(1+i):]
                        print(base)
                        cletters.append(letter)
                    else:
                        print(base)
                        print('Sorry that letter is not in the word.')
                        if len(letters) == 1:
                            head.draw(win)
                        if len(letters) == 2:
                            body.draw(win)
                        if len(letters) == 3:
                            arm.draw(win)
                        if len(letters) == 4:
                            arm2.draw(win)
                        if len(letters) == 5:
                            leg.draw(win)
                        if len(letters) == 6:
                            leg2.draw(win)
                        
                        letters.append(letter)
                    
                elif len(letter) > 1:
                    print('PLEASE ONLY ENTER ONE LETTER!')

                if len(letters) == 13:
                    print('I am sorry, you took many tries for this word.')
                    print('The word was: ', word)
                    print('Try again')
                    print('')

            if word == base:
                print('CONGRATULATIONS! That is the word! Now play again.')
                print('')
                p = len(letters)
                if p >= 3:
                    points = points + 8
                elif p >= 5:
                    points = points + 6
                elif p >= 7:
                    points = points + 4
                elif p >= 9:
                    points = points + 2
                elif p >= 11:
                    points = points
                elif p == 13:
                    points = points - 2
                else:
                    points = points + 10

            head.undraw()
            body.undraw()
            arm.undraw()
            arm2.undraw()
            leg.undraw()
            leg2.undraw()

        
    print()
    print()
    print()
    print()
    print('TOTAL SCORE: ', points)
    print()
    if points == 50:
        print('Wow... Perfect score? You are a hangman CHAMPION!')
    elif points <= 48:
        print('Youre pretty dang good at this. You deserve a cookie!')
    elif points <= 40:
        print('Not too bad... You get a solid B for your efforts.')
    elif points <= 30:
        print('You should catch up and learn some more words buddy.')
    elif points <= 20:
        print('REALLY?!?! That is all you got?')
    elif points <= 10:
        print('A first year coding student made this and you cannot even earn over ten points?')
        print('That is a pretty huge fail.')
    elif points <= 0:
        print('I am sorry but you fail at life.')
    

game()
