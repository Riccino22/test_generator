import streamlit as st
import generate_test as gtests
st.title("New Exam")

with st.form(key="new_exam"):
    topic = st.text_input("Set a new test topic")
    btn = st.form_submit_button()
    if btn:
        exam = gtests.generate(topic)
        exam
