class Question:
    """A class to represent a question in the quiz."""

    def __init__(self, q_text, q_answer):
        """Initialize a new Question object with the given text and answer."""
        self.text = q_text
        self.answer = q_answer
