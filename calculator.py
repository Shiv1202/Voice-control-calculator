
import speech_recognition as sr
import pyttsx3
import datetime
from factorial import fact
import re
from functions_for_power_calculation import (find_sqrt, 
    cube_root,
    power,
    square,
    cube,
)

from trigonometry import (
    sin_value,
    cos_value,
    tan_value,
)
print("Your Speech Recognition version is: " + sr.__version__)

engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[len(voice) - 1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-62)


def response(audio):
    print(f"Calc: {audio}")
    engine.say({audio})
    engine.runAndWait()

def my_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening....")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language="en-in")
        print(f"User: {command}" + '\n')
    except sr.UnknownValueError:
        response("Sorry boss! I did not get that. Could you please type it.")
        command = str(input('command: '))
    return command

def greeting():
    curr_time = int(datetime.datetime.now().hour)
    if curr_time >= 0 and curr_time < 12:
        response("Good Morning boss! how may i help you.")
    if curr_time >= 12 and curr_time < 17:
        response("Good Afternoon boss! how may i help you.")
    if curr_time >= 17 and curr_time != 0:
        response("Good Evening boss! how may i help you.")
# greeting()



if __name__ == "__main__":
    
    greeting()
    command = my_command()
    command = command.lower()
    if "square" in command:
        res = square(list(map(int, re.findall(r'\d+', command))))
        response(f"Square is: {res}")
    
    if "cube of" in command:
        res = cube(list(map(int, re.findall(r'\d+', command))))
        response(f"Cube is {res}")
    
    if "square root" in command:
        res = find_sqrt(list(map(int, re.findall(r'\d+', command))))
        response(f"Square root is: {res}")
    
    if "is to the power" in command or "power" in command:
        res = power(list(map(int, re.findall(r'\d+', command))))
        response(f"Result is {res}")
    
    if "cube root" in command:
        res = cube_root(list(map(int, re.findall(r'\d+', command))))
        response(f"Cube root is: {res}")
    
    if "factorial" in command:
        res = fact(list(map(int, re.findall(r'\d+', command))))
        response(f"Factorial is: {res}")
    
    if re.search("sine of", command):
        res = sin_value(list(map(int, re.findall(r'\d+', command))))
        response(f"sine value is: {res}")
    