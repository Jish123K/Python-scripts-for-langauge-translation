import spacy

# load pre-trained models for translation

nlp_en = spacy.load('en_core_web_sm')

nlp_de = spacy.load('de_core_news_sm')

nlp_fr = spacy.load('fr_core_news_sm')

# get input text from user

text = input('Enter text to translate: ')

# display language options to the user

print('Select language to translate to:')

print('1. German')

print('2. French')

# get user's language choice

choice = int(input('Enter choice number (1 or 2): '))

# translate the input text based on user's choice

if choice == 1:

    doc = nlp_en(text)

    translation = ' '.join([token.text for token in doc])

    print('German translation: ' + translation)

elif choice == 2:

    doc = nlp_en(text)

    translation = ' '.join([token.text for token in doc])

    print('French translation: ' + translation)

else:

    print('Invalid choice')

