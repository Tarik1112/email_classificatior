import pandas as pd
import random

# Set a random seed for reproducibility
random.seed(42)

# Generate a synthetic dataset
num_samples = 100
subjects = ["Meeting", "Project Update", "Lunch Plans", "Weekend Plans", "Vacation", "Report", "Research Proposal"]
messages = ["Hi, let's catch up for lunch tomorrow.", "Attached is the project update for this week.",
            "Are you free for a meeting this afternoon?", "Let's plan a weekend getaway.",
            "I'm on vacation next week, will be out of office.", "Please find the attached report.",
            "I have attached the research proposal for your review."]

data = {'subject': [], 'message': [], 'label': []}

for _ in range(num_samples):
    subject = random.choice(subjects)
    message = random.choice(messages)
    label = random.choice(['Personal', 'Work', 'University'])

    data['subject'].append(subject)
    data['message'].append(message)
    data['label'].append(label)

# Create a DataFrame from the generated data
df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv('email_dataset.csv', index=False)

# Display the first few rows of the dataset
print(df.head())
