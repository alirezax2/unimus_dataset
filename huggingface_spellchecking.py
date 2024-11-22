# -*- coding: utf-8 -*-
"""huggingface spellchecking.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13HD72M1CR9-peZ4jGBYnhpqoki6vgLbJ
"""

import pandas as pd
from transformers import pipeline

# Sample DataFrame
data = {
    'artifacts': ['Ths is a test.', 'Another exampl with errrors.', 'coinn' , 'cclothes']
}
df = pd.DataFrame(data)

# Load Hugging Face's spell checking pipeline (or a general text generation model for correction)
# spell_checker = pipeline('text2text-generation', model='vblagoje/bart_lf')
spell_checker = pipeline("text2text-generation",model="oliverguhr/spelling-correction-english-base")

# print(spell_checker("lets do a comparsion",max_length=2048))

# Function to check and correct spelling in a column
def correct_spelling(text):
    corrected = spell_checker(text)
    return corrected[0]['generated_text']

# Apply the function to the 'artifacts' column
df['corrected_artifacts'] = df['artifacts'].apply(correct_spelling)

df

from transformers import T5ForConditionalGeneration, AutoTokenizer

path_to_model = "ai-forever/T5-large-spell"

model = T5ForConditionalGeneration.from_pretrained(path_to_model)
tokenizer = AutoTokenizer.from_pretrained(path_to_model)
prefix = "grammar: "

sentence = "If you bought something goregous bef , after you well be very happy."
sentence = prefix + sentence

encodings = tokenizer(sentence, return_tensors="pt")
generated_tokens = model.generate(**encodings)
answer = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print(answer)

# ["If you bought something gorgeous, you will be very happy."]

