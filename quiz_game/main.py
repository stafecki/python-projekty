def AnswerInput():
    while True:
        guess = input().upper()
        if guess in ("A", "B", "C", "D"):
            return guess
        else:
            print("Please enter a valid answer: ", end="")

questions = ("How many elements are in periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's athmosphere?: ",
             "How many bones are in human body?: ",
             "Which planet is Solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
q_number = 0

for question in questions:
    print(f"\nQuestion number {q_number+1}: {question}")
    for option in options[q_number]:
        print(f"\t{option}")
    print("Your answer: ", end="")
    guesses.append(AnswerInput())
    if guesses[q_number] == answers[q_number]:
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
        print(f"Correct answer is: {answers[q_number]}")
    q_number += 1

print(f"Your score: {score}")