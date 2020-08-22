# Importing Libraries

import pyttsx3                     # Text to Speech Conversion Library
import os                          # Provides interaction with Operating System
import webbrowser as web           # Helps in Web based Activities
from datetime import datetime      # Provides System Date and time data



# Jexi Voice Code

def Jexi_Speak(Line):
    
    Driver = pyttsx3.init() 
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"     # Default Voice For Jexi
    
    Driver.setProperty('voice', voice_id)       # Setting the Voice id for Jexi
    Driver.setProperty('volume', 0.9)           # Loudness in Jexi's Voice
    Driver.setProperty('rate', 185)             # Speed of Jexi's Voice
    Driver.runAndWait()
    
    print(Line)                                 # Printing Jexi Response
    print()                                     # Adding space between Response
    pyttsx3.speak(Line)                         # Jexi's Audio Response
    
    
    
# Inital Greeting Code

def Greeting(): 
    
    current_Time = int(datetime.now().strftime("%H"))                         # Fetching Current System Time

    if (current_Time < 12):                                                   # Morning Time Condition
        greeting = "Good Morning"                                             
    elif (current_Time < 17):                                                 # Afternoon Time Condition
        greeting = "Good Afternoon"                                           
    elif (current_Time > 17):                                                 # Evening Time Condition
        greeting = "Good Evening"
    else:                                                                     # In case of Issue in system Time
        greeting = "Hello"                                                   

    first_Line = greeting + ", My name is Jexi \n How may i help You"         # Jexi's First Line
    print()
    Jexi_Speak(first_Line) 
    
    
    
# Key Words Function Code

def Key_Word(Action, Key):
    
    # Defining Key words for Easy future Expansion
  
    Url_Keys = ["youtube","google","instagram","yahoo","linkedin","facebook","gmail","amazon"]
    App_Keys = ["notepad","chrome","wmplayer","blender","explorer"]
    Exit_Keys = ["bye","close","exit","terminate","quit"]  
    
    Output = []
    
    if (Key == "url"):                      # Checking Url Keywords
        for x in Url_Keys:
            if (x in Action):
                Output = [True,x]
                return Output
            else:
                Output = [False,x]
            
    elif (Key == "App"):                    # Checking Application Keywords
        for x in App_Keys:
            if (x in Action):
                Output = [True,x]
                return Output
            else:
                Output = [False,x]
            
    elif (Key == "Exit"):                   # Checking Exit Keywords
        for x in Exit_Keys:
            if (x in Action):
                Output = [True,x]
                return Output
            else:
                Output = [False,x]
                
    return Output
    
    
    
# Web Activity Code

def Web_Browsing(Action):
    
    if (("search" in Action) or ("google" in Action)):                        # Google Search Action
        Jexi_Speak ("What do you want to search for?")
        search = input(" :) ")
        Jexi_Speak ("Here's what i found for " + search + " on google.")      
        web.open ("https://www.google.com/search?q=" + search)
        
    else:                                                                     # Going to a Website
        Jexi_Speak ("Where do you wanna go?")
        Action = input(" :) ").lower()
            
        if ("https" not in Action):                                           # Adding HTTPS for more secured Connection
            url = "https://" + Action 
            
        elif ("http" in Action):
            url = Action.replace("http", "https")                             # Replacing HTTP with HTTPS
            
        else:
            url = Action                                                      
            
        if ((".com" in url) or (".in" in url) or (".org" in url)):            # If address is in Correct Domain format
            web.open (url)
            Jexi_Speak("Have Fun.")
            
        elif (Key_Word (url, "url")[0]):                                      # If addess doesn't have a domain the check the Keyword List
            web.open (url + ".com")
            Jexi_Speak("Have Fun.")
            
        else:                                                                 # Still if not in recognised format then do a Google Search for the address
            Jexi_Speak ("I don't recognise this website, Let me run a Google Search for it instead.")
            web.open("https://www.google.com/search?q=" + url)
            
            
            
# Main Menu Code

def Menu():
    
    while True:
        Action = input(" :) ").lower()                                          # Taking Action Input & converting in Lower Case
        
        if (("hi" in Action) or ("hello" in Action)):                           # Interacting with Jexi with Hello or Hi
            Jexi_Speak("Hello, I hope you a having a nice day.")
        
        elif (("your" in Action) and ("name" in Action)):                       # Ask Name
            Jexi_Speak("My name is Jexi.")
                
        elif (Key_Word (Action, "App")[0]):                                     # Open an Application
            os.system(Key_Word (Action, "App")[1])
            Jexi_Speak("Sure")

        elif ("outlook" in Action):                                             # Open Calculator
            os.startfile("outlook")
            Jexi_Speak("Right away")
        
        elif ("calculator" in Action):                                          # Open Calculator
            os.system("C:\\Windows\\System32\\calc.exe")
            Jexi_Speak("Of Course")
        
        elif ("wordpad" in Action):                                             # Open Wordpad
            os.system("C:\\Windows\\System32\\write.exe")
            Jexi_Speak("Right away")
            
        elif (("website" in Action) or ("search" in Action)):                   # Web Activity Function Call
            Web_Browsing(Action)
       
        elif ("bye" in Action):                                                 # Saying Good Bye.
            Jexi_Speak("Until we meet again.")
            break                                                               # Break out of Menu Loop
            
        else:
            Jexi_Speak("Sorry, I don't support this Action")                    # Non Supported Action
            
            
            
# main Function

def main():
    
    Greeting()            # Greeting Function Call
    Menu()                # Main Menu Function Call
    
    
    
if __name__ == "__main__":
    main()
