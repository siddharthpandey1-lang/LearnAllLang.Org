print("what do you want to learn?")
language = input("Enter the language you want to learn: ")
print("you have chosen to learn " + language)
print("Great choice! Let's get started with some basics of " + language + ".")
print("Here are some common phrases in " + language + ":")
if language.lower() == "french":
    print("Hello - Bonjour")
    print("Thank you - Merci")
    print("Please - S'il vous plaît")
elif language.lower() == "spanish":
    print("Hello - Hola")
    print("Thank you - Gracias")
    print("Please - Por favor")
elif language.lower() == "german":
    print("Hello - Hallo")
    print("Thank you - Danke")
    print("Please - Bitte")
elif language.lower() == "italian":
    print("Hello - Ciao")
    print("Thank you - Grazie")
    print("Please - Per favore")
else:
    print("Sorry, we don't have lessons for that language yet.")