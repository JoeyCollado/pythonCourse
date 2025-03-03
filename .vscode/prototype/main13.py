import tkinter as tk
from PIL import Image, ImageTk
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

        self.bg_image2 = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop\\school.png")
        self.bg_image2 = self.bg_image2.resize((800, 600), Image.LANCZOS)
        self.bg_image2 = ImageTk.PhotoImage(self.bg_image2)

        self.bg_image1 = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop\\logo1.png")
        self.bg_image1 = self.bg_image1.resize((200, 200), Image.LANCZOS)
        self.bg_image1 = ImageTk.PhotoImage(self.bg_image1)

        self.start_frame = tk.Frame(window)
        self.start_frame.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(self.start_frame, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image2)
        center_x = 400
        center_y = 250
        self.canvas.create_image(center_x, center_y - 100, anchor="center", image=self.bg_image1)

        self.selected_subject = tk.StringVar(self.start_frame)
        self.selected_subject.set("Select Subject")
        self.subject_menu = tk.OptionMenu(self.start_frame, self.selected_subject, *subject_questions.keys())
        self.canvas.create_window(center_x, center_y + 150, window=self.subject_menu)

        self.start_button = tk.Button(self.start_frame, text="Start the quiz game", font=("System", 20), command=self.show_quiz)
        self.canvas.create_window(center_x, center_y + 100, window=self.start_button)

        self.quiz_frame = tk.Frame(window, bg="black")

        self.window.geometry("800x600")
        self.window.resizable(False, False)
        self.window.config(bg="black")
        self.icon = tk.PhotoImage(file="C:\\Users\\akosi\\OneDrive\\Desktop\\iccticon.png")
        self.window.iconphoto(True, self.icon)

        self.question_label = tk.Label(self.quiz_frame, text="", font=("System", 20), bg="black", fg="white")
        self.question_label.pack(pady=20)
        self.feedback_label = tk.Label(self.quiz_frame, text="", font=("System", 14), fg="red", bg="black")
        self.feedback_label.pack(pady=10)
        self.timer_label = tk.Label(self.quiz_frame, text="Time left: 10", font=("System", 14), fg="green", bg="black")
        self.timer_label.pack(pady=10)
        self.score_label = tk.Label(self.quiz_frame, text="Score: 0", font=("System", 14), fg="blue", bg="black")
        self.score_label.pack(pady=10)
        self.high_score_label = tk.Label(self.quiz_frame, text="Highest Score: 0", font=("System", 14), fg="orange", bg="black")
        self.high_score_label.pack(pady=10)

        self.buttons = []
        for i in range(4):
            button = tk.Button(self.quiz_frame, text="", font=("System", 14), command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.buttons.append(button)

        self.new_question_button = tk.Button(self.quiz_frame, text="New Question", command=self.new_question)
        self.new_question_button.pack(pady=10)
       
        self.restart_button = tk.Button(self.quiz_frame, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=10)

        self.back_button = tk.Button(self.quiz_frame, text="Return", command=self.show_start)
        self.back_button.pack(pady=10)

        self.remaining_questions = []
        self.score = 0
        self.high_score = 0
        self.timer_seconds = 10
        self.timer_id = None

    def show_quiz(self):
        selected_subject = self.selected_subject.get()
        if selected_subject == "Select Subject":
            tk.messagebox.showwarning("No Subject Selected", "Please select a subject before starting the quiz.")
            return
        self.remaining_questions = subject_questions[selected_subject].copy()
        self.start_frame.pack_forget()
        self.quiz_frame.pack(fill="both", expand=True)
        self.new_question()

    def show_start(self):
        self.quiz_frame.pack_forget()
        self.start_frame.pack(fill="both", expand=True)

    def new_question(self):
        if self.timer_id:
            self.window.after_cancel(self.timer_id)
        for button in self.buttons:
            button.config(state=tk.NORMAL)
        if not self.remaining_questions:
            self.remaining_questions = subject_questions[self.selected_subject.get()].copy()
        self.timer_seconds = 10
        self.update_timer()
        self.feedback_label.config(text="")
        question, choices, answer = random.choice(self.remaining_questions)
        self.current_answer = answer
        self.remaining_questions.remove((question, choices, answer))
        self.question_label.config(text=question)
        random.shuffle(choices)
        for i in range(4):
            self.buttons[i].config(text=choices[i])

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.timer_seconds}")
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.timer_id = self.window.after(1000, self.update_timer)
        else:
            self.check_answer(-1)

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
            self.score_label.config(text=f"Score: {self.score}")
            self.new_question_button.config(state=tk.DISABLED)  # disable the new question button when you got incorrect answer
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_label.config(text=f"Highest Score: {self.high_score}")
        self.window.after(1000, self.new_question)

    def restart_game(self):
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.new_question()
        self.new_question_button.config(state=tk.NORMAL)

# Main program
if __name__ == "__main__":
    window = tk.Tk()
    quiz = QuizGenerator(window)
    window.mainloop()
