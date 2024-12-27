import csv
from fpdf import FPDF

# Function to read data from a CSV file
def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

# Function to generate a PDF report
def generate_pdf_report(data, output_file):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title of the report
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Automated Report", ln=True, align="C")

    # Adding some space
    pdf.ln(10)

    # Table headers
    pdf.set_font("Arial", 'B', 12)
    headers = data[0]  # assuming the first row is headers
    for header in headers:
        pdf.cell(40, 10, txt=header, border=1, align='C')
    pdf.ln()

    # Table rows
    pdf.set_font("Arial", '', 12)
    for row in data[1:]:  # Skipping header row
        for col in row:
            pdf.cell(40, 10, txt=col, border=1, align='C')
        pdf.ln()

    # Save the pdf to a file
    pdf.output(output_file)

# Main function to run the script
def main():
    # Specify the CSV file and the output PDF file
    input_file = 'data.csv'  # Replace with your CSV file path
    output_file = 'report.pdf'

    # Read data from CSV
    data = read_data(input_file)

    # Generate the PDF report
    generate_pdf_report(data, output_file)

    print(f"Report generated successfully: {output_file}")

if __name__ == "__main__":
    main()
