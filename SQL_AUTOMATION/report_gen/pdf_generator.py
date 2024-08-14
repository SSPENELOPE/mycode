import os
from datetime import datetime
import matplotlib.pyplot as plt
import mysql.connector
from reportlab.lib.pagesizes import letter, landscape, portrait, A4, A3
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors

def generate_bar_graph(data, filename):
    # Extract starting area counts
    starting_areas = [row[1] for row in data]
    area_counts = {area: starting_areas.count(area) for area in set(starting_areas)}

    # Create a bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(area_counts.keys(), area_counts.values(), color='skyblue', edgecolor='black')
    plt.xlabel('Starting Area')
    plt.ylabel('Number of Users')
    plt.title('User Distribution by Starting Area')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Save the bar graph as an image
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

def generate_pie_chart(data, filename):
    # Extract verification status counts
    verification_statuses = [row[2] for row in data]  # Assuming verification status is the 3rd element
    status_counts = {status: verification_statuses.count(status) for status in set(verification_statuses)}

    # Create a pie chart
    plt.figure(figsize=(8, 12))
    plt.pie(status_counts.values(), labels=status_counts.values(), autopct='%1.1f%%', startangle=140, colors=plt.get_cmap('tab20').colors)
    plt.title('User Verification Status')
    plt.tight_layout()

    # Save the pie chart as an image
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

def generate_pdf(data):
    # Generate a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    
    # Ensure the "reports" directory exists within "report_gen"
    reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
    os.makedirs(reports_dir, exist_ok=True)
    
    # Create a timestamped PDF filename in the "reports" directory
    pdf_filename = os.path.join(reports_dir, f"output_{timestamp}.pdf")
    
    # Path for the bar graph and pie chart images
    bar_graph_filename = os.path.join(reports_dir, f"bar_graph_{timestamp}.png")
    pie_chart_filename = os.path.join(reports_dir, f"pie_chart_{timestamp}.png")
    
    # Generate the bar graph and pie chart
    generate_bar_graph(data, bar_graph_filename)
    generate_pie_chart(data, pie_chart_filename)
    
    # Calculate common statistics
    total_users = len(data)
    total_verified_users = sum(row[2] for row in data)  # Assuming row[2] is the boolean verification status

    # Create a PDF file
    pdf = canvas.Canvas(pdf_filename, pagesize=letter)  # Use landscape orientation for more space
    width, height = letter

    # Add title to the PDF
    pdf.setFont('Helvetica-Bold', 16)
    pdf.drawString(inch, height - inch, 'User Statistics Report')
    
    # Add common statistics to the PDF
    pdf.setFont('Helvetica', 12)
    pdf.drawString(inch, height - 1.5*inch, f'Total Users: {total_users}')
    pdf.drawString(inch, height - 2*inch, f'Users Verified: {total_verified_users}')
    
    # Adjust image positions to avoid overlap
    graph_start_y = height - 6*inch  # Adjusted to make room for both images

    # Add the bar graph image to the PDF
    pdf.drawImage(bar_graph_filename, inch, graph_start_y, width=7*inch, height=4*inch)
    
    # Add the pie chart image to the PDF
    pdf.drawImage(pie_chart_filename, inch, graph_start_y - 4*inch - 0.5*inch, width=4*inch, height=4*inch)

    # Save the PDF file
    pdf.save()

    print(f"PDF generated: {pdf_filename}")