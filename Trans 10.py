from transformers import pipeline

# create a translation pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")

# get input text from user

input_text = input("Enter the text you want to translate: ")

# get language choice from user

target_lang = input("Enter the language code you want to translate to (e.g. 'fr' for French): ")

# translate input text to target language

translated_text = translator(input_text, target_lang=target_lang)

# print translated text

print(translated_text[0]['translation_text'])

