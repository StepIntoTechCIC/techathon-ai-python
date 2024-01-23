import techathonai

USER_KEY = "test"

techathonai.connect(USER_KEY)

question = input("What question would you like to ask the computer? ")
prompt = "Q: " + question + "\nA: "

print("Your answer is:", techathonai.complete(prompt))

print("Balance remaining:", techathonai.getBalance(), "tokens")