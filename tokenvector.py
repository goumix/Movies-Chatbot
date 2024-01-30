import pandas as pd
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer


# text = "I would really like to tokenize and vectorize this sentence!" 

# tokenize the text 
# tokenized = nltk.tokenize.word_tokenize(text)


# vectorize the tokens 
# vectorizer = CountVectorizer()
# vectorized = vectorizer.fit_transform(tokenized).toarray()

# print(tokenized)
# print(vectorized)

# Lire le fichier CSV avec pandas
df = pd.read_csv('films.csv')

# Sélectionner la colonne contenant le texte à traiter
text_column = 'Titre' 
print(df[text_column])

text_data = df[text_column].tolist()

# # Tokenisation avec NLTK
# tokenized_data = [word_tokenize(text) for text in text_data]

# # Vectorisation avec CountVectorizer de scikit-learn
# vectorizer = CountVectorizer()
# vectorized_data = vectorizer.fit_transform([' '.join(tokens) for tokens in tokenized_data])

# # Afficher les mots vectorisés
# print(vectorizer.get_feature_names())

# # Afficher les vecteurs correspondants
# print(vectorized_data.toarray())