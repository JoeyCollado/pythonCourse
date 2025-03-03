import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame

# Initialize pygame for sound effects
pygame.mixer.init()

# Load sound effects
button_click_sound = pygame.mixer.Sound("C:\\Users\\akosi\\OneDrive\\Desktop\\click.wav")
correct_answer_sound = pygame.mixer.Sound("C:\\Users\\akosi\\OneDrive\\Desktop\\click.wav")
incorrect_answer_sound = pygame.mixer.Sound("C:\\Users\\akosi\\OneDrive\\Desktop\\click.wav")
game_over_sound = pygame.mixer.Sound("C:\\Users\\akosi\\OneDrive\\Desktop\\rizz.wav")
#game_over_sound = pygame.mixer.Sound("C:\\Users\\akosi\\OneDrive\\Desktop\\GameOver.wav")

# Load background music
start_music = "C:\\Users\\akosi\\OneDrive\\Desktop\\Audio1.wav"
quiz_music = "C:\\Users\\akosi\\OneDrive\\Desktop\\Audio1.wav"


# List of questions and choices categorized by subjects
subject_questions = {
    "General Knowledge": [
    ("What does CPU stand for?", ["Central Processing Unit", "Central Program Unit", "Control Processing Unit", "Central Performance Unit"], "Central Processing Unit"),
    ("What is the main function of an operating system?", ["Manage hardware and software resources", "Run applications", "Browse the internet", "Process data"], "Manage hardware and software resources"),
    ("What does CPU stand for?", ["Central Processing Unit", "Central Program Unit", "Control Processing Unit", "Central Performance Unit"], "Central Processing Unit"),
    ("What is the main function of an operating system?", ["Manage hardware and software resources", "Run applications", "Browse the internet", "Process data"], "Manage hardware and software resources"),
    ("What does RAM stand for?", ["Random Access Memory", "Read Access Memory", "Run Access Memory", "Random Application Memory"], "Random Access Memory"),
    ("What is the primary purpose of a firewall?", ["To block unauthorized access", "To speed up the internet", "To store data", "To connect devices"], "To block unauthorized access"),
    ("What does HTML stand for?", ["HyperText Markup Language", "HyperText Machine Language", "HyperText and Links Markup", "HyperTool Markup Language"], "HyperText Markup Language"),
    ("Who is known as the father of the computer?", ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"], "Charles Babbage"),
    ("What is the use of an IP address?", ["Identify a device on a network", "Store files", "Run applications", "Secure the network"], "Identify a device on a network"),
    ("What does HTTP stand for?", ["HyperText Transfer Protocol", "HyperText Transmission Protocol", "HighText Transfer Protocol", "HyperText Transport Protocol"], "HyperText Transfer Protocol"),
    ("What is the primary purpose of a database?", ["To store and manage data", "To connect to the internet", "To protect against viruses", "To run applications"], "To store and manage data"),
    ("What does DNS stand for?", ["Domain Name System", "Data Network System", "Domain Network Service", "Data Name Service"], "Domain Name System"),
    ("What is an algorithm?", ["A step-by-step procedure for solving a problem", "A type of software", "A programming language", "A hardware component"], "A step-by-step procedure for solving a problem"),
    ("What does SQL stand for?", ["Structured Query Language", "Simple Query Language", "Structured Question Language", "Sequential Query Language"], "Structured Query Language"),
    ("What is the function of a router?", ["To direct network traffic", "To store data", "To run applications", "To protect against viruses"], "To direct network traffic"),
    ("What is cloud computing?", ["Delivery of computing services over the internet", "Using multiple computers to solve a problem", "Storing data on physical disks", "Running applications on a local server"], "Delivery of computing services over the internet"),
    ("What is the main purpose of encryption?", ["To secure data by converting it into a code", "To store data", "To speed up data transmission", "To organize data"], "To secure data by converting it into a code"),
    ("What does GUI stand for?", ["Graphical User Interface", "General User Interface", "Graphical Universal Interface", "General Universal Interface"], "Graphical User Interface"),
    ("What is an API?", ["A set of rules for building software applications", "A type of operating system", "A programming language", "A database management system"], "A set of rules for building software applications"),
    ("What is machine learning?", ["A type of artificial intelligence that allows software to learn from data", "A process of encrypting data", "A programming language", "A type of database"], "A type of artificial intelligence that allows software to learn from data"),
    ("What does CSS stand for?", ["Cascading Style Sheets", "Computer Style Sheets", "Creative Style Sheets", "Cascading System Sheets"], "Cascading Style Sheets"),
    ("What is the function of a URL?", ["To specify the address of a web page", "To store data", "To connect to the internet", "To run applications"], "To specify the address of a web page"),
    ("What does IoT stand for?", ["Internet of Things", "Internet of Technology", "Interconnected Objects Technology", "Integrated Operational Technology"], "Internet of Things"),
    ("What is a function in programming?", ["A block of code designed to perform a particular task", "A type of variable", "A method of data encryption", "A type of database"], "A block of code designed to perform a particular task"),
    ("What is blockchain technology primarily used for?", ["Securing and verifying digital transactions", "Storing large amounts of data", "Connecting devices on a network", "Running applications in the cloud"], "Securing and verifying digital transactions"),
    ("What does SaaS stand for?", ["Software as a Service", "System as a Service", "Software and Application Service", "System and Application Service"], "Software as a Service"),
    ("What is the purpose of version control systems like Git?", ["To manage changes to source code", "To create user interfaces", "To encrypt data", "To run applications"], "To manage changes to source code"),
    ("What is an IDE?", ["Integrated Development Environment", "Intelligent Development Engine", "Interactive Development Environment", "Integrated Design Environment"], "Integrated Development Environment"),
    ("What is the purpose of a compiler?", ["To translate source code into executable code", "To store data", "To manage network connections", "To create graphical interfaces"], "To translate source code into executable code"),
    ("What does SSL stand for?", ["Secure Sockets Layer", "Simple Secure Layer", "Secure System Layer", "Safe Sockets Layer"], "Secure Sockets Layer"),
    ("What is the function of a VPN?", ["To create a secure connection over the internet", "To store data", "To run applications", "To manage network traffic"], "To create a secure connection over the internet"),
    ("What is phishing?", ["A method of trying to gather personal information using deceptive e-mails and websites", "A type of computer virus", "A network security tool", "A programming technique"], "A method of trying to gather personal information using deceptive e-mails and websites"),
    ("What is the main use of cookies on websites?", ["To store user preferences and track user behavior", "To increase loading speed", "To secure data", "To run applications"], "To store user preferences and track user behavior"),
    ("What does LAN stand for?", ["Local Area Network", "Large Area Network", "Long Area Network", "Light Area Network"], "Local Area Network"),
        # add more general knowledge questions
    ],
    
    "Technology": [

    ("What does RAM stand for?", ["Random Access Memory", "Read Access Memory", "Run Access Memory", "Random Application Memory"], "Random Access Memory"),
    ("What is the primary purpose of a firewall?", ["To block unauthorized access", "To speed up the internet", "To store data", "To connect devices"], "To block unauthorized access"),
    ("What does CPU stand for?", ["Central Processing Unit", "Central Program Unit", "Control Processing Unit", "Central Performance Unit"], "Central Processing Unit"),
    ("What is the main function of an operating system?", ["Manage hardware and software resources", "Run applications", "Browse the internet", "Process data"], "Manage hardware and software resources"),
    ("What does RAM stand for?", ["Random Access Memory", "Read Access Memory", "Run Access Memory", "Random Application Memory"], "Random Access Memory"),
    ("What is the primary purpose of a firewall?", ["To block unauthorized access", "To speed up the internet", "To store data", "To connect devices"], "To block unauthorized access"),
    ("What does HTML stand for?", ["HyperText Markup Language", "HyperText Machine Language", "HyperText and Links Markup", "HyperTool Markup Language"], "HyperText Markup Language"),
    ("Who is known as the father of the computer?", ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"], "Charles Babbage"),
    ("What is the use of an IP address?", ["Identify a device on a network", "Store files", "Run applications", "Secure the network"], "Identify a device on a network"),
    ("What does HTTP stand for?", ["HyperText Transfer Protocol", "HyperText Transmission Protocol", "HighText Transfer Protocol", "HyperText Transport Protocol"], "HyperText Transfer Protocol"),
    ("What is the primary purpose of a database?", ["To store and manage data", "To connect to the internet", "To protect against viruses", "To run applications"], "To store and manage data"),
    ("What does DNS stand for?", ["Domain Name System", "Data Network System", "Domain Network Service", "Data Name Service"], "Domain Name System"),
    ("What is an algorithm?", ["A step-by-step procedure for solving a problem", "A type of software", "A programming language", "A hardware component"], "A step-by-step procedure for solving a problem"),
    ("What does SQL stand for?", ["Structured Query Language", "Simple Query Language", "Structured Question Language", "Sequential Query Language"], "Structured Query Language"),
    ("What is the function of a router?", ["To direct network traffic", "To store data", "To run applications", "To protect against viruses"], "To direct network traffic"),
    ("What is cloud computing?", ["Delivery of computing services over the internet", "Using multiple computers to solve a problem", "Storing data on physical disks", "Running applications on a local server"], "Delivery of computing services over the internet"),
    ("What is the main purpose of encryption?", ["To secure data by converting it into a code", "To store data", "To speed up data transmission", "To organize data"], "To secure data by converting it into a code"),
    ("What does GUI stand for?", ["Graphical User Interface", "General User Interface", "Graphical Universal Interface", "General Universal Interface"], "Graphical User Interface"),
    ("What is an API?", ["A set of rules for building software applications", "A type of operating system", "A programming language", "A database management system"], "A set of rules for building software applications"),
    ("What is machine learning?", ["A type of artificial intelligence that allows software to learn from data", "A process of encrypting data", "A programming language", "A type of database"], "A type of artificial intelligence that allows software to learn from data"),
    ("What does CSS stand for?", ["Cascading Style Sheets", "Computer Style Sheets", "Creative Style Sheets", "Cascading System Sheets"], "Cascading Style Sheets"),
    ("What is the function of a URL?", ["To specify the address of a web page", "To store data", "To connect to the internet", "To run applications"], "To specify the address of a web page"),
    ("What does IoT stand for?", ["Internet of Things", "Internet of Technology", "Interconnected Objects Technology", "Integrated Operational Technology"], "Internet of Things"),
    ("What is a function in programming?", ["A block of code designed to perform a particular task", "A type of variable", "A method of data encryption", "A type of database"], "A block of code designed to perform a particular task"),
    ("What is blockchain technology primarily used for?", ["Securing and verifying digital transactions", "Storing large amounts of data", "Connecting devices on a network", "Running applications in the cloud"], "Securing and verifying digital transactions"),
    ("What does SaaS stand for?", ["Software as a Service", "System as a Service", "Software and Application Service", "System and Application Service"], "Software as a Service"),
    ("What is the purpose of version control systems like Git?", ["To manage changes to source code", "To create user interfaces", "To encrypt data", "To run applications"], "To manage changes to source code"),
    ("What is an IDE?", ["Integrated Development Environment", "Intelligent Development Engine", "Interactive Development Environment", "Integrated Design Environment"], "Integrated Development Environment"),
    ("What is the purpose of a compiler?", ["To translate source code into executable code", "To store data", "To manage network connections", "To create graphical interfaces"], "To translate source code into executable code"),
    ("What does SSL stand for?", ["Secure Sockets Layer", "Simple Secure Layer", "Secure System Layer", "Safe Sockets Layer"], "Secure Sockets Layer"),
    ("What is the function of a VPN?", ["To create a secure connection over the internet", "To store data", "To run applications", "To manage network traffic"], "To create a secure connection over the internet"),
    ("What is phishing?", ["A method of trying to gather personal information using deceptive e-mails and websites", "A type of computer virus", "A network security tool", "A programming technique"], "A method of trying to gather personal information using deceptive e-mails and websites"),
    ("What is the main use of cookies on websites?", ["To store user preferences and track user behavior", "To increase loading speed", "To secure data", "To run applications"], "To store user preferences and track user behavior"),
    ("What does LAN stand for?", ["Local Area Network", "Large Area Network", "Long Area Network", "Light Area Network"], "Local Area Network"),
        # add more technology questions
    ],
    
    "Science": [
        ("What does HTML stand for?", ["HyperText Markup Language", "HyperText Machine Language", "HyperText and Links Markup", "HyperTool Markup Language"], "HyperText Markup Language"),
        ("Who is known as the father of the computer?", ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"], "Charles Babbage"),
        ("How many bones does a avarage human adult have?", ["216 bones", "206 bones", "198 bones", "298 bones"], "206 bones"),
("What is the Third planet next the Sun in The Solar System?", ["Venus", "Mars", "Earth", "Mercury"], "Earth"),
("What Galaxy is our Solar System on?", ["Active Galaxy", "Spiral Galaxy", "Elliptical Galaxy", "Milky Way Galaxy"], "Milky Way Galaxy"),
("What one is not Part of The Six Kingdoms of Life?", ["Animalia", "eubacteria", "Protista", "Insectia"], "Insectia"),
("What does DNA stand for?", ["Deoxyribonucleic acid", "Deoxyribonucleic acloyte", "Deoxyribonucleic active", "Deoxyribonucleic aloye"], "Deoxyribonucleic acid"),
("What does RNA stand for?", ["Ribonucleic acloyte", "Ribonucleic actives", "Ribonucleic acid", "Ribonucleic aloye"], "Ribonucleic acid"),
("What is the most important part of the body?", ["Brain", "Heart", "Lungs", "Digestive System"], "Brain"),
("What is the 6th planet in the Solar System?", ["Jupiter", "Neptune", "Uranus", "Saturn"], "Saturn"),
("How long can a plant live without photosynthesis ?", ["3-15 Days", "4-20 Days", "5-30 Days", "6-35 Days"], "4-20 Days"),
("What type of element are we exhaling the most?", ["Nitrogen", "Oxygen", "Carbon Dioxide", "Carbon"], "Nitrogen"),
("Which part of the Eye is used to see?", ["Placenta", "Retina", "Cornea", "Pupil"], "Retina"),
("Which bone is the most important in the body?", ["Femur", "Tibia", "Humerus", "Phalanxes"], "Femur"),
("Who is the Father of Science?", ["Galileo Galilei", "Thomas Edison", "Isaac Newton", "Albert Einstein"], "Galileo Galilei"),
("Who Discovered Gravity?", ["Isaac Newton", "Aristotle", "Albert Einstein", "Pythagoras"], "Isaac Newton"),
("Which Country claimed to be The first ones to be on the moon?", ["America", "India", "Russia", "France"], "America"),
("What type of Planet is Earth Called?", ["Terrestrial Planets", "Gas Giants", "Ice Giants", "Dwarf Planets"], "Terrestrial Planets"),
("What is The most dominant Kingdom in the Six Kingdoms of Life?", ["Animalia", "eubacteria", "Protista", "Insectia"], "Animalia"),
("Which Cell Fights The bacteria?", ["Red Blood Cells", "Platelets", "White Blood Cells", "Medicine"], "White Blood Cells"),
("What is NOT part of an atom?", ["Electron", "Proton", "Nucleus", "Arton"], "Arton"),
("Who is the first man to Land in The Moon?", ["Neil Armstrong", "Nial Armstrong", "Neil Armsweak", "Nial Armsweak"], "Neil Armstrong"),
        # add more science questions
    ],
    
    "Physical Education": [
        ("What is the powerhouse of the cell?", ["Mitochondria", "Skin", "Hair", "Heart"], "Mitochondria"),
        #you can add more pe questions
    ],
    
    # you can add more subjects
}

class QuizGenerator:
    def __init__(self, window):
        self.window = window
        self.window.title("Random Quiz Generator")
        
        #declaring colors that can be used (i applied this hex values color to my buttons)
        self.color1 = '#020f12'
        self.color2 = '#05d7ff'
        self.color3 = '#65e7ff'
        self.color4 = 'BLACK'

        self.bg_image2 = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop\\bgcode1.jpg")
        self.bg_image2 = self.bg_image2.resize((800, 640), Image.LANCZOS)
        self.bg_image2 = ImageTk.PhotoImage(self.bg_image2)

        self.bg_image1 = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop\\logo.png")
        self.bg_image1 = self.bg_image1.resize((200, 200), Image.LANCZOS)
        self.bg_image1 = ImageTk.PhotoImage(self.bg_image1)

        self.buttonimg = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop\\button1.png")
        self.buttonimg = self.buttonimg.resize((200, 50), Image.LANCZOS)
        self.buttonimg = ImageTk.PhotoImage(self.buttonimg)    

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
        self.canvas.create_window(center_x, center_y + 180, window=self.subject_menu)

        self.start_button = tk.Button(self.start_frame, text="Start the quiz game", font=("System", 20, 'bold'), command=self.show_quiz, bg=self.color2, fg=self.color4, activebackground=self.color3, activeforeground=self.color4, highlightthickness=2, highlightbackground=self.color2, highlightcolor='WHITE', cursor='hand1', border=0, width=20,height=1, borderwidth=10)
        self.canvas.create_window(center_x, center_y + 100, window=self.start_button)

        self.quiz_frame = tk.Frame(window, bg="black")

        self.window.geometry("800x640")
        self.window.resizable(False, False)
        self.window.config(bg="black")
        self.icon = tk.PhotoImage(file="C:\\Users\\akosi\\OneDrive\\Desktop\\iccticon.png")
        self.window.iconphoto(True, self.icon)

        # Hearts frame for lives
        self.hearts_frame = tk.Frame(self.quiz_frame, bg="black")
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
        self.question_frame = tk.Frame(self.quiz_frame, bg="black")
        self.question_frame.pack(pady=2)

        self.question_label = tk.Label(self.question_frame, text="", font=("System", 15, 'bold'), bg="black", fg="white")
        self.question_label.pack(pady=2)
        self.feedback_label = tk.Label(self.question_frame, text="", font=("System", 14, 'bold'), fg="red", bg="black")
        self.feedback_label.pack(pady=2)
        self.timer_label = tk.Label(self.question_frame, text="Time left: 10", font=("System", 14, 'bold'), fg="green", bg="black")
        self.timer_label.pack(pady=2)
        self.score_label = tk.Label(self.question_frame, text="Score: 0", font=("System", 14, 'bold'), fg="blue", bg="black")
        self.score_label.pack(pady=2)
        self.high_score_label = tk.Label(self.question_frame, text="Highest Score: 0", font=("System", 14, 'bold'), fg="orange", bg="black")
        self.high_score_label.pack(pady=2)

        self.buttons = []
        for i in range(4):
            button = tk.Button(self.question_frame, text="", font=("System", 14, 'bold'), command=lambda i=i: self.check_answer(i), background=self.color2, foreground=self.color4, activebackground=self.color3, activeforeground=self.color4, highlightthickness=2, highlightbackground=self.color2, highlightcolor='WHITE', cursor='hand1', border=0, width=70,height=1, borderwidth=10)
            button.pack(pady=5)
            self.buttons.append(button)

        self.new_question_button = tk.Button(self.question_frame, text="New Question", command=self.new_question, bg=self.color2, fg=self.color4, activebackground=self.color3, activeforeground=self.color4, highlightthickness=2, highlightbackground=self.color2, highlightcolor='WHITE', cursor='hand1', border=0, width=10,height=1, borderwidth=10)
        self.new_question_button.pack(pady=2)
        self.restart_button = tk.Button(self.question_frame, text="Restart", command=self.restart_game, bg=self.color2, fg=self.color4, activebackground=self.color3, activeforeground=self.color4, highlightthickness=2, highlightbackground=self.color2, highlightcolor='WHITE', cursor='hand1', border=0, width=10,height=1, borderwidth=10)
        self.restart_button.pack(pady=3)
        self.back_button = tk.Button(self.question_frame, text="Return", command=self.show_start, bg=self.color2, fg=self.color4, activebackground=self.color3, activeforeground=self.color4, highlightthickness=2, highlightbackground=self.color2, highlightcolor='WHITE', cursor='hand1', border=0, width=10,height=1, borderwidth=10)
        self.back_button.pack(pady=3)

        self.remaining_questions = []
        self.score = 0
        self.high_score = 0
        self.timer_seconds = 10
        self.timer_id = None
        self.lives = 5

        
        # Start background music for the start interface
        self.play_background_music(start_music)

    def play_background_music(self, music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)  # Play the music in a loop

    def stop_background_music(self):
        pygame.mixer.music.stop()

    def play_sound(self, sound):
        pygame.mixer.Sound.play(sound)

    def show_quiz(self):
        self.play_sound(button_click_sound)
        selected_subject = self.selected_subject.get()
        if selected_subject == "Select Subject":
            tk.messagebox.showwarning("No Subject Selected", "Please select a subject before starting the quiz.")
            return
        self.remaining_questions = subject_questions[selected_subject].copy()
        self.lives = 5  # Reset lives
        self.update_lives_display()  # Update hearts display
        self.start_frame.pack_forget()
        self.quiz_frame.pack(fill="both", expand=True)
        # Switch to quiz background music
        self.stop_background_music()
        self.play_background_music(quiz_music)  
        self.new_question()
        

    def show_start(self):
        
        self.play_background_music(quiz_music)
        self.play_sound(button_click_sound)
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
        self.new_question_button.config(state=tk.NORMAL)
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
        self.play_sound(button_click_sound)
        if self.timer_id:
            self.window.after_cancel(self.timer_id)
        for button in self.buttons:
            button.config(state=tk.DISABLED)
        chosen_answer = self.buttons[chosen_index].cget("text") if chosen_index != -1 else ""
        if chosen_answer == self.current_answer:
            self.play_sound(correct_answer_sound)
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")  # Update the score label
        else:
            self.play_sound(incorrect_answer_sound)
            self.feedback_label.config(text=f"Incorrect! The correct answer was: {self.current_answer}", fg="red")
            self.new_question_button.config(state=tk.DISABLED)
            self.lives -= 1
            if self.lives > 0:
                self.hearts[self.lives].pack_forget()  # Remove a heart
            else:
                self.game_over()
                self.update_lives_display()
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_label.config(text=f"Highest Score: {self.high_score}")
        if self.lives > 0:
            self.window.after(1000, self.new_question)

    def update_lives_display(self):
        for i in range(5):
            if i < self.lives:
                self.hearts[i].pack(side="left")
            else:
                self.hearts[i].pack_forget()

    def game_over(self):
        pygame.mixer.music.stop()
        self.play_sound(game_over_sound)
        self.feedback_label.config(text="Game Over", fg="red")
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def restart_game(self):
        pygame.mixer.music.stop()
        self.play_background_music(quiz_music)
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.lives = 5
        for heart in self.hearts:
            heart.pack(side="left")
        self.new_question()
        self.new_question_button.config(state=tk.NORMAL)

# Main program
if __name__ == "__main__":
    window = tk.Tk()
    quiz = QuizGenerator(window)
    window.mainloop()
