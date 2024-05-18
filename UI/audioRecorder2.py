import subprocess
import os
import tkinter as tk
from tkinter import filedialog
import psutil
import time
from pywifi import PyWiFi
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pyautogui
from selenium import webdriver
import speech_recognition as sr
import eel
import threading

class AudioRecorder:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.listening = False
        self.audio_buffer = []
        self.chunk_duration = 3  # Duration of audio chunks (in seconds)

    def start_listening(self):
        self.listening = True
        self.audio_buffer = []
        self.listen_thread = threading.Thread(target=self._listen_loop)
        self.listen_thread.start()

    def stop_listening(self):
        self.listening = False

    def _listen_loop(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while self.listening:
                print('Listening...')
                audio_data = self.recognizer.listen(source, timeout=None, phrase_time_limit=self.chunk_duration)
                self.audio_buffer.append(audio_data)
                self._process_audio_chunk()

    def _process_audio_chunk(self):
        if self.audio_buffer:
            audio_chunk = self.audio_buffer.pop(0)
            allCommands(audio_chunk)

recorder = None

class VoiceCommandProcessor:
    def __init__(self, ml_model):
        self.ml_model = ml_model

    def process_voice_command(self, audio_data):
        # Pass the audio data to the machine learning model for processing
        # Modify this part based on your ML model's requirements
        processed_command = self.ml_model.process_audio(audio_data)
        return processed_command

@eel.expose
def allCommands(message=1):
    if message == 1:
        print('Recording audio...')
        eel.DisplayMessage('Recording audio...')
        # Code to record audio goes here
        audio_data = record_audio()

        # Initialize VoiceCommandProcessor with your ML model
        #voice_processor = VoiceCommandProcessor(ml_model)

        # Process the audio command
        query = "Control Panel"#voice_processor.process_voice_command(audio_data)
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        if "Assistance ON" in query:
            subprocess.Popen(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
            script_directory = r"C:\Users\DELL\Desktop\EEL UI"
            script_name = "main.py"
            process = subprocess.Popen(["py", os.path.join(script_directory, script_name)])
            process.wait()
        elif "Assistance OF" in query:
            script_name = "main.py"
            for process in psutil.process_iter(['pid', 'name']):
                if script_name.lower() in process.info['name'].lower():
                    pid = process.info['pid']
                    os.system(f"taskkill /f /pid {pid}")
        elif "New Folder" in query:
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
        elif "WiFi On" in query:
            wifi = PyWiFi()
            iface = wifi.interfaces()[0]
            iface.scan()
            time.sleep(2)
            iface.disconnect()
            iface.status()
            time.sleep(2)
        elif "WiFi Off" in query:
            wifi = PyWiFi()
            iface = wifi.interfaces()[0]
            iface.disconnect()
            iface.status()
        elif "Control Panel" in query:
            os.system("control")
        elif "Movie" in query:
            instance = vlc.Instance("--no-xlib")
            player = instance.media_player_new()
            media = instance.media_new(movie_path)
            player.set_media(media)
            player.play()
            time.sleep(5)
            player.stop()
            media = instance.media_new(next_movie_path)
            player.set_media(media)
            player.play()
            time.sleep(10)
            player.stop()
        elif "Speakers" in query:
            unmute_volume()
            volume_down()
            volume_up()
        elif "Start Menu" in query:
            open_start_menu()
        elif "Search for a Specific File" in query:
            file_path = search_for_file()
        elif "Zoom In" in query:
            zoom_in()
        elif "Zoom Out" in query:
            zoom_out()
        elif "Browser" in query:
            open_google()
        elif "Bluetooth On" in query:
            turn_on_bluetooth()
        elif "Bluetooth Off" in query:
            turn_off_bluetooth()
    except Exception as e:
        print("Error:", e)

    eel.ShowHood()

@eel.expose
def start_recording():
    global recorder
    recorder = AudioRecorder()
    recorder.start_listening()

@eel.expose
def stop_recording():
    if recorder:
        recorder.stop_listening()

@eel.expose
def record_audio():
    # Function to record audio data from microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=None, phrase_time_limit=5)
    return audio

# Instantiate your ML model here
#ml_model = YourMLModel()

# Start your Eel application here