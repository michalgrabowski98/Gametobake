from playsound import playsound
import threading

def playpiwosound():
    threading.Thread(targert=playsound, agrs=('ASMRPIWO.mp3',), daemon=True).start()