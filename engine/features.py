import os
import re
import sqlite3
import webbrowser
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
#open youtube and play any video
import pywhatkit as kit

con = sqlite3.connect("lucky.db")
cursor = con.cursor()

#playing assistant sound function
@eel.expose
def playAssistantSound():
    music_dir = "front\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0:
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                if len(results) !=0:
                    speak("opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

            
# play youtube
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("playing"+search_term+" on YouTube")
    kit.playonyt(search_term)


def extract_yt_term(command):
    #define a regular to find the match in the command
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    #IF A MATCH IS FOUND, RETURN THE EXTRACTED SONG NAME; OTHERWISE, RETURN NONE
    return match.group(1) if match else None
  