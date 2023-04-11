import subprocess

# Input text from user

input_text = input("Enter the text to translate: ")

# Language selection

print("Select the language to translate to:")

print("1. Spanish")

print("2. French")

print("3. German")

choice = input("Enter your choice (1/2/3): ")

# Translation using Moses

if choice == "1":

    cmd = "echo \"" + input_text + "\" | ~/mosesdecoder/bin/moses -f ~/mosesdecoder/model/translation/en-es/moses.ini"

    translated_text = subprocess.check_output(cmd, shell=True).decode("utf-8")

    print("Translation to Spanish: " + translated_text)

elif choice == "2":

    cmd = "echo \"" + input_text + "\" | ~/mosesdecoder/bin/moses -f ~/mosesdecoder/model/translation/en-fr/moses.ini"

    translated_text = subprocess.check_output(cmd, shell=True).decode("utf-8")

    print("Translation to French: " + translated_text)

elif choice == "3":

    cmd = "echo \"" + input_text + "\" | ~/mosesdecoder/bin/moses -f ~/mosesdecoder/model/translation/en-de/moses.ini"

    translated_text = subprocess.check_output(cmd, shell=True).decode("utf-8")

    print("Translation to German: " + translated_text)

else:

    print("Invalid choice. Please try again.")

