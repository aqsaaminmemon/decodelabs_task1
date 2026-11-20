# ============================================================
# Project 1: Rule-Based AI Chatbot
# DecodeLabs - Industrial Training Kit (Batch 2026)
# Model used: IPO (Input -> Process -> Output)
# ============================================================
import string

# ---------- KNOWLEDGE BASE (dictionary with 5+ intents) ----------
responses = {
    "how are you": "I am a bot, but I am doing great. Thanks for asking!",
    "what is your name": "My name is RuleBot. I follow rules, I do not guess!",
    "what can you do": "I can greet you, answer simple questions and remember your name.",
    "who made you": "A student AI engineer at DecodeLabs built me using if-else logic.",
    "what is ai": "AI means Artificial Intelligence: machines that do smart tasks.",
    "what is a chatbot": "A chatbot is a program that talks with people using text.",
    "tell me a joke": "Why do programmers like dark mode? Because light attracts bugs!",
    "help": "Try: hello, how are you, what is your name, what is ai, tell me a joke, or bye.",
    "thanks": "You are welcome!",
    "thank you": "You are welcome!",
}

# ---------- COMMAND LISTS ----------
greetings = ["hello", "hi", "hey", "good morning", "good evening", "salam"]
exit_commands = ["exit", "bye", "quit", "goodbye"]

user_name = None  # the bot remembers the name here

print("RuleBot: Hello! I am RuleBot. Type 'bye' or 'exit' to stop.")

# ---------- INPUT LOOP (continuous 'while' cycle) ----------
while True:
    # PHASE 1: INPUT + SANITIZATION (case, spaces, punctuation)
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip().strip(string.punctuation + " ")

    # PHASE 2: PROCESS (if-elif-else logic)

    # 1) EXIT STRATEGY: clean break command
    if clean_input in exit_commands:
        if user_name:
            print("RuleBot: Goodbye " + user_name + "! Have a nice day.")
        else:
            print("RuleBot: Goodbye! Have a nice day.")
        break

    # 2) EMPTY INPUT
    elif clean_input == "":
        print("RuleBot: Please type something.")

    # 3) GREETINGS (with a nested condition)
    elif clean_input in greetings:
        if user_name:
            print("RuleBot: Hello again, " + user_name + "!")
        else:
            print("RuleBot: Hi there! What is your name?")

    # 4) USER TELLS THEIR NAME (nested condition)
    elif clean_input.startswith("my name is "):
        name = clean_input.replace("my name is ", "", 1).strip().title()
        if name:
            user_name = name
            print("RuleBot: Nice to meet you, " + user_name + "!")
        else:
            print("RuleBot: I did not catch your name. Please try again.")

    # 5) ASK THE BOT ABOUT THE USER'S NAME
    elif clean_input == "what is my name":
        if user_name:
            print("RuleBot: Your name is " + user_name + ".")
        else:
            print("RuleBot: I do not know yet. Say 'my name is ...'")

    # 6) KNOWLEDGE BASE LOOKUP
    elif clean_input in responses:
        print("RuleBot:", responses[clean_input])

    # 7) FALLBACK for unknown input
    else:
        print("RuleBot: Sorry, I do not understand that. Type 'help' to see what I know.")
