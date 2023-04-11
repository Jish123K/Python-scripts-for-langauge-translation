import tensorflow as tf

import tensorflow_datasets as tfds

# Load the pre-trained models from TensorFlow

models = tfds.features.text.SubwordTextEncoder.load_from_file('models.tfds')

# Get a list of available languages for translation

langs = list(models.subwords.keys())

# Ask the user for input text

input_text = input("Enter the text you want to translate: ")

# Ask the user for the target language

print("Select a language to translate to:")

for i, lang in enumerate(langs):

    print(f"{i+1}. {lang}")

target_lang_index = int(input()) - 1

target_lang = langs[target_lang_index]

# Encode the input text and target language

input_text_encoded = models.subwords_to_indices(input_text)

target_lang_encoded = models.subwords_to_indices([target_lang])

# Load the pre-trained translation model for the target language

model = tf.keras.models.load_model(f'models/{target_lang}')

# Perform the translation

output = model.predict(input_text_encoded)

# Decode the output

output_text = models.decode(output)

# Output the translation

print(f"Translation: {output_text}")

