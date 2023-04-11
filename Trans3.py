import sys

import subprocess

import os

# check if nematus is installed

try:

    subprocess.check_output(["nematus"])

except OSError:

    print("nematus is not installed. Please install it using 'pip install nematus'")

    sys.exit(1)

# define language codes

LANG_CODES = {

    'en': 'English',

    'fr': 'French',

    'es': 'Spanish',

    'de': 'German',

    'it': 'Italian',

    'ru': 'Russian',

    'zh': 'Chinese',

    'ar': 'Arabic',

    'ja': 'Japanese',

    'ko': 'Korean'

}

# get input text from user

input_text = input("Enter the text to translate: ")

# print available languages for translation

print("Available languages:")

for code, lang in LANG_CODES.items():

    print(f"{code} - {lang}")

# get user's choice of language

target_lang_code = input("Enter the code for the target language: ")

# check if the target language code is valid

if target_lang_code not in LANG_CODES.keys():

    print("Invalid language code.")

    sys.exit(1)

# translate input text

model_dir = "path/to/pretrained/models"

model_name = f"model.{target_lang_code}.npz"

input_file = "input.txt"

output_file = "output.txt"

# write input text to file

with open(input_file, 'w') as f:

    f.write(input_text)

# translate input file to output file using nematus

subprocess.call(["nematus/translate.sh",

                 "-m", os.path.join(model_dir, model_name),

                 "-i", input_file,

                 "-o", output_file])

# read translated text from output file

with open(output_file, 'r') as f:

    translated_text = f.read()

# print translated text

print("Translation:")

print(translated_text)

# delete input and output files

os.remove(input_file)

os.remove(output_file)

