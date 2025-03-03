import tkinter as tk
import random

# List of questions and choices, each tuple contains a question and its choices
questions = [
    ("What is the capital of France?", ["Paris", "Berlin", "Madrid", "Rome"], "Paris"),
    ("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
    ("What color is the sky?", ["Blue", "Green", "Red", "Yellow"], "Blue"),
    ("Who is the Founder of ICCT Colleges Foundation Inc?", ["Dr. William S. Co.", "Ranielle_Lopez", "Jake_Acang", "Kyle_tan"], "Dr._William_S._Co."),
    ("What is the first campus in ICCT?", ["San Mateo", "Sumulong", "Cainta", "Binangonan"], "Cainta")
    # Add more questions as needed
]

class QuizGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Quiz Generator")  # Set the window title

        # Create a label to display the question
        self.question_label = tk.Label(root, text="", font=("Comic Sans", 16))
        self.question_label.pack(pady=20)

        # Create a label to display feedback messages
        self.feedback_label = tk.Label(root, text="", font=("Comic Sans", 14), fg="red")
        self.feedback_label.pack(pady=10)

        # set the property of the gui window
        self.root.geometry("600x500") #set the window height and width (width, height)
        self.root.resizable(False,False) #set the window unresizeable
        self.root.config(bg="black")

        # List to hold the answer buttons
        self.buttons = []
        for i in range(4):  # Create 4 buttons for the choices
            button = tk.Button(root, text="", font=("Comic Sans", 14), command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.buttons.append(button)

        # Button to generate a new question
        self.new_question_button = tk.Button(root, text="New Question", command=self.new_question)
        self.new_question_button.pack(pady=20)

        self.new_question()  # Generate the first question when the app starts

    def new_question(self):
        # Select a random question and its choices
        self.current_question, self.current_choices, self.correct_answer = random.choice(questions)
        self.question_label.config(text=self.current_question)  # Update the label with the new question
        for i, choice in enumerate(self.current_choices):  # Update the buttons with the new choices
            self.buttons[i].config(text=choice)
        self.feedback_label.config(text="Choices")  # Clear feedback message

    def check_answer(self, i):
        selected_answer = self.buttons[i].cget("text")
        if selected_answer == self.correct_answer:
            self.feedback_label.config(text="Correct!", fg="blue")
        else:
            self.feedback_label.config(text=f"Incorrect! The correct answer is {self.correct_answer}.", fg="red")

# Main part of the program
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGenerator(root)
    root.mainloop()
