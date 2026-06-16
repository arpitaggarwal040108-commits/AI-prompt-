import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("ERROR: GEMINI_API_KEY not found in .env file")
    exit()

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
You are an Expert Study Mentor and Curriculum Designer.

When the user provides a topic, generate a study roadmap.

Output format:

==================================================
STUDY ROADMAP : <TOPIC>
==================================================

STEP 1 : <SUBTOPIC>
Purpose : <ONE LINE DESCRIPTION>

STEP 2 : <SUBTOPIC>
Purpose : <ONE LINE DESCRIPTION>

STEP 3 : <SUBTOPIC>
Purpose : <ONE LINE DESCRIPTION>

STEP 4 : <SUBTOPIC>
Purpose : <ONE LINE DESCRIPTION>

STEP 5 : <SUBTOPIC>
Purpose : <ONE LINE DESCRIPTION>

==================================================
Recommended Order : 1 → 2 → 3 → 4 → 5
==================================================

Rules:
- Keep descriptions under 20 words.
- Follow the exact format.
- Maintain logical learning order.
- Do not provide unrelated information.
- Do not generate long paragraphs.
"""

# Initialize chat history for context management
chat_history = []

print("=" * 50)
print("AI POWERED STUDY ASSISTANT")
print("=" * 50)

topic = input("\nEnter a topic to study: ").strip()

questions_asked = 0

try:
    # Add system prompt and user message to history
    chat_history.append({
        "role": "user",
        "parts": [f"System Instructions: {SYSTEM_PROMPT}\n\nCreate a study plan for {topic}"]
    })
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=chat_history
    )

    print("\n")
    print(response.text)
    
    # Add assistant response to history
    chat_history.append({
        "role": "model",
        "parts": [response.text]
    })

except Exception as e:
    print(f"Error: {e}")
    exit()

print("\nYou can now ask follow-up questions.")
print("Type 'quit' or 'exit' to end.\n")

while True:

    user_input = input("Ask a question: ").strip()

    if user_input.lower() in ["quit", "exit"]:
        break

    try:
        # Add user question to history
        chat_history.append({
            "role": "user",
            "parts": [user_input]
        })
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=chat_history
        )

        print("\n" + response.text + "\n")
        
        # Add assistant response to history
        chat_history.append({
            "role": "model",
            "parts": [response.text]
        })

        questions_asked += 1

    except Exception as e:
        print(f"Error: {e}")

print("\n" + "=" * 50)
print("SESSION SUMMARY")
print("=" * 50)
print(f"Topic Studied : {topic}")
print(f"Questions Asked : {questions_asked}")
print("Thank you for using Study Assistant!")