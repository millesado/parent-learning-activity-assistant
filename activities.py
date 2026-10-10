
# Michelle Salgado, 10/09/26, CSC-128 Capstone Project
# Parent Learning Activity Assistant
# This module generates educational activities for children.

def generate_spelling_activity(word_list):
    """Create missing-letter spelling exercises."""

    words = [
        word.strip().lower()
        for word in word_list.split(",")
        if word.strip()
    ]

    if not words:
        return "Please enter some spelling words separated by commas."

    activity = "Complete the missing letters:\n\n"

    for number, word in enumerate(words, start=1):
        if len(word) < 2 or not word.isalpha():
            continue

        # Remove the middle letter to create a spelling exercise
        middle = len(word) // 2
        missing_word = word[:middle] + "_" + word[middle + 1:]

        activity += f"{number}. {missing_word}\n\n"

    return activity

# Create instructions for a reading activity
def generate_reading_prompt(topic, grade_level, activity_length):
    """Build a prompt for a grade-appropriate reading activity."""

    prompt = (
        f"Create a reading activity for a child in {grade_level}. "
        f"The topic is: {topic}. "
        f"The activity should take approximately {activity_length}. "
        "Write a short, age-appropriate reading passage using "
        "simple vocabulary suitable for the child's grade level. "
        "After the passage, include three reading comprehension "
        "questions about the story. "
        "Keep the activity educational, positive, and engaging."
    )

    return prompt



def generate_writing_prompt(topic, grade_level, activity_length):
    """Create an AI prompt for a grade-appropriate writing activity."""

    prompt = f"""
    Create a fun writing activity for a child in {grade_level}.

    Topic: {topic}
    Activity duration: {activity_length}

    Include:
    1. A creative title for the activity.
    2. A short explanation for the parent.
    3. Clear, simple instructions for the child.
    4. Three writing prompts or sentence starters.
    5. One optional creative challenge.
    6. Helpful tips for parents.

    Make the activity appropriate for the child's grade level.
    For younger children, allow drawing, tracing, or short sentences.
    For older children, encourage complete sentences and details.

    Keep the activity positive, engaging, and easy to do at home.
    """

    return prompt



def generate_explanation_prompt(topic, grade_level, activity_length):
    """Create a prompt to explain a concept to a child."""

    prompt = f"""
    Explain the following concept to a child in {grade_level}.

    Concept: {topic}
    Activity duration: {activity_length}

    Include:
    1. A simple, child-friendly explanation.
    2. An everyday example the child can understand.
    3. A fun analogy or comparison.
    4. Three questions to check understanding.
    5. A short hands-on activity parents can do at home.
    6. Helpful tips for parents.

    Use simple vocabulary appropriate for the child's grade level.
    Keep the explanation accurate, positive, and engaging.

    If the topic involves diagnosing a medical, learning, or
    developmental condition, do not provide a diagnosis.
    Recommend consulting a qualified professional instead.
    """

    return prompt



def check_safety(user_input):
    """Detect requests for diagnoses or medical advice."""

    text = user_input.lower()

    restricted_phrases = [
        "does my child have autism",
        "does my child have adhd",
        "diagnose my child",
        "does my child have dyslexia",
        "what medication",
        "what medicine should",
        "medical advice",
        "learning disability diagnosis",
    ]

    for phrase in restricted_phrases:
        if phrase in text:
            return (
                "I can't diagnose medical, learning, or developmental "
                "conditions or recommend medication. Please speak with "
                "your child's teacher, pediatrician, or a qualified "
                "professional for personalized guidance."
            )

    return None
