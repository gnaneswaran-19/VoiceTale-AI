import google.generativeai as genai
import streamlit as st
from elevenlabs.client import ElevenLabs 
from elevenlabs import save   
genai.configure(api_key="Your API key")
model=genai.GenerativeModel('gemini-2.5-flash')
st.title("Story Teller voice Generator")
category = st.selectbox(
    "Choose Story Type",
    ["Horror", "Comedy", "Kids stories", "Motivational"]
)
language = st.selectbox(
    "Choose Language",
    ["English", "Tamil", "Hindi"]
)
lang_model=ElevenLabs(api_key="sk_64c3fd02c7e05100826b87c64ff40af938f7985cdb1fda88")
role="generate a story based on the title provided. The story should be engaging and suitable for all peoples. whatever language is given the story should be reply all of them"
prompt=st.text_input("Enter the story title:")
res=model.generate_content(prompt+role+category+language).text
id="gCr8TeSJgJaeaIoV4RWH"
if st.button("Submit") and prompt:
    audio=lang_model.text_to_speech.convert(text=res,voice_id=id)
    save(audio,"voice.mp3")
    print(st.audio("voice.mp3")) 
    print(st.write(res))

