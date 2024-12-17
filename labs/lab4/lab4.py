from collections import Counter
import re

text = input("Введіть текст для аналізу: ")

sentences = re.split(r'(?<=[.!?])\s+', text.strip())  
question_sentences = [s for s in sentences if s.endswith('?')]  
words = re.findall(r'\b\w+\b', ' '.join(question_sentences).lower())
word_frequencies = Counter(words)  

print(f"Кількість питальних речень: {len(question_sentences)}")
print("Частота слів у питальних реченнях:")
print(dict(word_frequencies))