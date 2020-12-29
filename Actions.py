## Setup:
## This is everything needed to setup (getting stuff from the .env, imports, setting up enginges for tts, setting up APi's)

#imports
import datetime  # to find the date+time
import os  # to open programs
import re  # for searching in files
import time #for telling the time
import pyttsx3  # for text-to-speech
import speech_recognition as sr  # for speech-to-text
import wolframalpha  # to do maths
from dotenv import load_dotenv  # for getting info from the env file

# Initialize speech 
engine = pyttsx3.init('sapi5')

#Initialize dotenv & get the requirements
load_dotenv()
wolframappid = os.getenv('wolframappid')
Your_Username = os.getenv('Your_Username')
Codingemail = os.getenv('Codingemail')
Normalemail = os.getenv('Normalemail')
Your_Password = os.getenv('Your_Password')

#set the username
MASTER = os.getenv('MASTER')
TriggerName = os.getenv('TriggerName')

#what voice the text to speech will use
american = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0" #Path to the american voice
british = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0" #Path to the british voice
speakingvoice = os.getenv('speakingvoice') # set the speaking voice from the .env

#wolfram setup
client = wolframalpha.Client(wolframappid)

#set the speaking engine
voices = engine.getProperty('voices')
#set the words per minute rate of speech engine
engine.setProperty('voice', speakingvoice)


# -> Start of miscilanious commands
def greetme(): #say either good morning, good afternoon or good evening depending on the time.
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        printspeak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        printspeak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        printspeak('Good Evening!')
# -< End of micelanious commands
#
# -> Start of help commands

def help(): #list all the help commands (Kept in the 'commands.txt' file)
    print('Listing commands...')
    file = open('commands.txt')
    printspeak(file.read()) #read the "commands.txt" file and then respond with the content

# -< End of help commands
#
#-> Start of file help (TODO list, commands)

def ifinlist(query): # if the query is in commands.txt as a valid command
    file = open("commands.txt", "r")
    str = (file.read())
    x = re.search(query, str)
    if(x!=None):
        return True
    else:
        return False

def addtolist(line): #add line to commands.txt to make it a valid command
    file = open("commands.txt", "w")
    file.write(line)

def todolist():# list the things I have written down to do to improve on
    file = open('TODO')
    printspeak(file.read()) #read the "TODO" file and then respond with the content

# -< End of file help (TODO list, commands)
#
# -> Start of starting commands
def startup(): #run startup stuff (saying hello etc)
    printspeak("Initializing "+ TriggerName)
    print("")
    print("")
    greetMe()
    time.sleep(1)
    printspeak('Hello '+ MASTER)
    printspeak('')
    printspeak('I am your digital assistant; '+ TriggerName)

# -< End of setup commands
#
# -> Start of test commands
def test(): # a test function
    printspeak("This is a test function")
thisisatest = test
# -< End of test commands
#
# -> Start of 