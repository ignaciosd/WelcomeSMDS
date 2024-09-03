# ----- LIBRARIES
import streamlit as st
from PIL import Image
import numpy as np
import time
import base64

# ----- FUNCTIONS
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true" loop="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


#from streamlit_TTS import auto_play, text_to_speech, text_to_audio
#from gtts.lang import tts_langs
#langs=tts_langs().keys()

#get the audio first
#audio=text_to_audio("Choose a language, type some text, and click 'Speak it out!'.",language='en')
#then play it
#auto_play(audio)
#lang=st.selectbox("Choose a language",options=langs)
#text=st.text_input("Choose a text to speak out:")
#speak=st.button("Speak it out!")

#if lang and text and speak:
#    #plays the audio directly
#    text_to_speech(text=text, language=lang)

#import pyttsx3
# init function to get an engine instance for the speech synthesis 
#engine = pyttsx3.init()
# say method on the engine that passing input text to be spoken
#engine.say('Hello sir, how may I help you, sir.')
# run and wait method, it processes the voice commands. 
#engine.runAndWait()

#from gtts import gTTS
#import os    

#tts = gTTS(text="This is the pc speaking", lang='en')
#tts.save("pcvoice.mp3")
# to start the file from python
#os.system("pcvoice.mp3")

#import os
#os.system("echo 'hello world'")
#os.system("say 'hello world'") 

#import streamlit as st
#from streamlit_talk import message
#message("My message") 
#message("Hello bot! How are you doing today ???", is_user=True)  # align's the message to the right

#autoplay_audio("thp-jfk-space-clip.mp3")


# ----- MAIN CODE
st.subheader("Smile  📸 😊 📸  Smile") 
img_file_buffer = st.camera_input("")  

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    #progress_text = "** Calculating Awesomeness... **"
    progress_text = "** Calculating Awesomeness... **"
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.progress(percent_complete + 1, text="**AWESOMENESS level -> 100% **")

    # SOUND V2
    #st.write("# Auto-playing Audio!")
    #autoplay_audio("thp-reagan-bomb-russia.mp3")
    autoplay_audio("country-rock-109318.mp3")

    for iter in range(10):
        st.balloons()
        time.sleep(1)
        st.snow()
        time.sleep(1)








