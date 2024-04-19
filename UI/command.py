import subprocess
import os
import tkinter as tk
import subprocess
import os
import tkinter as tk
from tkinter import filedialog
from pywifi import PyWiFi
import time
import psutil
import vlc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pyautogui
from selenium import webdriver
import speech_recognition as sr
import platform
import eel
#importing feartures
import featureExtraction as FE
import joblib
import numpy as np
import pandas as pd
import io
import wave
import os
import random
import string
from datetime import datetime
#pip install xgboost -- for job lib
global count 

def getC(a):
    count = a

#commands 
commands = {
    0: "assistance_off",
    1: "assistance_on",
    2: "create_new_folder",
    3: "dont_listen_while_you_speak",
    4: "hello",
    5: "next_movie",
    6: "open_control_panel",
    7: "open_google",
    8: "open_start_menu",
    9: "play_movie",
    10: "search_for_specific_file",
    11: "stop_movie",
    12: "turn_off_bluetooth",
    13: "turn_off_wifi",
    14: "turn_on_bluetooth",
    15: "turn_on_wifi",
    16: "unmute_volume",
    17: "volume_down",
    18: "volume_up",
    19: "zoom_in",
    20: "zoom_out"
}

def print_command_text(query):
    if isinstance(query, np.ndarray):
        query = query.item()  # Convert NumPy array to a scalar
    command_text = commands.get(query)
    if command_text:
        print("Command text:", command_text)
    else:
        print("Command not found for query:", query)

def set_system_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level, None)

def unmute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(0, None)

def volume_down():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = max(current_volume - 0.1, 0.0)
    volume.SetMasterVolumeLevelScalar(new_volume, None)

def volume_up():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = min(current_volume + 0.1, 1.0)
    volume.SetMasterVolumeLevelScalar(new_volume, None)

def open_start_menu():
    time.sleep(1)
    pyautogui.press("win")

def search_for_file():
    search_directory = input("Enter the directory to search: ")
    file_name_to_search = input("Enter the file name to search: ")

    for root, dirs, files in os.walk(search_directory):
        if file_name_to_search in files:
            file_path = os.path.join(root, file_name_to_search)
            print(f"Found {file_name_to_search} at: {file_path}")
            return file_path

    print(f"{file_name_to_search} not found in {search_directory}")
    return None

def zoom_in():
    pyautogui.hotkey("ctrl", "+")

def zoom_out():
    pyautogui.hotkey("ctrl", "-")

def open_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

def turn_on_bluetooth():
    if platform.system() == "Windows":
        subprocess.run(["devcon.exe", "enable", "USB\VID_1234&PID_5678"])
    else:
        print("Bluetooth control not implemented for this platform.")

def turn_off_bluetooth():
    if platform.system() == "Windows":
        subprocess.run(["devcon.exe", "disable", "USB\VID_1234&PID_5678"])
    else:
        print("Bluetooth control not implemented for this platform.")

def wifi_operations(state):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    
    if state == 'on':
        iface.scan()
        time.sleep(2)
        iface.disconnect()
        status = iface.status()
        print("Wi-Fi turned on. Status:", status)
    elif state == 'off':
        iface.disconnect()
        status = iface.status()
        print("Wi-Fi turned off. Status:", status)

# Loading the pre-trained model from the JOBLIB file
model = joblib.load('ensemble_model.joblib')


def generate_random_name():
    """Generate a random name with a timestamp for the WAV file."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Format: YYYYMMDDHHMMSS
    return f"audio_{timestamp}.wav"


def record_audio():
    # Function to record audio data from the microphone and save it in a WAV file
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening....')
        r.adjust_for_ambient_noise(source)
        audio_data = r.listen(source, timeout=None, phrase_time_limit= 2)

    # Generate a random file name for the WAV file
    file_name = generate_random_name() + ".wav"
    
    # Define the directory to store the audio files
    directory = "inputs"
    
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Construct the full file path
    file_path = os.path.join(directory, file_name)

    # Save the audio data in WAV format to the generated file name
    with open(file_path, 'wb') as wf:
        wf.write(audio_data.get_wav_data())

    return file_path


movie_path = r"A:\Seasons\SpongeBob SquarePants (1999)\SpongeBob SquarePants Season 1 (1999-2000)\101 Help Wanted.avi"
next_movie_path = r"A:\Seasons\SpongeBob SquarePants (1999)\SpongeBob SquarePants Season 1 (1999-2000)\102 Reef Blower.avi"
@eel.expose
def allCommands(message=22):
    if message == 22:
        
        print('Recording audio...')
        eel.DisplayMessage('Recording audio...')
        # Code to record audio goes here
 
        #audio_data = "Control Pannel.wav" 
        #audio_data = "Create New Folder.wav" 
        #audio_data = "Play Movie.wav" 
        #audio_data = "Turn off wifi.wav" 
        #audio_data = "Turn on Wifi.wav" 

        #record_audio()
        audio_data = record_audio() 
        test = FE.compute_features(audio_data)
        data_processor = FE.Data_Preprocessing(test)
        x=data_processor.preprocessing()
        x

        # Load the saved ensemble model from disk
        loaded_model = FE.load('ensemble_model.joblib')
        predictions = loaded_model.predict(x)
        print(predictions)

        # Process the audio command
        query = predictions
        """ 0: "assistance_off",
    1: "assistance_on",
    2: "create_new_folder",
    3: "dont_listen_while_you_speak",
    4: "hello",
    5: "next_movie",
    6: "open_control_panel",
    7: "open_google",
    8: "open_start_menu",
    9: "play_movie",
    10: "search_for_specific_file",
    11: "stop_movie",
    12: "turn_off_bluetooth",
    13: "turn_off_wifi",
    14: "turn_on_bluetooth",
    15: "turn_on_wifi",
    16: "unmute_volume",
    17: "volume_down",
    18: "volume_up",
    19: "zoom_in",
    20: "zoom_out" """
        query = predictions
        print_command_text(query)
        #eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        if 1 in query:
            subprocess.Popen(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
            script_directory = r"C:\Users\DELL\Desktop\UI"
            script_name = "main.py"
            process = subprocess.Popen(["py", os.path.join(script_directory, script_name)])
            process.wait()
        elif 0 in query:
            script_name = "main.py"
            for process in psutil.process_iter(['pid', 'name']):
                if script_name.lower() in process.info['name'].lower():
                    pid = process.info['pid']
                    os.system(f"taskkill /f /pid {pid}")
        elif 2 in query:
            folder_name = input("Enter the name for the new folder: ")
            root = tk.Tk()
            root.withdraw()
            selected_folder = filedialog.askdirectory(title="Select Folder to Store the New Folder")
            if selected_folder:
                new_folder_path = os.path.join(selected_folder, folder_name)
                os.mkdir(new_folder_path)
                print(f"New folder '{folder_name}' created and stored in '{selected_folder}'.")
            else:
                print("Operation canceled by the user.")
        elif 15 in query:
            wifi_operations('on')
        elif 13  in query:
            wifi_operations('off')
        elif 6 in query:
            os.system("control")
        elif 9 in query:
            instance = vlc.Instance("--no-xlib")
            player = instance.media_player_new()
            media = instance.media_new(movie_path)
            player.set_media(media)
            player.play()
            time.sleep(5)
            player.stop()
        elif 5 in query:
            media = instance.media_new(next_movie_path)
            player.set_media(media)
            player.play()
            time.sleep(600)
            player.stop()
        elif 11 in query:
            player.stop()
        elif 16 in query:
            unmute_volume()
        elif 17 in query:
            volume_down()
        elif 18 in query:
            volume_up()
        elif 8 in query:
            open_start_menu()
        elif 10 in query:
            file_path = search_for_file()
        elif 19 in query:
            zoom_in()
        elif 20 in query:
            zoom_out()
        elif 7 in query:
            open_google()
        elif 14 in query:
            turn_on_bluetooth()
        elif 12 in query:
            turn_off_bluetooth()
    except Exception as e:
        print("Error:", e)
    
    eel.ShowHood()