import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
    
# nltk.download('punkt')

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

# Convert sentence into single words (Tokenize) and store in an array
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    pass

a = "How long does shipping take?"
print(a)
a = tokenize(a)
print(a)

words = ["sleeping", "sleeps", "sleep", "slept"]
stemmed_words = [stem(w) for w in words]
print(stemmed_words)
