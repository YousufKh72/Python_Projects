class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.question} (True/False)?: ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")

    def pass_or_fail(self):
        print("You have completed the quiz. 🎉")
        print(f"Your final score is: {self.score}/{self.question_number}.")
        if self.score >= 9:
            print("😍😁!You passed!😁😍")
        else:
            print("😂😂!You failed!😂😂")
