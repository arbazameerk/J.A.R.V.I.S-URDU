import os
import eel
from engine.features import *

eel.init("www")

playAssistantSound()

# Use the 'start-maximized' option to open the app in maximized mode
# Use the 'start' command to specify the window position
os.system('start msedge.exe --start-maximized --window-position=center --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)
