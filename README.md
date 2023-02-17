# Movie Quiz
## Overview
Movie Quiz is a Python application that lets users test their knowledge of popular movies. The quiz is a series of True/False questions, and users can see their score at the end.

The application is built using Python's Tkinter library for the GUI and is supported on all platforms where Python is available.

## Installation
To install the application, simply clone this repository and run the `main.py` file:

```
$ git clone https://github.com/username/movie-quiz.git
$ cd movie-quiz
$ python movie_quiz.py
```

## Usage
When the application is launched, the user is presented with a question and two buttons: "True" and "False". The user clicks one of the buttons to select their answer, and the application provides feedback in the form of a green or red background. After one second, the application moves on to the next question. At the end of the quiz, the user is presented with their score.

## Customization
The quiz questions are retrieved from the Open Trivia Db using their API. The parameters and API fetch request can be customized to be able to get different questions, categories, types etc.
To learn more go to https://opentdb.com/ 

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.
