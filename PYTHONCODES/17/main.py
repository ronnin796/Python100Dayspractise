import random as rd
from data import question_data
from question_model import Question
from quiz_brain import Quiz_Brain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = question_bank.append(Question(question_text, question_answer))
no_of_questions = len(question_bank)
score = 0
quiz = Quiz_Brain(question_bank)
while quiz.questions_left():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{no_of_questions}")
