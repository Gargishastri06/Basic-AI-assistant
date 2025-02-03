#jarvis: voice activated virtual assistant

import speech_recognition as sr         #IT HELP IN SPEECH REGOGINATION
import webbrowser 
import pyttsx3                           # it help to convert speech into text


def speak(text):
    engine = pyttsx3.init()    
    engine.say(text)
    engine.runAndWait()

speak('Initializing Jarvis......')

recognizer = sr.Recognizer()

def processCommand(command):
    if command.lower()=='open google':
        webbrowser.open('https://google.com')
    elif command.lower()== 'open youtube':
        webbrowser.open('https://www.youtube.com/')
    elif command.lower()=='open spotify':
        webbrowser.open('https://open.spotify.com/')




def record_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source,timeout=4,phrase_time_limit=2)
        print('recognizing')
    return audio

def recognize_speech(audio):
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        if (text.lower()=='Jarvis'):
            speak('How can i help you')
            print('jarvis active')
            command_audio = record_audio()  # Record the next command
            command_text = recognizer.recognize_google(command_audio)
            processCommand(command_text)
        
        
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")




while True:
    audio = record_audio()
    recognize_speech(audio)

   





   
   
   





