# generate_visualization.py

import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

DATA_DIR = 'content/data'
MILESTONES_FILE = os.path.join(DATA_DIR, 'milestones.json')
IMAGES_DIR = 'content/images'
os.makedirs(IMAGES_DIR, exist_ok=True)
CHART_FILE = os.path.join(IMAGES_DIR, 'milestones_chart.png')

def load_milestones():
    """Load milestones from JSON."""
    with open(MILESTONES_FILE, 'r') as f:
        milestones = json.load(f)
    return milestones

def plot_milestones(milestones):
    """Plot milestones over time."""
    past_milestones = [m for m in milestones if not m.get('predicted', False)]
    predicted_milestones = [m for m in milestones if m.get('predicted', False)]
    
    past_dates = [datetime.strptime(m['date'], "%Y-%m-%d") for m in past_milestones]
    past_categories = [m['category'] for m in past_milestones]
    predicted_dates = [datetime.strptime(m['date'], "%Y-%m-%d") for m in predicted_milestones]
    predicted_categories = [m['category'] for m in predicted_milestones]
    
    # Assign colors based on category
    category_colors = {
        "Human Creativity": "blue",
        "Generative AI": "green",
        "Other": "gray"
    }
    past_colors = [category_colors.get(cat, "gray") for cat in past_categories]
    predicted_colors = [category_colors.get(cat, "gray") for cat in predicted_categories]
    
    plt.figure(figsize=(12, 6))
    plt.scatter(past_dates, [1]*len(past_dates), color=past_colors, label='Past Milestones', marker='o')
    plt.scatter(predicted_dates, [1.05]*len(predicted_dates), color=predicted_colors, label='Predicted Milestones', marker='x')
    
    # Annotate milestones
    for m in past_milestones:
        date = datetime.strptime(m['date'], "%Y-%m-%d")
        plt.annotate(m['description'], (date, 1), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    for m in predicted_milestones:
        date = datetime.strptime(m['date'], "%Y-%m-%d")
        plt.annotate(m['description'], (date, 1.05), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='red')
    
    plt.yticks([])
    plt.xlabel('Date')
    plt.title('Evolution of Human Creativity and Generative AI')
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHART_FILE)
    plt.close()
    print(f"Saved milestones chart to {CHART_FILE}")

if __name__ == "__main__":
    milestones = load_milestones()
    plot_milestones(milestones)
