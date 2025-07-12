questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. HTML", "B. Python", "C. Java", "D. C"],
        "answer": "A"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Program Unit", "B. Central Processing Unit", "C. Control Processing Unit", "D. Computer Power Unit"],
        "answer": "B"
    },
    {
        "question": "Which is a Python data type?",
        "options": ["A. tree", "B. loop", "C. list", "D. html"],
        "answer": "C"
    },
    {
        "question": "Which company created Android?",
        "options": ["A. Apple", "B. Google", "C. Microsoft", "D. Amazon"],
        "answer": "B"
    }
]

score = 0

print("Welcome to the Quiz!\n")

for i, q in enumerate(questions):
    print(f"Q{i+1}: {q['question']}")
    for opt in q['options']:
        print(opt)
    user_ans = input("Your answer (A/B/C/D): ").upper()
    
    if user_ans == q['answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['answer']}\n")

print(f"Quiz Over! You got {score} out of {len(questions)} correct.")
