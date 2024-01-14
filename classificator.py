# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def classify_email(subject, message):
    # Combine subject and message into a single text
    email_text = f"{subject} {message}"

    # Vectorize the input text
    input_features = vectorizer.transform([email_text])

    # Make a prediction
    prediction = classifier.predict(input_features)[0]

    return prediction


if __name__ == '__main__':
    # Load your email dataset (assuming you have a CSV file with 'subject', 'message', and 'label' columns)
    # Replace 'your_dataset.csv' with the actual file path and name
    dataset = pd.read_csv('email_dataset.csv')

    # Assuming 'label' column contains 'Personal' and 'Work' labels
    # You can adjust these labels based on your dataset
    labels = ['Personal', 'Work']

    # Combine 'subject' and 'message' into a single 'text' column
    dataset['text'] = dataset['subject'] + ' ' + dataset['message']

    # Convert the text data into numerical features using CountVectorizer
    vectorizer = CountVectorizer()
    features = vectorizer.fit_transform(dataset['text'])

    # Train a Naive Bayes classifier
    classifier = MultinomialNB()
    classifier.fit(features, dataset['label'])

    # Take input from the user
    subject = input("Enter the email subject: ")
    message = input("Enter the email message: ")

    # Classify the email
    classification = classify_email(subject, message)

    # Display the result
    print(f"The email is classified as: {classification}")