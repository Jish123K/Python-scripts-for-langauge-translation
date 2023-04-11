from transformers import pipeline

# prompt the user for input text

input_text = input("Enter the text to be translated: ")

# prompt the user to select the target language

print("Select the target language: ")

print("1. German")

print("2. French")

print("3. Spanish")

selected_language = int(input("Enter the language number: "))

# define the translation pipeline

if selected_language == 1:

    translator = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")

elif selected_language == 2:

    translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")

elif selected_language == 3:

    translator = pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es")

else:

    print("Invalid language selection.")

    exit()

# perform the translation

translated_text = translator(input_text, max_length=500)[0]["translation_text"]

# display the translation

print("Translated text: ")

print(translated_text)

