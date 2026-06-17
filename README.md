# AI-Powered Study Assistant CLI

## Overview

**AI-Powered Study Assistant CLI** is a command-line application powered by the **Gemini API** that helps students learn any subject through structured study roadmaps and interactive conversations.

The application uses **prompt engineering techniques** to generate organized learning paths, explain concepts clearly, and answer follow-up questions while maintaining conversational context.

---

## Features

### Topic-Based Study Roadmap

* Accepts any study topic from the user.
* Generates a structured learning roadmap.
* Organizes subtopics in a recommended learning sequence.
* Provides concise explanations for each topic.

### Interactive Learning Session

* Ask follow-up questions about any topic.
* Maintains conversation context throughout the session.
* Supports continuous learning and concept clarification.

### Engineered System Prompt

* Assigns the AI the role of an Expert Study Mentor and Curriculum Designer.
* Enforces a consistent roadmap format.
* Controls response structure and length.
* Improves output quality through explicit instructions and constraints.

### Session Summary

* End the session using `quit` or `exit`.
* Displays:

  * Studied topic
  * Total questions asked during the session

---

## Technologies Used

* Python 3
* Gemini API (`gemini-2.0-flash`)
* Google GenAI SDK (`google-genai`)
* Python Dotenv (`python-dotenv`)

---

## Installation

### Clone the Repository

```bash
git clone <your-github-repository-url>
cd AI-Study-Assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Application

```bash
python main.py
```

---

## Project Structure

```text
AI-Study-Assistant/
│
├── main.py
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```
![alt text](image.png)
![alt text](image-1.png)
---

## Learning Workflow

1. Enter a study topic.
2. Receive a structured learning roadmap.
3. Explore subtopics in sequence.
4. Ask follow-up questions for deeper understanding.
5. Continue learning interactively.
6. Exit anytime and view the session summary.

---

## Author

**Arpit Aggarwal**

FORGETRACK 2026 – Week 03 Tech Track
