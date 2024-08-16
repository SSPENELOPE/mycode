import matplotlib.pyplot as plt 
import os

def generate_bar_graph(data, filename_prefix):
    try:
        plt.figure(figsize=(10, 10))
        plt.bar(data[data.columns[0]], data['Count'], color='skyblue', edgecolor='black')
        plt.xlabel('Values')
        plt.ylabel('Count')
        plt.title('Distribution of Values')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        plt.savefig(filename_prefix, bbox_inches='tight')
        plt.close()
        print(f"Saved bar graph as {filename_prefix}")
    except Exception as e:
        print(f"Error generating bar graph: {e}")
