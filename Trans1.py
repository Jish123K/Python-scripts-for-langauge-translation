import os

from google.cloud import translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credential/file.json"

# Instantiates a client

translate_client = translate.TranslationServiceClient()

# User Input

input_text = input("Enter the text to translate: ")

# Translate to the desired language

target_language = input("Enter the target language: ")

# The text to translate

text = input_text

# The target language code

target_language_code = target_language

# The source language code, if known

source_language_code = "en"

# Translates the text into the target language

response = translate_client.translate_text(

    request={

        "parent": f"projects/{project_id}",

        "contents": [text],

        "mime_type": "text/plain",

        "source_language_code": source_language_code,

        "target_language_code": target_language_code,

    }

)

# Display the translation

print(f"Input Text: {input_text}")

print(f"Translation: {response.translations[0].translated_text}")

