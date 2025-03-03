#define all the functions first
#-------------------------------------------------------------------------
def new_game(): #everytime this is called it will create a new game for us
    
    guesses = []
    corect_guesses = 0
    question_num = 1 #index 1 represents the first question

    for key in questions: #display all questions within the dictionary
        print("#------------------------------") #represent a line break to separate each question
        print(key)
        for i in options[question_num-1]: #display all the possible options for each question using nested for loop, but since we use question_num-1 it will only display that option in that index -1 being that elements always starts at 0, and since the value is 1 we counter it by -1 to make it 0
            print(i)
        guess = input("Enter (A, B, C, D): ")# user input
        guess = guess.upper() #make it so every input is automatic upper case
        guesses.append(guess)

        corect_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(corect_guesses, guesses) #display final score

#-------------------------------------------------------------------------
def check_answer(answer, guess):
    
    if answer == guess : #checks to see if answer is equal to guess
        print("Correct!")
        return 1         #returns 1 as a point back to the correct guesses
    else: #if its not the correct answer
        print("Wrong")
        return 0
    
#-------------------------------------------------------------------------
def display_score(correct_guesses, guesses): #parameterse
     print("#------------------------------")
     print("Results")
     print("#------------------------------")

     print("Answers: ", end="")                                                 
     for i in questions:   #display all the values within the dictionary
         print(questions.get(i), end=" ") #since we dont want to end on a new line we set end to nothing
     print() #print new line

     print("Guesses: ", end="")                                                 
     for i in guesses:   #display all the guesses
         print(i, end=" ") #prints i 
     print() #print new line

     #calculate the final score
     score = int((correct_guesses/len(questions))*100) #we cast an int to that it wont include the decimal portions
     print("Your score is: " +str(score)+"%")
#-------------------------------------------------------------------------
def play_again():
    
    response = input("Do you want to play again?:  (Yes or No): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False
#-------------------------------------------------------------------------

#collections to hold all the questions and answers [dictionary]
questions = {
    "Who created Python? :": "A",
    "What year was Python Created? :  ": "B",
    "Python is tributed to which comedy group? :": "C",
    "Is my Balls Round? :": "A"
}
#collections to hold all possible answers    [2d list]
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Joe Rogan", "D. Ligma Balls"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. RDC World"],
           ["A. True", "B. False", "C. Sometimes", "D. None of the above"]]

#call the new game function
new_game()

while play_again():
    new_game()

print("Bye")

