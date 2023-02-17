# Import the requests module for making HTTP requests
import requests

# Define the parameters for the API request
parameters = {
    "amount": 10,  # Number of questions to fetch
    "category": 11,  # The category of questions to fetch
    "type": "boolean",  # The type of questions to fetch (True/False)
}

# Send an HTTP GET request to the Open Trivia API with the given parameters
response = requests.get("https://opentdb.com/api.php", params=parameters)
# Check if the request was successful (HTTP status code 200)
response.raise_for_status()
# Parse the response data (in JSON format) into a dictionary
data = response.json()
# Extract the list of question dictionaries from the response data
questions = data["results"]
