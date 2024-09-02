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

from gtts import gTTS
import os    

tts = gTTS(text="This is the pc speaking", lang='en')
tts.save("pcvoice.mp3")
# to start the file from python
os.system("pcvoice.mp3")



# ----- MAIN CODE
st.subheader("Smile  📸 😊 📸  Smile") 
img_file_buffer = st.camera_input("")  

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    progress_text = "** Calculating Awesomeness... **"
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.progress(percent_complete + 1, text="## AWESOMENESS level -> 100%")

    st.balloons()

    # SOUND V2
    #st.write("# Auto-playing Audio!")
    autoplay_audio("thp-reagan-bomb-russia.mp3")






