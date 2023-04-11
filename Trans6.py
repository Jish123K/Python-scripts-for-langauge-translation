import torch

from transformers import T5ForConditionalGeneration, T5Tokenizer

# load the T5 model and tokenizer

model = T5ForConditionalGeneration.from_pretrained('t5-base')

tokenizer = T5Tokenizer.from_pretrained('t5-base')

# get user input

input_text = input("Enter the text to translate: ")

# get the available language options for translation

languages = ['en', 'es', 'fr', 'de']

print("Select the language to translate to:")

for i, lang in enumerate(languages):

    print(f"{i+1}. {lang}")

# get user choice for the target language

choice = int(input()) - 1

target_language = languages[choice]

# prepare the input for the T5 model

input_ids = tokenizer.encode(input_text, return_tensors='pt')

decoder_input_ids = tokenizer.encode(f"translate {input_text} to {target_language}", return_tensors='pt')

# generate the translation

outputs = model.generate(input_ids=input_ids, decoder_input_ids=decoder_input_ids)

translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

# print the translation

print(f"The translation to {target_language} is:\n{translated_text}")

