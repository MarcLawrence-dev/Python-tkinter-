import tkinter as tk
import random 
 
class Questions:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.currentQuestionIndex  = 0
        self.score = 0
    
    def nextQuestion(self):
        if self.currentQuestionIndex < len(self.questions):
            question = self.questions[self.currentQuestionIndex]
            self.currentQuestionIndex += 1
            return question
        else:
            return None
    
    def checkAnswer(self, question, selectedOption):
        if selectedOption == question.answer:
            self.score += 1
            return True
        else:
            return False

class QuizAppGui:
    def __init__(self, quiz):
        self.quiz = quiz
        self.root = tk.Tk()
        self.root.title("Quiz App")
        self.root.geometry("350x400")
        self.questionLabel = tk.Label(self.root, text="")
        self.questionLabel.grid(row=0, column=3, columnspan=10, pady=50, padx=50)
        self.optionsButton = []
        for i in range(4):
            button = tk.Button(self.root, text="", command=lambda i=i: self.selectOption(i))
            button.grid(row=i+1, column=3, columnspan=10, pady=5, padx=50)
            self.optionsButton.append(button)
        self.scoreLabel = tk.Label(self.root, text="Current Score: 0")
        self.scoreLabel.grid(row=5, column=3, columnspan=10, pady=10)

        self.loadNextQuestion()

        self.quitButton = tk.Button(self.root, text="Quit Quiz", command=self.root.quit)
        self.quitButton.grid(row=7, column=3, columnspan=2, pady=10, padx=50)

        self.evaluateButton = tk.Button(self.root, text="Evaluate Quiz", command=self.quizEvaluation)
        self.evaluateButton.grid(row=7, column=4, columnspan=4, pady=50, padx=40)

        self.quizRetakeButton = tk.Button(self.root, text="Retake Quiz", command=self.quizRetake)
        self.quizRetakeButton.grid(row=7, column=5, columnspan=6, pady=10, padx=50)


    def  quizEvaluation(self):
        if self.quiz.score >= 7:
            self.questionLabel.config(text=f"Congratulations! You passed the quiz, score: {self.quiz.score}/10.")
        else:
            self.questionLabel.config(text=f"Sorry, you failed the quiz, score: {self.quiz.score}/10.")
            
    def loadNextQuestion(self):
        question = self.quiz.nextQuestion()
        if question:
            self.questionLabel.config(text=question.question)
            for i in range(4):
                self.optionsButton[i].config(text=question.options[i])
        else:
            self.questionLabel.config(text="Quiz Completed!")
            for button in self.optionsButton:
                button.config(state=tk.DISABLED)
    
    def selectOption(self, index):
        question = self.quiz.questions[self.quiz.currentQuestionIndex - 1]
        selected_option = question.options[index]
        if self.quiz.checkAnswer(question, selected_option):
            self.scoreLabel.config(text=f"Current Score: {self.quiz.score}")
        self.loadNextQuestion()
    
    def quizRetake(self):
        self.quiz.currentQuestionIndex = 0
        self.quiz.score = 0
        self.scoreLabel.config(text="Current Score: 0")
        for button in self.optionsButton:
            button.config(state=tk.NORMAL)
        self.loadNextQuestion()

questions_dict = [
    Questions("What is the capital of Japan?", ["Paris", "London", "USA", "Tokyo"], "Tokyo"),
    Questions("What is the largest planet in our solar system?", ["Mars", "Venus", "Jupiter", "Saturn"], "Jupiter"),
    Questions("What is the chemical symbol for gold?", ["Ag", "Fe", "Au", "Pb"], "Au"),
    Questions("Who wrote the play 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "William Shakespeare"),
    Questions("What is the smallest prime number?", ["1", "2", "3", "5"], "2"),
    Questions("What is the currency of the United States?", ["Euro", "Yen", "Dollar", "Peso"], "Dollar"),
    Questions("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "Blue Whale"),
    Questions("What is the tallest mountain in the world?", ["K2", "Mount Kilimanjaro", "Mount Everest", "Mount Fuji"], "Mount Everest"),
    Questions("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"], "Pacific Ocean"),
    Questions("What is the chemical symbol for water?", ["CO2", "H2O", "NaCl", "O2"], "H2O")
]

random.shuffle(questions_dict)
quiz = Quiz(questions_dict)
app = QuizAppGui(quiz)

app.root.mainloop()