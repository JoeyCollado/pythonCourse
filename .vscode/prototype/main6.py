import tkinter as tk
import random

# List of questions and choices, each tuple contains a question, a list of choices, and the correct answer
questions = [
    ("What is the capital of France?", ["Paris", "Berlin", "Madrid", "Rome"], "Paris"),
    ("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
    ("What color is the sky?", ["Blue", "Green", "Red", "Yellow"], "Blue"),
    ("Who is the Founder of ICCT Colleges Foundation Inc?", ["Dr. William S. Co.", "Ranielle Lopez", "Jake Acang", "Kyle Tan"], "Dr. William S. Co."),
    ("What is the first campus in ICCT?", ["San Mateo", "Sumulong", "Cainta", "Binangonan"], "Cainta"),
    ("What do you call a person that writes a program?", ["Programmer", "Plumber", "Teacher", "Fighter"], "Programmer"),
    ("Where is Philippines located?", ["Europe", "Asia", "South America", "Antarctica"], "Asia"),
    ("First man to set foot on moon?", ["Neil Armstrong", "Saul Goodwill", "Luffy", "Lebron"], "Neil Armstrong"),
    ("What is the largest planet in our solar system?", ["Earth", "Venus", "Jupiter", "Mars"], "Jupiter"),
    ("Who wrote the play 'Romeo and Juliet'?", ["William Shakespeare", "Jane Austen", "Charles Dickens", "Leo Tolstoy"], "William Shakespeare"),
    ("What is the chemical symbol for water?", ["H2O", "CO2", "O2", "NaCl"], "H2O"),
    ("What year did World War II end?", ["1945", "1939", "1941", "1950"], "1945"),
    ("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"], "Leonardo da Vinci"),
    ("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Saturn", "Mercury"], "Mars"),
    ("Who discovered penicillin?", ["Alexander Fleming", "Albert Einstein", "Marie Curie", "Isaac Newton"], "Alexander Fleming"),
    ("What is the largest ocean on Earth?", ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "Pacific Ocean"),
    ("What is the currency of Japan?", ["Yen", "Yuan", "Won", "Dollar"], "Yen"),
    ("Who was the first President of the United States?", ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], "George Washington"),
    ("Which country is famous for the Great Wall?", ["China", "India", "Japan", "Russia"], "China"),
    ("Who wrote 'The Great Gatsby'?", ["F. Scott Fitzgerald", "Ernest Hemingway", "Mark Twain", "Jane Austen"], "F. Scott Fitzgerald"),
    ("What is the smallest state in the United States?", ["Rhode Island", "Delaware", "Connecticut", "Maryland"], "Rhode Island"),
    ("What is the tallest mountain in the world?", ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"], "Mount Everest"),
    ("Which animal is known as the 'King of the Jungle'?", ["Lion", "Tiger", "Elephant", "Giraffe"], "Lion"),
    ("Who invented the telephone?", ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "James Watt"], "Alexander Graham Bell"),
    ("What is the largest mammal in the world?", ["Blue Whale", "Elephant", "Giraffe", "Hippopotamus"], "Blue Whale"),
    ("What is the chemical symbol for gold?", ["Au", "Ag", "Pt", "Fe"], "Au"),
    ("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "J.K. Rowling", "George Orwell", "Ernest Hemingway"], "Harper Lee"),
    ("What is the tallest tree in the world?", ["Redwood", "Sequoia", "Pine", "Oak"], "Redwood"),
    ("What is the main ingredient in guacamole?", ["Avocado", "Tomato", "Onion", "Lime"], "Avocado"),
    ("Who painted 'Starry Night'?", ["Vincent van Gogh", "Pablo Picasso", "Claude Monet", "Leonardo da Vinci"], "Vincent van Gogh"),
    ("What is the largest bird in the world?", ["Ostrich", "Eagle", "Albatross", "Emu"], "Ostrich"),
    ("Who is known as the 'Father of Computer'?", ["Charles Babbage", "Alan Turing", "Ada Lovelace", "Bill Gates"], "Charles Babbage"),
    ("Which country is famous for the Eiffel Tower?", ["France", "Italy", "Spain", "Germany"], "France"),
    ("What is the chemical symbol for oxygen?", ["O", "O2", "O3", "O4"], "O"),
    ("Who wrote 'Hamlet'?", ["William Shakespeare", "Jane Austen", "Charles Dickens", "Leo Tolstoy"], "William Shakespeare"),
    ("What is the largest desert in the world?", ["Sahara Desert", "Arabian Desert", "Gobi Desert", "Kalahari Desert"], "Sahara Desert"),
    ("What is the capital of Japan?", ["Tokyo", "Kyoto", "Osaka", "Seoul"], "Tokyo"),
    ("Who discovered America?", ["Christopher Columbus", "Marco Polo", "Vasco da Gama", "Amerigo Vespucci"], "Christopher Columbus"),
    ("What is the chemical symbol for carbon?", ["C", "Ca", "Co", "Cr"], "C"),
    ("Who wrote 'Pride and Prejudice'?", ["Jane Austen", "Charlotte Bronte", "Emily Dickinson", "George Eliot"], "Jane Austen"),
    ("What is the largest continent?", ["Asia", "Africa", "North America", "Europe"], "Asia"),
    ("Which planet is known as the 'Morning Star'?", ["Venus", "Mars", "Jupiter", "Saturn"], "Venus"),
    ("Who painted 'The Persistence of Memory'?", ["Salvador Dali", "Pablo Picasso", "Claude Monet", "Vincent van Gogh"], "Salvador Dali"),
    ("What is the chemical symbol for silver?", ["Ag", "Au", "Pt", "Cu"], "Ag"),
    ("Who wrote '1984'?", ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.K. Rowling"], "George Orwell"),
    ("What is the largest river in the world?", ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"], "Amazon River"),
    ("Who is known as the 'Father of Physics'?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Niels Bohr"], "Galileo Galilei"),
    ("Which country is famous for the Taj Mahal?", ["India", "China", "Japan", "Thailand"], "India"),
    ("What is the chemical symbol for sodium?", ["Na", "Sn", "Si", "Sb"], "Na"),
    ("Who wrote 'The Catcher in the Rye'?", ["J.D. Salinger", "F. Scott Fitzgerald", "Ernest Hemingway", "Mark Twain"], "J.D. Salinger"),
    ("What is the largest volcano in the world?", ["Mauna Loa", "Mount Vesuvius", "Mount Etna", "Mount Fuji"], "Mauna Loa"),
    ("What is the main ingredient in hummus?", ["Chickpeas", "Lentils", "Beans", "Quinoa"], "Chickpeas"),
    ("Who painted 'The Last Supper'?", ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"], "Leonardo da Vinci"),
    ("What is the fastest land animal?", ["Cheetah", "Lion", "Gazelle", "Leopard"], "Cheetah"),
    ("Who invented the light bulb?", ["Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "James Watt"], "Thomas Edison"),
    ("What is the largest reptile in the world?", ["Saltwater Crocodile", "Komodo Dragon", "Galapagos Tortoise", "Green Anaconda"], "Saltwater Crocodile"),
    ("What is the chemical symbol for iron?", ["Fe", "Au", "Ag", "Pb"], "Fe"),
    ("Who wrote 'Moby Dick'?", ["Herman Melville", "Mark Twain", "Emily Dickinson", "Walt Whitman"], "Herman Melville"),
    ("What is the deepest part of the ocean?", ["Mariana Trench", "Puerto Rico Trench", "Java Trench", "Philippine Trench"], "Mariana Trench")
]

class QuizGenerator:
    def __init__(self, window):
        self.window = window
        self.window.title("Random Quiz Generator")

        # Start screen with a Start button
        self.start_frame = tk.Frame(window, bg="black")
        self.start_frame.pack(fill="both", expand=True)
        self.start_button = tk.Button(self.start_frame, text="Start the quiz game", font=("Comic Sans", 50), command=self.show_quiz)
        self.start_button.pack(pady=200)

        # Main quiz interface
        self.quiz_frame = tk.Frame(window, bg="black")

         # Set the size and properties of the GUI window
        self.window.geometry("900x800")  # Set the window width and height
        self.window.resizable(False, False)  # Make the window non-resizable
        self.window.config(bg="black")  # Set the background color to black

        # Set the window icon
        self.icon = tk.PhotoImage(file="C:\\Users\\akosi\\OneDrive\\Desktop\\iccticon.png")  # Update this path to your icon file
        self.window.iconphoto(True, self.icon)

        self.question_label = tk.Label(self.quiz_frame, text="", font=("Comic Sans", 16), bg="black", fg="white")
        self.question_label.pack(pady=20)

        self.feedback_label = tk.Label(self.quiz_frame, text="", font=("Comic Sans", 14), fg="red", bg="black")
        self.feedback_label.pack(pady=10)

        self.score_label = tk.Label(self.quiz_frame, text="Score: 0", font=("Comic Sans", 14), fg="green", bg="black")
        self.score_label.pack(pady=10)

        self.buttons = []
        for i in range(4):
            button = tk.Button(self.quiz_frame, text="", font=("Comic Sans", 14), command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.buttons.append(button)

        self.new_question_button = tk.Button(self.quiz_frame, text="New Question", command=self.new_question)
        self.new_question_button.pack(pady=20)

        self.restart_button = tk.Button(self.quiz_frame, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=20)

        self.remaining_questions = questions.copy()
        self.score = 0

    def show_quiz(self):
        self.start_frame.pack_forget()  # Hide the start frame
        self.quiz_frame.pack(fill="both", expand=True)  # Show the quiz frame
        self.new_question()  # Generate the first question

    def new_question(self):
        for button in self.buttons:
            button.config(state=tk.NORMAL)
        self.new_question_button.config(state=tk.NORMAL)
        
        if not self.remaining_questions:
            self.remaining_questions = questions.copy()
        
        self.current_question, self.current_choices, self.correct_answer = random.choice(self.remaining_questions)
        self.remaining_questions.remove((self.current_question, self.current_choices, self.correct_answer))
        
        self.question_label.config(text=self.current_question)
        for i, choice in enumerate(self.current_choices):
            self.buttons[i].config(text=choice)
        self.feedback_label.config(text="Choices", fg="white")

    def check_answer(self, i):
        selected_answer = self.buttons[i].cget("text")
        if selected_answer == self.correct_answer:
            self.feedback_label.config(text="Correct!", fg="blue")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.feedback_label.config(text=f"Incorrect! The correct answer is {self.correct_answer}.", fg="red")
            for button in self.buttons:
                button.config(state=tk.DISABLED)
            self.new_question_button.config(state=tk.DISABLED)

    def restart_game(self):
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.remaining_questions = questions.copy()
        self.new_question()

if __name__ == "__main__":
    window = tk.Tk()
    myApp = QuizGenerator(window)
    window.mainloop()
