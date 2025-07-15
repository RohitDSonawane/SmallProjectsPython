import random

# List of questions with options and correct answer
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who wrote the national anthem of India?",
        "options": ["A. Rabindranath Tagore", "B. Mahatma Gandhi", "C. Subhash Chandra Bose", "D. Jawaharlal Nehru"],
        "answer": "A"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Pacific", "C. Indian", "D. Arctic"],
        "answer": "B"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["A. 90", "B. 80", "C. 100", "D. 120"],
        "answer": "C"
    }
]

# Shuffle questions
random.shuffle(questions)

# Prize money list
prizes = ["₹1,000", "₹5,000", "₹10,000", "₹50,000", "₹1,00,000"]

# Lifeline usage tracker
lifeline_used = False

# Game loop
for i, q in enumerate(questions):
    print(f"\nQuestion {i+1} for {prizes[i]}")
    print(q["question"])
    for opt in q["options"]:
        print(opt)

    if not lifeline_used:
        use_lifeline = input("Do you want to use 50-50 lifeline? (yes/no): ").lower()
        if use_lifeline == "yes":
            lifeline_used = True
            correct = q["answer"]
            options = ["A", "B", "C", "D"]
            options.remove(correct)
            removed = random.sample(options, 2)
            print("After 50-50 lifeline, the remaining options are:")
            for opt in q["options"]:
                if opt[0] == correct or opt[0] not in removed:
                    print(opt)

    ans = input("Your answer (A/B/C/D): ").upper()
    if ans == q["answer"]:
        print(f"✅ Correct! You've won {prizes[i]}")
    else:
        print("❌ Wrong answer!")
        print(f"The correct answer was: {q['answer']}")
        print("Game Over. Thanks for playing!")
        break
else:
    print("\n🎉 Congratulations! You've answered all questions correctly and won ₹1,00,000!")
