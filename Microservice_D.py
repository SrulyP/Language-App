import zmq
import random

print("Starting Microservice_D server...")
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5558")
print("Microservice_D server connected successfully.")

language_learning_tips = [
    "Practice speaking with native speakers to build confidence.",
    "Consistency is key: Try to practice every day, even if it's just for 15 minutes.",
    "Don't be afraid to make mistakes. They are a natural part of the learning process.",
    "Immerse yourself in the language: watch movies, listen to music, or read books in the target language.",
    "Focus on learning useful vocabulary that you will use in everyday conversations.",
    "Use flashcards or spaced repetition systems to memorize new vocabulary.",
    "Set specific, measurable goals: Aim to learn a set number of words or phrases each week to stay motivated.",
    "Participate in online language communities or find a language exchange partner to practice with.",
    "Don't translate everything: Try thinking in the target language instead of translating from your native language.",
    "Focus on learning the most commonly used phrases and sentences that you’ll use in daily conversations.",
    "Spend a few minutes every day revisiting previous lessons to reinforce what you've learned.",
    "Practice speaking the language daily, even if you only have time to say a few sentences or read aloud."
]

while True:
    print("Waiting for request...")
    request = socket.recv_json()
    print("Request received. Returning tip now.")
    response = {"tips": random.choice(language_learning_tips)}
    print("Sending response back to client.")
    socket.send_json(response)