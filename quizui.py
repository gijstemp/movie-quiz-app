from tkinter import *
from quiz import Quiz

THEME_COLOR = "#0000FF"


class QuizUI:
    """A class to handle the user interface for a quiz game."""

    def __init__(self, quiz: Quiz):
        """Initialize the QuizUI object.

        Args:
            quiz (Quiz): The Quiz object containing the quiz questions.
        """
        self.quiz = quiz

        # Set up the main window
        self.window = Tk()
        self.window.title("Movie Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Add the score label to the window
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Add the canvas to the window
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Add the true and false buttons to the window
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.true_answered
        )
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image, highlightthickness=0, command=self.false_answered
        )
        self.false_button.grid(row=2, column=1)

        # Display the first quiz question
        self.get_next_question()

        # Start the main event loop
        self.window.mainloop()

    def get_next_question(self):
        """Get the next quiz question and display it on the canvas."""
        # Reset the canvas background color
        self.canvas.config(bg="white")

        if self.quiz.question_left():
            # Update the score label with the current score
            self.score_label.config(text=f"Score: {self.quiz.score}")

            # Get the next question and update the canvas with the question text
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # Display a message on the canvas when the quiz is completed
            self.canvas.itemconfig(self.question_text, text="Quiz completed.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answered(self):
        """Handle the case when the user selects the 'True' answer."""
        self.feedback(self.quiz.check_answer("True"))

    def false_answered(self):
        """Handle the case when the user selects the 'False' answer."""
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        """Provide feedback to the user after an answer is submitted.

        Args:
            is_right (bool): A boolean value indicating whether the submitted answer is correct.
        """
        # Update the canvas background color to green for correct answers or red for incorrect ones
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # Wait for one second and then display the next quiz question
        self.window.after(1000, self.get_next_question)
