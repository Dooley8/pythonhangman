#hangman game
from turtle import *
from random import randint
import math
import time

sw = 700
sh = 800
s= getscreen()
s.setup(sw,sh)
s.bgcolor('lightblue')
t1=getturtle()
t1.speed(0)
t1.hideturtle()

secretWord=''
displayWord=''
fails = 6
lwrong = ''
lcorrect=''
gameDone = False
alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


tw= Turtle()
tw.hideturtle()

tb = Turtle()
tb.hideturtle()




def gallows():
    t1.width(5)
    t1.color('black')
    t1.penup()
    t1.setheading(0)
    t1.goto(-int(sw/4), -int(sh/4))
    
    t1.pendown()
    t1.forward(int(sw/2))

    
    t1.forward(-int(sw/4))
    t1.left(90)
    t1.forward(sh/2)
    t1.left(90)
    t1.forward(sw/4)
    t1.left(90)
    t1.forward(sw/8)






def head():
    hr=45
    t1.penup()
    t1.goto(t1.xcor() -hr,t1.ycor()-hr)
    t1.pendown()
    t1.circle(hr)
    t1.penup()
    t1.goto(t1.xcor() +hr,t1.ycor()-hr)

#head()
    
def body():
    t1.pendown()
    t1.forward(int(sh*.12))

#body()

def rleg():
    t1.left(30)
    t1.forward(50)
    t1.penup()
    t1.backward(50)
    t1.right(30)

#rleg()

def lleg():
    t1.pendown()
    t1.right(30)
    t1.forward(50)
    t1.backward(50)
    t1.left(30)

#lleg()

def rarm():
    t1.left(180)
    t1.forward(35)
    t1.left(60)
    t1.forward(50)
    
#rarm()

def larm():
    t1.backward(50)
    t1.right(120)
    t1.forward(50)

#larm()

def face():
    hr = 45
    t1.penup()
    t1.goto(t1.xcor() +hr,t1.ycor()+hr)
    t1.setheading(180)
    t1.forward(60)
    t1.right(90)
    t1.forward(10)
    t1.left(90)
    t1.pendown()
    t1.circle(2)
    t1.penup()
    t1.backward(30)
    t1.pendown()
    t1.circle(2)
    t1.penup()
    t1.forward(15)
    t1.left(90)
    t1.forward(30)
    t1.right(90)
    t1.forward(15)
    t1.right(90)
    t1.forward(5)
    t1.left(180)
    t1.pendown()
    t1.circle(15,180)
    t1.penup()
    t1.goto(t1.xcor() +hr,t1.ycor()-hr)
    t1.setheading(180)
    t1.forward(58)
    t1.left(90)
    t1.backward(15)
   # t1.forward(10)
   # t1.backward(20)

    
#face()

wList = ['beseech','blithe','traverse','constrain','implicit','purge','chronological', \
        'dominion', 'abate', 'aesthetic','anomaly','austere','candor','clinical', \
         'corroborate','culmination', 'deference','enumerate','imprudent','insatiable',\
         'malleable', 'pragmatic', 'promulgate', 'repudiate']
#print(len(wList))


def secretword():
    global sWord
    sWord = wList[randint(0, len(wList)-1)]
    #print('The secret word is ' + sWord)
    


fonts = int(sh*0.04)

def dointro():
    tw.penup()
    tw.goto(-int(sw*0.4), -int(sh/3))
    tw.write('Guess a letter...', font=('Arial', fonts, 'bold'))


def makeWordString():
    global displayWord, alpha
    displayWord = ""
    for l in sWord:
        if str(l) in alpha:
            if str(l).lower() in lcorrect.lower():
                displayWord += str(l) + " "
            else:
                displayWord += "_" + " "
        else:
            displayWord += str(l) + " "
    #print(displayWord)

def displaytext(newText):
    tw.clear()
    tw.penup()
    tw.goto(-int(sw*0.4), -int(sh/3))
    tw.write(newText, font=("Arial", fonts, 'bold'))

def wrongtext(newText):
    tb.clear()
    tb.penup()
    tb.goto(-int(sw*0.4), int(sh/3))
    tb.write(newText, font=("Arial", fonts, 'bold'))


def updateHangman():
    global fails
    if fails == 5:
        head()
        face()
    if fails == 4:
        body()
    if fails == 3:
        rleg()
    if fails == 2:
        lleg()
    if fails == 1:
        rarm()
    if fails == 0:
        larm()





def getGuess():
    boxTitle="Letters Used: " + lwrong
    guess = s.textinput(boxTitle, "Enter a Guess type $$ to Guess the word")
    return guess

def checkWordGuess():
    global fails, gameDone
    boxTitle="Word Guess"
    theGuess = s.textinput(boxTitle, "Ok Awesome...Guess the word")
    if theGuess == sWord:
        displaytext("Correct the word is " + sWord)
        gameDone = True
    else:
        displaytext("No the word is not "+ theGuess)
        time.sleep(1)
        displaytext(displayWord)
        fails-=1
        updateHangman()


def restartGame():
    global fails, lcorrect, lwrong, gameDone
    boxTitle = "Want to play again"
    guess = s.textinput(boxTitle, "Type Yes to play again")
    if guess.lower()=='y' or guess.lower()== 'yes':
        time.sleep(1)
        t1.clear()
        gallows()
        secretword()
        displaytext("Guess a Letter...")
        wrongtext("Not in word: [" + lwrong + "]")


        time.sleep(1)
        makeWordString()
        displaytext(displayWord)
        gameDone = False
        lwrong =""
        lcorrect =""
        wrongtext("Not in word: [" + lwrong + "]")
             
    else:
        wrongtext("See you later")









def playGame():
    global gameDone, fails, alpha, lcorrect, lwrong
    while gameDone == False and fails > 0:
        theGuess = getGuess()
        if theGuess == "$$":
            print("let them guess the word")
            checkWordGuess()
        elif len(theGuess) > 1 or theGuess =="":
                displaytext(theGuess + " is not a letter, guess again")
                time.sleep(1)
                displaytext(displayWord)
        elif theGuess not in alpha:
                displaytext(theGuess + " is not a letter, guess again")
                time.sleep(1)
                displaytext(displayWord)
        elif theGuess.lower() in sWord.lower():
                lcorrect += theGuess.lower()
                makeWordString()
                displaytext(displayWord)
        else:
            if theGuess.lower() not in lwrong:
                lwrong += theGuess.lower() + ", "
                fails -=1
                displaytext(theGuess + " is not in the word, guess again")
                time.sleep(1)
                updateHangman()
                displaytext(displayWord)
                wrongtext("Not in word: [" + lwrong + "]")
            else:
                displaytext(theGuess + " was already guessed. Try again")
                time.sleep(1)
                dispalytext(displayWord)

        if "_" not in displayWord:
            displaytext("You won, the word is : " + sWord)
            gameDone = True
        if fails <= 0:
            displaytext("Sorry you lose word is " + sWord)
            gameDone = True
        if gameDone == True:
            restartGame()




gallows()
head()
face()
body()
rleg()
lleg()
rarm()
larm()



time.sleep(1)
t1.clear()
gallows()
secretword()
displaytext("Guess a Letter...")
wrongtext("Not in word: [" + lwrong + "]")


time.sleep(1)
makeWordString()
displaytext(displayWord)
playGame()

