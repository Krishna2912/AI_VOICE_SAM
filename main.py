import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
   engine.say(text)
   engine.runAndWait()

def take_command():

 try:
    with sr.Microphone() as source:
        print('listening....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'mango' in command:
           command = command.replace('mango', '')
           talk(command)

 except:
    pass
 return command

def run_mango():
    command = take_command()
    print(command)

    if 'hello mango' in command:
        talk('hello boss how can i help you')

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)


    elif 'who is your boss' in command:
        talk('krishna is my boss')

    elif 'your favourite color' in command:
        talk('my favourite color is yellow')

    elif 'tell me a joke' in command:
        talk(pyjokes.get_jokes())

    else:
        talk('boss say it again')

while True:

 run_mango()
