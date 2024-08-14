from report_gen.pdf_generator import generate_pdf
from db.db_connector import fetch_data

def main():
    # Fetch data from MySQL
    data = fetch_data()
    print("Data fetched successfully!")
    
    # Generate a PDF with the fetched data
    generate_pdf(data)
    print("PDF generated successfully!")

if __name__ == "__main__":
    main()