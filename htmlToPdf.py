import pdfkit

# Define path to wkhtmltopdf
path_to_wkhtmltopdf = r'/bin/wkhtmltopdf'

# Define path to HTML file
path_to_file = 'index.html'

# Point pdfkit configuration to wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)


# Convert HTML file to PDF
pdfkit.from_file(path_to_file, output_path='mohamed_hafez_resume.pdf', configuration=config)