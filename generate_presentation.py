from pptx import Presentation
from pptx.util import Inches, Pt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Project data
company_name = "Naresh & Co"
subtitle = "Telecommunication Infrastructure & EPC Solutions"
tagline = "Tower Infrastructure | EB Cement Poles | Fiber, Power, & Site Safety"
address = "718/3, T.H Road, Thiruvottiyur, Chennai 600019"
email_list = ["nareshandco@yahoo.com", "sivam@nareshandco.co.in", "muthazhagupandian@nareshandco.co.in"]
phones = ["+91 98840 56221", "+91 72990 25588", "044 – 25726411"]
contact_person = "Sivam (Director)"
gst = "GST: 33ANLPS8411K2ZL"

executive_summary = (
    "Naresh & Co delivers professional telecommunication infrastructure services with end-to-end engineering, construction, installation, commissioning, "
    "and maintenance. We combine telecom tower delivery with in-house manufacturing, safety-driven execution, and multi-technology rollout expertise."
)

core_strengths = [
    "ISO 9001:2015 certified telecom infrastructure delivery",
    "Tower erection up to 55 meters and EB cement pole manufacturing",
    "Supply of EB panel boards, cable trays, clamps, and telecom grounding systems",
    "Multi-vendor experience with AirTel, Vodafone, Huawei, Kone Elevators, TNEB and Radar Systems projects",
    "Safety-first project execution with OHSE management, site audits and compliance"
]

services = [
    "Telecom tower construction, site survey, foundation and civil works",
    "Wireless and wireline installation: 2G, 3G, 4G, 5G, MW, WIFI, IWAN, FTTH, FTTB",
    "Power infrastructure: DG sets, LT/HT cabling, distribution, earthing and lightning protection",
    "EB panel boards, cable trays, clamps, cable management and site equipment supply",
    "Inspection, testing, commissioning, traffic migration and network optimization",
    "Project management, documentation, OHSE compliance and turnkey delivery"
]

supply_services = [
    "EB cement poles and telecom tower foundations",
    "EB panel boards and power distribution systems",
    "Cable trays, clamps, cable ladders and trunking",
    "Grounding, earthing and lightning arrestor systems",
    "Telecom shelter equipment and site utilities"
]

clients = [
    "Bharti Airtel Ltd",
    "Vodafone Idea Ltd",
    "Huawei Telecommunications India Pvt Ltd",
    "Kone Elevators",
    "EASAT Radar Systems Ltd",
    "TNEB",
    "Tech Mahindra Ltd",
    "Data Dimension"
]

safety_measures = [
    "Mandatory PPE for all site personnel",
    "Site-specific safety plans and risk assessments",
    "Regular toolbox talks and emergency drills",
    "High-voltage safety and electrical protection protocols",
    "Quality inspections for all materials and installations"
]

project_images = [
    "images/painted-tower.jpg",
    "images/tower-foundation.jpg",
    "images/EB Cement pole 1.jpg",
    "images/Thailand 1.jpg"
]
project_images = [img for img in project_images if os.path.exists(img)]

pptx_filename = "Naresh_and_Co_Company_Profile_Professional.pptx"
pdf_filename = "Naresh_and_Co_Company_Profile_Professional.pdf"

# Create PPTX
prs = Presentation()

# Cover slide
cover = prs.slides.add_slide(prs.slide_layouts[0])
cover.shapes.title.text = company_name
cover.placeholders[1].text = f"{subtitle}\n{tagline}"

# About slide
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "About Naresh & Co"
body = slide.shapes.placeholders[1].text_frame
body.text = executive_summary

# Services slide
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Our Service Portfolio"
body = slide.shapes.placeholders[1].text_frame
body.text = services[0]
for service in services[1:]:
    p = body.add_paragraph()
    p.text = service
    p.level = 0

# Supply slide
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Supply & Infrastructure"
body = slide.shapes.placeholders[1].text_frame
body.text = supply_services[0]
for item in supply_services[1:]:
    p = body.add_paragraph()
    p.text = item
    p.level = 0

# Safety slide
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Safety & Quality"
body = slide.shapes.placeholders[1].text_frame
body.text = safety_measures[0]
for item in safety_measures[1:]:
    p = body.add_paragraph()
    p.text = item
    p.level = 0

# Clients slide
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Our Clients"
body = slide.shapes.placeholders[1].text_frame
body.text = clients[0]
for client in clients[1:]:
    p = body.add_paragraph()
    p.text = client
    p.level = 0

# Project photo slide
if project_images:
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = "Project Highlights"
    left = Inches(0.75)
    top = Inches(1.6)
    width = Inches(8)
    slide.shapes.add_picture(project_images[0], left, top, width=width)
    if len(project_images) > 1:
        slide.shapes.add_picture(project_images[1], Inches(0.75), Inches(5.0), width=Inches(3.8))
        slide.shapes.add_picture(project_images[2], Inches(5.1), Inches(5.0), width=Inches(3.8))

# Contact slide
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Contact Us"
body = slide.shapes.placeholders[1].text_frame
body.text = f"Address: {address}"
for email in email_list:
    p = body.add_paragraph()
    p.text = f"Email: {email}"
for phone in phones:
    p = body.add_paragraph()
    p.text = f"Phone: {phone}"
p = body.add_paragraph()
p.text = f"Contact Person: {contact_person}"
p = body.add_paragraph()
p.text = gst

prs.save(pptx_filename)

# Create PDF
pdf = canvas.Canvas(pdf_filename, pagesize=A4)
width, height = A4

# Use Helvetica or fallback
font_name = 'Helvetica'
text_color = HexColor('#1f2633')
accent_color = HexColor('#004999')
secondary_color = HexColor('#ff6b35')
light_gray = HexColor('#f4f7fb')

pdf.setFillColor(accent_color)
pdf.rect(0, height - 55 * mm, width, 55 * mm, fill=True, stroke=False)
pdf.setFillColor('#ffffff')
pdf.setFont(font_name, 24)
pdf.drawString(30 * mm, height - 35 * mm, company_name)
pdf.setFont(font_name, 10)
pdf.drawString(30 * mm, height - 45 * mm, subtitle)
pdf.drawString(30 * mm, height - 51 * mm, tagline)

pdf.setFillColor(text_color)
pdf.setFont(font_name, 13)
pdf.drawString(30 * mm, height - 70 * mm, "Executive Summary")
text = pdf.beginText(30 * mm, height - 78 * mm)
text.setFont(font_name, 10)
text.setLeading(14)
for line in executive_summary.split('. '):
    if line.strip():
        text.textLine(line.strip())
pdf.drawText(text)

if project_images:
    try:
        pdf.drawImage(project_images[0], width - 90 * mm, height - 110 * mm, width=55 * mm, height=40 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass

pdf.showPage()

pdf.setFillColor(accent_color)
pdf.rect(0, height - 20 * mm, width, 20 * mm, fill=True, stroke=False)
pdf.setFillColor('#ffffff')
pdf.setFont(font_name, 14)
pdf.drawString(30 * mm, height - 15 * mm, "Our Services & Supply Capabilities")

pdf.setFillColor(text_color)
pdf.setFont(font_name, 10)
text = pdf.beginText(30 * mm, height - 35 * mm)
text.setLeading(12)
for service in services:
    text.textLine(f"• {service}")
pdf.drawText(text)

text = pdf.beginText(110 * mm, height - 35 * mm)
text.setLeading(12)
for item in supply_services:
    text.textLine(f"• {item}")
pdf.drawText(text)

pdf.showPage()

pdf.setFillColor(accent_color)
pdf.rect(0, height - 20 * mm, width, 20 * mm, fill=True, stroke=False)
pdf.setFillColor('#ffffff')
pdf.setFont(font_name, 14)
pdf.drawString(30 * mm, height - 15 * mm, "Safety & Client References")

pdf.setFillColor(text_color)
pdf.setFont(font_name, 10)
text = pdf.beginText(30 * mm, height - 35 * mm)
text.setLeading(12)
text.textLine("Safety & Quality")
for item in safety_measures:
    text.textLine(f"  • {item}")
text.textLine("")
text.textLine("Clients")
for client in clients:
    text.textLine(f"  • {client}")
pdf.drawText(text)

if len(project_images) > 1:
    try:
        pdf.drawImage(project_images[1], width - 90 * mm, height - 120 * mm, width=55 * mm, height=40 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass

pdf.showPage()

pdf.setFillColor(accent_color)
pdf.rect(0, height - 20 * mm, width, 20 * mm, fill=True, stroke=False)
pdf.setFillColor('#ffffff')
pdf.setFont(font_name, 14)
pdf.drawString(30 * mm, height - 15 * mm, "Contact & Engagement")

pdf.setFillColor(text_color)
pdf.setFont(font_name, 10)
text = pdf.beginText(30 * mm, height - 35 * mm)
text.setLeading(12)
text.textLine(f"Address: {address}")
for email in email_list:
    text.textLine(f"Email: {email}")
for phone in phones:
    text.textLine(f"Phone: {phone}")
text.textLine(f"Contact: {contact_person}")
text.textLine(gst)
pdf.drawText(text)

# Editable request form fields
from reportlab.pdfbase.acroform import AcroForm
form = AcroForm(pdf)
pdf.setFont(font_name, 11)
pdf.drawString(30 * mm, height - 90 * mm, "Request a Quote / Message")
form.textfield(name='client_name', tooltip='Client Name', x=30 * mm, y=height - 112 * mm, width=120 * mm, height=8 * mm,
               borderColor=HexColor('#004999'), fillColor=HexColor('#f4f7fb'), textColor=HexColor('#000000'), forceBorder=True)
pdf.drawString(30 * mm, height - 120 * mm, "Name")
form.textfield(name='client_email', tooltip='Client Email', x=30 * mm, y=height - 132 * mm, width=120 * mm, height=8 * mm,
               borderColor=HexColor('#004999'), fillColor=HexColor('#f4f7fb'), textColor=HexColor('#000000'), forceBorder=True)
pdf.drawString(30 * mm, height - 140 * mm, "Email")
form.textfield(name='client_phone', tooltip='Client Phone', x=30 * mm, y=height - 154 * mm, width=120 * mm, height=8 * mm,
               borderColor=HexColor('#004999'), fillColor=HexColor('#f4f7fb'), textColor=HexColor('#000000'), forceBorder=True)
pdf.drawString(30 * mm, height - 162 * mm, "Phone")
form.textfield(name='client_message', tooltip='Message', x=30 * mm, y=height - 210 * mm, width=120 * mm, height=40 * mm,
               borderColor=HexColor('#004999'), fillColor=HexColor('#f4f7fb'), textColor=HexColor('#000000'), forceBorder=True)
pdf.drawString(30 * mm, height - 218 * mm, "Message")

pdf.save()

print(f"Generated files: {pptx_filename}, {pdf_filename}")
