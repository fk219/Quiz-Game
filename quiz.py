import random

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    
    def run_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            user_answer = input(question.prompt + "\nYour answer: ")
            if user_answer.lower() == question.answer.lower():
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
        print(f"You've got {self.score}/{len(self.questions)} questions correct.")

class Player:
    def __init__(self, name):
        self.name = name

# Sample questions
questions = [
    Question("What is the capital of France? ", "Paris"),
    Question("Who wrote 'Romeo and Juliet'? ", "William Shakespeare"),
    Question("What is the chemical symbol for water? ", "H2O"),
]

# Main function
def main():
    print("Welcome to the Online Quiz Game!")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    quiz = Quiz(questions)
    quiz.run_quiz()
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
