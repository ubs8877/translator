import streamlit as st 
from deep_translator import GoogleTranslator


st.set_page_config(
    page_title="English 2 Hindi",
    page_icon="✍️",
)


with st.container(border=True):
    st.title('English - Marathi Translator')
    msgs = st.text_area('Enter text to translate in marathi unicode',key='txtContents')


    def clear_form():
        st.session_state["txtContents"] = ""

    def translate_txt():
        hindi_paragraph = GoogleTranslator(source='en', target='mr').translate(msgs)
        st.markdown('<font color="blue">Your translated text is : </font>', unsafe_allow_html=True)
        st.write(hindi_paragraph)
    

    with st.form("myform"):
        c1,c2 = st.columns([1,1])
        with c1:
            submit = st.form_submit_button(label="Submit",on_click=translate_txt)
        with c2:
            clear = st.form_submit_button(label="Clear", on_click=clear_form)

    st.toast('Welcome to my first English to Marathi translator app - :blue[Umesh S ] :sunglasses:')
