import re
import nltk
import string

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)

    tokens = text.split()

    tokens = [w.translate(str.maketrans('', '', string.punctuation)) for w in tokens]

    tokens = [w for w in tokens if w.isalpha() and len(w)]

    tokens = [w for w in tokens if w not in stop_words]

    tokens = [stemmer.stem(w) for w in tokens]

    return " ".join(tokens)