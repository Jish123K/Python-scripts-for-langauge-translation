import deepl_translator

# Take input text from user

input_text = input("Enter the text to translate: ")

# Get list of supported languages for translation

supported_languages = deepl_translator.get_supported_languages()

# Print list of supported languages

print("Select the language to translate to: ")

for lang in supported_languages:

    print(lang)

# Take input language code from user

target_lang = input("Enter the language code to translate to (e.g. 'de' for German): ")

# Use deepl_translator library to translate the text

translated_text = deepl_translator.translate(input_text, target_lang)

# Print the translated text

print("Translated text: ")

print(translated_text)

