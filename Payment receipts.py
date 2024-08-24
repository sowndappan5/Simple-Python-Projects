# Import necessary modules from reportlab 
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 

# Data to be displayed in the table 
receipt_data = [ 
	["Date", "Name", "Subscription", "Price (Rs.)"], 
	[ 
		"16/11/2020", 
		"Full Stack Development with React & Node JS - Live", 
		"Lifetime", 
		"10,999.00/-", 
	], 
	["16/11/2020", "Geeks Classes: Live Session", "6 months", "9,999.00/-"], 
	["Sub Total", "", "", "20,998.00/-"], 
	["Discount", "", "", "-3,000.00/-"], 
	["Total", "", "", "17,998.00/-"], 
] 

# Create a PDF document with A4 page size
pdf_document = SimpleDocTemplate("receipt.pdf", pagesize=A4) 

# Load standard stylesheet from reportlab 
styles = getSampleStyleSheet() 

# Retrieve the style for Heading1 
title_style = styles["Heading1"] 

# Set the alignment for the title (0: left, 1: center, 2: right)
title_style.alignment = 1

# Create a title paragraph with the specified style 
title_paragraph = Paragraph("GeeksforGeeks", title_style) 

# Define table style configurations
table_style = TableStyle( 
	[ 
		("BOX", (0, 0), (-1, -1), 1, colors.black), 
		("GRID", (0, 0), (4, 4), 1, colors.black), 
		("BACKGROUND", (0, 0), (3, 0), colors.gray), 
		("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke), 
		("ALIGN", (0, 0), (-1, -1), "CENTER"), 
		("BACKGROUND", (0, 1), (-1, -1), colors.beige), 
	] 
) 

# Create a table with the data and apply the style 
receipt_table = Table(receipt_data, style=table_style) 

# Build the final PDF document with the title and table 
pdf_document.build([title_paragraph, receipt_table]) 
