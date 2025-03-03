import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import random

# List of questions and choices categorized by subjects
subject_questions = {
    "General Knowledge": [
        ("What does CPU stand for?", ["Central Processing Unit", "Central Program Unit", "Control Processing Unit", "Central Performance Unit"], "Central Processing Unit"),
        ("What is the main function of an operating system?", ["Manage hardware and software resources", "Run applications", "Browse the internet", "Process data"], "Manage hardware and software resources"),
        # add more general knowledge questions
    ],
    "Technology": [
        ("What does RAM stand for?", ["Random Access Memory", "Read Access Memory", "Run Access Memory", "Random Application Memory"], "Random Access Memory"),
        ("What is the primary purpose of a firewall?", ["To block unauthorized access", "To speed up the internet", "To store data", "To connect devices"], "To block unauthorized access"),
        # add more technology questions
    ],
    "Science": [
        ("What does HTML stand for?", ["HyperText Markup Language", "HyperText Machine Language", "HyperText and Links Markup", "HyperTool Markup Language"], "HyperText Markup Language"),
        ("Who is known as the father of the computer?", ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"], "Charles Babbage"),
        # add more science questions
    ],
    "Physical Education": [
        ("What is the powerhouse of the cell?", ["Mitochondria", "Skin", "Hair", "Heart"], "Mitochondria"),
    ],
    # you can add more subjects
}

class QuizGenerator:
    def __init__(self, window):
        self.window = window
        self.window.title("Random Quiz Generator")

        # Load and set the background image for the start window
        self.bg_image2 = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop\\school.png")
        self.bg_image2 = self.bg_image2.resize((800, 600), Image.LANCZOS)
        self.bg_image2 = ImageTk.PhotoImage(self.bg_image2)

        # Load and set the logo image for the start window
        self.bg_image1 = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop\\logo1.png")
        self.bg_image1 = self.bg_image1.resize((200, 200), Image.LANCZOS)
        self.bg_image1 = ImageTk.PhotoImage(self.bg_image1)

        # Create the start window frame
        self.start_frame = tk.Frame(window)
        self.start_frame.pack(fill="both", expand=True)

        # Create a canvas for the start window to hold background and logo
        self.canvas = tk.Canvas(self.start_frame, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image2)

        # Center coordinates for the logo and widgets
        center_x = 400
        center_y = 250
        self.canvas.create_image(center_x, center_y - 100, anchor="center", image=self.bg_image1)

        # Subject selection menu
        self.selected_subject = tk.StringVar(self.start_frame)
        self.selected_subject.set("Select Subject")
        self.subject_menu = tk.OptionMenu(self.start_frame, self.selected_subject, *subject_questions.keys())
        self.canvas.create_window(center_x, center_y + 150, window=self.subject_menu)

        # Start button to begin the quiz
        self.start_button = tk.Button(self.start_frame, text="Start the quiz game", font=("System", 20), command=self.show_quiz)
        self.canvas.create_window(center_x, center_y + 100, window=self.start_button)

        # Create the quiz frame
        self.quiz_frame = tk.Frame(window, bg="black")

        # Window configuration
        self.window.geometry("800x600")
        self.window.resizable(False, False)
        self.window.config(bg="black")
        self.icon = tk.PhotoImage(file="C:\\Users\\akosi\\OneDrive\\Desktop\\iccticon.png")
        self.window.iconphoto(True, self.icon)

        # Canvas for GIF background
        self.quiz_canvas = tk.Canvas(self.quiz_frame, width=800, height=600)
        self.quiz_canvas.pack(fill="both", expand=True)

        # Load and set the GIF background
        self.gif_path = "C:\\Users\\akosi\\OneDrive\\Desktop\\quizbg.gif"
        self.load_gif(self.gif_path)

        # Hearts frame for lives
        self.hearts_frame = tk.Frame(self.quiz_canvas, bg="black")
        self.hearts_frame.pack(anchor='nw', pady=10, padx=10)
        self.hearts = []
        for i in range(5):
            heart = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop\\heart.png")
            heart = heart.resize((30, 30), Image.LANCZOS)
            heart = ImageTk.PhotoImage(heart)
            heart_label = tk.Label(self.hearts_frame, image=heart, bg="black")
            heart_label.image = heart  # Keep a reference to avoid garbage collection
            heart_label.pack(side="left")
            self.hearts.append(heart_label)

        # Frame for question and feedback
        self.question_frame = tk.Frame(self.quiz_canvas, bg="black")
        self.question_frame.pack(pady=10)

        # Question label
        self.question_label = tk.Label(self.question_frame, text="", font=("System", 20), bg="black", fg="white")
        self.question_label.pack(pady=20)

        # Feedback label
        self.feedback_label = tk.Label(self.question_frame, text="", font=("System", 14), fg="red", bg="black")
        self.feedback_label.pack(pady=10)

        # Timer label
        self.timer_label = tk.Label(self.question_frame, text="Time left: 10", font=("System", 14), fg="green", bg="black")
        self.timer_label.pack(pady=10)

        # Score label
        self.score_label = tk.Label(self.question_frame, text="Score: 0", font=("System", 14), fg="blue", bg="black")
        self.score_label.pack(pady=10)

        # High score label
        self.high_score_label = tk.Label(self.question_frame, text="Highest Score: 0", font=("System", 14), fg="orange", bg="black")
        self.high_score_label.pack(pady=10)

        # Answer buttons
        self.buttons = []
        for i in range(4):
            button = tk.Button(self.question_frame, text="", font=("System", 14), command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.buttons.append(button)

        # New question button
        self.new_question_button = tk.Button(self.question_frame, text="New Question", command=self.new_question)
        self.new_question_button.pack(pady=10)

        # Restart button
        self.restart_button = tk.Button(self.question_frame, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=10)

        # Back button
        self.back_button = tk.Button(self.question_frame, text="Return", command=self.show_start)
        self.back_button.pack(pady=10)

        # Initialize quiz variables
        self.remaining_questions = []
        self.score = 0
        self.high_score = 0
        self.timer_seconds = 10
        self.timer_id = None
        self.lives = 5

        # Place hearts and question frames on the canvas
        self.quiz_canvas.create_window(10, 10, anchor="nw", window=self.hearts_frame)
        self.quiz_canvas.create_window(400, 300, anchor="center", window=self.question_frame)

    # Method to display the quiz frame
    def show_quiz(self):
        selected_subject = self.selected_subject.get()
        if selected_subject == "Select Subject":
            messagebox.showwarning("No Subject Selected", "Please select a subject before starting the quiz.")
            return
        self.remaining_questions = subject_questions[selected_subject].copy()
        self.start_frame.pack_forget()
        self.quiz_frame.pack(fill="both", expand=True)
        self.new_question()

    # Method to display the start frame
    def show_start(self):
        self.quiz_frame.pack_forget()
        self.start_frame.pack(fill="both", expand=True)

    # Method to load and set the gif background
    def load_gif(self, gif_path):
        self.gif_image = Image.open(gif_path)
        self.gif_frames = [ImageTk.PhotoImage(frame.resize((800, 600), Image.LANCZOS)) for frame in ImageSequence.Iterator(self.gif_image)]
        self.gif_index = 0
        self.bg_label = tk.Label(self.quiz_canvas, image=self.gif_frames[self.gif_index])
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.update_gif()

    # Method to update the gif background
    def update_gif(self):
        self.gif_index = (self.gif_index + 1) % len(self.gif_frames)
        self.bg_label.config(image=self.gif_frames[self.gif_index])
        self.window.after(100, self.update_gif)

    # Method to load a new question
    def new_question(self):
        if not self.remaining_questions:
            self.feedback_label.config(text="No more questions available.", fg="red")
            return
        self.timer_seconds = 10
        self.update_timer()
        question, choices, self.current_answer = random.choice(self.remaining_questions)
        self.remaining_questions.remove((question, choices, self.current_answer))
        self.question_label.config(text=question)
        random.shuffle(choices)
        for i in range(4):
            self.buttons[i].config(text=choices[i], state=tk.NORMAL)

    # Method to update the timer
    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.timer_seconds}")
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.timer_id = self.window.after(1000, self.update_timer)
        else:
            self.check_answer(-1)

    # Method to check the selected answer
    def check_answer(self, chosen_index):
        if self.timer_id:
            self.window.after_cancel(self.timer_id)
        for button in self.buttons:
            button.config(state=tk.DISABLED)
        chosen_answer = self.buttons[chosen_index].cget("text") if chosen_index != -1 else ""
        if chosen_answer == self.current_answer:
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")  # Update the score label
        else:
            self.feedback_label.config(text=f"Incorrect! The correct answer was: {self.current_answer}", fg="red")
            self.lives -= 1
            if self.lives > 0:
                self.hearts[self.lives].pack_forget()  # Remove a heart
            else:
                self.game_over()
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_label.config(text=f"Highest Score: {self.high_score}")
        if self.lives > 0:
            self.window.after(3000, self.new_question)

    # Method to handle game over state
    def game_over(self):
        self.feedback_label.config(text="Game Over", fg="red")
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    # Method to restart the game
    def restart_game(self):
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.lives = 5
        for heart in self.hearts:
            heart.pack(side="left")
        self.new_question()
        self.new_question_button.config(state=tk.NORMAL)

# Main program entry point
if __name__ == "__main__":
    window = tk.Tk()
    quiz = QuizGenerator(window)
    window.mainloop()
