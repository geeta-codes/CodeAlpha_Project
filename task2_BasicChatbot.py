# A simple Chatbot

def chatbot():
    # Welcome message 
    print("Chatbot : Hello!! wants to talk to me?? ")

    while True:
        # Take input from user 
        user = input ("you:").lower().strip()
        if user == "hello":
            print("Chatbot:Hi!")

        elif user == "how are you":
            print("chatbot: I'm fine , Thanks!")

        elif user == "bye":
            print("Chatbot : Goodbye! Have a nice day")

        else:
            print("Chatbot : Sorry! I can't understand")

# Call the function 
chatbot()