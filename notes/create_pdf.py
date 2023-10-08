from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors, units
from io import BytesIO


def create_pdf(Notes):
                # Retrieve data from your models, including title, description, and due-date
        data = Notes.objects.all()

        # Create a BytesIO buffer to receive the PDF data
        buffer = BytesIO()

        # Create the PDF document using ReportLab
        doc = SimpleDocTemplate(buffer, pagesize=letter)

        # Create a list to hold table data
        table_data = []

        # Define table headers
        table_data.append(['Title', 'Description', 'Due Date', 'Completed'])

        # Add data to the table
        for item in data:
            title = item.title
            description = item.description
            completed = item.completed
            due_date = item.due_date.strftime("%Y-%m-%d")  # Format due date as desired
            table_data.append([title, description, due_date, completed])

        # Create the table and set styles
        table = Table(table_data, colWidths = [2 * units.inch, 2 * units.inch, 2 * units.inch],rowHeights = 0.4 * units.inch)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        # Build the PDF document
        elements = []
        elements.append(table)
        doc.build(elements)

        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.
        # buffer.seek(0)
        return buffer