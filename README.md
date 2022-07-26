# text-summary-use-spacy-library
- Input: file .txt contain text
- Output: The text is shortened but the meaning remains the same
- Steps:
1) Open and read document.
2) Create stop words list to ignore them.
3) Add model "en_core_web_sm" from spacy library to natural language processing.
4) Convert input to raw text.
5) Separate each word in a sentence.
6) Convert to lowercase, ignore words in stop words list and punctuation. 
7) Count the number of occurrences of a word and save to the dictionary.
8) Find the word with the highest number of occurrences.
9) Separate each sentence in the text.
10) Score each sentence.
11) Choose the sentences with the appropriate length for the condition.
12) Sort the sentences in select_lenght by score from highest to lowest.
13) Remove the summary from the list.
---> Get the complete summary.

