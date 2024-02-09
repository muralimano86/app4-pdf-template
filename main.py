from fpdf import FPDF


pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hi There!", ln=1, border=1, align="L")
pdf.cell(w=0, h=12, txt="Hi You!", ln=1, border=0, align="L")

pdf.add_page()

pdf.cell(w=0, h=12, txt="Hi there!", ln=1, border=1, align="M")

pdf.output("output.pdf")