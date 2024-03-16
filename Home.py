import streamlit as st 
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Translator",
    page_icon="✍️",
)

st.snow()

st.write("# Welcome to Translator ! ✍️")
exit_app = st.sidebar.button("Shut Down")

if exit_app:
    # Give a bit of delay for user experience
    time.sleep(3)
    # Close streamlit browser tab
    keyboard.press_and_release('ctrl+w')
    # Terminate streamlit python process
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()
