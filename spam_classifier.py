import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB #multinomialNB is used for text classification problems, especially when the features are word counts or term frequencies. 
from sklearn.metrics import accuracy_score, classification_report


df = pd.read_csv("spam.csv", encoding='latin-1')

df = df[['v1', 'v2']]
df.columns = ['label', 'message']


df['label'] = df['label'].map({'ham': 0, 'spam': 1})


X = df['message']
y = df['label']

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("===============================================================================")

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
print("===============================================================================")

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Test Custom Email
while True:
    email = input("\nEnter email text (or 'quit' to exit): ")

    if email.lower() == "quit":
        break

    email_vector = vectorizer.transform([email])
    prediction = model.predict(email_vector)

    if prediction[0] == 1:
        print("SPAM EMAIL")
    else:
        print("NOT SPAM")