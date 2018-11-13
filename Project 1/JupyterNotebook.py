
#%%
import xword
import random
import time
from collections import Counter

with open ("Words.txt", "r") as myfile:
    data=myfile.read()
    data=data.split("\n");

randomWord = random.choice(xword.suggest('-------'));

print(randomWord);


#%%
import time
start =0;

start = time.time()

playerWords = "sail abigail eail 4ail 5ail"
playerWords = playerWords.lower();
playerWords = playerWords.split(" ");
print(playerWords)
len(playerWords)


#%%
end =0;
end = time.time()

clearedTests = True;

        #this tests for Word Length
testString = "orE"
for givenWord in playerWords:
    if len(givenWord) < 3:
        print("THIS ", givenWord, " is too short")
        clearedTests = False;
        
        
print(clearedTests)

#this checks if the words exist
if clearedTests:
    clearedTests = False;
    if all(x in data for x in playerWords):
        clearedTests = True; 
        print("ALL CORRECT")

            
print(clearedTests)

#this tests for the letter frequency
for givenWord in playerWords:
    bag = Counter(randomWord)
    bag.subtract(Counter(givenWord))
    if all(v >= 0 for v in bag.values()):
        print ('Word is contained')
    if any(v < 0 for v in bag.values()):
        print('Word is Not Contained')
        clearedTests = False;
        
print(clearedTests)

#tests for duplicates

if any(playerWords.count(x) > 1 for x in playerWords):
       clearedTests = False;
       print("DUPES DETECTED")
       
       
print(clearedTests)

#tests for random Word generated
for givenWord in playerWords:
    if givenWord == randomWord:
        print("THIS IS THE SOURCE ", givenWord)
        clearedTests = False;


print(clearedTests)


#%%
letters = 'dnaeeli'
words = 'line', 'linda', 'need', 'den', 'x'

for word in words:
    if not Counter(word) - Counter(letters):
        Counter(word) - Counter(letters)      
        
print(round(end - start,2))


#%%



            


#%%
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

if hasNumbers(playerWords):
    print("ASASASA")


#%%
my_string="ASdsad"
my_string.isdigit()
if my_string.isdigit() == False: 
    print("ASAS")
    


#%%
str(input("Enter a name: "))


#%%



#%%
l1 = ["fish", "boat", "oar"]
l2 = ["rod", "gunwale", "fish", "net"]
l3 = ["net", "fish", "weight"] 



for w in randomWord:
  if w in data:
    print ('found ',w,' in Data!')
    


#%%



#%%



#%%



#%%



#%%



#%%



