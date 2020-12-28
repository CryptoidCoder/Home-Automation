# -> Start of setup commands
def setup(type): # determines whether to boot into Pi mode or Laptop mode
    if type == 1 or pi in type.lower():
        setupPi()
    else:
        setupLaptop()

def setupLaptop(): # everything needed to setup on a Laptop
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
    speakingvoice = british # default speaking voice is british

    #wolfram setup
    client = wolframalpha.Client(wolframappid)

    #set the speaking engine
    voices = engine.getProperty('voices')
    #set the words per minute rate of speech engine
    engine.setProperty('voice', speakingvoice)

def setupPi(): # everythign needed to setup on a Raspberry Pi
    #imports
    import datetime  # to find the date+time
    import os  # to open programs
    import re  # for searching in files
    import time # for telling the time
    import pyttsx3  # for text-to-speech
    import speech_recognition as sr  # for speech-to-text
    import wolframalpha  # to do maths
    from dotenv import load_dotenv  # for getting info from the env file

    #imports for Pi only
    import RPi.GPIO as GPIO # for interfacing with the Raspbery Pi GPIO's
    import Adafruit_PCA9685 # for interfacing with the servo control board plugged into the Raspberry Pi

    #setup for Pi only
    pwm = Adafruit_PCA9685.PCA9685() # Initialise the PCA9685 using the default address (0x40).
    servo_min = 90  # Min pulse length out of 4096
    servo_max = 600  # Max pulse length out of 4096
    servo_middle = 400 # Middle pulse length out of 4096
    # GPIO setup goes here aswell

    pwm.set_pwm_freq(60) # Set frequency to 60hz, good for servos.

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

# -< End of startup commands
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
# -> Start of command taking & verifying
# -> Also Start text-to-speech

def takecommand(): #version 1 of speech-to-text
    #Sample rate is how often values are recorded 
    sample_rate = 48000
    #Chunk is like a buffer. It stores 2048 samples (bytes of data) 
    #here. 
    #it is advisable to use powers of 2 such as 1024 or 2048 
    chunk_size = 2048
    #Initialize the recognizer 
    r = sr.Recognizer() 

    with sr.Microphone(device_index = 1, sample_rate = sample_rate, 
                            chunk_size = chunk_size) as source: 
        #wait for a second to let the recognizer adjust the 
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source)
        printspeak("Say Something")
        #listens for the user's input 
        audio = r.listen(source, phrase_time_limit = 5) 
            
        try: 
            text = r.recognize_google(audio) 
            printspeak("you said: " + text )
            return text
        
        #error occurs when google could not understand what was said 
        
        except sr.UnknownValueError: 
            printspeak("Google Speech Recognition could not understand audio")
            return None
        
        except sr.RequestError as e: 
            printspeak("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

def myCommand(): #version 2 of speech-to-text (the one we're using)

	r = sr.Recognizer() 
	audio = '' 

	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		printspeak("Listening...") 
		
		# recording the audio using speech recognition 
		audio = r.listen(source, phrase_time_limit = 5) 
	printspeak("Ok... Processing...") # limit 5 secs 

	try: 

		text = r.recognize_google(audio, language ='en-US') 
		printspeak("You said: "+ text)
		return text.lower()		

	except sr.UnknownValueError: 
		printspeak("Google Speech Recognition could not understand audio")
		return None
        
	except sr.RequestError as e: 
		printspeak("Could not request results from Google Speech Recognition service; {0}".format(e))
		return None

def docommand(command): # execute text as a function
    exec(command+'()')

def redirect(query, word, replace_with): # redirect and do a different command if it finds a certain word in the query
    if word in query:
        docommand(replace_with)
        message =  ('Replaced words')
    else:
        if ifinlist(query) == True: # if its in the command list
            docommand(query)
            message = ('In command list')
        
        else:
            message = ('Not in command list')
    return message

def verifycommand(query): # verify that it is a command using the commands.txt file
    if query != None: #verify that we have a command input
        message = (redirect(query, 'test', 'test')) # redirect if 'test' in query and replace with the test() command, #save message as 'Replaced words' OR 'In command List' OR 'Not in command list'
        message = ('Valid talking - '+message)
    else:
        message = ('It is not valid talking')
    return message

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

# -< End of command taking and verifying
# -< Also End text-to-speech
#
# -> Start of starting commands
def Startup(): #run startup stuff (saying hello etc)
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
# -< end of test commands