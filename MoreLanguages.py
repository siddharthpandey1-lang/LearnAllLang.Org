print("there are many languages you can learn")
language = input("Enter the language you want to learn: ")
print("you have chosen to learn " + language)
print("Great choice! Let's get started with some basics of " + language + ".")
print("Here are some common phrases in " + language + ":")
if language.lower() == "chainese":
    print("Hello - 你好 (Nǐ hǎo)")
    print("Thank you - 谢谢 (Xièxiè)")
    print("Please - 请 (Qǐng)")
elif language.lower() == "japanese":
    print("Hello - こんにちは (Konnichiwa)")
    print("Thank you - ありがとう (Arigatō)")
    print("Please - お願いします (Onegaishimasu)")
else:
    print("Sorry, we don't have lessons for that language yet.")
print("you can learn more languages in the next update")    
print("stay tuned for more updates")
print("thank you for using LearnAllLang.Org")
print("goodbye")