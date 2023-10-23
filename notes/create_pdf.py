from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.units import inch
from reportlab.platypus import Spacer
from io import BytesIO
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(Notes, user_id):
    # Retrieve data from your models, including title, description, and due-date
    data = Notes.objects.filter(user=user_id)

    # Create a BytesIO buffer to receive the PDF data
    buffer = BytesIO()

    # Create the PDF document using ReportLab
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Create a list to hold PDF elements
    elements = []

    # Define a style for the heading
    heading_style = getSampleStyleSheet()["Heading1"]

    # Add a heading for each note
    for item in data:
        title = item.title
        description = item.description
        priority = item.priority
        category = item.category
        completed = item.completed
        due_date = item.due_date.strftime("%Y-%m-%d")  # Format due date as desired

        # Create a heading with the title
        heading = Paragraph(title, heading_style)
        elements.append(heading)

        # Add note details
        elements.append(Paragraph(f"Description: {description}", getSampleStyleSheet()["Normal"]))
        elements.append(Paragraph(f"Category: {category}", getSampleStyleSheet()["Normal"]))
        elements.append(Paragraph(f"Due Date: {due_date}", getSampleStyleSheet()["Normal"]))
        elements.append(Paragraph(f"Completed: {completed}", getSampleStyleSheet()["Normal"]))
        elements.append(Paragraph(f"Priority: {priority}", getSampleStyleSheet()["Normal"]))

        # Add some space between notes
        elements.append(Spacer(1, 0.2 * inch))

    # Build the PDF document
    doc.build(elements)

    return buffer
