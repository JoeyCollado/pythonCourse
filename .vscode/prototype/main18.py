# Import the tkinter library for GUI creation
import tkinter as tk
# Import PIL (Python Imaging Library) for handling images
from PIL import Image, ImageTk, ImageSequence
# Import random module for random selection of questions
import random
# Import pygame library for handling sound effects
import pygame

# Initialize pygame mixer for sound effects
pygame.mixer.init()

# Load sound effects
button_click_sound = pygame.mixer.Sound("C:\\Users\\akosi\\OneDrive\\Desktop\\click.wav")  # Sound for button click
correct_answer_sound = pygame.mixer.Sound("C:\\Users\\akosi\\OneDrive\\Desktop\\click.wav")  # Sound for correct answer
incorrect_answer_sound = pygame.mixer.Sound("C:\\Users\\akosi\\OneDrive\\Desktop\\click.wav")  # Sound for incorrect answer
game_over_sound = pygame.mixer.Sound("C:\\Users\\akosi\\OneDrive\\Desktop\\rizz.wav")  # Sound for game over

# Load background music files
start_music = "C:\\Users\\akosi\\OneDrive\\Desktop\\Audio1.wav"  # Music for the start interface
quiz_music = "C:\\Users\\akosi\\OneDrive\\Desktop\\chiptune-grooving-142242.wav"  # Music for the quiz interface

# List of questions categorized by subjects with their choices and correct answers
subject_questions = {
    "General Knowledge": [
        ("What does CPU stand for?", ["Central Processing Unit", "Central Program Unit", "Control Processing Unit", "Central Performance Unit"], "Central Processing Unit"),
        ("What is the main function of an operating system?", ["Manage hardware and software resources", "Run applications", "Browse the internet", "Process data"], "Manage hardware and software resources"),
        # Add more general knowledge questions
    ],
    "Technology": [
        ("What does RAM stand for?", ["Random Access Memory", "Read Access Memory", "Run Access Memory", "Random Application Memory"], "Random Access Memory"),
        # Add more technology questions
    ],
    "Science": [
        ("What does HTML stand for?", ["HyperText Markup Language", "HyperText Machine Language", "HyperText and Links Markup", "HyperTool Markup Language"], "HyperText Markup Language"),
        # Add more science questions
    ],
    "Physical Education": [
        ("What is the powerhouse of the cell?", ["Mitochondria", "Skin", "Hair", "Heart"], "Mitochondria"),
        # Add more PE questions
    ],
    # Add more subjects as needed
}

# Class to handle quiz generation and GUI
class QuizGenerator:
    def __init__(self, window):
        self.window = window  # Main window
        self.window.title("Random Quiz Generator")  # Window title

        # Colors used for buttons and labels
        self.color1 = '#020f12'
        self.color2 = '#05d7ff'
        self.color3 = '#65e7ff'
        self.color4 = 'BLACK'

        # Load and configure background images
        self.bg_image2 = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop")
        self.bg_image2 = self.bg_image2.resize((800, 640), Image.LANCZOS)
        self.bg_image2 = ImageTk.PhotoImage(self.bg_image2)

        self.bg_image1 = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop")
        self.bg_image1 = self.bg_image1.resize((200, 200), Image.LANCZOS)
        self.bg_image1 = ImageTk.PhotoImage(self.bg_image1)

        self.buttonimg = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop")
        self.buttonimg = self.buttonimg.resize((200, 50), Image.LANCZOS)
        self.buttonimg = ImageTk.PhotoImage(self.buttonimg)

        # Create the start frame
        self.start_frame = tk.Frame(window)
        self.start_frame.pack(fill="both", expand=True)
        
        # Create canvas for the start frame
        self.canvas = tk.Canvas(self.start_frame, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image2)  # Set background image
        center_x = 400
        center_y = 250
        self.canvas.create_image(center_x, center_y - 100, anchor="center", image=self.bg_image1)  # Set logo image

        # Subject selection dropdown menu
        self.selected_subject = tk.StringVar(self.start_frame)
        self.selected_subject.set("Select Subject")  # Default value
        self.subject_menu = tk.OptionMenu(self.start_frame, self.selected_subject, *subject_questions.keys())
        self.canvas.create_window(center_x, center_y + 180, window=self.subject_menu)

        # Start button configuration
        self.start_button = tk.Button(self.start_frame, text="Start the quiz game", font=("System", 20, 'bold'), command=self.show_quiz, bg=self.color2, fg=self.color4, activebackground=self.color3, activeforeground=self.color4, highlightthickness=2, highlightbackground=self.color2, highlightcolor='WHITE', cursor='hand1', border=0, width=20, height=1, borderwidth=10)
        self.canvas.create_window(center_x, center_y + 100, window=self.start_button)

        # Quiz frame for displaying questions and answers
        self.quiz_frame = tk.Frame(window, bg="black")
        self.window.geometry("800x640")  # Set window size
        self.window.resizable(False, False)  # Disable resizing
        self.window.config(bg="black")  # Set background color
        self.icon = tk.PhotoImage(file="C:\\Users\\akosi\\OneDrive\\Desktop")
        self.window.iconphoto(True, self.icon)  # Set window icon

        # Hearts frame for displaying lives
        self.hearts_frame = tk.Frame(self.quiz_frame, bg="black")
        self.hearts_frame.pack(anchor='nw', pady=10, padx=10)
        self.hearts = []
        for i in range(5):  # Load and display heart images for lives
            heart = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop")
            heart = heart.resize((30, 30), Image.LANCZOS)
            heart = ImageTk.PhotoImage(heart)
            heart_label = tk.Label(self.hearts_frame, image=heart, bg="black")
            heart_label.image = heart  # Keep a reference to avoid garbage collection
            heart_label.pack(side="left")
            self.hearts.append(heart_label)

        # Frame for question and feedback
        self.question_frame = tk.Frame(self.quiz_frame, bg="black")
        self.question_frame.pack(pady=2)
        
        # Label for displaying questions
        self.question_label = tk.Label(self.question_frame, text="", font=("System", 15, 'bold'), bg="black", fg="white")
        self.question_label.pack(pady=2)
        
        # Label for displaying feedback
        self.feedback_label = tk.Label(self.question_frame, text="", font=("System", 14, 'bold'), fg="red", bg="black")
        self.feedback_label.pack(pady=2)
        
        # Label for displaying timer
        self.timer_label = tk.Label(self.question_frame, text="Time left: 10", font=("System", 14, 'bold'), fg="green", bg="black")
        self.timer_label.pack(pady=2)
        
        # Label for displaying score
        self.score_label = tk.Label(self.question_frame, text="Score: 0", font=("System", 14, 'bold'), fg="blue", bg="black")
        self.score_label.pack(pady=2)
        
        # Label for displaying high score
        self.high_score_label = tk.Label(self.question_frame, text="Highest Score: 0", font=("System", 14, 'bold'), fg="orange", bg="black")
        self.high_score_label.pack(pady=2)

        # Create buttons for answer choices
        self.buttons = []
        for i in range(4):  # Create four buttons for multiple choice answers
            button = tk.Button(self.question_frame, text="", font=("System", 14, 'bold'), command=lambda i=i: self.check_answer(i), background=self.color2, foreground=self.color4, activebackground=self.color3, activeforeground=self.color4, highlightthickness=2, highlightbackground=self.color2, highlightcolor='WHITE', cursor='hand1', border=0, width=70, height=1, borderwidth=10)
            button.pack(pady=5)
            self.buttons.append(button)

        # Button for generating new question
        self.new_question_button = tk.Button(self.question_frame, text="New Question", command=self.new_question, bg=self.color2, fg=self.color4, activebackground=self.color3, activeforeground=self.color4, highlightthickness=2, highlightbackground=self.color2, highlightcolor='WHITE', cursor='hand1', border=0, width=10, height=1, borderwidth=10)
        self.new_question_button.pack(pady=2)
        
        # Button for restarting the game
        self.restart_button = tk.Button(self.question_frame, text="Restart", command=self.restart_game, bg=self.color2, fg=self.color4, activebackground=self.color3, activeforeground=self.color4, highlightthickness=2, highlightbackground=self.color2, highlightcolor='WHITE', cursor='hand1', border=0, width=10, height=1, borderwidth=10)
        self.restart_button.pack(pady=3)
        
        # Button for returning to the start interface
        self.back_button = tk.Button(self.question_frame, text="Return", command=self.show_start, bg=self.color2, fg=self.color4, activebackground=self.color3, activeforeground=self.color4, highlightthickness=2, highlightbackground=self.color2, highlightcolor='WHITE', cursor='hand1', border=0, width=10, height=1, borderwidth=10)
        self.back_button.pack(pady=3)

        # Initialize game variables
        self.remaining_questions = []  # List of remaining questions
        self.score = 0  # Initial score
        self.high_score = 0  # Initial high score
        self.timer_seconds = 10  # Initial timer seconds
        self.timer_id = None  # Timer ID
        self.lives = 5  # Initial lives

        # Add a GIF to the bottom left of the main quiz window
        self.gif_label = tk.Label(self.quiz_frame, bg="black")
        self.gif_label.place(x=660, y=500)  # Adjust the coordinates as needed
        self.load_gif("C:\\Users\\akosi\\OneDrive\\Desktop\\gif2.gif")  # Load GIF file

        # Start background music for the start interface
        self.play_background_music(start_music)

    # Load and prepare GIF animation
    def load_gif(self, gif_path):
        self.gif = Image.open(gif_path)
        self.gif_frames = []
        self.gif_index = 0
        # Convert and resize each frame
        for frame in ImageSequence.Iterator(self.gif):
            frame = frame.convert("RGBA")
            new_frame = frame.resize((100, 100), Image.LANCZOS)  # Resize the frame
            self.gif_frames.append(ImageTk.PhotoImage(new_frame))
        self.update_gif_frame()  # Start updating GIF frames

    # Update the GIF frame by frame
    def update_gif_frame(self):
        if self.gif_frames:
            self.gif_label.config(image=self.gif_frames[self.gif_index])
            self.gif_index = (self.gif_index + 1) % len(self.gif_frames)
            self.window.after(100, self.update_gif_frame)  # Adjust the delay as needed

    # Play background music
    def play_background_music(self, music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)  # Play the music in a loop

    # Stop background music
    def stop_background_music(self):
        pygame.mixer.music.stop()

    # Play sound effect
    def play_sound(self, sound):
        pygame.mixer.Sound.play(sound)

    # Display the quiz interface
    def show_quiz(self):
        self.play_sound(button_click_sound)  # Play button click sound
        selected_subject = self.selected_subject.get()
        if selected_subject == "Select Subject":  # Check if a subject is selected
            tk.messagebox.showwarning("No Subject Selected", "Please select a subject before starting the quiz.")
            return
        self.remaining_questions = subject_questions[selected_subject].copy()  # Copy questions for the selected subject
        self.lives = 5  # Reset lives
        self.update_lives_display()  # Update hearts display
        self.start_frame.pack_forget()
        self.quiz_frame.pack(fill="both", expand=True)
        self.stop_background_music()  # Switch to quiz background music
        self.play_background_music(quiz_music)
        self.new_question()  # Generate new question

    # Display the start interface
    def show_start(self):
        self.play_background_music(start_music)  # Play start music
        self.play_sound(button_click_sound)  # Play button click sound
        self.quiz_frame.pack_forget()
        self.start_frame.pack(fill="both", expand=True)
        self.score = 0  # Reset score
        self.high_score = 0  # Reset high score
        self.score_label.config(text=f"Score: {self.score}")
        self.high_score_label.config(text=f"Highest Score: {self.high_score}")

    # Generate a new question
    def new_question(self):
        if self.timer_id:
            self.window.after_cancel(self.timer_id)  # Cancel previous timer if any
        for button in self.buttons:
            button.config(state=tk.NORMAL)  # Enable answer buttons
        if not self.remaining_questions:  # Check if no questions are left
            self.remaining_questions = subject_questions[self.selected_subject.get()].copy()  # Refill questions
        self.timer_seconds = 10  # Reset timer seconds
        self.new_question_button.config(state=tk.NORMAL)
        self.update_timer()  # Start the timer
        self.feedback_label.config(text="")
        question, choices, answer = random.choice(self.remaining_questions)  # Select a random question
        self.current_answer = answer  # Set current answer
        self.remaining_questions.remove((question, choices, answer))  # Remove the question from remaining questions
        self.question_label.config(text=question)  # Display the question
        random.shuffle(choices)  # Shuffle choices
        for i in range(4):  # Display shuffled choices
            self.buttons[i].config(text=choices[i])

    # Update the timer countdown
    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.timer_seconds}")
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.timer_id = self.window.after(1000, self.update_timer)
        else:
            self.check_answer(-1)  # Time's up, check answer with -1 indicating no answer chosen

    # Check the chosen answer
    def check_answer(self, chosen_index):
        self.play_sound(button_click_sound)  # Play button click sound
        if self.timer_id:
            self.window.after_cancel(self.timer_id)  # Cancel the timer
        for button in self.buttons:
            button.config(state=tk.DISABLED)  # Disable answer buttons
        chosen_answer = self.buttons[chosen_index].cget("text") if chosen_index != -1 else ""  # Get chosen answer
        if chosen_answer == self.current_answer:  # Check if the chosen answer is correct
            self.play_sound(correct_answer_sound)  # Play correct answer sound
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1  # Increase score
            self.score_label.config(text=f"Score: {self.score}")  # Update the score label
        else:
            self.play_sound(incorrect_answer_sound)  # Play incorrect answer sound
            self.feedback_label.config(text=f"Incorrect! The correct answer was: {self.current_answer}", fg="red")
            self.new_question_button.config(state=tk.DISABLED)
            self.lives -= 1  # Decrease lives
            if self.lives > 0:
                self.hearts[self.lives].pack_forget()  # Remove a heart
            else:
                self.game_over()  # End the game
                self.update_lives_display()
        if self.score > self.high_score:  # Update high score if necessary
            self.high_score = self.score
            self.high_score_label.config(text=f"Highest Score: {self.high_score}")
        if self.lives > 0:
            self.window.after(1000, self.new_question)  # Generate a new question after a delay

    # Update the display of lives (hearts)
    def update_lives_display(self):
        for i in range(5):
            if i < self.lives:
                self.hearts[i].pack(side="left")  # Display heart
            else:
                self.hearts[i].pack_forget()  # Remove heart

    # Handle game over state
    def game_over(self):
        pygame.mixer.music.stop()  # Stop music
        self.play_sound(game_over_sound)  # Play game over sound
        self.feedback_label.config(text="Game Over", fg="red")
        for button in self.buttons:
            button.config(state=tk.DISABLED)  # Disable answer buttons

    # Restart the game
    def restart_game(self):
        pygame.mixer.music.stop()  # Stop music
        self.play_background_music(quiz_music)  # Play quiz music
        self.score = 0  # Reset score
        self.score_label.config(text=f"Score: {self.score}")
        self.lives = 5  # Reset lives
        for heart in self.hearts:
            heart.pack(side="left")  # Display all hearts
        self.new_question()  # Generate a new question
        self.new_question_button.config(state=tk.NORMAL)

# Main program entry point
if __name__ == "__main__":
    window = tk.Tk()  # Create main window
    quiz = QuizGenerator(window)  # Create QuizGenerator instance
    window.mainloop()  # Run the Tkinter main loop
