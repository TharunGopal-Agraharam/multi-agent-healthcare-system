from fpdf import FPDF

class ProjectPDF(FPDF):
    def header(self):
        # Add a header to each page
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Multi-Agent Healthcare System - Project Documentation', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        # Add a footer to each page
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_title_page(self, title, author):
        self.add_page()
        self.set_font('Arial', 'B', 24)
        self.cell(0, 60, title, 0, 1, 'C')
        self.set_font('Arial', '', 16)
        self.cell(0, 10, f'Author: {author}', 0, 1, 'C')
        self.ln(20)

    def add_section(self, title, content):
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, content)
        self.ln(10)

    def add_image_page(self, image_path, caption):
        self.add_page()
        self.image(image_path, x=10, y=30, w=190)
        self.ln(150)
        self.set_font('Arial', 'I', 12)
        self.cell(0, 10, caption, 0, 1, 'C')

# Create a PDF document
pdf = ProjectPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Title Page
project_title = "Multi-Agent Healthcare System"
author_name = "Tharun Gopal Agraharam"
pdf.add_title_page(project_title, author_name)

# Introduction Section
introduction = (
    "The Multi-Agent Healthcare System aims to automate healthcare workflows "
    "using advanced multi-agent communication and collaboration. This system provides "
    "patients, healthcare providers, and administrators with a seamless experience while ensuring "
    "efficiency and accuracy in healthcare processes."
)
pdf.add_section("Introduction", introduction)

# Use Case Diagram Section (Placeholder)
use_case_description = (
    "Below is the placeholder for the use case diagram representing interactions between various actors:\n"
    "- Patients: Scheduling appointments, viewing reports.\n"
    "- Healthcare Providers: Managing patient details, generating prescriptions.\n"
    "- Administrators: Monitoring system performance and ensuring compliance."
)
pdf.add_section("Use Case Diagram", use_case_description)

# Flowchart Section (Placeholder)
flowchart_description = (
    "Below is the placeholder for the system workflow:\n"
    "1. Patient requests an appointment.\n"
    "2. System assigns the appropriate healthcare provider.\n"
    "3. Provider consults the patient and updates records.\n"
    "4. Reports are generated and shared with the patient."
)
pdf.add_section("System Flowchart", flowchart_description)

# Real-Time Images Section (Placeholder)
pdf.add_image_page("placeholder_image.jpg", "Example of Real-Time System Interface (Placeholder)")

# Conclusion Section
conclusion = (
    "The Multi-Agent Healthcare System demonstrates the potential of automating healthcare workflows. "
    "Future enhancements may include integrating AI diagnostics, expanding multi-agent communication, and "
    "enhancing patient data security."
)
pdf.add_section("Conclusion", conclusion)

# Save PDF
pdf_output = "Multi-Agent_Healthcare_System.pdf"
pdf.output(pdf_output)
print(f"PDF generated successfully: {pdf_output}")
