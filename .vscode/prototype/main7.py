import tkinter as tk
from PIL import Image, ImageTk
import random

# List of questions and choices, each tuple contains a question, a list of choices, and the correct answer
questions = [
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
]

class QuizGenerator: #class
    def __init__(self, window): #instance and inside is called the constructor with parameters
        self.window = window    #initializing and setting the window
        self.window.title("Random Quiz Generator") #setting the title of the window

        # Load and set the background image
        self.bg_image = Image.open("C:\\Users\\akosi\\OneDrive\\Desktop\\icon.png")  # getting the path of the image
        self.bg_image = self.bg_image.resize((200, 200), Image.LANCZOS) #resize the image of bg
        self.bg_image = ImageTk.PhotoImage(self.bg_image) #setting the image as the background

        # Start screen with a Start button
        self.start_frame = tk.Frame(window)
        self.start_frame.pack(fill="both", expand=True)

        # Label to display the background image
        self.bg_label = tk.Label(self.start_frame, image=self.bg_image) #placing the image to a label
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=0.50) #position the bg image to the top

        

        # Start button to begin the quiz
        self.start_button = tk.Button(self.start_frame, text="Start the quiz game", font=("Comic Sans", 20), command=self.show_quiz)
        self.start_button.place(relx=0.5, rely=0.5, anchor="center") #place the position of the button

        # Main quiz interface frame
        self.quiz_frame = tk.Frame(window, bg="black")

        # Set the size and properties of the GUI window
        self.window.geometry("800x600")  # Set the window width and height
        self.window.resizable(False, False)  # Make the window non-resizable
        self.window.config(bg="black")  # Set the background color to black

        # Set the window icon
        self.icon = tk.PhotoImage(file="C:\\Users\\akosi\\OneDrive\\Desktop\\iccticon.png")  # Update this path to your icon file
        self.window.iconphoto(True, self.icon) 

        # Label to display the question
        self.question_label = tk.Label(self.quiz_frame, text="", font=("Comic Sans", 16), bg="black", fg="white")
        self.question_label.pack(pady=20)

        # Label to display feedback on the answer
        self.feedback_label = tk.Label(self.quiz_frame, text="", font=("Comic Sans", 14), fg="red", bg="black")
        self.feedback_label.pack(pady=10)

        # Label to display the current score
        self.score_label = tk.Label(self.quiz_frame, text="Score: 0", font=("Comic Sans", 14), fg="green", bg="black")
        self.score_label.pack(pady=10)

        # Buttons for answer choices
        self.buttons = []
        for i in range(4):
            button = tk.Button(self.quiz_frame, text="", font=("Comic Sans", 14), command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.buttons.append(button)

        # Button to generate a new question
        self.new_question_button = tk.Button(self.quiz_frame, text="New Question", command=self.new_question)
        self.new_question_button.pack(pady=20)

        # Button to restart the game
        self.restart_button = tk.Button(self.quiz_frame, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=20)

        # Initialize the list of remaining questions and score
        self.remaining_questions = questions.copy()
        self.score = 0

    def show_quiz(self):
        """Function to show the quiz interface and generate the first question"""
        self.start_frame.pack_forget()  # Hide the start frame
        self.quiz_frame.pack(fill="both", expand=True)  # Show the quiz frame
        self.new_question()  # Generate the first question

    def new_question(self):
        """Function to generate and display a new question"""
        for button in self.buttons:
            button.config(state=tk.NORMAL)  # Enable all answer buttons
        self.new_question_button.config(state=tk.NORMAL)  # Enable the new question button
        
        if not self.remaining_questions:
            self.remaining_questions = questions.copy()  # Reset questions if all have been used
        
        self.current_question, self.current_choices, self.correct_answer = random.choice(self.remaining_questions)  # Select a random question
        self.remaining_questions.remove((self.current_question, self.current_choices, self.correct_answer))  # Remove selected question
        
        self.question_label.config(text=self.current_question)  # Display the question
        for i, choice in enumerate(self.current_choices):
            self.buttons[i].config(text=choice)  # Display answer choices
        self.feedback_label.config(text="Choices", fg="white")  # Reset feedback label

    def check_answer(self, i):
        """Function to check if the selected answer is correct"""
        selected_answer = self.buttons[i].cget("text")  # Get the text of the selected button
        if selected_answer == self.correct_answer:
            self.feedback_label.config(text="Correct!", fg="blue")  # Display correct feedback
            self.score += 1  # Increase the score
            self.score_label.config(text=f"Score: {self.score}")  # Update the score label
        else:
            self.feedback_label.config(text=f"Incorrect! The correct answer is {self.correct_answer}.", fg="red")  # Display incorrect feedback
            for button in self.buttons:
                button.config(state=tk.DISABLED)  # Disable all answer buttons
            self.new_question_button.config(state=tk.DISABLED)  # Disable the new question button

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
