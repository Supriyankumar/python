# letting the user choose when to quit

prompt = "\n Tell me something, and I will repeat it back to you: "

prompt += "\n Enter 'quit' to end the program. "

message = " "

while message != 'quit':
    message = input(prompt)

    if message != 'quit' :
        print(message)
