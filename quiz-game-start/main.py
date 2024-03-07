from question_model import Question
from data import question_data, trivia_data
from quiz_brain import QuizBrain

question_bank = []
difficulty = input("Choose difficulty. (One|Two):").lower()
if difficulty == "one":
    for question in question_data:
        new_q = Question(question["text"], question["answer"])
        question_bank.append(new_q)
elif difficulty == "two":
    for question in trivia_data:
        new_q = Question(question["question"], question["correct_answer"])
        question_bank.append(new_q)
else:
    print("Choose proper difficulty.")

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

quiz.pass_or_fail()
