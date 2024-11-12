import time

def quiz_game():
    # List of questions, options, and correct answers
    questions = [
        {
            "question": "Which language is known as the 'language of the web'?",
            "options": ["1. Java", "2. C++", "3. Python", "4. JavaScript"],
            "answer": "4"
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "options": ["1. James Cameron", "2. Christopher Nolan", "3. Steven Spielberg", "4. Martin Scorsese"],
            "answer": "2"
        },
        {
            "question": "What does the acronym 'CPU' stand for?",
            "options": ["1. Central Processing Unit", "2. Central Programming Unit", "3. Control Processing Unit", "4. Computer Personal Unit"],
            "answer": "1"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["1. Venus", "2. Earth", "3. Mars", "4. Jupiter"],
            "answer": "3"
        },
        {
            "question": "What year did the Titanic sink?",
            "options": ["1. 1905", "2. 1912", "3. 1923", "4. 1945"],
            "answer": "2"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["1. Vincent van Gogh", "2. Pablo Picasso", "3. Leonardo da Vinci", "4. Claude Monet"],
            "answer": "3"
        },
        {
            "question": "What is the capital of Japan?",
            "options": ["1. Tokyo", "2. Seoul", "3. Beijing", "4. Bangkok"],
            "answer": "1"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["1. Gold", "2. Oxygen", "3. Osmium", "4. Opium"],
            "answer": "2"
        },
        {
            "question": "What is the largest mammal on Earth?",
            "options": ["1. Elephant", "2. Giraffe", "3. Blue Whale", "4. Great White Shark"],
            "answer": "3"
        },
        {
            "question": "Who wrote 'Harry Potter'?",
            "options": ["1. J.R.R. Tolkien", "2. C.S. Lewis", "3. George R.R. Martin", "4. J.K. Rowling"],
            "answer": "4"
        }
    ]

    # Start the game
    print("Welcome to the Simple Quiz Game 🎮!")
    time.sleep(1)

    # Main quiz loop
    while True:
        score = 0  # Initialize score for each game

        # Loop through each question
        for q in questions:
            print("\n" + q["question"])
            for option in q["options"]:
                print(option)

            # Get user's answer
            answer = input("Your answer (enter the number): ")
            if answer == q["answer"]:
                print("Correct! 🎉")
                score += 1
            else:
                print("Oops, that's incorrect!")

        # Display the score
        print(f"\nYour score: {score}/{len(questions)}")
        if score == len(questions):
            print("🏆 Excellent! You got a perfect score!")
        elif score > len(questions) // 2:
            print("🎉 Good job! You scored above average.")
        else:
            print("Better luck next time!")

        # Ask if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Run the quiz game
quiz_game()
