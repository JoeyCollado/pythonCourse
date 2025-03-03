import tkinter as tk
from PIL import Image, ImageTk
import random

# List of questions and choices
questions = [
    ("What does CPU stand for?", ["Central Processing Unit", "Central Program Unit", "Control Processing Unit", "Central Performance Unit"], "Central Processing Unit"),
    ("What is the main function of an operating system?", ["Manage hardware and software resources", "Run applications", "Browse the internet", "Process data"], "Manage hardware and software resources"),
    ("What does RAM stand for?", ["Random Access Memory", "Read Access Memory", "Run Access Memory", "Random Application Memory"], "Random Access Memory"),
    # Add other questions similarly...
]

class QuizGenerator:
    def __init__(self, window):
        self.window = window  # Store the reference to the main window
        self.window.title("Random Quiz Generator")  # Set the title of the window

        # Load and set the second background image to fill the entire window
        self.bg_image2 = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop\\school.png")
        self.bg_image2 = self.bg_image2.resize((800, 600), Image.LANCZOS)  # Resize the image to fit the window
        self.bg_image2 = ImageTk.PhotoImage(self.bg_image2)  # Convert the image for Tkinter

        # Load and set the first image to be centered
        self.bg_image1 = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop\\logo1.png")
        self.bg_image1 = self.bg_image1.resize((200, 200), Image.LANCZOS)  # Resize the image
        self.bg_image1 = ImageTk.PhotoImage(self.bg_image1)  # Convert the image for Tkinter

        # Start screen with a Start button
        self.start_frame = tk.Frame(window)  # Create a frame for the start screen
        self.start_frame.pack(fill="both", expand=True)  # Pack the frame to fill the window
        self.canvas = tk.Canvas(self.start_frame, width=800, height=600)  # Create a canvas
        self.canvas.pack(fill="both", expand=True)  # Pack the canvas to fill the frame

        # Add the background image to the canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image2)  # Add the image to the canvas

        # Calculate the center position for the first image
        center_x = 400  # width is 800
        center_y = 250  # height is 600

        # Add the first image to the center of the canvas
        self.canvas.create_image(center_x, center_y - 100, anchor="center", image=self.bg_image1)

        # Start button to begin the quiz
        self.start_button = tk.Button(self.start_frame, text="Start the quiz game", font=("System", 20), command=self.show_quiz)
        self.canvas.create_window(center_x, center_y + 100, window=self.start_button)  # Position the button below the image

        # Main quiz interface frame
        self.quiz_frame = tk.Frame(window, bg="black")  # Create a frame for the quiz interface with a black background

        # Set the size and properties of the GUI window
        self.window.geometry("800x600")  # Set the window size
        self.window.resizable(False, False)  # Make the window non-resizable
        self.window.config(bg="black")  # Set the background color of the window to black

        # Set the window icon
        self.icon = tk.PhotoImage(file="C:\\Users\\akosi\\OneDrive\\Desktop\\iccticon.png")
        self.window.iconphoto(True, self.icon)  # Set the icon of the window

        # Label to display the question
        self.question_label = tk.Label(self.quiz_frame, text="", font=("System", 25), bg="black", fg="white")
        self.question_label.pack(pady=20)  # Pack the label with padding

        # Label to display feedback on the answer
        self.feedback_label = tk.Label(self.quiz_frame, text="", font=("System", 14), fg="red", bg="black")
        self.feedback_label.pack(pady=10)  # Pack the label with padding

        # Label to display the current score
        self.score_label = tk.Label(self.quiz_frame, text="Score: 0", font=("System", 14), fg="blue", bg="black")
        self.score_label.pack(pady=10)  # Pack the label with padding

        # Buttons for answer choices
        self.buttons = []
        for i in range(4):
            button = tk.Button(self.quiz_frame, text="", font=("System", 14), command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)  # Pack the button with padding
            self.buttons.append(button)  # Add the button to the list of buttons

        # Button to generate a new question
        self.new_question_button = tk.Button(self.quiz_frame, text="New Question", command=self.new_question)
        self.new_question_button.pack(pady=20)  # Pack the button with padding

        # Button to restart the game
        self.restart_button = tk.Button(self.quiz_frame, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=20)  # Pack the button with padding

        # Initialize the list of remaining questions and score
        self.remaining_questions = questions.copy()  # Make a copy of the list of questions
        self.score = 0  # Initialize the score to 0

    def show_quiz(self):
        """Function to show the quiz interface and generate the first question"""
        self.start_frame.pack_forget()  # Hide the start frame
        self.quiz_frame.pack(fill="both", expand=True)  # Show the quiz frame
        self.new_question()  # Generate the first question

    def new_question(self):
        """Function to generate and display a new question"""
        for button in self.buttons:
            button.config(state=tk.NORMAL)  # Enable all answer buttons
        self.new_question_button.config(state=tk.DISABLED)  # Disable the new question button

        if not self.remaining_questions:
            self.remaining_questions = questions.copy()  # Reset questions if all have been used

        # Select a random question
        self.current_question, self.current_choices, self.correct_answer = random.choice(self.remaining_questions)
        self.remaining_questions.remove((self.current_question, self.current_choices, self.correct_answer))  # Remove selected question

        # Shuffle the choices while keeping the correct answer identifiable
        shuffled_choices = self.current_choices[:]
        random.shuffle(shuffled_choices)

        self.question_label.config(text=self.current_question)  # Display the question
        for i, choice in enumerate(shuffled_choices):
            self.buttons[i].config(text=choice)  # Display answer choices
        self.feedback_label.config(text="")  # Reset feedback label

    def check_answer(self, i):
        """Function to check if the selected answer is correct"""
        selected_answer = self.buttons[i].cget("text")  # Get the text of the selected button
        if selected_answer == self.correct_answer:
            self.feedback_label.config(text="Correct!", fg="blue")  # Display correct feedback
            self.score += 1  # Increase the score
            self.score_label.config(text=f"Score: {self.score}")  # Update the score label
            self.window.after(1000, self.new_question)  # Wait for 1 second and then move to the next question
        else:
            self.feedback_label.config(text=f"Incorrect! The correct answer is {self.correct_answer}.", fg="red")  # Display incorrect feedback
            for button in self.buttons:
                button.config(state=tk.DISABLED)  # Disable all answer buttons
            self.new_question_button.config(state=tk.NORMAL)  # Enable the new question button

    def restart_game(self):
        """Function to restart the game"""
        self.score = 0  # Reset the score
        self.score_label.config(text=f"Score: {self.score}")  # Update the score label
        self.remaining_questions = questions.copy()  # Reset the list of remaining questions
        self.new_question()  # Generate a new question

if __name__ == "__main__":
    window = tk.Tk()  # Create the main window
    app = QuizGenerator(window)  # Create an instance of the QuizGenerator class
    window.mainloop()  # Start the Tkinter event loop
