from flask import Flask, render_template, request,session

app = Flask(__name__)

#@Author Sean Abner Nash
#@Login C00217019
#@Known Issues: I wasnt able to implement a high score table or flask sessiong
#@Time taken: 9 hours
#What is here, The server functions, it can loop throught the pages, It takes words from the player
#and compares them to the rules.

#Import
import xword
import random
import time
from collections import Counter

with open ("Words.txt", "r") as myfile:
    data=myfile.read()
    data=data.split("\n")#Reads the file, initalises the list, splits it into words and suggests one of appropriate length
    randomWord = random.choice(xword.suggest('-------'))
    timerStart = time.time()#Time value is initialised


@app.route('/')
def display_hello():
    return render_template('first.html',the_name = 'Sean`s Word Game!')#Welcome and rule screen



@app.route('/startgame')#Screen where the game starts
def play_game():
    global timerStart
    timerStart = 0.0
    timerStart = time.time()#Starts the timer
    global randomWord
    randomWord = random.choice(xword.suggest('-------'))#Generates a random word so a new one is picked everytime they come to this page.
    return render_template('playGame.html',the_randomWord = randomWord)

    
@app.route('/processwords', methods=['POST']  )#Processes words
def process_words():
    timerResult = round(time.time() - timerStart,2) #gets the timing result, rounded to 2 decimal points.

    playerWords = request.form['seven_words']
    playerWords = playerWords.lower()
    playerWords = playerWords.split(" ")#Gets the player's words
    errorString = ""#Sets up the string that catches errors
    clearedTests = True #Value to see if the player has cleared all the rules

 
#this tests for the number of words the player gave.
    if len(playerWords) < 7:
        errorString = errorString + "Too Few words. "
        clearedTests = False

   #this tests for Word Length
    for givenWord in playerWords:
        if len(givenWord) < 3:
            errorString = errorString + "This word, " + givenWord + " is too Short. \n "
            clearedTests = False

    #this checks if the words exist in the dictionary
    if clearedTests:
        clearedTests = False
        if all(x in data for x in playerWords):
            clearedTests = True; 
        if not all(x in data for x in playerWords):
             errorString = errorString + "Some of these words are not real. "
                

    #this tests for the letter frequency and which ones are used are possible given the source word
    for givenWord in playerWords:
        bag = Counter(randomWord)
        bag.subtract(Counter(givenWord))#Subtracts all the letters of one word from the other 
        #if the letter are rearranged to form words, then none shoule be below zero

        if all(v >= 0 for v in bag.values()):
            print ('Word is contained')#The word is made of letters from the source word

        if any(v < 0 for v in bag.values()):
            errorString = errorString + "The Word '" + givenWord + "' Cannot be made from the Source word. "
            clearedTests = False


    #tests for duplicates

    if any(playerWords.count(x) > 1 for x in playerWords):
        clearedTests = False
        errorString = errorString + "You used duplicates. "


    #tests for random Word generated
    for givenWord in playerWords:
        if givenWord == randomWord:
            errorString = errorString + "You used the source word, " + givenWord + ". "
            clearedTests = False

#Sets the ending message
    if clearedTests:
        endingMessage = "Congrats on winning the game!"
    if not clearedTests:
        endingMessage = "Unfortunately you broke one of the rules =/ "        
  
#Sets the ending screen
    return render_template('thanks.html',the_time = timerResult, errors = errorString, endingLine = endingMessage)

app.run(debug=True)

