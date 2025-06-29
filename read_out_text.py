# # Copyright 2025 ( @annuaicoder )
# Read out loud any text using your computer’s voice.

import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, this is a text to speech test!")
engine.runAndWait()
