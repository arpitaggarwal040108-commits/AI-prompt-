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

Your task is to create a clear, visually appealing, and structured study roadmap for any topic provided by the user.

Follow this exact format:

==================================================
TOPIC: <TOPIC NAME>

Goal
<One sentence explaining the overall learning objective>

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
<One sentence describing what the learner will be able to achieve>

Rules:

- Act as an expert study mentor and curriculum designer.
- Generate exactly 6 relevant subtopics.
- Arrange subtopics from beginner to advanced level.
- Keep each description under 15 words.
- Include Goal, Study Roadmap, Recommended Order, Practice Tasks, and Outcome sections.
- Ensure all subtopics are directly related to the user's topic.
- Keep the entire response concise and well-structured.
- Do not generate long paragraphs.
- Do not include explanations outside the specified format.
- Do not add markdown formatting, code blocks, or extra headings.
- Do not include unrelated topics or unnecessary details.
"""


chat_history = ""

print("=" * 50)
print("AI POWERED STUDY ASSISTANT")
print("=" * 50)

topic = input("\nEnter a topic to study: ").strip()

if not topic:
    print("Topic cannot be empty")
    exit()

questions_asked = 0

try:
    
    chat_history += f"""
    System Instructions:
    {SYSTEM_PROMPT}

    User:
    Create a study plan for {topic}
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=chat_history
    )

    print("\n")
    print(response.text)
    
    
    chat_history += f"\nASSISTANT: {response.text}\n"

except Exception as e:
    print(f"Error: {e}")
    exit()

print("\nYou can now ask follow-up questions.")
print("Type 'quit' or 'exit' to end.\n")

while True:

    user_input = input("Ask a question: ").strip()

    if not user_input:
        continue

    if user_input.lower() in ["quit", "exit"]:
        break

    try:
        
        chat_history += f"\nUSER: {user_input}\n"
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=chat_history
        )

        print("\n" + response.text + "\n")
        
       
        chat_history += f"\nAssistant:\n{response.text}\n"

        questions_asked += 1

    except Exception as e:
        print(f"Error: {e}")

print("\n" + "=" * 50)
print("SESSION SUMMARY")
print("=" * 50)
print(f"Topic Studied : {topic}")
print(f"Questions Asked : {questions_asked}")
print("Thank you for using Study Assistant!")