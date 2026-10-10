
# Michelle Salgado, 10/09/26, CSC-128 Capstone Project
# Parent Learning Activity Assistant
# This module connects the chatbot to the Groq AI model.

import streamlit as st
from groq import Groq


def generate_ai_response(prompt):
    """Generate an educational response using Groq."""

    try:
        # Read the API key from Streamlit secrets
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a Parent Learning Activity Assistant. "
                        "Help parents create educational activities for "
                        "children in Kindergarten through 5th Grade. "
                        "Use age-appropriate language and keep activities "
                        "safe, positive, and educational. "
                        "Do not diagnose learning disabilities or "
                        "provide medical advice."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=700
        )

        return response.choices[0].message.content


    except Exception as e:
        print(f"Groq error: {type(e).__name__}: {e}")
        return "Sorry, I couldn't generate the activity right now. Please try again shortly."
