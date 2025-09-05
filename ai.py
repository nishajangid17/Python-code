import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

r = sr.Recognizer()

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")      #  collect voice
    engine.setProperty("voice",voices[1].id)   # change voice
    engine.say(command)
    engine.runAndWait()
    
    
    
def  commands():
    
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("listening....  ask.... now...")
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin)
            my_text = my_text.lower()
            print(my_text)
            speak(my_text)
            
            # ask to play song
            if 'play' in my_text:
                my_text = my_text.replace('play','')
                speak('playing'+my_text)
                pywhatkit.playonyt(my_text)
                
            
            #if 'date' in my_text:
                #today = datetime.date.today()
                #speak(str(today))
    except:
            print("error in capturing microphone")
        
        
        
speak("welcome to nisha's project")
commands()

   
   
   
   
   
   
   
    