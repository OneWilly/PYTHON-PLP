import random

def generate_joke():
    """Randomly selects and prints a joke."""

    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What's a programmer's favorite hangout place? Foo Bar!",
        "Why was the Python developer calm? Because he knew how to 'handle' exceptions!",
        "Why did the computer go to therapy? It had too many bytes of emotional baggage.",
        "There are 10 types of people in the world: those who understand binary, and those who don't.",
        "Why did the database administrator leave his wife? She had one-to-many relationships.",
        "Knock, knock. Who's there? Very long pause... Java.",
        "What do you call a programmer who can't see? A see-sharp developer!",
        "Why did the python dev get lost? He had no path.",
    ]

    random_joke = random.choice(jokes)
    print(random_joke)

generate_joke()