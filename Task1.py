# Project 1: Rule-Based AI Chatbot
# DecodeLabs - Industrial Training Kit

# KNOWLEDGE BASE: a dictionary with 5+ intents (key : value pairs)
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to meet you.",
    "how are you": "I am a bot, but I am doing great. Thanks for asking!",
    "what is your name": "My name is RuleBot. I was built with if-else logic.",
    "what can you do": "I can chat with you using simple rules.",
    "help": "Try saying: hello, how are you, what is your name, or bye.",
    "thanks": "You are welcome!",
}

# Words that stop the bot (the "kill command")
exit_commands = ["exit", "bye", "quit"]

print("RuleBot: Hello! Type 'bye' or 'exit' to stop.")

# INPUT LOOP: keeps running until we break
while True:
    # PHASE 1: INPUT + SANITIZATION (fix case and spaces)
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()

    # EXIT STRATEGY: clean break
    if clean_input in exit_commands:
        print("RuleBot: Goodbye! Have a nice day.")
        break

    # Empty message check
    if clean_input == "":
        print("RuleBot: Please type something.")
        continue

    # PROCESS + OUTPUT: look up the answer, with a FALLBACK for unknown words
    reply = responses.get(clean_input, "Sorry, I do not understand that.")
    print("RuleBot:", reply)
