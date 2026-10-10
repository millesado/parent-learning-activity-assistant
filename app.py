
# Michelle Salgado, 10/09/26, CSC-128 Capstone Project
# Parent Learning Activity Assistant
# This chatbot helps parents create educational activities
# for children, including spelling, reading, and writing practice.


import streamlit as st

from activities import (
    generate_spelling_activity,
    generate_reading_prompt,
    generate_writing_prompt,
    generate_explanation_prompt,
    check_safety
)

from ai_helper import generate_ai_response


# Set up the chatbot page
st.set_page_config(
    page_title="Parent Learning Activity Assistant",
    page_icon="📚"
)

# Display the chatbot title and description
st.title("📚 Parent Learning Activity Assistant")

st.write(
    "Welcome! I'm a chatbot designed to help parents "
    "create fun educational activities for their children."
)

st.info(
    "I can help with spelling, reading, writing, and "
    "explaining concepts in child-friendly language."
)

# Let parents choose the type of learning activity
st.subheader("Choose a Learning Activity")

activity_type = st.selectbox(
    "What would you like to practice?",
    [
        "Spelling Activities",
        "Reading Activities",
        "Writing Activities",
        "Explain a Concept"
    ]
)

# Collect the child's grade level
grade_level = st.selectbox(
    "What is your child's grade level?",
    [
        "Kindergarten",
        "1st Grade",
        "2nd Grade",
        "3rd Grade",
        "4th Grade",
        "5th Grade"
    ]
)

# Collect words or a topic from the parent
st.subheader("Activity Details")

user_input = st.text_area(
    "Enter spelling words or a learning topic:",
    placeholder="Example: cat, dog, house, tree OR the water cycle"
)

# Let the parent choose the activity length
activity_length = st.selectbox(
    "How long should the activity take?",
    [
        "5 minutes",
        "10 minutes",
        "15 minutes",
        "20 minutes"
    ]
)

# Button to generate the activity
generate_button = st.button("Generate Activity")

# Generate the selected learning activity
if generate_button:

    if not user_input.strip():
        st.warning("Please enter spelling words or a learning topic.")

    elif check_safety(user_input):
        st.warning(check_safety(user_input))

    elif activity_type == "Spelling Activities":
        st.subheader("Your Spelling Activity")

        result = generate_spelling_activity(user_input)

        st.write(result)


    elif activity_type == "Reading Activities":
        st.subheader("Your Reading Activity")

        prompt = generate_reading_prompt(
            user_input, grade_level, activity_length
        )

        with st.spinner("Creating your reading activity..."):
            result = generate_ai_response(prompt)

        st.write(result)


    elif activity_type == "Writing Activities":
        st.subheader("Your Writing Activity")

        prompt = generate_writing_prompt(
            user_input, grade_level, activity_length
        )

        with st.spinner("Creating your writing activity..."):
            result = generate_ai_response(prompt)

        st.write(result)


    elif activity_type == "Explain a Concept":
        st.subheader("Your Child-Friendly Explanation")

        prompt = generate_explanation_prompt(
            user_input, grade_level, activity_length
        )

        with st.spinner("Creating your explanation..."):
            result = generate_ai_response(prompt)

        st.write(result)

    else:
        st.warning("Please select a valid activity type.")
