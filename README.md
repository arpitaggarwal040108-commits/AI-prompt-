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
## Sample Output

```text
==================================================
AI POWERED STUDY ASSISTANT
==================================================

Enter a topic to study: Data Structures

==================================================
TOPIC: DATA STRUCTURES
==================================================

Goal
Learn fundamental data structures and their applications.

Study Roadmap

1 Arrays
→ Store elements efficiently in contiguous memory.

2 Linked Lists
→ Learn dynamic memory allocation concepts.

3 Stacks
→ Understand LIFO data organization.

4 Queues
→ Understand FIFO data organization.

5 Trees
→ Learn hierarchical data structures.

6 Graphs
→ Represent complex relationships.

Recommended Order
1 → 2 → 3 → 4 → 5 → 6

Practice Tasks
• Implement a stack
• Build a linked list
• Solve traversal problems

Outcome
Ability to select and use appropriate data structures.

Ask any follow-up question about the topic.
Type 'quit' or 'exit' to end the session.

Ask a question: What is the difference between a stack and a queue?

A stack follows Last In First Out (LIFO), while a queue follows
First In First Out (FIFO). Stacks use push/pop operations,
whereas queues use enqueue/dequeue operations.

Ask a question: exit

==================================================
SESSION SUMMARY
==================================================
Topic Studied    : Data Structures
Questions Asked  : 1
==================================================
Thank you for using Study Assistant!
```

---

## Example-2
```text
==================================================
AI POWERED STUDY ASSISTANT
==================================================

Enter a topic to study: Complex Analysis

==================================================
TOPIC: COMPLEX ANALYSIS
==================================================

Goal
Develop a strong understanding of functions of complex variables.

Study Roadmap

1 Complex Numbers
→ Learn algebraic and geometric representations.

2 Complex Functions
→ Understand mappings and function properties.

3 Analytic Functions
→ Study differentiability in the complex plane.

4 Cauchy's Theorem
→ Explore fundamental integral results.

5 Taylor and Laurent Series
→ Represent functions using power series.

6 Residue Theory
→ Evaluate complex integrals efficiently.

Recommended Order
1 → 2 → 3 → 4 → 5 → 6

Practice Tasks
• Convert complex numbers between forms.
• Verify whether functions are analytic.
• Solve contour integration problems.

Outcome
Ability to analyze complex functions and solve advanced integration problems.

Ask any follow-up question about the topic.
Type 'quit' or 'exit' to end the session.

Ask a question: What is an analytic function?

An analytic function is a complex function that is differentiable
at every point in an open region of the complex plane. Such functions
satisfy the Cauchy-Riemann equations and possess many useful properties.

Ask a question: Why is Cauchy's Theorem important?

Cauchy's Theorem states that the integral of an analytic function
around a closed contour is zero under suitable conditions. It forms
the foundation of many results in complex analysis.

Ask a question: exit

==================================================
SESSION SUMMARY
==================================================
Topic Studied   : Complex Analysis
Questions Asked : 2
==================================================
Thank you for using Study Assistant!
```
---

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
