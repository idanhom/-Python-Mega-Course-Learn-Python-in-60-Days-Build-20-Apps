import json

# Correct filename (assuming it's a JSON file)
with open('bonus15_list.json', 'r') as file:
    data = json.load(file)  # Directly loading JSON into Python objects

score = 0  # Initialize score outside loop

# Iterate over each question and handle user interaction
for question in data:
    print(question["question_text"])

    # Enumerate alternatives starting from 1
    for idx, alternative in enumerate(question["alternatives"], 1):
        print(f"{idx}. {alternative}")

    # Prompt user for their choice
    user_choice = int(input("Enter your answer (number): "))

    # Store user's choice in the dictionary for later comparison
    question["user_choice"] = user_choice

# Evaluate the user's choices and display results
print("\nQuiz Results:")
for index, question in enumerate(data, 1):
    correct = question["correct_answer"]
    user_answer = question["user_choice"]

    # Increment score if user's choice matches the correct answer
    if user_answer == correct:
        score += 1
        result = "Correct"
    else:
        result = "Wrong"

    # Display individual question result clearly
    print(f"Question {index}: {result} (Your answer: {user_answer}, Correct: {correct})")

# Display final score
print(f"\nYour total score: {score}/{len(data)}")
