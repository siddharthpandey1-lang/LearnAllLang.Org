print("update 0.0.2 is here")
print("you can now learn more languages")
print("there are many languages you can learn")
language = input("Enter the language you want to learn: ")
print("you have chosen to learn " + language)
print("Great choice! Let's get started with some basics of " + language + ".")
print("Here are some common phrases in " + language + ":")
if language.lower() == "german":
    print("Hello - Hallo")
    print("Thank you - Danke")
    print("Please - Bitte")
elif language.lower() == "irish":
    print("Hello - Dia dhuit")
    print("Thank you - Go raibh maith agat")
    print("Please - Le do thoil")
elif language.lower() == "swahili":
    print("Hello - Jambo")
    print("Thank you - Asante")
    print("Please - Tafadhali")
else:
    print("Sorry, we don't have lessons for that language yet.")
