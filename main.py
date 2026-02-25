import tkinter as tk  # tkinter will be used to create our GUI
import csv  # will write results to csv
from tkinter import messagebox # displays a message window
from quiz_data import load_questions  # to load our questions from 
from quiz_utils import clean_name, character_check, length_check, presence_check  # to check for validation criteria
from datetime import datetime  # used to record a timestamp


BG = "#f5f5f5"
HEADER_BG = "#cc0000"
HEADER_FG = "#ffffff"
TEXT = "#1a1a1a"
BUTTON_BG = "#cc0000"
BUTTON_FG = "#ffffff"
ACCENT = "#cc0000"

questions = load_questions()

class QuizzApp(tk.Tk):

    """
    A class which represents my quiz application
    """

    def __init__(self, questions):
        super().__init__()
        self.title("Hitachi Rail Safety Quiz")
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.configure(bg=BG)
        self.geometry("680x900")
        self.name = tk.StringVar()
        self.answer_var = tk.IntVar(value=-1)
        self.answer_vars = []

        self.header_label = tk.Label(
            self,
            text="Hitachi Rail Safety Quiz",
            bg=HEADER_BG,
            fg=HEADER_FG,
            font=("Arial", 18, "bold"),
        )
        self.header_label.pack(fill="x", pady=0, ipady=18)

        self.name_label = tk.Label(
            self,
            text="Enter your full name please:",
            bg=BG,
            fg=TEXT,
            font=("Arial", 15),
        )
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(
            self,
            textvariable=self.name,
            font=("Arial", 14),
            fg=TEXT,
            relief="solid",
            bd=1
        )
        self.name_entry.pack(pady=6, padx=40, fill="x")

        self.build_question_screen()

        self.submit_button = tk.Button(
            self,
            text="Submit😊",
            font=("Arial", 15, "bold"),
            fg=BUTTON_FG,
            bg=BUTTON_BG,
            activebackground="#a80000",
            activeforeground="#ffffff",
            relief="flat",
            padx=20,
            pady=10,
            command=self.handle_submit
        )
        self.submit_button.pack(pady=16)

    def build_question_screen(self):

            """
            Will build the question section of the quiz
            """

            question_number = 1

            for question in self.questions:
                q_label = tk.Label(
                    self,
                    text=f"Question {question_number}. {question['question']}",
                    font=("Arial", 13, "bold"),
                    wraplength=560,
                    justify="left",
                    bg=BG,
                    fg=ACCENT,
                    anchor="w"
                )
                q_label.pack(anchor="w", padx=40, pady=(18, 4))

                answer_var = tk.IntVar(value=-1)
                self.answer_vars.append(answer_var)

                option_value = 0
                for option in question["options"]:
                    rb = tk.Radiobutton(
                    self,
                    text=option,
                    variable=answer_var,
                    value=option_value,
                    font=("Arial", 12),
                    bg=BG,
                    fg=TEXT,
                    activebackground=BG,
                    selectcolor=BG,
                    anchor="w"
                    )
                    rb.pack(anchor="w", padx=70)
                    option_value += 1

                question_number += 1

    def handle_submit(self):

        """
        Saves the name, answer, and timestamp of the user 
        to a CSV file when the submit button is pressed
        """

        st_name = clean_name(self.name_entry.get())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if self.validate_name_with_messages(st_name):

            answers = []
            for var in self.answer_vars:
                answers.append(var.get())

            with open("user_records.csv", mode="a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow([st_name, timestamp, answers])
           
            self.build_thank_you_screen(st_name)

    def build_thank_you_screen(self, name):

        """
        Displays confirmation screen after a valid submission attempt
        """

        self.clear_screen()

        tk.Label(
            self,
            text="Hitachi Rail Safety Quiz",
            bg=HEADER_BG,
            fg=HEADER_FG,
            font=("Arial", 18, "bold"),
        ).pack(fill="x", ipady=18)

        tk.Label(
            self,
            text="Your answers have been submitted!",
            font=("Arial", 18, "bold"),
            bg=BG,
            fg="#007a33"
        ).pack(pady=40)

        tk.Label(
            self,
            text=(
                f"Thank you, {name}.\n\n 😊"
                "Your responses have been recorded.\n"
                "A member of the team\n"
                "will be in touch with your results."
            ),
            font=("Arial", 14),
            wraplength=500,
            justify="center",
            bg=BG,
            fg=TEXT
        ).pack(pady=10)

        tk.Button(
            self,
            text="QUIT",
            font=("Arial", 14, "bold"),
            fg=BUTTON_FG,
            bg=BUTTON_BG,
            activebackground="#a80000",
            activeforeground="#ffffff",
            relief="flat",
            padx=20,
            pady=10,
            command=self.destroy
        ).pack(pady=40)

    def validate_name_with_messages(self, cleaned_name: str) -> bool:

        """
        Validates the cleaned name and shows an error message if invalid.
        Returns True if the name is valid.
        """

        valid = True

        if not presence_check(cleaned_name):
            messagebox.showerror(
                "Invalid name",
                "Please enter your name."
            )
            valid = False

        if valid and not length_check(cleaned_name):
            messagebox.showerror(
                "Invalid name",
                "Name must be between 2 and 50 characters."
            )
            valid = False

        if valid and not character_check(cleaned_name):
            messagebox.showerror(
                "Invalid name",
                "Names must only contain letters, spaces, hyphens, or apostrophes."
            )
            valid = False

        return valid

    def clear_screen(self):

        """Removes all widgets from the window."""

        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = QuizzApp(questions)
    app.mainloop()
            