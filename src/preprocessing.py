import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_text(text):
    #Set of Stopwords
    stop_words = set(stopwords.words('english')) 
    # Lemmatizer
    lemmatizer = nltk.WordNetLemmatizer()

    #Convert to lowercase
    text = text.lower()
    #Lemmatization and remove stopwords
    tokens = [lemmatizer.lemmatize(word) for word in word_tokenize(text) if word.isalnum()]
    filtered_tokens = [word for word in tokens if word not in stop_words]
    #Join tokens back to a string 
    processed_text = ' '.join(filtered_tokens)
    return processed_text
