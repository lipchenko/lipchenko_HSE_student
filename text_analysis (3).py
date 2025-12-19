

import re
from collections import Counter

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    return data

def clean_text(text):
    cleaned_text = re.sub(r'<[^>]+>', '', text)
    cleaned_text = cleaned_text.lower()
    return cleaned_text

def tokenize_text(text):
  
    new_text = re.sub(r'[^а-яёa-z0-9.,!?;: -]', ' ', text)
    new_text = re.sub(r'\s+', ' ', new_text).strip()
    tokens = new_text.split()
    return tokens

def create_frequency_dict(tokens):
    freq_dict = Counter(tokens)
    return freq_dict

if __name__ == "__main__":

      text = load_data("MovieCorpus.txt")
      print(f"Длина файла: {len(text)}")
      print("Первые 200 символов:", text[:200])
      
      cleaned_text = clean_text(text)
      tokens = tokenize_text(cleaned_text)  
      print("После токенизации:", tokens[:200])

      freq_dict = create_frequency_dict(tokens)  
      print("Самые частые слова:", freq_dict.most_common(5))
