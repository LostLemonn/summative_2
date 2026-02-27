import csv  # for reading the CSV file
import os  # for correct file path

def load_questions(filepath=None):

    """
    Load questions from a CSV file and return a list of question dictionaries.
    The output depends on external state (the contents of questions.csv) — not pure.
    If the file changes, the function returns different results for the same input.
    """

    if filepath is None:
        filepath = os.path.join(os.path.dirname(__file__), "questions.csv")

    questions = []

    try:
        with open(filepath, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                questions.append({
                    "question": row["question"],
                    "options": [
                        row["option_a"],
                        row["option_b"],
                        row["option_c"],
                        row["option_d"],
                    ],
                    "correct": int(row["correct"]) - 1
                })
    except FileNotFoundError:
        print(f"Error: could not find '{filepath}'. Make sure questions.csv is in the same folder as main.py.")

    return questions