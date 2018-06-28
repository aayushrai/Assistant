from gtts import gTTS
import speech_recognition as sp
import playsound
import os
import webbrowser
from api.Quickstart import email      # here i import my api python file
import random

def talker(text):
    gtts = gTTS(text,lang='en')                           # convert text in speech
    rand = random.randrange(1000)                         # random name to file
    gtts.save('audio{}.mp3'.format(rand))                 # save speech in audio.mp3 file
    playsound.playsound('audio{}.mp3'.format(rand))       # play mp3 file
    os.remove('audio{}.mp3'.format(rand))                 # remove mp3 file to save storage


def listener_fun():
    with sp.Microphone() as source:                                  # activate microphone
        print("listening........................")
        sp.Recognizer().adjust_for_ambient_noise(source,duration=1)  # adjust noise
        sp.Recognizer().pause_threshold = 1                          # adjust pauses
        audio = sp.Recognizer().listen(source)                       # listen microphone
    try:
        command = sp.Recognizer().recognize_google(audio).lower()     # convert speech to text

    except sp.UnknownValueError:                                      # if any problem in recognize the voice it will retry
        command=listener_fun()

    return command


def main(command):           # just use if else command
    if "hey google" or 'hey jarvis' or 'hey alexa' or 'ok gooogle' in command:

        while True:
            print('listening--google')
            heycmd = listener_fun()
            print('You said: ' + heycmd + '\n')
            if "open facebook" in heycmd:
                webbrowser.open("https://www.facebook.com/")     # open fb url
                break

            if "send email" in heycmd:     # here you can use any api as your use
                print("sender email")
                talker("who do you want to send email")
                reciver = listener_fun()
                print("subject")
                talker("what's a subject")
                subject = listener_fun()
                print("subject is " + subject)
                print('message')
                talker("what's a massage")
                massage = listener_fun()
                print("message is "+ massage)
                talker("do you wanna send it or change it ")
                decision = listener_fun()
                if "send it" in decision:
                    email('sender email',reciver,subject,massage) # use google api for email
                    print('email send')
                    break
                elif 'change it' in decision:
                    pass


while True:
    main(listener_fun())

