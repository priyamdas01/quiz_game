class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) != self.question_number

    def check_answer(self, user_ans, ques_ans):
        if user_ans.lower() == ques_ans.lower():
            print("you got it right")
            self.score += 1
        else:
            print("Sorry that was incorrect")
        print(f"The correct ans was {ques_ans}")
        print(f"Your current score is {self.score}/{self.question_number+1}")
        print("\n\n")

    def next_question(self):
        question = self.question_list[self.question_number].text
        answer = input(f"Q.{self.question_number + 1} {question} (True/False)?: ")
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1
