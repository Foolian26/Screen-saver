from ctypes import Structure, windll, c_uint, sizeof, byref
import time
import webbrowser

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

while True:
    if get_idle_duration() >10.0:#Time in Sec.
        webbrowser.open("https://www.youtube.com/watch?v=_-WWwNt8AzU")#Example Screensaver
        time.sleep(1)
        exit(0)

