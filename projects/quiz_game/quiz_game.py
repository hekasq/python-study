class Quiz_Game:
    score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.get_question()}(True/False)")
        self.check_answer(answer, question.get_answer())


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

        # return {"number": self.question_number, "question": question.get_question(), "answer": question.get_answer()}


    def check_answer(self, input, answer):
        if input.lower() == answer.lower():
            self.score += 1
            print("Correct")

        else:
            print("You got it wrong")
            print("Correct answer:", answer)
        print("Total score" + str(self.score) + "/" + str(self.question_number))

    def __init__(self, question_bank):
        self.question_list = question_bank
        self.question_number = 0
