from Actions import * #import all the functions

setup_type = os.getenv('setup_type')
setup(setup_type)


#query = myCommand() #execute myCommand function and the output will be called query & change query to lowercase

query= 'help'

print(verifycommand(query)) # should return one of four states:
                            # (Valid talking - Replaced words {Where it was valid talking and it redirected as it saw a specific word})
                            # (Valid Talking - In command list {Where it was valid talking and it was a valid command but didn'tneed redirecting as no keyword was seen})
                            # (Valid takling - Not in command list {Where it was valid talking but it wasn't a command})
                            # (It is not valid talking - Where the microphone didn't pick anything up or when the google speech-to-text wasn't working)

