from Actions import * #import all the functions

# -> Start of command taking & verifying
# -> Also Start text-to-speech

def myCommand(): #speech-to-text

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
        message = (redirect(query, 'test', 'test')) # redirect if 'test' in query and replace with the test() command,
        message = (redirect(query, 'greet me', 'greetme'))
        message = ('Valid talking - '+message) #save message as 'Replaced words' OR 'In command List' OR 'Not in command list'
    else:
        message = ('It is not valid talking')
    return message

def printspeak(text): #definition to speak and print what is inputed: printspeak(what you want him to say and print)
    print(text)
    engine.say(text)
    engine.runAndWait()

# -< End of command taking and verifying
# -< Also End text-to-speech

query = myCommand() #execute myCommand function and the output will be called query & change query to lowercase

#query= 'help' #for testing

print(verifycommand(query)) # should return one of four states: #it will also execiute the command.
                            # (Valid talking - Replaced words {Where it was valid talking and it redirected as it saw a specific word})
                            # (Valid Talking - In command list {Where it was valid talking and it was a valid command but didn'tneed redirecting as no keyword was seen})
                            # (Valid takling - Not in command list {Where it was valid talking but it wasn't a command})
                            # (It is not valid talking - Where the microphone didn't pick anything up or when the google speech-to-text wasn't working)

