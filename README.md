# Home-Automation
A project involving servos, relays and other things to turn my home smart.

[Here is the Plan of Production/ Brainstorming.](Plan-Of-Production.md)

[Here is the TODO.](TODO)


# Please note that this was intended to run on a Raspberry Pi, as it is only python it can be modified to run on a Laptop, but I only made this so that I could test on my laptop and then run it headlessly on my Pi.

## To setup:
### Create a ```.env``` file with the format as follows:

These can be whatever you want: 

```
#Usernames
Master = "***"
TriggerName = "***"

#text-to-speech
speakingvoice = american/british

```

Master = 'The name it will call you'
TriggerName = 'what you will call it'
speakingvoice = american/british - this is the voice it will speak in


### Install modules:
```pip install -r Pi_requirements.txt``` - for running on the Pi

```pip install -r Laptop_requirements.txt``` - for testing on a Laptop