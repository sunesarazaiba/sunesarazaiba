letter = '''Dear<|NAME|>,
Greeting from abc coding house. I am happy to tell you about your selection
You are seleted!
Have a great day ahead!
Thanks and regards,
Bill
Date:<|DATE|>
'''
name = input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date )
print(letter)