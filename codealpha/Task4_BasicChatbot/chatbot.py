print("===== BASIC CHATBOT =====")
print("Type 'bye' to exit.")

while True:
    user = input("\nYou: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hi! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user == "what is your name":
        print("Bot: I'm a simple Python chatbot.")

    elif user == "help":
        print("Bot: You can say hello, ask how I am, or say bye.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")