"""
Convert the eClerx interview-prep Markdown to a clean, styled PDF.
Handles headings, bullets, numbered lists, tables, blockquotes, bold/italic/code, rules.
Per-page header/footer. Usage: python3 md_to_pdf.py in.md out.pdf "Title"
"""
import sys, re, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, HRFlowable)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import matplotlib

NAVY=colors.HexColor("#1F3864"); BLUE=colors.HexColor("#2E5496"); GREEN=colors.HexColor("#385723")
LBLUE=colors.HexColor("#D9E1F2"); LGREY=colors.HexColor("#F2F2F2"); GREY=colors.HexColor("#808080")
RED=colors.HexColor("#C00000"); AMBER=colors.HexColor("#FFF7E0")

fdir=os.path.join(os.path.dirname(matplotlib.__file__),"mpl-data","fonts","ttf")
pdfmetrics.registerFont(TTFont("DV",os.path.join(fdir,"DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DV-B",os.path.join(fdir,"DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("DV-I",os.path.join(fdir,"DejaVuSans-Oblique.ttf")))
pdfmetrics.registerFontFamily("DV",normal="DV",bold="DV-B",italic="DV-I",boldItalic="DV-B")

inp,outp,title=sys.argv[1],sys.argv[2],sys.argv[3]
st=getSampleStyleSheet()
def S(n,**k): st.add(ParagraphStyle(n,parent=st["Normal"],fontName=k.pop("fontName","DV"),**k))
S("Body",fontSize=9.5,leading=14,alignment=TA_JUSTIFY,spaceAfter=5)
S("H1",fontSize=16,textColor=NAVY,fontName="DV-B",spaceBefore=10,spaceAfter=5,leading=19)
S("H2",fontSize=12.5,textColor=BLUE,fontName="DV-B",spaceBefore=9,spaceAfter=4,leading=15)
S("H3",fontSize=10.5,textColor=GREEN,fontName="DV-B",spaceBefore=6,spaceAfter=2,leading=13)
S("Bull",fontSize=9.5,leading=13.5,leftIndent=12,spaceAfter=2)
S("Quote",fontSize=9,leading=13,textColor=colors.HexColor("#444444"),fontName="DV-I",leftIndent=10,rightIndent=6,spaceAfter=6,backColor=AMBER,borderPadding=4)
S("Cell",fontSize=8,leading=10.5,fontName="DV")
S("CellB",fontSize=8,leading=10.5,fontName="DV-B",textColor=colors.white)
DISC="eClerx Interview Preparation  |  Personal study material  |  Educational only - not investment advice"

def hf(c,d):
    c.saveState(); c.setFillColor(NAVY); c.rect(0,A4[1]-11*mm,A4[0],11*mm,fill=1,stroke=0)
    c.setFillColor(colors.white); c.setFont("DV-B",7.6); c.drawCentredString(A4[0]/2,A4[1]-7.3*mm,DISC)
    c.setStrokeColor(GREY); c.setLineWidth(0.4); c.line(15*mm,11*mm,A4[0]-15*mm,11*mm)
    c.setFillColor(GREY); c.setFont("DV",7.3)
    c.drawString(15*mm,6.5*mm,"Prepared for Apoorva Singh")
    c.drawRightString(A4[0]-15*mm,6.5*mm,f"Page {d.page}"); c.restoreState()

doc=BaseDocTemplate(outp,pagesize=A4,leftMargin=15*mm,rightMargin=15*mm,topMargin=15*mm,bottomMargin=13*mm,title=title)
doc.addPageTemplates([PageTemplate(id="a",frames=[Frame(doc.leftMargin,doc.bottomMargin,doc.width,doc.height-2*mm)],onPage=hf)])

def sanitize(t): return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace("₹","Rs ")
def inline(t):
    t=sanitize(t)
    t=re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>",t)
    t=re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)",r"<i>\1</i>",t)
    t=re.sub(r"`(.+?)`",r"<font face='Courier'>\1</font>",t)
    return t

lines=open(inp,encoding="utf-8").read().split("\n")
E=[]; i=0
def flush_table(rows):
    data=[[Paragraph(inline(c),st["CellB"] if r==0 else st["Cell"]) for c in row] for r,row in enumerate(rows)]
    ncol=max(len(r) for r in rows); w=doc.width/ncol
    t=Table(data,colWidths=[w]*ncol,repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("GRID",(0,0),(-1,-1),0.4,colors.HexColor("#C8C8C8")),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,LGREY]),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("LEFTPADDING",(0,0),(-1,-1),4)]))
    E.append(t); E.append(Spacer(1,6))
while i<len(lines):
    ln=lines[i].rstrip()
    if not ln.strip(): E.append(Spacer(1,4)); i+=1; continue
    if ln.startswith("# "): E.append(Paragraph(inline(ln[2:]),st["H1"])); E.append(HRFlowable(width="100%",color=LBLUE,thickness=1)); i+=1; continue
    if ln.startswith("### "): E.append(Paragraph(inline(ln[4:]),st["H3"])); i+=1; continue
    if ln.startswith("## "): E.append(Paragraph(inline(ln[3:]),st["H2"])); i+=1; continue
    if ln.startswith("> "): E.append(Paragraph(inline(ln[2:]),st["Quote"])); i+=1; continue
    if ln.strip()=="---": E.append(HRFlowable(width="100%",color=GREY,thickness=0.5,spaceBefore=3,spaceAfter=3)); i+=1; continue
    if ln.lstrip().startswith("|"):
        rows=[]
        while i<len(lines) and lines[i].lstrip().startswith("|"):
            cells=[c.strip() for c in lines[i].strip().strip("|").split("|")]
            if not all(set(c)<=set("-: ") for c in cells): rows.append(cells)
            i+=1
        if rows: flush_table(rows)
        continue
    if re.match(r"^\s*[-*] ",ln): E.append(Paragraph("&bull; "+inline(re.sub(r"^\s*[-*] ","",ln)),st["Bull"])); i+=1; continue
    if re.match(r"^\s*\d+\. ",ln): E.append(Paragraph(inline(ln.strip()),st["Bull"])); i+=1; continue
    E.append(Paragraph(inline(ln),st["Body"])); i+=1
doc.build(E)
print("PDF:",outp,"(",round(os.path.getsize(outp)/1024),"KB )")
