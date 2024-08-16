import matplotlib.pyplot as plt 
import os

def generate_pie_chart(data, filename_prefix):
    try:
        plt.figure(figsize=(8, 8))
        plt.pie(data['Count'], labels=data[data.columns[0]], autopct='%1.1f%%', colors=plt.get_cmap('Set2').colors)
        plt.title('Proportions as Percentages')
        plt.tight_layout()

        plt.savefig(filename_prefix, bbox_inches='tight')
        plt.close()
        print(f"Saved pie chart as {filename_prefix}")
    except Exception as e:
        print(f"Error generating pie chart: {e}")