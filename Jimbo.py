import streamlit as st
import wikipedia as ai
st.title("Jimbo")
prompt = ""
if prompt == "":
    pass
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! Do you want to ask me somthing?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
def home():
    global prompt
    prompt = st.chat_input("ask something", key="question")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        try:
            x = ai.summary(prompt)
            st.chat_message('ai').write(x)
        except:
            st.chat_message('ai').write("Sorry i can't able to say that right now")
        finally:
            prompt = ""
home()
exit()