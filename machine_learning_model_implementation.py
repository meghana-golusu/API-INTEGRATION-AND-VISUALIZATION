# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
import os

# Load and extract the dataset from the ZIP file
zip_path = r"C:\Users\megha\Downloads\smsspamcollection.zip"
with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall()  # Extracts all files into the current directory

# Path to the extracted file
file_name = "SMSSpamCollection"

# Read the dataset
df = pd.read_csv(file_name, sep='\t', header=None, names=["label", "message"])

# Display the first few rows of the dataset
print(df.head())

# Preprocessing: Encode the labels (spam = 1, ham = 0)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.3, random_state=42)

# Convert text data to numeric vectors using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Predict on the test data
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Display classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Display confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Optionally, test with a new message
new_message = ["Free entry into the contest, claim your prize now!"]
new_message_tfidf = vectorizer.transform(new_message)
new_prediction = model.predict(new_message_tfidf)

if new_prediction == 1:
    print("Prediction: Spam")
else:
    print("Prediction: Ham")
