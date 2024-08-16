import os
from datetime import datetime
from db.db_connector import fetch_data
from report_gen.generate_bar import generate_bar_graph;
from report_gen.generate_pie import generate_pie_chart;
from report_gen.pdf_generator import select_rows;
from report_gen.pdf_generator import generate_pdf

def main():
    # Fetch data from the database
    df = fetch_data()

    # Allow user to select specific rows
    selected_rows = select_rows(df)

    # Generate a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    
    # Ensure the "reports" directory exists within "report_gen"
    reports_dir = os.path.join('reports')
    os.makedirs(reports_dir, exist_ok=True)
    
    # File paths for the PDF and images
    pdf_filename = os.path.join(reports_dir, f"output_{timestamp}.pdf")
    bar_graph_filename = os.path.join(reports_dir, f"bar_graph_{timestamp}.png")
    pie_chart_filename = os.path.join(reports_dir, f"pie_chart_{timestamp}.png")

    # Generate the bar graph and pie chart
    generate_bar_graph(selected_rows, bar_graph_filename)
    generate_pie_chart(selected_rows, pie_chart_filename)

    # Generate the PDF report with the graphs
    generate_pdf(selected_rows, pdf_filename, bar_graph_filename, pie_chart_filename)

if __name__ == "__main__":
    main()