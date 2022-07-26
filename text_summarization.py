import spacy
import heapq
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation


# Open and read document
f = open(r'D:\Learn\Code\text_summarization\text.txt', 'r', errors='ignore')
text = f.read()

# Create stop words list to ignore 
stopwords = list(STOP_WORDS)

# Add model en_core_web_sm from spacy to handle english document
# Convert input to raw text 
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

# Separate each word in a sentence
tokens = [token.text for token in doc]

# Convert to lowercase. Ignore words in stop words list, punctuation. 
# And count the number of occurrences of a word
word_frequencies = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

# The word with the highest number of occurrences
max_frequency = max(word_frequencies.values())

# Occurrence rate of each word (in percent)
for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency

# Separate each sentence in the text
sentence_tokens = [sent for sent in doc.sents]

# Score each sentence
sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]

# Choose the sentences with the appropriate length for the condition
select_lenght = int(len(sentence_tokens)*0.4)

# Sort the sentences in select_lenght by score from highest to lowest
summary = heapq.nlargest(select_lenght, sentence_scores, key=sentence_scores.get)

final_summary = [word.text for word in summary]
summary = ''.join(final_summary)
print(summary)

print('Text: ', len(text))
print('Summary: ', len(summary))
