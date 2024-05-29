import streamlit as st
import generate_test as gtests  # Assuming 'generate_test.py' exists

# Title for the Streamlit app
st.title("New Exam")
exam_generated = False
# Form for user input
with st.form(key="new_exam"):
    # Text input for topic
    topic = st.text_input("Set a new test topic", help="Enter the desired topic for the exam.")
    quantity = st.selectbox("Select a questions quantity", [5, 10, 15, 20, 25])
    # Submit button
    btn = st.form_submit_button("Generate Exam")  # Clearer button text
    st.session_state.exam =  []
    if btn:
        # Spinner to indicate exam generation is in progress
        with st.spinner("Generating exam..."):
            exam = gtests.generate(topic, quantity)  # Calls the 'generate' function from 'generate_test.py'
            exam_generated = True
            st.session_state.exam = exam
        # Loop through each question in the generated exam
        for index_qt, question in enumerate(exam):
            # Header for the question
            st.header(question["question"])  # Display the question text

            # List of answer choices
            answers = []
            for index, res in enumerate(question["answers"]):
                answers.append(res["answer"])

            # Radio button component for selecting an answer
            opt = st.radio("Options:", options=answers, key=question["question"])  # Use question as key for uniqueness

btn_finish = st.button("finish exam")

