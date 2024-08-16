import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image, KeepTogether, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet                                

def select_rows(df):
    print("DataFrame shape before selection:", df.shape)
    print("Here are the first few rows of the data:")
    print(df.head())

    # Ask the user which column they want to summarize
    column_name = input("Enter the column name you want to summarize (e.g., starting_area): ").strip()

    if column_name in df.columns:
        # Count occurrences of each unique value in the specified column
        selected_data = df[column_name].value_counts().reset_index()
        selected_data.columns = [column_name, 'Count']  # Rename columns for clarity
    else:
        print("Invalid column name. Please enter a valid column name from the DataFrame.")
        return select_rows(df)

    print("Shape of selected data:", selected_data.shape)
    print(selected_data)

    return selected_data

def generate_pdf(data, pdf_filename, bar_graph_filename, pie_chart_filename):
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    
    # Title
    title = Paragraph("Summary of Selected Data ", styles['Title'])
    elements.append(title)

    # Table of data
    table_data = [data.columns.tolist()] + data.values.tolist()
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    # Bar Graph
    if os.path.exists(bar_graph_filename):
        bar_heading = Paragraph("Bar Graph: Distribution of Values", styles['Heading2'])
        bar_image = Image(bar_graph_filename, width=400, height=300)
        elements.append(KeepTogether([bar_heading, bar_image]))
    else:
        print(f"Error: Bar graph file not found: {bar_graph_filename}")

    # Spacer between graphs
    elements.append(Spacer(1, 12))  # Adjust spacing as needed

    # Pie Chart
    if os.path.exists(pie_chart_filename):
        pie_heading = Paragraph("Pie Chart: Proportions as Percentages", styles['Heading2'])
        pie_image = Image(pie_chart_filename, width=400, height=300)
        elements.append(KeepTogether([pie_heading, pie_image]))
    else:
        print(f"Error: Pie chart file not found: {pie_chart_filename}")

    # Build the PDF
    doc.build(elements)
    print(f"PDF generated: {pdf_filename}")