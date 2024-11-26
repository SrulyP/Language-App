# Author: Israel Polasak
# Class: CS361
# GitHub username: SrulyP
# Description: This is a project for CS361 with the intention to learn how to use microservices,
# the Scrum Agile project management framework, as well as working in teams to complete microservices for each other's
# programs. This program helps users decide which FSI language they want to learn, keep track of the languages they
# are currently learning, and helps them research more FSI languages they might potentially learn.


# ZeroMQ setup for the microservices
import zmq
context = zmq.Context()
socketA = context.socket(zmq.REQ)  # Microservice_A, written by Jazzmyne
socketB = context.socket(zmq.REQ)  # Microservice_B
socketC = context.socket(zmq.REQ)  # Microservice_C
socketD = context.socket(zmq.REQ)  # Microservice_D
socketA.connect("tcp://localhost:5555")
socketB.connect("tcp://localhost:5556")
socketC.connect("tcp://localhost:5557")
socketD.connect("tcp://localhost:5558")


class User:
    """Creates a class for a user with their username, pin, and language list"""
    def __init__(self, username, pin, languages_learning=None):
        self._username = username
        self._pin = pin

        if languages_learning is not None:
            self._languages_learning = languages_learning
        else:
            self._languages_learning = []

    def get_username(self):
        return self._username

    def get_pin(self):
        return self._pin

    def get_languages_learning(self):
        return self._languages_learning

    def add_language(self, language):
        language = language.strip().lower().title()
        if language not in self._languages_learning:
            while True:
                yes_or_no = input(f'Are you sure you want to add {language} to your list of languages? Type "yes" to add it, or type "back" to go back: ')
                if yes_or_no.lower() == "yes":
                    self._languages_learning.append(language)
                    print(f"{language} was added to your language list.")
                    return
                elif yes_or_no.lower() == "back":
                    print(f"{language} was not added to your language list.")
                    return
                else:
                    print(f'Unknown response.')
        else:
            print(f"{language} is already in your language list.")
        return

    def remove_language(self, language):
        language = language.strip().lower().title()
        if language in self._languages_learning:
            self._languages_learning.remove(language)
        else:
            print(f"{language} is not in your list of languages.")


# dictionary of [username: user objects] where user object contains a username, pin, and languages_learning list.
users = {}


def homepage():
    """The main function of the app, the 'homepage'."""
    logged_in_user = None
    print('Welcome to the free FSI language information App.')
    while logged_in_user is None:
        signup_or_login = input('\nPlease choose one of the following options:\n'
                                '- Type "1" or "sign up" to create an account.\n'
                                '- Type "2" or "log in" to log into your account if you are a returning user.\n'
                                '- Type "3" or "information" to read about the purpose of this app.\n\n'
                                'What would you like to do?: ')

        if signup_or_login.lower() == "sign up" or signup_or_login.lower() == "1":
            logged_in_user = sign_up()
        elif signup_or_login.lower() == "log in" or signup_or_login.lower() == "2":
            logged_in_user = log_in()
        elif signup_or_login.lower() == "information" or signup_or_login.lower() == "3":
            information()
        else:
            print("Invalid option. Please try again.")

        if logged_in_user is not None:
            logged_in_user = logged_in(logged_in_user)  # go to main functions once user logged in


def sign_up():
    """Signs a user up and returns the user object"""
    while True:
        username = input("Please enter a username: ")
        if username in users:
            print(f"The username {username} is already taken. Please choose another username.")
        else:
            pincode = input("Please enter a pincode: ")
            users[username] = User(username, pincode)
            print(f"Thank you for signing up, {username}!")
            return users[username]  # returns the user object for the username inputted


def log_in():
    """Logs a user into their account and returns the user object"""
    while True:
        username = input("Please enter your username: ")
        if username in users:
            pincode = input("Please enter your pincode: ")
            user = users[username]
            if user.get_pin() == pincode:
                print(f"Welcome back, {username}!")
                return user  # Returns the user object for the username inputted
            else:
                print("Incorrect pincode. Please try again.")
        # if username is not in the usernames (it is not a valid account):
        else:
            # have user choose to go back to the homepage or to retry entering username
            next_action = input('\nThe entered username is not associated with any account. \n'
                                'Please choose one of the following options: \n'
                                '- Type "1" or "homepage" to return to the main menu.\n'
                                '- Type "2" or "retry" to trying entering your username again.\n\n'
                                'What would you like to do?: ')
            if next_action.lower() == "homepage" or next_action == "1":
                return None
            elif next_action.lower() == "retry" or next_action == "2":
                continue
            else:
                print("Invalid input. Please type 'homepage' or 'retry'.")


def information():
    print("The purpose of this app is to help you decide which language described by the FSI "
          "you want to add to your learning journey. \n"
          "To use this app, it is completely free, but you will need to create an account."
          "To do so, you will have to go to the sign up page, and create an account with a username and pincode.\n"
          "You will then have the option to add a language to your list. \n")
    input("Press the Enter key on your keyboard to go back to the main menu.")


def log_out():
    """Logs the user out and returns to the homepage."""
    print("You have been logged out. Returning to the homepage.")
    return None


def logged_in(user):
    """A main function hub to access other functions after the user logs in/signs up."""
    language_learning_list(user)
    while True:
        option = input(
            '\nPlease choose one of the following options:\n'
            '- Type "1" or "add language" to add a new language.\n'
            '- Type "2" or "information" for more information about the app.\n'
            '- Type "3" or "category" to see the FSI category of a language.\n'
            '- Type "4" or "hours" to see the number of hours the FSI estimates it will take to learn a language.\n'
            '- Type "5" or "log out" to log out of your account and be taken to the homepage.\n'
            '- Type "6" or "quit" to quit the program.\n\n'
            'What would you like to do?: '
        )
        option = option.lower().strip()
        if option == "add language" or option == "1":
            language_adder(user)
            if not user.get_languages_learning():
                print("Your language list is currently empty.")
            else:
                print(f"You are currently learning {user.get_languages_learning()}.")
        elif option == "information" or option == "2":
            information()
        elif option == "category" or option == "3":
            language_request = input("Please type the language name: ")
            language_request = language_request.lower().title()
            language_category(language_request)
        elif option == "hours" or option == "4":
            language_request = input("Please type the language name: ")
            language_request = language_request.lower().title()
            language_hours(language_request)
        elif option == "log out" or option == "5":
            return log_out()  # log out the user object and return to the homepage (makes User object None)
        elif option == "quit" or option == "6":
            print("Hope to see you again soon!")
            return False
        else:
            print("Invalid input, try again!")


def language_learning_list(user):
    """Returns a language learning list for a user"""
    if not user.get_languages_learning():
        print("Your language list is currently empty.")
    else:
        print(f"Your current language list includes the following languages: {user.get_languages_learning()}")


def language_adder(user):
    """Adds a language to the user's language list."""
    language = input("What FSI language would you like to add to your list? ")
    language = language.lower().title()
    if valid_language(language):
        user.add_language(language)
        print("Your language list is now updated.")
    else:
        print(f"{language} is not an FSI language, try again!")


def valid_language(language):
    """Validates if a language is an FSI language by checking with Microservice_A if it is in the list."""
    socketA.send_json({"language": language})
    response = socketA.recv_json()
    if response.get("category") != "Language not found.":
        return True
    return False


# Microservice_A
def language_category(language):
    """Returns the category of a language from Microservice_A, implemented by Jazzmyne."""
    socketA.send_json({"language": language})
    response = socketA.recv_json()
    category = response["category"]
    print(f"According to the FSI, the {language} language is of {category}")


# Microservice_B
def language_hours(language):
    """Returns the hours needed to learn a specific language."""
    socketB.send_json({"language": language})
    response = socketB.recv_json()
    hours = response["hours"]
    print(f"According to the FSI, it takes about {hours} to learn the {language} language.")


if __name__ == "__main__":
    homepage()