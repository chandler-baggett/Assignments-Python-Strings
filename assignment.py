# 1. Product Review Analysis

# Objective:
# The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter

#     Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

words = ["good", "excellent", "bad", "poor", "average"]

def extract_review(reviews):
    for review in reviews:
        for word in words:
            if review.lower().find(word.lower()) != -1:
                print(word.upper())

extract_review(reviews)

# 2. User Input Data Processor

# Objective:
# The aim of this assignment is to process and format user input data.

# Task 1: Input Length Validator
# Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

# Task 2: Password Complexity Checker
# Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number. If the password does not meet these criteria, print a message explaining the complexity requirements.

# Task 3: Email Formatter
# Implement a script that ensures all user email addresses are in a standard format


# def input_length_validator(first_name, last_name):
#     if len(first_name) <= 2 or len(last_name) <= 2:
#         print("Error! First and last names should be at least two characters long")
#     else:
#         print(len(first_name) + len(last_name))
#         return len(first_name) + len(last_name)

# while(True):
#     first_name = input("Enter your first name: ")
#     last_name = input("Enter your last name: ")

#     input_length_validator(first_name, last_name)

# def password_checker(password):
#     if len(password) < 8:
#         print("Error! The password must be equal to or greater than 8 characters long")
#     elif password.lower() == password:
#         print("Error! The password must contain one upper case letter")
#     elif password.upper() == password:
#         print("Error! The password must contain one lowercase letter")
#     elif not any(char.isdigit() for char in password):
#         print("Error! The password must contain at least one number")

# while(True):

#     password = input("Enter a password. The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number: ")

#     password_checker(password)

# import re

# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# def email_formatter(email):
#     if re.fullmatch(regex, email):
#         print("The email address is valid")
#     else:
#         print("The email address is not valid")

# while True:
#     email_address = input("Please enter an email address: ")
#     email_formatter(email_address)

# 3. Interactive Help Desk Bot

# Objective:
# The aim of this assignment is to create an interactive help desk bot that processes user queries and responds appropriately for a SaaS application.

# Task 1: Command Parser
# Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.

# Task 2: Issue Categorizer
# If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. Print out the category of the issue for the support team.

def command_parser(command):
    if "help" in command:
        print("Help can be found by clicking the help button in the menu bar")
    elif "issue" in command:
        if "login" in command:
            print("Please click the forgot username/password links. If additional help is needed, reach out to support by clicking the phone icon in the menu bar.")
        elif "performance" in command:
            print("Please contact support by clicking the phone icon in the menu bar")
        elif "error" in command:
            print("Please contact support by clicking the phone icon in the menu bar")
    elif "contact support" in command:
        print("Support can be contacted by clicking the phone icon in the menu bar")

while(True):
    command = input("Please enter a command: ")
    command_parser(command)