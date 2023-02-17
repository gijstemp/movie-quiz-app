from question_class import Question
from data import questions
from quiz import Quiz
from quizui import QuizUI

# Create an empty list to hold the Question objects
q_list = []

# Loop over each question in the questions list
for question in questions:
    # Extract the question text and correct answer from the dictionary
    q_text = question["question"]
    q_answer = question["correct_answer"]
    # Create a new Question object using the extracted text and answer
    question_object = Question(q_text, q_answer)
    # Add the new Question object to the list
    q_list.append(question_object)

# Create a new Quiz object using the list of Question objects
quiz_object = Quiz(q_list)
# Create a new QuizUI object using the Quiz object
quiz_ui_object = QuizUI(quiz_object)
