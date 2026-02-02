class Quiz_Brain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.no_of_questions = len(self.question_list)
        self.score = 0

    def questions_left(self):
        return self.question_number < self.no_of_questions

    def next_question(self):
        current_question_number = self.question_number
        current_question = self.question_list[current_question_number]
        self.question_number += 1
        ans = input(
            f"Q{current_question_number+1}. {current_question.text} (True/False): "
        ).lower()
        if ans == current_question.answer.lower():
            print("Correct!. The answer was ", current_question.answer, ".")
            self.score += 1
        else:
            print("You are wrong. The answer was ", current_question.answer, ".")
        print("Current score: ", self.score, "/", self.question_number)
