# AI-Powered Study Assistant 

## 📘 Overview

**AI-Powered Study Assistant CLI** is a command-line application powered by the **Gemini API** that helps students learn any subject through structured study roadmaps and interactive conversations.

It uses **prompt engineering techniques** to generate organized learning paths, explain concepts clearly, and maintain contextual learning during follow-up questions.

---

##  Features
### How it works
```text
User enters a study topic
        ↓
Gemini generates roadmap
        ↓
User asks questions
        ↓
Conversation context maintained
        ↓
Session summary displayed
```

###  Topic-Based Study Roadmap
- Accepts any study topic from the user  
- Generates a structured learning roadmap  
- Organizes subtopics in a logical learning sequence  
- Provides clear and concise explanations  

###  Interactive Learning Session
- Ask follow-up questions anytime  
- Maintains conversation context  
- Supports continuous concept clarification  

###  Engineered System Prompt
- Acts as an Expert Study Mentor & Curriculum Designer  
- Enforces consistent response formatting  
- Controls output structure and clarity  
- Improves response quality using prompt engineering  
## Example-1
<img width="638" height="852" alt="image" src="https://github.com/user-attachments/assets/1659cc5b-5a71-4c85-ace7-3736630b1eee" />

<img width="630" height="853" alt="image" src="https://github.com/user-attachments/assets/cb4e8c71-afb5-4941-a65d-98167d4e17b0" />

---

## Example-2

<img width="627" height="833" alt="image" src="https://github.com/user-attachments/assets/4084f2e4-8c12-4daf-a113-8c71e0fa4620" />
<img width="615" height="618" alt="image" src="https://github.com/user-attachments/assets/afb7dba2-7c92-4772-a0df-db6d11e48c6e" />

###  Session Summary
- Exit using `quit` or `exit`  
- Displays:
  - Studied topic  
  - Total questions asked  

---

##  Technologies Used
- Python 3  
- Gemini API (`gemini-2.0-flash`)  
- Google GenAI SDK (`google-genai`)  
- Python Dotenv (`python-dotenv`)  

---

##  Installation

### Clone the Repository
```bash
git clone <your-github-repository-url>
cd AI-Study-Assistant


## Prompt Engineering Write-Up

### 1. What role did you assign in your system prompt, and why did you choose that framing?

I assigned the role of **Expert Study Mentor and Curriculum Designer**. This role helps the model behave like an educator who can organize learning material into a logical sequence. It improves the quality, structure, and educational value of the generated study roadmap.

### 2. What format did you specify for the study plan output, and how did you enforce it in the prompt?

I specified a fixed structure containing a **Goal**, **Study Roadmap**, **Recommended Order**, **Practice Tasks**, and **Outcome** section. The format was enforced by providing an exact template, limiting the number of subtopics to six, requiring short descriptions, and including explicit rules on what the model should and should not generate.

### 3. What happens if you remove the system prompt entirely — how does the output change?

Without the system prompt, the model still generates information about the topic, but the format becomes inconsistent and less organized. The response may contain long explanations, different section layouts, or missing elements such as recommended order and practice tasks, making the study plan less structured and predictable.
