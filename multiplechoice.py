def run(questions):
    score = 0
    for Q uestion in questions:
        answer = input(Question.prompt)
        if answer == Question.answer:
            score = score + 1
    print("Congratulations! Your score is " + str(score) + "/" + str(len(questions)))

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questionprompt = [
    "Which of these countries were nuetral in WWII?\n(A) Britian\n(B) Japan\n(C) Switzerland\n\n",
    "What is 11x19?\n(A) 121\n(B) 122\n(C) 209\n\n",
    "What color is grass?\n(A) Green\n(B) Yellow\n(C) Orange\n\n"
]
questions = [
    Question(questionprompt[0], "C".lower()),
    Question(questionprompt[1], "C".lower()),
    Question(questionprompt[2], "A".lower())
]

run(questions)