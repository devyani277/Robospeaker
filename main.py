
#for windows

import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robospeaker Created by Devyani")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want me to speak (or 'q' to quit): ")
        if x.lower() == "q":
            break
        engine.say(x)
        engine.runAndWait()


