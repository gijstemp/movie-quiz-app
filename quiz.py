import html


class Quiz:
    """A class to represent the quiz itself."""

    def __init__(self, q_list):
        """Initialize a new Quiz object with the given list of questions."""
        self.q_number = 0
        self.score = 0
        self.q_list = q_list
        self.current_q = None

    def question_left(self):
        """Return True if there are more questions left to ask, else False."""
        return self.q_number < len(self.q_list)

    def next_question(self):
        """Move on to the next question and return its text."""
        self.current_q = self.q_list[self.q_number]
        self.q_number += 1
        # Use the html.unescape function to decode any special characters in the question text
        q_text = html.unescape(self.current_q.text)
        return f"Q.{self.q_number}: {q_text}"

    def check_answer(self, user_answer):
        """Check if the given answer is correct and return True if it is, else False."""
        correct_answer = self.current_q.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
