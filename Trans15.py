import torch

from transformers import MarianMTModel, MarianTokenizer

# Load the pre-trained model and tokenizer

model_name = 'Helsinki-NLP/opus-mt-en-<target_language>' # replace <target_language> with the desired language code, e.g. 'fr' for French

model = MarianMTModel.from_pretrained(model_name)

tokenizer = MarianTokenizer.from_pretrained(model_name)

# Prompt the user for input text

text = input("Enter the text to translate: ")

# Prompt the user for the target language

target_language = input("Enter the target language code (e.g. 'fr' for French): ")

# Translate the input text to the target language

translated = model.generate(**tokenizer.prepare_seq2seq_batch([text], return_tensors="pt"))

output = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

# Print the translated text

print("Translation: ", output[0])

