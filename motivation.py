import random

messages = [
    "Keep going!",
    "You are doing great!",
    "Small steps still move forward.",
    "Focus on the next action."
]

name = input ("Enter your name: ")
print(f"Hey {name}, {random.choice(messages)}"