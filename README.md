# AI-Powered Study Assistant CLI

## Overview

AI-Powered Study Assistant is a command-line application built using the Gemini API. The application generates a structured study roadmap for any topic and allows users to ask follow-up questions while maintaining conversation context.

## Features

* Generate study roadmaps for any topic
* Interactive question-answering session
* Context-aware conversations
* Session summary on exit
* Secure API key management using `.env`

## Technologies Used

* Python
* Gemini API
* google-generativeai
* python-dotenv

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

3. Run the program:

```bash
python study_assistant.py
```

---

# Prompt Engineering Questions

## 1. What role did you assign in your system prompt and why?

I assigned the role of **Expert Study Mentor and Curriculum Designer**. This helps the model generate structured learning paths and educational responses instead of generic answers.

## 2. What format did you specify and how did you enforce it?

I instructed the model to generate a study roadmap with ordered learning steps and short descriptions. The format was enforced by explicitly defining the structure and rules in the system prompt.

## 3. What happens if you remove the system prompt entirely?

Without the system prompt, responses become less consistent. The study plans may vary in structure, include unnecessary information, and follow no fixed format.

---

## Conclusion

This project demonstrates the use of Prompt Engineering techniques such as role prompting, format control, response constraints, and conversational context management using the Gemini API.
