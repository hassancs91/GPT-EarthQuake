from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import textwrap

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import textwrap

def generate_pdf_report(topic, summaries, content_ideas, tweets,cost,token_count):
    # Create a new PDF document with the given filename
    pdf_filename = 'report.pdf'
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Function to create a new page
    def new_page():
        nonlocal y
        c.showPage()
        y = 750

    # Set the font and font size for the report
    c.setFont("Helvetica", 12)

    # Write the report title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "Report for Topic: {}".format(topic))

    # Write section headings and corresponding text
    y = 700
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Summaries:")
    c.setFont("Helvetica", 12)
    y -= 20
    for summary in summaries:
        for line in textwrap.wrap(summary, width=70):
            c.drawString(50, y, "- " + line)
            y -= 15
            if y < 30:
                new_page()

    # Add a space between sections
    y -= 20
    if y < 30:
        new_page()

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Content Ideas:")
    c.setFont("Helvetica", 12)
    y -= 20
    for idea in content_ideas:
        for line in textwrap.wrap(idea, width=70):
            c.drawString(50, y, "- " + line)
            y -= 15
            if y < 30:
                new_page()

    # Add a space between sections
    y -= 20
    if y < 30:
        new_page()

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Twitter Tweets:")
    c.setFont("Helvetica", 12)
    y -= 20
    for tweet in tweets:
        for line in textwrap.wrap(tweet, width=70):
            c.drawString(50, y, "- " + line)
            y -= 15
            if y < 30:
                new_page()

    # Add a space between sections
    y -= 20
    if y < 30:
        new_page()

   
    
    c.setFont("Helvetica", 14)
    c.drawString(50, y, "Estimated Cost: $ {} for {} tokens".format(cost,token_count))

    # Save the PDF document
    c.save()


  


