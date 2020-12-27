from dotenv import load_dotenv # for getting info from the env file
import pyttsx3 # for text-to-speech
import webbrowser #for opening web pages
import smtplib #for emailing
import random # to pick random
import speech_recognition as sr #for speech-to-text
import wikipedia #to look stuff up
import datetime #to find the date+time
import wolframalpha # to do maths
import os # to open programs
import sys # to use the system
import time #so you can wait
from googlesearch import search # to search google for things

import Actions


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
speakingvoice = british # default speaking voice is british

#wolfram setup
client = wolframalpha.Client(wolframappid)

#set the speaking engine
voices = engine.getProperty('voices')
#set the words per minute rate of speech engine
engine.setProperty('voice', speakingvoice)

#definitions
def listallcommands():
    print('Listing commands...')
    #Need to write down all the commands you can say and put them here in text format
 

def todolist():# list the things I have written down to do to improve on
    file = open('TODO')
    printspeak(file.read()) #read the "TODO" file and then respond with the content

def justspeak(audio): #definition to just speak what is inputed: justspeak(what you want him to say)
    engine.say(audio)
    engine.runAndWait()

def printspeak(text): #definition to speak and print what is inputed: printspeak(what you want him to say and print)
    print(text)
    engine.say(text)
    engine.runAndWait()

def greetMe(): #say either good morning, good afternoon or good evening depending on the time.
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        printspeak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        printspeak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        printspeak('Good Evening!')

def startup():
    printspeak("Initializing "+ TriggerName)
    print("")
    print("")
    greetMe()
    time.sleep(1)
    printspeak('Hello '+ MASTER)
    printspeak('')
    printspeak('I am your digital assistant; '+ TriggerName)

def myCommand(): 

	rObject = sr.Recognizer() 
	audio = '' 

	with sr.Microphone() as source: 
		printspeak("Listening...") 
		
		# recording the audio using speech recognition 
		audio = rObject.listen(source, phrase_time_limit = 5) 
	printspeak("Ok... Processing...") # limit 5 secs 

	try: 

		text = rObject.recognize_google(audio, language ='en-US') 
		print("You said: ", text) 
		return text 

	except: 

		printspeak("Could not understand your audio, Please try again !") 
		return 0

query = myCommand() #execute myCommand function and the output will be called query & change query to lowercase
query= query.lower()
printspeak(query)