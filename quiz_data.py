import csv  # for reading the CSV file


def load_questions(filepath="questions.csv"):

    """
    Load questions from a CSV file and return a list of question dictionaries.
    The output depends on external state (the contents of questions.csv) — not pure.
    If the file changes, the function returns different results for the same input.
    """

    questions = []

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
 

    return questions