import pandas as pd

student_data = {
    "name": [
        "Ava",
        "Liam",
        "Sophia",
        "Noah",
        "Ethan",
        "Isabella",
        "Benjamin",
        "Charlotte",
        "Alexander",
        "Mia",
    ],
    "score": [85, 92, 78, 88, 90, 95, 81, 89, 94, 76],
}

student_data = pd.DataFrame(student_data)
print(student_data)
# loop through dataframe

for index, row in student_data.iterrows():
    print(row["name"])
