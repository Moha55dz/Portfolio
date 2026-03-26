#!/usr/bin/env python3
"""
Portfolio PDF Generator
Generates a comprehensive PDF document with portfolio information, certificates, and projects links
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from datetime import datetime
import os

# Create PDF
pdf_path = os.path.join(os.path.dirname(__file__), "Mohamed_Portfolio.pdf")
doc = SimpleDocTemplate(pdf_path, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)

# Container for PDF elements
elements = []

# Define styles
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=28,
    textColor=colors.HexColor('#6366f1'),
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

subtitle_style = ParagraphStyle(
    'CustomSubtitle',
    parent=styles['Normal'],
    fontSize=12,
    textColor=colors.HexColor('#64748b'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica'
)

section_title_style = ParagraphStyle(
    'SectionTitle',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.HexColor('#6366f1'),
    spaceAfter=12,
    spaceBefore=12,
    fontName='Helvetica-Bold'
)

content_style = ParagraphStyle(
    'ContentStyle',
    parent=styles['Normal'],
    fontSize=11,
    textColor=colors.HexColor('#1e293b'),
    alignment=TA_JUSTIFY,
    spaceAfter=10,
    fontName='Helvetica'
)

# ==================== HEADER ====================
elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph("Mohamed", title_style))
elements.append(Paragraph("Front-End Developer | Web Developer", subtitle_style))
elements.append(Spacer(1, 0.15*inch))

# Contact info
contact_data = [
    ["📧 mohamedaba012@gmail.com", "📍 Algeria", "🔗 linkedin.com/in/mohamed-aba"],
    ["🐙 github.com/Moha55dz", "📷 @dev_dz_studio", "👤 Age: 18"]
]
contact_table = Table(contact_data, colWidths=[2.2*inch, 2.2*inch, 2.2*inch])
contact_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#475569')),
]))
elements.append(contact_table)
elements.append(Spacer(1, 0.1*inch))

# ==================== ABOUT SECTION ====================
elements.append(Paragraph("About Me", section_title_style))
about_text = """
I am a passionate Front-End Developer with a keen eye for design and a drive to create seamless digital 
experiences. I specialize in building robust and scalable web applications using modern technologies. 
Currently advancing my expertise in React and Django with a focus on creating responsive, user-centric 
web experiences with clean, maintainable code.
"""
elements.append(Paragraph(about_text, content_style))
elements.append(Spacer(1, 0.08*inch))

# ==================== SKILLS SECTION ====================
elements.append(Paragraph("Technical Skills", section_title_style))
skills_data = [
    ["HTML", "CSS", "JavaScript", "Python"],
    ["95%", "90%", "85%", "70%"],
    ["Git", "React", "Django", "Chart.js"],
    ["80%", "75%", "70%", "75%"]
]
skills_table = Table(skills_data, colWidths=[1.575*inch]*4)
skills_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e0e7ff')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#6366f1')),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('FONTSIZE', (0, 1), (-1, 1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('TOPPADDING', (0, 0), (-1, 0), 8),
    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#cbd5e1')),
    ('ROWBACKGROUNDS', (0, 2), (-1, -1), [colors.white, colors.HexColor('#f8fafc')]),
    ('FONTNAME', (0, 2), (-1, -1), 'Helvetica'),
]))
elements.append(skills_table)
elements.append(Spacer(1, 0.1*inch))

# ==================== CERTIFICATES SECTION ====================
elements.append(Paragraph("Certificates & Achievements", section_title_style))

certificates = [
    {
        "title": "Web & App Development",
        "issuer": "Caravan2Digital",
        "date": "2025",
        "link": "https://moha55dz.github.io/Portfolio/assets/certificates/web-app-certificate.html"
    },
    {
        "title": "ICSC Final Round",
        "issuer": "International Coding & Science Competition",
        "date": "2025",
        "link": "https://moha55dz.github.io/Portfolio/assets/certificates/icsc-final-certificate.html"
    },
    {
        "title": "ICSC Pre-Final Round",
        "issuer": "International Coding & Science Competition",
        "date": "2025",
        "link": "https://moha55dz.github.io/Portfolio/assets/certificates/icsc-prefinal-certificate.html"
    },
    {
        "title": "ICSC Qualification Round",
        "issuer": "International Coding & Science Competition",
        "date": "2025",
        "link": "https://moha55dz.github.io/Portfolio/assets/certificates/icsc-qualification-certificate.html"
    },
    {
        "title": "Python Programming",
        "issuer": "Programming",
        "date": "2025",
        "link": "https://moha55dz.github.io/Portfolio/assets/certificates/python-certificates.html"
    }
]

cert_data = []
for idx, cert in enumerate(certificates, 1):
    cert_data.append([
        f"{idx}.",
        f"{cert['title']}\n{cert['issuer']}\n{cert['date']}\n🔗 {cert['link']}",
    ])

cert_table = Table(cert_data, colWidths=[0.4*inch, 5.6*inch])
cert_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#1e293b')),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
    ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, colors.HexColor('#f8fafc')]),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
]))
elements.append(cert_table)
elements.append(Spacer(1, 0.08*inch))

# ==================== PROJECTS SECTION ====================
elements.append(Paragraph("Featured Projects", section_title_style))

projects = [
    {
        "title": "E-Commerce Platform",
        "description": "A full-featured online store with cart functionality and payment integration.",
        "technologies": ["HTML", "CSS", "JavaScript"],
        "link": "https://moha55dz.github.io/E-commerce-page/"
    },
    {
        "title": "Premium Dashboard UI",
        "description": "A high-end administrative dashboard featuring real-time analytics, revenue tracking, and inventory management.",
        "technologies": ["HTML", "CSS", "Chart.js"],
        "link": "https://moha55dz.github.io/Dashboard-UI/"
    },
    {
        "title": "Smart Study Planner",
        "description": "A comprehensive student productivity tool for tracking subjects, scheduling tasks, and monitoring study streaks.",
        "technologies": ["HTML", "CSS", "JavaScript"],
        "link": "https://moha55dz.github.io/smart_study_planner/"
    }
]

for idx, project in enumerate(projects, 1):
    # Project title with number
    project_title = f"{idx}. {project['title']}"
    elements.append(Paragraph(project_title, 
        ParagraphStyle('ProjectTitle', parent=styles['Heading3'], fontSize=13, 
                      textColor=colors.HexColor('#6366f1'), fontName='Helvetica-Bold', spaceAfter=6)))
    
    # Project description
    elements.append(Paragraph(project['description'], content_style))
    
    # Technologies
    tech_str = ", ".join(project['technologies'])
    tech_style = ParagraphStyle('TechStyle', parent=styles['Normal'], fontSize=9, 
                               textColor=colors.HexColor('#7c3aed'), fontName='Helvetica-Bold')
    elements.append(Paragraph(f"<b>Technologies:</b> {tech_str}", tech_style))
    
    # Project link
    link_style = ParagraphStyle('LinkStyle', parent=styles['Normal'], fontSize=10, 
                               textColor=colors.HexColor('#0ea5e9'), fontName='Helvetica')
    elements.append(Paragraph(f"<b>View Project:</b> {project['link']}", link_style))
    
    elements.append(Spacer(1, 0.15*inch))

elements.append(Spacer(1, 0.1*inch))

# ==================== LEARNING & INTERESTS ====================
elements.append(Paragraph("Current Learning & Interests", section_title_style))
learning_text = """
<b>Advanced React:</b> Building scalable and performant React applications with modern hooks, state management, 
and component optimization.<br/><br/>
<b>Django:</b> Developing robust backend solutions with Python and Django framework for web applications.<br/><br/>
<b>Web Design:</b> Creating responsive, accessible, and visually stunning user interfaces that prioritize user experience.
"""
elements.append(Paragraph(learning_text, content_style))

# ==================== BUILD PDF ====================
try:
    doc.build(elements)
    print(f"✅ PDF generated successfully: {pdf_path}")
    print(f"📄 File size: {os.path.getsize(pdf_path) / 1024:.2f} KB")
except Exception as e:
    print(f"❌ Error generating PDF: {e}")
