import streamlit

from core.history import History
from interface import streaming_interface

instructions = """Slides's Personal Script:
Without changing any of my text, can you put his writing into 5 slides using my style of writing: 

I was SO WRONG about this!! I’m an ADHD coach for smart women. And in my work, I take the premise that ADHD meds are supposed to help you LIVE A MEANINGFUL LIFE, not become a MORE “PRODUCTIVE” capitalist drone. If you’re reading this, chances are good that you’re a pretty professionally successful ADHD woman. But guess what? You’re a whole-azz person! With dreams to pursue BEYOND your work life. Medication is a tool that can help you realize those dreams and live that life. Meds don’t work for everybody, but if they do work for you, and you have your doctors blessing, I highly encourage you to use them for any part of your life that you need support in.
"""


if __name__ == "__main__":
    company_name = "Slides"
    emoji = ""

    if "history" not in streamlit.session_state:
        streamlit.session_state.history = History()
        streamlit.session_state.history.system(instructions)
        streamlit.session_state.initial_size = 0
    # Main program logic (call this function when you want to start the thread)
    try:
        streaming_interface(company_name, emoji)
    except KeyboardInterrupt:
        print("Program interrupted.")
