from question_model import Question
from quiz_brain import QuizBrain
import requests
import json
from art import logo

response_API = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")
data = response_API.text
parse_json = json.loads(data)

question_bank = []
for question in parse_json["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

print(logo)
print("Welcome to the quiz! There are 10 questions. Good luck!")
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
