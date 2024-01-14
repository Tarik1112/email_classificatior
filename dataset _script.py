import pandas as pd
import random

# Set a random seed for reproducibility
random.seed(42)

# Generate a synthetic dataset
num_samples = 1000
subjects = ["Meeting", "Project Update", "Lunch Plans", "Weekend Plans", "Vacation", "Report", "Research Proposal"]
messages = [
    "Hi, let's catch up for lunch tomorrow.",
    "Attached is the project update for this week.",
    "Are you free for a meeting this afternoon?",
    "Let's plan a weekend getaway.",
    "I'm on vacation next week, will be out of office.",
    "Please find the attached report.",
    "I have attached the research proposal for your review.",
    "We need to discuss the budget for the upcoming project.",
    "Reminder: Team meeting at 3 PM today.",
    "Can you share your availability for the upcoming week?",
    "Let's schedule a call to discuss the client's requirements.",
    "The deadline for submitting the proposal is approaching.",
    "I'll be working remotely for the next few days.",
    "Please review the latest version of the document.",
    "Congratulations on completing the project successfully!",
    "Don't forget to submit your timesheet for this week.",
    "The conference has been rescheduled to next month.",
    "I'll be attending a workshop on data science next week.",
    "Reminder: Submit your travel expenses by the end of the month.",
    "I need your input on the new project proposal.",
]

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
