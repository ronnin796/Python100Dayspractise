import requests
import html


def get_data():
    response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
    data = response.json()
    question_data = data["results"]
    question_data = [
        {
            "question": html.unescape(question["question"]),
            "answer": question["correct_answer"],
        }
        for question in question_data
    ]
    return question_data
