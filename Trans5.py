import torch

from fairseq.models.transformer import TransformerModel

# Load the pre-trained model

model_name = 'transformer.wmt19.en-de'

model = TransformerModel.from_pretrained(

    model_name,

    checkpoint_file='model1.pt',

    bpe='fastbpe'

)

# Define the available languages

languages = {

    'en': 'English',

    'de': 'German',

    'fr': 'French'

}

# Ask the user for input text

input_text = input('Enter the text to be translated: ')

# Ask the user to select a language

print('Select a language to translate to:')

for code, language in languages.items():

    print(f'{code}: {language}')

target_code = input('Enter the language code: ')

# Translate the input text

input_tokens = model.tokenize(input_text)

input_tokens = input_tokens.to('cuda')

output_tokens = model.generate(input_tokens, beam=5, max_len_b=100)

output_tokens = output_tokens[0].cpu()

output_text = model.decode(output_tokens)

# Print the translation

target_language = languages.get(target_code, 'Unknown')

print(f'Translation to {target_language}:')

print(output_text)

