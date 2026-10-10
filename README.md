
# Parent Learning Activity Assistant

## CSC-128 Capstone Project
Created by Michelle Salgado

## Project Description
Parent Learning Activity Assistant is an AI-powered chatbot designed to help parents and caregivers create educational activities for children in Kindergarten through 5th Grade.

The application uses Python, Streamlit, and the Groq API to generate personalized learning activities.

## Features
The chatbot supports four main activity types:

1. Spelling Activities
2. Reading Activities
3. Writing Activities
4. Explain a Concept

Parents can select their child's grade level, enter a topic or spelling words, and choose an activity duration.

## How It Works
- Spelling activities use deterministic Python logic to create missing-letter exercises.
- Reading activities use AI to generate passages and comprehension questions.
- Writing activities use AI to create creative writing exercises.
- Concept explanations use AI to explain educational topics in child-friendly language.

## Safety Features
The chatbot includes a basic keyword-based safety check to identify certain requests for medical, developmental, or learning-disability diagnoses.

Instead of providing a diagnosis, the chatbot recommends consulting a teacher, pediatrician, or qualified professional.

## Technologies Used
- Python
- Streamlit
- Groq API
- GitHub
- Streamlit Community Cloud

## Live Application
https://parent-learning-activity-assistant.streamlit.app/

## GitHub Repository
https://github.com/millesado/parent-learning-activity-assistant

## Limitations
AI-generated activities may occasionally contain mistakes or unclear instructions. Parents should review activities before using them with children.

The chatbot is an educational support tool and does not replace teachers or qualified professionals.
