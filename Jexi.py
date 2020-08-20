# Importing Libraries

import pyttsx3
import os
import webbrowser as web
from datetime import datetime


# Jexi Voice Code

def Jexi_Speak(Line):
    
    Driver = pyttsx3.init() 
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    Driver.setProperty('voice', voice_id)  
    Driver.setProperty('volume', 0.9)
    Driver.setProperty('rate', 185)
    Driver.runAndWait()
    print(Line)
    pyttsx3.speak(Line)
	

# Inital Greeting Code

def Greeting(): 
    
    current_Time = int(datetime.now().strftime("%H"))

    if (current_Time < 12):
        greeting = "Good Morning"
    elif (current_Time < 17):
        greeting = "Good Afternoon"
    elif (current_Time > 17):
        greeting = "Good Evening"
    else:
        greeting = "Hello"    

    first_Line = greeting + ", My name is Jexi \n How may i help You"    

    Jexi_Speak(first_Line) 
	
	
# Web Activity Code

def Web_Browsing(Action):
    
    if (("search" in Action) or ("google" in Action)):
        Jexi_Speak ("What do you want to search for?")
        search = input()
        Jexi_Speak ("Here's what i found for " + search + " on google.")
        web.open ("https://www.google.com/search?q=" + search)
        
    else:
        Jexi_Speak ("Where do you wanna go?")
        Action = input()
            
        if ("https" not in Action):
            url = "https://" + Action 
            
        elif ("http" in Action):
            url = Action.replace("http", "https")
            
        else:
            url = Action
            
        if ((".com" in url) or (".in" in url) or (".org" in url)):
            web.open (url)
            
        elif (("youtube" in url) or ("facebook" in url) or ("gmail" in url)):
            web.open (url + ".com")
            
        else:
            Jexi_Speak ("I don't recognise this website, Let me run a Google Search for it instead.")
            web.open("https://www.google.com/search?q=" + url)


# Main Menu Code

def Menu():
    
    while True:
        Action = input(":)")
        
        if (("hi" in Action) or ("hello" in Action)):
            os.system("Hello")
            
        elif ("chrome" in Action):
            os.system("chrome")
   
        elif (("notepad" in Action) or ("text editor" in Action)):
            os.system("notepad")
            
        elif (("your" in Action) and ("name" in Action)):
            Jexi_Speak("My name is Jexi.")
            
        elif ("media player" in Action):
            os.system("wmplayer")
            
        elif ("blender" in Action):
            os.system("blender")
        
        elif (("my files" in Action) or ("my computer" in Action)):
            os.system("explorer")
        
        elif (("website" in Action) or ("search" in Action)):
            Web_Browsing(Action)
        
        elif (("bye" in Action) or ("quit" in Action) or ("exit" in Action)):
            Jexi_Speak("Until we meet again.")
            break
        else:
            Jexi_Speak("Sorry, I don't support this Action")
			
# main Function
	
def main():
    
    Greeting()
    Menu()
	
if __name__ == "__main__":
    main()