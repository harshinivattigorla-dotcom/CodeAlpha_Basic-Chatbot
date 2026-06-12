def chatbot():
    print("🤖 Welcome to the Basic Chatbot!")
    print("You can say: hello, how are you, bye")
    print("Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            print("Chat ended.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()