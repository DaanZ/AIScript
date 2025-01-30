import streamlit as st

from core.chatgpt import llm_stream, process_stream


def streaming_interface(name: str, emoji: str, pages=None):
    st.set_page_config(
        page_title=f"{name}'s Persona",
        page_icon=emoji,
        layout="wide"
    )
    st.title(f"{name}'s Persona")

    # Display all previous messages
    for message in st.session_state.history.logs:
        if message["role"] == "system":
            continue
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_prompt = st.chat_input()  # Input box for the user

    if user_prompt is not None:
        st.session_state.history.user(user_prompt)
        st.session_state.history.system("Rewrite the user script into the persona's script writing style.")
        with st.chat_message("user"):
            st.markdown(user_prompt)

        # Placeholder for the assistant's reply
        assistant_message_placeholder = st.chat_message("assistant")
        assistant_text = assistant_message_placeholder.empty()
        assistant_text.markdown("⌂")
        # Stream response
        response_stream = llm_stream(st.session_state.history)
        answers = process_stream(response_stream)
        chunk = ""
        for chunk in answers:
            assistant_text.markdown(chunk)  # Update progressively
        st.session_state.history.assistant(chunk)  # Save final message in history
