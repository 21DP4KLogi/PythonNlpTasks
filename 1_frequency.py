import re
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."
processedText = re.sub("[,.]", "", text).lower()  # Removes punctuation and makes sentence lowercase

tokens = word_tokenize(processedText)
frequencies = FreqDist(tokens)

print("Text:", text)
print("Frequencies:")
for i in frequencies:
    print("   ", i, frequencies[i])

# Sources:
# https://www.nltk.org/api/nltk.probability.html#nltk.probability.FreqDist
# https://stackoverflow.com/questions/4634787/freqdist-with-nltk
# https://www.w3schools.com/python/python_regex.asp#sub
