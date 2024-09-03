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

# ----- MAIN CODE
st.subheader("Smile  📸 😊 📸  Smile") 
img_file_buffer = st.camera_input("")  

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    #progress_text = "** Calculating Awesomeness... **"
    progress_text = "Calculating..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.015)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.progress(percent_complete + 1, text="")
    st.subheader("AWESOMENESS level = 100%") 
    
    # SOUND V2
    #st.write("# Auto-playing Audio!")
    #autoplay_audio("thp-reagan-bomb-russia.mp3")
    autoplay_audio("country-rock-109318.mp3")

    st.subheader("_Welcome_ to the :blue[School of Mathematical and Data Sciences]! 🤩♾️🤓") 

    for iter in range(10):
        st.balloons()
        time.sleep(2)
        st.snow()
        time.sleep(7)








