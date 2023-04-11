from transformers import MarianMTModel, MarianTokenizer

# Load the model and tokenizer

model_name = "Helsinki-NLP/opus-mt-en-<your_language_code>"

model = MarianMTModel.from_pretrained(model_name)

tokenizer = MarianTokenizer.from_pretrained(model_name)

# Get user input

input_text = input("Enter text to translate: ")

# Get available language codes

langs = model.supported_language_codes

# Prompt user to select a language

print("Select a language to translate to:")

for i, lang in enumerate(langs):

    print(f"{i+1}. {lang}")

lang_idx = int(input()) - 1

target_lang = langs[lang_idx]

# Translate the input text

input_ids = tokenizer.encode(input_text, return_tensors="pt")

output_ids = model.generate(input_ids, num_beams=4, max_length=100, target_language=target_lang)

output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Print the translation

print(f"\nTranslation ({target_lang}):")

print(output_text)

