# Import the tkinter module for creating the GUI
import tkinter as tk
# Import the random module to randomly select questions
import random

# List of questions and choices, each tuple contains a question, a list of choices, and the correct answer
questions = [
    ("What is the capital of France?", ["Paris", "Berlin", "Madrid", "Rome"], "Paris"),
    ("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
    ("What color is the sky?", ["Blue", "Green", "Red", "Yellow"], "Blue"),
    ("Who is the Founder of ICCT Colleges Foundation Inc?", ["Dr. William S. Co.", "Ranielle Lopez", "Jake Acang", "Kyle Tan"], "Dr. William S. Co."),
    ("What is the first campus in ICCT?", ["San Mateo", "Sumulong", "Cainta", "Binangonan"], "Cainta")
    # Add more questions as needed
]

# Define a class to create and manage the quiz application
class QuizGenerator:
    def __init__(self, root):
        # Initialize the root window and set its title
        self.root = root
        self.root.title("Random Quiz Generator")

        # Create a label to display the question and pack it into the window with padding
        self.question_label = tk.Label(root, text="", font=("Comic Sans", 16))
        self.question_label.pack(pady=20)

        # Create a label to display feedback messages and pack it into the window with padding
        self.feedback_label = tk.Label(root, text="", font=("Comic Sans", 14), fg="red")
        self.feedback_label.pack(pady=10)

        # Set the size and properties of the GUI window
        self.root.geometry("600x500")  # Set the window width and height
        self.root.resizable(False, False)  # Make the window non-resizable
        self.root.config(bg="black")  # Set the background color to black

        # List to hold the answer buttons
        self.buttons = []
        for i in range(4):  # Create 4 buttons for the answer choices
            button = tk.Button(root, text="", font=("Comic Sans", 14), command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)  # Pack each button into the window with padding
            self.buttons.append(button)  # Add each button to the list

        # Create a button to generate a new question and pack it into the window with padding
        self.new_question_button = tk.Button(root, text="New Question", command=self.new_question)
        self.new_question_button.pack(pady=20)

        # Generate the first question when the application starts
        self.new_question()

    def new_question(self):
        # Select a random question, choices, and the correct answer from the list of questions
        self.current_question, self.current_choices, self.correct_answer = random.choice(questions)
        # Update the question label with the new question
        self.question_label.config(text=self.current_question)
        # Update each button with the new choices
        for i, choice in enumerate(self.current_choices):
            self.buttons[i].config(text=choice)
        # Clear the feedback message and set it to "Choices"
        self.feedback_label.config(text="Choices")

    def check_answer(self, i):
        # Get the text of the button that was clicked
        selected_answer = self.buttons[i].cget("text")
        # Check if the selected answer is correct
        if selected_answer == self.correct_answer:
            # If correct, update the feedback label to indicate a correct answer
            self.feedback_label.config(text="Correct!", fg="blue")
        else:
            # If incorrect, update the feedback label to indicate the correct answer
            self.feedback_label.config(text=f"Incorrect! The correct answer is {self.correct_answer}.", fg="red")

# Main part of the program to start the application
if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    # Create an instance of the QuizGenerator class
    app = QuizGenerator(root)
    # Start the tkinter event loop
   



