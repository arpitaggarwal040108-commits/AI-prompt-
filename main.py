
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

Your task is to create a clear, structured study roadmap for any topic provided by the user.

Follow this exact format:

==================================================
TOPIC: <TOPIC NAME>
==================================================

Goal
<One sentence explaining the learning objective>

Study Roadmap

1 <SUBTOPIC>
→ <ONE-LINE DESCRIPTION>

2 <SUBTOPIC>
→ <ONE-LINE DESCRIPTION>

3 <SUBTOPIC>
→ <ONE-LINE DESCRIPTION>

4 <SUBTOPIC>
→ <ONE-LINE DESCRIPTION>

5 <SUBTOPIC>
→ <ONE-LINE DESCRIPTION>

6 <SUBTOPIC>
→ <ONE-LINE DESCRIPTION>

Recommended Order
1 → 2 → 3 → 4 → 5 → 6

Practice Tasks
• <TASK 1>
• <TASK 2>
• <TASK 3>

Outcome
<One sentence describing what the learner will achieve>

Rules:
- Generate exactly 6 relevant subtopics.
- Arrange subtopics from beginner to advanced level.
- Keep descriptions concise.
- Include Goal, Study Roadmap, Recommended Order, Practice Tasks, and Outcome.
- Do not generate long paragraphs.
- Do not add markdown, code blocks, or extra headings.
"""

print("=" * 50)
print("AI POWERED STUDY ASSISTANT")
print("=" * 50)

topic = input("\nEnter a topic to study: ").strip()

if not topic:
    print("Topic cannot be empty.")
    exit()

questions_asked = 0

try:
    
    chat = client.chats.create(
        model="gemini-2.5-flash"
    )

    
    response = chat.send_message(
        f"{SYSTEM_PROMPT}\n\nCreate a study roadmap for: {topic}"
    )

    print("\n" + response.text)

except Exception as e:
    print(f"Error: {e}")
    exit()

print("\nAsk any follow-up question about the topic.")
print("Type 'quit' or 'exit' to end the session.\n")

while True:
    user_input = input("Ask a question: ").strip()

    if not user_input:
        continue

    if user_input.lower() in ["quit", "exit"]:
        break

    try:
        response = chat.send_message(user_input)

        print("\n" + response.text + "\n")

        questions_asked += 1

    except Exception as e:
        print(f"Error: {e}")

print("\n" + "=" * 50)
print("SESSION SUMMARY")
print("=" * 50)
print(f"Topic Studied   : {topic}")
print(f"Questions Asked : {questions_asked}")
print("=" * 50)
print("Thank you for using Study Assistant!")

