import fasttext

import os

# Load the pre-trained models

model_path = 'cc.en.300.bin' # This is the path to the pre-trained English model, change it to the appropriate path for your system

if not os.path.exists(model_path):

    print("Model not found. Please download the model from the FastText website (https://fasttext.cc/docs/en/crawl-vectors.html) and place it in the same directory as this script.")

    exit()

english_model = fasttext.load_model(model_path)

model_path = 'cc.fr.300.bin' # This is the path to the pre-trained French model, change it to the appropriate path for your system

if not os.path.exists(model_path):

    print("Model not found. Please download the model from the FastText website (https://fasttext.cc/docs/en/crawl-vectors.html) and place it in the same directory as this script.")

    exit()

french_model = fasttext.load_model(model_path)

# Get input text from user

text = input("Enter the text you want to translate: ")

# Ask user to select target language

print("Select target language:")

print("1. French")

print("2. English")

choice = int(input("Enter your choice (1 or 2): "))

# Translate the text based on user's choice of target language

if choice == 1:

    translated_text = french_model.predict(text, k=1)[0][0]

elif choice == 2:

    translated_text = english_model.predict(text, k=1)[0][0]

else:

    print("Invalid choice. Please select 1 or 2.")

    exit()

# Print the translated text

print("Translated text:")

print(translated_text)

