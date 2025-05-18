import pdfkit
from jinja2 import Environment, FileSystemLoader
import os
import tempfile

def generate_report(data_html, summary_html, ai_insights):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    report_html = template.render(
        data_html=data_html,
        summary_html=summary_html,
        ai_insights=ai_insights
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        pdf_path = f.name
        pdfkit.from_string(report_html, pdf_path)
    
    return pdf_path
