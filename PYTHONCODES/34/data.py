import requests


def get_data():
    response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
    print(response.status_code)
    data = response.json()
    question_data = data["results"]
    print(question_data)
    question_data = [
        {"question": question["question"], "answer": question["correct_answer"]}
        for question in question_data
    ]
    return question_data
