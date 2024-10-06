# generate_milestones.py

import json
import os
from datetime import datetime, timedelta
import random

DATA_DIR = 'content/data'
os.makedirs(DATA_DIR, exist_ok=True)
MILESTONES_FILE = os.path.join(DATA_DIR, 'milestones.json')

def initial_milestones():
    """Define initial historical milestones."""
    return [
        {
            "date": "1950-01-01",
            "description": "Alan Turing proposes the Turing Test.",
            "category": "Human Creativity"
        },
        {
            "date": "1956-08-30",
            "description": "Dartmouth Workshop - Birth of Artificial Intelligence as a field.",
            "category": "Human Creativity"
        },
        {
            "date": "2014-06-19",
            "description": "Generative Adversarial Networks (GANs) introduced by Ian Goodfellow.",
            "category": "Generative AI"
        },
        {
            "date": "2020-06-11",
            "description": "OpenAI releases GPT-3, a powerful language model.",
            "category": "Generative AI"
        },
        {
            "date": "2023-03-14",
            "description": "DALL·E 2 released, enabling high-quality image generation from text.",
            "category": "Generative AI"
        }
        # Add more initial milestones as needed
    ]

def load_milestones():
    """Load milestones from JSON or initialize."""
    if os.path.exists(MILESTONES_FILE):
        with open(MILESTONES_FILE, 'r') as f:
            milestones = json.load(f)
        print(f"Loaded {len(milestones)} milestones.")
    else:
        milestones = initial_milestones()
        save_milestones(milestones)
        print("Initialized with initial milestones.")
    return milestones

def save_milestones(milestones):
    """Save milestones to JSON."""
    with open(MILESTONES_FILE, 'w') as f:
        json.dump(milestones, f, indent=4)
    print(f"Saved {len(milestones)} milestones.")

def predict_future_milestones(milestones, num_predictions=5):
    """Predict future milestones based on existing data."""
    last_date_str = milestones[-1]['date']
    last_date = datetime.strptime(last_date_str, "%Y-%m-%d")
    predictions = []
    for _ in range(num_predictions):
        # Predict a milestone 1 to 3 years after the last prediction
        delta_years = random.randint(1, 3)
        next_date = last_date + timedelta(days=365 * delta_years)
        next_date_str = next_date.strftime("%Y-%m-%d")
        # Generate a dummy description
        description = f"Predicted advancement in Generative AI at {next_date.year}."
        category = "Generative AI"
        prediction = {
            "date": next_date_str,
            "description": description,
            "category": category,
            "predicted": True  # Flag to indicate prediction
        }
        predictions.append(prediction)
        last_date = next_date
    # Append predictions to milestones
    milestones.extend(predictions)
    save_milestones(milestones)
    print(f"Added {num_predictions} predicted milestones.")
    return milestones

if __name__ == "__main__":
    milestones = load_milestones()
    milestones = predict_future_milestones(milestones, num_predictions=3)
