# Question

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer

# Quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0

    def get_question(self):
        if self.load_questions():
            return self.questions[self.current_question_index]
        else:
            return None
        
    def display_question(self):
        question = self.get_question()
        print(f"Question {self.current_question_index + 1}: {question.text}")
        for i, choice in enumerate(question.choices):
            print(f"{i + 1}. {choice}")

        user_answer = input("Your answer (type the choice number): ")
        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        question = self.get_question()
        if question.check_answer(user_answer):
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect.")
        
        self.current_question_index += 1
        if self.load_questions():
            self.display_question()
        else:
            self.show_score()

    def load_questions(self):
        return self.current_question_index < len(self.questions)
    
    def show_score(self):
        print(f"Quiz finished! Your score: {self.score}/{len(self.questions)}")
        

q1 = Question(
    "What is the capital of France?",
    ["Berlin", "Madrid", "Paris", "Rome"],
    "3"
)
q2 = Question(
    "What is 2 + 2?",
    ["3", "4", "5", "6"],
    "2"
)
q3 = Question(
    "What is the largest planet in our solar system?",
    ["Earth", "Mars", "Jupiter", "Saturn"],
    "3"
)
list_of_questions = [q1, q2, q3]

quiz = Quiz(list_of_questions)
quiz.display_question()
