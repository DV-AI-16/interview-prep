"""
Buy-side equity DCF for Thangamayil Jewellery Ltd (NSE: THANGAMAYL)
Generates a 3-sheet workbook: Cover | Assumptions | DCF
All inputs sourced from public filings/aggregators (see Cover sources block).
Colour convention:
  BLUE  font  = hardcoded input (Assumptions only)
  BLACK font  = formula referencing the same sheet
  GREEN font  = cross-sheet link
  YELLOW fill = key output cell
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ---------------------------------------------------------------- styles
BLUE   = "FF0000FF"
BLACK  = "FF000000"
GREEN  = "FF006100"
WHITE  = "FFFFFFFF"
GREY   = "FF808080"
RED    = "FFC00000"

F_TITLE   = Font(name="Calibri", size=16, bold=True, color="FF1F3864")
F_SUB     = Font(name="Calibri", size=10, italic=True, color=GREY)
F_HDR     = Font(name="Calibri", size=11, bold=True, color=WHITE)
F_SECT    = Font(name="Calibri", size=11, bold=True, color="FF1F3864")
F_LBL     = Font(name="Calibri", size=10, color=BLACK)
F_LBLB    = Font(name="Calibri", size=10, bold=True, color=BLACK)
F_BLUE    = Font(name="Calibri", size=10, color=BLUE)
F_BLACKF  = Font(name="Calibri", size=10, color=BLACK)
F_GREEN   = Font(name="Calibri", size=10, color=GREEN)
F_RAT     = Font(name="Calibri", size=9, italic=True, color=GREY)
F_FLAG    = Font(name="Calibri", size=9, italic=True, color=RED)

FILL_HDR   = PatternFill("solid", fgColor="FF1F3864")
FILL_SECT  = PatternFill("solid", fgColor="FFD9E1F2")
FILL_KEY   = PatternFill("solid", fgColor="FFFFFF00")   # yellow key cells
FILL_BEAR  = PatternFill("solid", fgColor="FFFCE4D6")
FILL_BASE  = PatternFill("solid", fgColor="FFE2EFDA")
FILL_BULL  = PatternFill("solid", fgColor="FFDDEBF7")
FILL_LEG   = PatternFill("solid", fgColor="FFF2F2F2")
FILL_COVER = PatternFill("solid", fgColor="FF1F3864")

thin = Side(style="thin", color="FFBFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
med = Side(style="medium", color="FF1F3864")
BOX = Border(left=med, right=med, top=med, bottom=med)

# number formats
NUM   = '#,##0;(#,##0);"–"'
NUM1  = '#,##0.0;(#,##0.0);"–"'
NUM2  = '#,##0.00;(#,##0.00);"–"'
PCT1  = '0.0%;(0.0%);"–"'
PCT2  = '0.00%;(0.00%);"–"'
RS    = '"₹"#,##0;("₹"#,##0);"–"'
RS1   = '"₹"#,##0.0;("₹"#,##0.0);"–"'

CENTER = Alignment(horizontal="center", vertical="center")
LEFT   = Alignment(horizontal="left", vertical="center", wrap_text=False)
RIGHT  = Alignment(horizontal="right", vertical="center")
WRAP   = Alignment(horizontal="left", vertical="center", wrap_text=True)

SCN = ["Bear", "Base", "Bull"]
SCN_FILL = {"Bear": FILL_BEAR, "Base": FILL_BASE, "Bull": FILL_BULL}

wb = Workbook()

# ================================================================ helpers
def put(ws, ref, value, *, fmt=None, font=None, fill=None, align=None,
        border=None):
    c = ws[ref]
    c.value = value
    if fmt:    c.number_format = fmt
    if font:   c.font = font
    if fill:   c.fill = fill
    if align:  c.alignment = align
    if border: c.border = border
    return c

def col(i):  # 1-indexed -> letter
    return get_column_letter(i)

# =====================================================================
#  ASSUMPTIONS SHEET
# =====================================================================
A = wb.active
A.title = "Assumptions"
A.sheet_view.showGridLines = False
widths = {"A": 34, "B": 12, "C": 13, "D": 13, "E": 13, "F": 44,
          "G": 11, "H": 11, "I": 11, "J": 11, "K": 11, "L": 11}
for k, v in widths.items():
    A.column_dimensions[k].width = v
A.column_dimensions["N"].width = 46

ref = {}  # storage for cell addresses to link from DCF

put(A, "A1", "THANGAMAYIL JEWELLERY LTD  —  DCF ASSUMPTIONS", font=F_TITLE)
put(A, "A2", "NSE: THANGAMAYL | BSE: 533158 | Sector: Consumer Durables – Jewellery Retail | "
             "All figures ₹ Crore unless stated | Currency: INR", font=F_SUB)
A.merge_cells("A1:F1"); A.merge_cells("A2:F2")

r = 4
# ---- Section A: Market & Company data ----
put(A, f"A{r}", "A.  MARKET & COMPANY DATA  (Actuals)", font=F_HDR, fill=FILL_HDR)
for cc in "BCDEF":
    put(A, f"{cc}{r}", None, fill=FILL_HDR)
A.merge_cells(f"A{r}:F{r}")
r += 1
put(A, f"B{r}", "Value", font=F_LBLB, align=CENTER)
put(A, f"F{r}", "Rationale / Source", font=F_LBLB, align=LEFT)
r += 1

def srow(label, value, fmt, rationale, *, key=False, blue=True):
    """single-value input row -> value in col B"""
    global r
    put(A, f"A{r}", label, font=F_LBL, align=LEFT)
    f = F_BLUE if blue else F_BLACKF
    cell = put(A, f"B{r}", value, fmt=fmt, font=f, align=RIGHT, border=BORDER)
    if key: cell.fill = FILL_KEY
    put(A, f"F{r}", rationale, font=F_RAT, align=WRAP)
    addr = f"B{r}"
    r += 1
    return addr

ref["valdate"] = srow("Valuation date", "25-Jun-2026", None,
    "Last NSE/BSE close used as CMP reference.")
ref["cmp"] = srow("Current Market Price (₹/share)", 5594, RS,
    "Close 25-Jun-2026 (screener.in / ETMoney). 52-wk range ₹1,750–5,765.", key=True)
ref["shares"] = srow("Diluted shares outstanding (Cr)", 3.108, NUM2,
    "Equity capital ₹31.08 Cr @ FV ₹10 = 3.108 Cr shares (screener.in).")
ref["rev26"] = srow("FY26 Revenue (Actual)", 8514, NUM,
    "FY26 (yr-end Mar-2026) standalone net sales (screener.in / ETMoney).")
ref["rev25"] = srow("FY25 Revenue (Actual)", 4911, NUM,
    "FY25 standalone net sales (screener.in).")
ref["ebitda26"] = srow("FY26 EBITDA (Actual)", 579, NUM,
    "FY26 operating profit = sales − operating expenses (screener.in). OPM 6.8%.")
ref["ebitda25"] = srow("FY25 EBITDA (Actual)", 219, NUM,
    "FY25 operating profit (screener.in). OPM 4.5%.")
ref["dna26"] = srow("FY26 D&A (Actual)", 40, NUM,
    "FY26 depreciation & amortisation (screener.in). ~0.5% of sales.")
ref["debt"] = srow("Total Debt – FY26 (Actual)", 913, NUM,
    "FY26 total borrowings (screener.in). D/E 0.64 (matches AngelOne).")
ref["cash"] = srow("Cash & Equivalents – FY26", 124, NUM,
    "[ESTIMATED — basis: FY25 close ₹88.6 Cr (Rediff CF) + FY26 net cash flow +₹36 Cr]. "
    "FY26 balance-sheet not yet filed; FY25 AR is latest on BSE.")
put(A, f"A{r}", "Net Cash  (= Cash − Total Debt)", font=F_LBLB, align=LEFT)
ref["netcash"] = f"B{r}"
put(A, f"B{r}", f"={ref['cash']}-{ref['debt']}", fmt=NUM, font=F_BLACKF,
    align=RIGHT, border=BORDER, fill=FILL_KEY)
put(A, f"F{r}", "Negative ⇒ company is in NET DEBT; reduces equity value.", font=F_RAT, align=WRAP)
r += 2

# ---- Section B: WACC build (cols C=Bear, D=Base, E=Bull) ----
put(A, f"A{r}", "B.  WACC BUILD  (market-value weighted, CAPM)", font=F_HDR, fill=FILL_HDR)
for cc in "BCDEF":
    put(A, f"{cc}{r}", None, fill=FILL_HDR)
A.merge_cells(f"A{r}:F{r}")
r += 1
put(A, f"A{r}", "Driver", font=F_LBLB, align=LEFT)
put(A, f"C{r}", "Bear", font=F_HDR, fill=FILL_BEAR, align=CENTER)
A[f"C{r}"].font = F_LBLB
put(A, f"D{r}", "Base", font=F_LBLB, fill=FILL_BASE, align=CENTER)
put(A, f"E{r}", "Bull", font=F_LBLB, fill=FILL_BULL, align=CENTER)
put(A, f"F{r}", "Rationale / Source", font=F_LBLB, align=LEFT)
r += 1

WCOL = {"Bear": "C", "Base": "D", "Bull": "E"}

def wrow(label, vals, fmt, rationale, *, formula=None, blue=True, key=False):
    """vals: dict scen->value OR None when formula given (per-scenario formula func)"""
    global r
    put(A, f"A{r}", label, font=F_LBL, align=LEFT)
    addrs = {}
    for s in SCN:
        cc = WCOL[s]
        if formula:
            v = formula(s, r)
            f = F_BLACKF
        else:
            v = vals[s]
            f = F_BLUE if blue else F_BLACKF
        cell = put(A, f"{cc}{r}", v, fmt=fmt, font=f, align=RIGHT, border=BORDER)
        if key: cell.fill = SCN_FILL[s]
        addrs[s] = f"{cc}{r}"
    put(A, f"F{r}", rationale, font=F_RAT, align=WRAP)
    r += 1
    return addrs

ref["rf"] = wrow("Risk-free rate (Rf)", {"Bear":0.068,"Base":0.068,"Bull":0.068}, PCT2,
    "India 10-yr G-Sec yield 6.77% on 25-Jun-2026 (TradingEconomics); benchmark 6.94% 2036 ~6.84%.")
ref["erp"] = wrow("Equity risk premium (ERP)", {"Bear":0.0849,"Base":0.0849,"Bull":0.0849}, PCT2,
    "Damodaran India TOTAL ERP, Jan-2026 update (mature 4.74% + India CRP 3.75%).")
ref["beta"] = wrow("Beta (levered)", {"Bear":1.10,"Base":1.00,"Bull":0.90}, NUM2,
    "[ESTIMATED — basis: Yahoo 5Y-monthly β 0.98]. 2-yr weekly vs Nifty not directly sourceable; "
    "scenario-flexed ±0.10 for cyclicality of gold demand.")
ref["ke"] = wrow("Cost of equity (Ke = Rf+β·ERP)", None, PCT2,
    "CAPM. Black = same-sheet formula.",
    formula=lambda s,row: f"={ref['rf'][s]}+{ref['beta'][s]}*{ref['erp'][s]}")
ref["kdpre"] = wrow("Pre-tax cost of debt (Kd)", {"Bear":0.08,"Base":0.08,"Bull":0.08}, PCT2,
    "FY26 interest ₹68 Cr / avg debt ₹855 Cr = 7.95% (screener.in).")
ref["tax"] = wrow("Tax rate", {"Bear":0.25,"Base":0.25,"Bull":0.25}, PCT1,
    "Effective tax FY26 25% / FY25 26% (screener.in); India concessional regime ~25.17%.")
ref["kdat"] = wrow("After-tax Kd = Kd·(1−tax)", None, PCT2, "Same-sheet formula.",
    formula=lambda s,row: f"={ref['kdpre'][s]}*(1-{ref['tax'][s]})")
ref["we"] = wrow("Weight of equity (We)", {"Bear":0.95,"Base":0.95,"Bull":0.95}, PCT1,
    "Market value: equity = mkt-cap ₹17,388 Cr; debt ₹913 Cr ⇒ We 95.0%.")
ref["wd"] = wrow("Weight of debt (Wd)", {"Bear":0.05,"Base":0.05,"Bull":0.05}, PCT1,
    "Debt ₹913 Cr / (17,388+913) = 5.0%.")
ref["wacc"] = wrow("WACC = We·Ke + Wd·Kd(at)", None, PCT2, "Linked into DCF discounting.",
    formula=lambda s,row: f"={ref['we'][s]}*{ref['ke'][s]}+{ref['wd'][s]}*{ref['kdat'][s]}",
    key=True)
r += 1

# ---- Section C: Operating scalars (cols C/D/E) ----
put(A, f"A{r}", "C.  OPERATING ASSUMPTIONS  (per scenario)", font=F_HDR, fill=FILL_HDR)
for cc in "BCDEF":
    put(A, f"{cc}{r}", None, fill=FILL_HDR)
A.merge_cells(f"A{r}:F{r}")
r += 1
put(A, f"A{r}", "Driver", font=F_LBLB, align=LEFT)
put(A, f"C{r}", "Bear", font=F_LBLB, fill=FILL_BEAR, align=CENTER)
put(A, f"D{r}", "Base", font=F_LBLB, fill=FILL_BASE, align=CENTER)
put(A, f"E{r}", "Bull", font=F_LBLB, fill=FILL_BULL, align=CENTER)
put(A, f"F{r}", "Rationale / Source", font=F_LBLB, align=LEFT)
r += 1

ref["dna_pct"] = wrow("D&A (% of revenue)", {"Bear":0.005,"Base":0.005,"Bull":0.005}, PCT2,
    "FY26 D&A ₹40 Cr = 0.47% of sales; asset-light retail format.")
ref["capex_pct"] = wrow("Capex (% of revenue)", {"Bear":0.012,"Base":0.018,"Bull":0.022}, PCT2,
    "FY26 capex ~₹132 Cr = 1.55% of sales. Bull = faster showroom roll-out.")
ref["nwc_pct"] = wrow("ΔNWC (% of Δrevenue)", {"Bear":0.13,"Base":0.11,"Bull":0.09}, PCT1,
    "Inventory-heavy (gold ~142 inv-days). Incremental NWC ~11% of incremental sales; "
    "Bear assumes worse gold tie-up.")
ref["tgr"] = wrow("Terminal growth (g)", {"Bear":0.040,"Base":0.055,"Bull":0.065}, PCT1,
    "Below India nominal GDP ~10–11%; kept << WACC. Steady-state store + price growth.",
    key=True)
r += 1

# ---- Section D: Revenue growth by year (years across cols C..L) ----
YEARS = [f"FY{y}" for y in range(27, 37)]   # FY27..FY36
NY = len(YEARS)
ycols = [col(3 + k) for k in range(NY)]     # C..L

def year_block(title, data, fmt, rationale):
    """data: dict scen-> list of 10 values; years across cols C..L, 3 scenario rows."""
    global r
    put(A, f"A{r}", title, font=F_HDR, fill=FILL_HDR)
    for cc in ["B"] + ycols:
        put(A, f"{cc}{r}", None, fill=FILL_HDR)
    A.merge_cells(f"A{r}:B{r}")
    r += 1
    put(A, f"A{r}", "Scenario", font=F_LBLB, align=LEFT)
    for k, yy in enumerate(YEARS):
        put(A, f"{ycols[k]}{r}", yy, font=F_LBLB, align=CENTER)
    put(A, f"N{r}", rationale, font=F_RAT, align=WRAP)
    A.merge_cells(f"N{r}:N{r+3}")
    r += 1
    addrs = {}
    for s in SCN:
        put(A, f"A{r}", s, font=F_LBLB, fill=SCN_FILL[s], align=LEFT)
        addrs[s] = []
        for k in range(NY):
            cell = put(A, f"{ycols[k]}{r}", data[s][k], fmt=fmt, font=F_BLUE,
                       align=RIGHT, border=BORDER)
            addrs[s].append(f"{ycols[k]}{r}")
        r += 1
    return addrs

growth_data = {
    "Bear": [0.08,0.07,0.06,0.06,0.05,0.05,0.05,0.05,0.05,0.05],
    "Base": [0.15,0.14,0.13,0.12,0.11,0.10,0.09,0.085,0.08,0.075],
    "Bull": [0.22,0.20,0.18,0.16,0.14,0.13,0.12,0.11,0.10,0.09],
}
ref["growth"] = year_block("D.  REVENUE GROWTH % BY YEAR (FY27–FY36)", growth_data, PCT1,
    "FY26 base inflated by record gold prices (+73% YoY). Growth decays toward terminal. "
    "10-yr median historical sales growth ~19%.")
r += 1

margin_data = {
    "Bear": [0.062,0.060,0.059,0.058,0.057,0.057,0.056,0.056,0.055,0.055],
    "Base": [0.069,0.0695,0.070,0.0705,0.071,0.071,0.0715,0.0715,0.072,0.072],
    "Bull": [0.072,0.075,0.077,0.079,0.080,0.081,0.082,0.083,0.084,0.085],
}
ref["margin"] = year_block("E.  EBITDA MARGIN % BY YEAR (FY27–FY36)", margin_data, PCT2,
    "FY26 OPM 6.8% (FY25 4.5%). Base: mild expansion from scale & studded mix; "
    "Bull: premiumisation; Bear: gold volatility & competition.")
r += 1

put(A, f"A{r}", "Flags:  [ESTIMATED] inputs — FY26 cash balance (BS not yet filed) and "
    "Beta (2-yr weekly proxy). All other inputs sourced from public filings/aggregators.",
    font=F_FLAG, align=WRAP)
A.merge_cells(f"A{r}:F{r}")

print("Assumptions sheet built; key refs stored.")

# save ref dict for the DCF builder (same process, just continue)
import json
# we continue in same script below



# =====================================================================
#  DCF SHEET
# =====================================================================
D = wb.create_sheet("DCF")
D.sheet_view.showGridLines = False
D.column_dimensions["A"].width = 30
D.column_dimensions["B"].width = 8
for i in range(3, 15):
    D.column_dimensions[col(i)].width = 11
D.column_dimensions["O"].width = 2
D.column_dimensions["P"].width = 46

BASECOL = "C"                              # FY26A
DCOL = [col(4 + k) for k in range(NY)]     # D..M  (FY27..FY36)

def asm(key, scen=None):
    """cross-sheet link string to Assumptions cell"""
    a = ref[key]
    if isinstance(a, dict):
        return f"Assumptions!{a[scen]}"
    return f"Assumptions!{a}"

put(D, "A1", "THANGAMAYIL JEWELLERY LTD  —  DISCOUNTED CASH FLOW (FCFF)", font=F_TITLE)
put(D, "A2", "₹ Crore | 10-yr explicit (FY27–FY36) + Gordon Growth terminal value | "
             "Bear / Base / Bull | GREEN = link to Assumptions, BLACK = same-sheet formula",
    font=F_SUB)
D.merge_cells("A1:N1"); D.merge_cells("A2:N2")

dr = 4
def yhead(rr, with_base=True):
    put(D, f"A{rr}", "", font=F_LBLB)
    if with_base:
        put(D, f"{BASECOL}{rr}", "FY26A", font=F_LBLB, align=CENTER, fill=FILL_SECT)
    for k, yy in enumerate(YEARS):
        put(D, f"{DCOL[k]}{rr}", f"{yy}E", font=F_LBLB, align=CENTER, fill=FILL_SECT)

def sect(rr, text):
    put(D, f"A{rr}", text, font=F_SECT, fill=FILL_SECT)
    for i in range(2, 15):
        put(D, f"{col(i)}{rr}", None, fill=FILL_SECT)
    D.merge_cells(f"A{rr}:A{rr}")

def scen_rows(rr, label, gen, fmt, *, base_gen=None, fill_key=False, note=None):
    """write 3 sub-rows (Bear/Base/Bull). gen(scen,k)->formula for forecast col k.
       base_gen(scen)->formula for FY26A col (optional). returns {scen: rownum}."""
    rows = {}
    for idx, s in enumerate(SCN):
        row = rr + idx
        lbl = label if idx == 0 else ""
        put(D, f"A{row}", lbl, font=F_LBL, align=LEFT)
        put(D, f"B{row}", s, font=F_LBL, fill=SCN_FILL[s], align=CENTER)
        if base_gen is not None:
            v = base_gen(s)
            f = F_GREEN if (isinstance(v, str) and "Assumptions!" in v) else F_BLACKF
            put(D, f"{BASECOL}{row}", v, fmt=fmt, font=f, align=RIGHT, border=BORDER)
        for k in range(NY):
            v = gen(s, k)
            f = F_GREEN if (isinstance(v, str) and "Assumptions!" in v) else F_BLACKF
            cell = put(D, f"{DCOL[k]}{row}", v, fmt=fmt, font=f, align=RIGHT, border=BORDER)
            if fill_key: cell.fill = FILL_KEY
        rows[s] = row
    if note:
        put(D, f"P{rr}", note, font=F_RAT, align=WRAP)
    return rows

# ---- Period row (drives discounting & sensitivity) ----
yhead(dr); PERIOD_HDR = dr; dr += 1
put(D, f"A{dr}", "Discount period (t)", font=F_LBL, align=LEFT)
put(D, f"{BASECOL}{dr}", 0, fmt=NUM, font=F_BLACKF, align=RIGHT)
for k in range(NY):
    put(D, f"{DCOL[k]}{dr}", k + 1, fmt=NUM, font=F_BLACKF, align=RIGHT)
PERIOD_ROW = dr
dr += 2

# ---- ① Revenue build ----
sect(dr, "①  REVENUE BUILD"); dr += 1
g_rows = scen_rows(dr, "Revenue growth %",
    gen=lambda s,k: f"={asm('growth',s)[k] if False else 'Assumptions!'+ref['growth'][s][k]}",
    fmt=PCT1, base_gen=lambda s: None,
    note="Growth links from Assumptions §D (blue). Revenue compounds off FY26A base.")
dr += 3
rev_rows = scen_rows(dr, "Revenue (₹ Cr)",
    gen=lambda s,k: (f"={BASECOL}{rev_rows_self[s]}*(1+{DCOL[0]}{g_rows[s]})"
                     if k == 0 else
                     f"={DCOL[k-1]}{rev_rows_self[s]}*(1+{DCOL[k]}{g_rows[s]})"),
    fmt=NUM, base_gen=lambda s: f"={asm('rev26')}") \
    if False else None
# revenue needs self-reference to its own row numbers; build manually:
rev_rows = {}
for idx, s in enumerate(SCN):
    row = dr + idx
    put(D, f"A{row}", "Revenue (₹ Cr)" if idx == 0 else "", font=F_LBLB, align=LEFT)
    put(D, f"B{row}", s, font=F_LBL, fill=SCN_FILL[s], align=CENTER)
    put(D, f"{BASECOL}{row}", f"={asm('rev26')}", fmt=NUM, font=F_GREEN, align=RIGHT, border=BORDER)
    prev = BASECOL
    for k in range(NY):
        put(D, f"{DCOL[k]}{row}", f"={prev}{row}*(1+{DCOL[k]}{g_rows[s]})",
            fmt=NUM, font=F_BLACKF, align=RIGHT, border=BORDER)
        prev = DCOL[k]
    rev_rows[s] = row
dr += 4

# ---- ② EBITDA bridge ----
sect(dr, "②  EBITDA BRIDGE"); dr += 1
m_rows = scen_rows(dr, "EBITDA margin %",
    gen=lambda s,k: f"=Assumptions!{ref['margin'][s][k]}",
    fmt=PCT2, base_gen=lambda s: f"={asm('ebitda26')}/{asm('rev26')}",
    note="Margin links from Assumptions §E. EBITDA = margin × revenue.")
dr += 3
ebitda_rows = {}
for idx, s in enumerate(SCN):
    row = dr + idx
    put(D, f"A{row}", "EBITDA (₹ Cr)" if idx == 0 else "", font=F_LBLB, align=LEFT)
    put(D, f"B{row}", s, font=F_LBL, fill=SCN_FILL[s], align=CENTER)
    put(D, f"{BASECOL}{row}", f"={asm('ebitda26')}", fmt=NUM, font=F_GREEN, align=RIGHT, border=BORDER)
    for k in range(NY):
        put(D, f"{DCOL[k]}{row}", f"={DCOL[k]}{rev_rows[s]}*{DCOL[k]}{m_rows[s]}",
            fmt=NUM, font=F_BLACKF, align=RIGHT, border=BORDER)
    ebitda_rows[s] = row
dr += 4

# ---- ③ FCFF waterfall ----
sect(dr, "③  FCFF WATERFALL   (EBITDA → D&A → EBIT → Tax → NOPAT → +D&A → −Capex → −ΔNWC → FCFF)")
dr += 1
yhead(dr); dr += 1

def wf_line(label, gen, fmt, bold=False, key=False):
    rows = {}
    for idx, s in enumerate(SCN):
        row = dr_ref[0] + idx
        put(D, f"A{row}", label if idx == 0 else "", font=(F_LBLB if bold else F_LBL), align=LEFT)
        put(D, f"B{row}", s, font=F_LBL, fill=SCN_FILL[s], align=CENTER)
        for k in range(NY):
            v = gen(s, k, row)
            f = F_GREEN if (isinstance(v, str) and "Assumptions!" in v) else F_BLACKF
            cell = put(D, f"{DCOL[k]}{row}", v, fmt=fmt, font=f, align=RIGHT, border=BORDER)
            if key: cell.fill = FILL_KEY
        rows[s] = row
    dr_ref[0] += 3
    return rows

dr_ref = [dr]
ebitda_wf = wf_line("EBITDA", lambda s,k,row: f"={DCOL[k]}{ebitda_rows[s]}", NUM, bold=True)
dna_wf    = wf_line("(−) D&A", lambda s,k,row: f"=-{DCOL[k]}{rev_rows[s]}*{asm('dna_pct',s)}", NUM)
ebit_wf   = wf_line("EBIT", lambda s,k,row: f"={DCOL[k]}{ebitda_wf[s]}+{DCOL[k]}{dna_wf[s]}", NUM, bold=True)
tax_wf    = wf_line("(−) Tax on EBIT", lambda s,k,row: f"=-{DCOL[k]}{ebit_wf[s]}*{asm('tax',s)}", NUM)
nopat_wf  = wf_line("NOPAT", lambda s,k,row: f"={DCOL[k]}{ebit_wf[s]}+{DCOL[k]}{tax_wf[s]}", NUM, bold=True)
adddna_wf = wf_line("(+) D&A", lambda s,k,row: f"=-{DCOL[k]}{dna_wf[s]}", NUM)
capex_wf  = wf_line("(−) Capex", lambda s,k,row: f"=-{DCOL[k]}{rev_rows[s]}*{asm('capex_pct',s)}", NUM)
# ΔNWC: (Rev_t - Rev_{t-1}) * nwc%   ; t=0 uses FY26A base col
def dnwc_gen(s, k, row):
    prev = f"{BASECOL}{rev_rows[s]}" if k == 0 else f"{DCOL[k-1]}{rev_rows[s]}"
    return f"=-({DCOL[k]}{rev_rows[s]}-{prev})*{asm('nwc_pct',s)}"
dnwc_wf   = wf_line("(−) ΔNWC", dnwc_gen, NUM)
fcff_wf   = wf_line("FCFF", lambda s,k,row:
    f"={DCOL[k]}{nopat_wf[s]}+{DCOL[k]}{adddna_wf[s]}+{DCOL[k]}{capex_wf[s]}+{DCOL[k]}{dnwc_wf[s]}",
    NUM, bold=True, key=True)
df_wf     = wf_line("Discount factor @ WACC",
    lambda s,k,row: f"=1/(1+{asm('wacc',s)})^{DCOL[k]}{PERIOD_ROW}", NUM2)
pv_wf     = wf_line("PV of FCFF",
    lambda s,k,row: f"={DCOL[k]}{fcff_wf[s]}*{DCOL[k]}{df_wf[s]}", NUM, bold=True)
dr = dr_ref[0] + 1

# ---- ④ WACC summary (linked from Assumptions) ----
sect(dr, "④  WACC SUMMARY   (linked from Assumptions)"); dr += 1
put(D, f"A{dr}", "Driver", font=F_LBLB, align=LEFT)
wcols = {"Bear": "C", "Base": "D", "Bull": "E"}
for s in SCN:
    put(D, f"{wcols[s]}{dr}", s, font=F_LBLB, fill=SCN_FILL[s], align=CENTER)
dr += 1
def wsumm(label, key, fmt):
    global dr
    put(D, f"A{dr}", label, font=F_LBL, align=LEFT)
    for s in SCN:
        put(D, f"{wcols[s]}{dr}", f"=Assumptions!{ref[key][s]}", fmt=fmt,
            font=F_GREEN, align=RIGHT, border=BORDER)
    dr += 1
wsumm("Risk-free rate", "rf", PCT2)
wsumm("Equity risk premium", "erp", PCT2)
wsumm("Beta", "beta", NUM2)
wsumm("Cost of equity (Ke)", "ke", PCT2)
wsumm("After-tax cost of debt", "kdat", PCT2)
wsumm("Weight of equity", "we", PCT1)
wsumm("Weight of debt", "wd", PCT1)
put(D, f"A{dr}", "WACC", font=F_LBLB, align=LEFT)
for s in SCN:
    c = put(D, f"{wcols[s]}{dr}", f"=Assumptions!{ref['wacc'][s]}", fmt=PCT2,
            font=F_GREEN, align=RIGHT, border=BORDER); c.fill = FILL_KEY
dr += 2

# ---- ⑤ Valuation table (scenarios side by side) ----
sect(dr, "⑤  VALUATION SUMMARY   (Bear / Base / Bull side by side)"); dr += 1
vcols = {"Bear": "C", "Base": "D", "Bull": "E"}
put(D, f"A{dr}", "₹ Crore unless stated", font=F_LBLB, align=LEFT)
for s in SCN:
    put(D, f"{vcols[s]}{dr}", s, font=F_LBLB, fill=SCN_FILL[s], align=CENTER)
dr += 1
val = {}   # label -> rownum
def vline(label, gen, fmt, *, key=False, bold=False, green=False):
    global dr
    put(D, f"A{dr}", label, font=(F_LBLB if bold else F_LBL), align=LEFT)
    for s in SCN:
        v = gen(s)
        f = F_GREEN if (green or (isinstance(v, str) and "Assumptions!" in v)) else F_BLACKF
        c = put(D, f"{vcols[s]}{dr}", v, fmt=fmt, font=f, align=RIGHT, border=BORDER)
        if key: c.fill = FILL_KEY
    val[label] = dr
    dr += 1

vline("Terminal-yr FCFF (FY36)", lambda s: f"={DCOL[NY-1]}{fcff_wf[s]}", NUM)
vline("Terminal growth (g)", lambda s: f"=Assumptions!{ref['tgr'][s]}", PCT1)
vline("WACC", lambda s: f"=Assumptions!{ref['wacc'][s]}", PCT2)
vline("Terminal Value (GGM)",
      lambda s: f"={vcols[s]}{val['Terminal-yr FCFF (FY36)']}*(1+{vcols[s]}{val['Terminal growth (g)']})/"
                f"({vcols[s]}{val['WACC']}-{vcols[s]}{val['Terminal growth (g)']})", NUM)
vline("PV of Terminal Value",
      lambda s: f"={vcols[s]}{val['Terminal Value (GGM)']}/(1+{vcols[s]}{val['WACC']})^{DCOL[NY-1]}{PERIOD_ROW}", NUM)
vline("PV of explicit FCFFs",
      lambda s: f"=SUM({DCOL[0]}{pv_wf[s]}:{DCOL[NY-1]}{pv_wf[s]})", NUM)
vline("Enterprise Value (EV)",
      lambda s: f"={vcols[s]}{val['PV of Terminal Value']}+{vcols[s]}{val['PV of explicit FCFFs']}",
      NUM, key=True, bold=True)
vline("(+) Net Cash", lambda s: f"=Assumptions!{ref['netcash']}", NUM)
vline("Equity Value",
      lambda s: f"={vcols[s]}{val['Enterprise Value (EV)']}+{vcols[s]}{val['(+) Net Cash']}",
      NUM, key=True, bold=True)
vline("Diluted shares (Cr)", lambda s: f"=Assumptions!{ref['shares']}", NUM2)
vline("Implied value / share (₹)",
      lambda s: f"={vcols[s]}{val['Equity Value']}/{vcols[s]}{val['Diluted shares (Cr)']}",
      RS, key=True, bold=True)
vline("Current Market Price (₹)", lambda s: f"=Assumptions!{ref['cmp']}", RS)
vline("Upside / (Downside) %",
      lambda s: f"={vcols[s]}{val['Implied value / share (₹)']}/{vcols[s]}{val['Current Market Price (₹)']}-1",
      PCT1, key=True, bold=True)
vline("PV(TV) as % of EV",
      lambda s: f"={vcols[s]}{val['PV of Terminal Value']}/{vcols[s]}{val['Enterprise Value (EV)']}", PCT1)
IMPLIED_ROW = val["Implied value / share (₹)"]
UPSIDE_ROW  = val["Upside / (Downside) %"]
dr += 1

# ---- ⑥ Sensitivity 5x5 : WACC (rows) x TGR (cols), Base scenario, GGM ----
sect(dr, "⑥  SENSITIVITY — Implied Value/Share (₹):  WACC (rows) × Terminal Growth (cols), Base case")
dr += 1
put(D, f"A{dr}", "Base-case FCFF stream; GGM terminal value re-priced at each WACC × g.",
    font=F_RAT, align=LEFT)
dr += 1
TGR_AXIS  = [0.045, 0.050, 0.055, 0.060, 0.065]
WACC_AXIS = [0.128, 0.138, 0.148, 0.158, 0.168]
hdr_row = dr
put(D, f"B{hdr_row}", "WACC \\ g", font=F_LBLB, align=CENTER, fill=FILL_SECT, border=BORDER)
tgr_cols = [col(3 + j) for j in range(5)]      # C..G
for j, g in enumerate(TGR_AXIS):
    put(D, f"{tgr_cols[j]}{hdr_row}", g, fmt=PCT1, font=F_LBLB, align=CENTER,
        fill=FILL_SECT, border=BORDER)
dr += 1
base_fcff_rng = f"${DCOL[0]}${fcff_wf['Base']}:${DCOL[NY-1]}${fcff_wf['Base']}"
base_fcffN    = f"${DCOL[NY-1]}${fcff_wf['Base']}"
period_rng    = f"${DCOL[0]}${PERIOD_ROW}:${DCOL[NY-1]}${PERIOD_ROW}"
netcash_ref   = f"Assumptions!{ref['netcash']}"
shares_ref    = f"Assumptions!{ref['shares']}"
for i, w in enumerate(WACC_AXIS):
    row = dr + i
    put(D, f"B{row}", w, fmt=PCT1, font=F_LBLB, align=CENTER, fill=FILL_SECT, border=BORDER)
    wabs = f"$B{row}"
    for j, g in enumerate(TGR_AXIS):
        gabs = f"{tgr_cols[j]}${hdr_row}"
        f = (f"=(SUMPRODUCT({base_fcff_rng},(1+{wabs})^(-{period_rng}))"
             f"+({base_fcffN}*(1+{gabs})/({wabs}-{gabs}))/(1+{wabs})^10"
             f"+{netcash_ref})/{shares_ref}")
        c = put(D, f"{tgr_cols[j]}{row}", f, fmt=RS, font=F_BLACKF, align=RIGHT, border=BORDER)
        if abs(w - 0.148) < 1e-9 and abs(g - 0.055) < 1e-9:
            c.fill = FILL_KEY
SENS_TOP = dr
dr = dr + 5 + 2

# ---- ⑦ Reverse DCF ----
sect(dr, "⑦  REVERSE DCF  (what the market is pricing — Base WACC & g)"); dr += 1
rv = {}
def rvline(label, value, fmt, *, key=False, bold=False, note=None):
    global dr
    put(D, f"A{dr}", label, font=(F_LBLB if bold else F_LBL), align=LEFT)
    f = F_GREEN if (isinstance(value, str) and "Assumptions!" in value
                    and value.count("Assumptions!") == 1 and ("*" not in value and "-" not in value.replace("=-",""))) else F_BLACKF
    # simpler: green only if pure single cross-sheet link
    if isinstance(value, str) and value.startswith("=Assumptions!") and all(ch not in value[1:] for ch in "+*/") and value.count("Assumptions!")==1:
        f = F_GREEN
    else:
        f = F_BLACKF
    c = put(D, f"C{dr}", value, fmt=fmt, font=f, align=RIGHT, border=BORDER)
    if key: c.fill = FILL_KEY
    if note: put(D, f"P{dr}", note, font=F_RAT, align=WRAP)
    rv[label] = dr
    dr += 1

rvline("Current Market Price (₹)", f"=Assumptions!{ref['cmp']}", RS)
rvline("Diluted shares (Cr)", f"=Assumptions!{ref['shares']}", NUM2)
rvline("Market capitalisation", f"=C{rv['Current Market Price (₹)']}*C{rv['Diluted shares (Cr)']}", NUM)
rvline("(−) Net Cash", f"=Assumptions!{ref['netcash']}", NUM)
rvline("Implied Enterprise Value", f"=C{rv['Market capitalisation']}-C{rv['(−) Net Cash']}", NUM, bold=True,
       note="Implied EV = Mkt-cap − Net Cash (Net Cash is negative ⇒ EV > mkt-cap).")
rvline("Base WACC", f"=Assumptions!{ref['wacc']['Base']}", PCT2)
rvline("Base terminal growth (g)", f"=Assumptions!{ref['tgr']['Base']}", PCT1)
rvline("Implied steady-state FCFF (yr-1)",
       f"=C{rv['Implied Enterprise Value']}*(C{rv['Base WACC']}-C{rv['Base terminal growth (g)']})",
       NUM, key=True, bold=True,
       note="Single-stage Gordon perpetuity: FCFF₁ that justifies today's EV.")
rvline("Model Base FY27 FCFF (explicit)", f"={DCOL[0]}{fcff_wf['Base']}", NUM,
       note="For comparison vs the implied requirement.")
rvline("Model Base terminal FCFF (FY36)", f"={DCOL[NY-1]}{fcff_wf['Base']}", NUM)
rvline("Implied FCFF ÷ FY26 revenue",
       f"=C{rv['Implied steady-state FCFF (yr-1)']}/Assumptions!{ref['rev26']}", PCT1, bold=True,
       note="FCFF margin the market is pricing vs ~2–3% achievable for a jeweller.")
# implied revenue at steady-state margin
put(D, f"A{dr}", "Assumed steady-state FCFF margin", font=F_LBL, align=LEFT)
put(D, f"C{dr}", 0.04, fmt=PCT1, font=F_BLACKF, align=RIGHT, border=BORDER)
put(D, f"P{dr}", "Editable assumption (DCF sheet). ~4% is optimistic for gold retail.", font=F_RAT, align=WRAP)
rv["Assumed steady-state FCFF margin"] = dr; dr += 1
rvline("Implied steady-state revenue",
       f"=C{rv['Implied steady-state FCFF (yr-1)']}/C{rv['Assumed steady-state FCFF margin']}",
       NUM, key=True, bold=True,
       note="Revenue needed at that FCFF margin to justify CMP.")
rvline("Implied revenue ÷ FY26 revenue (×)",
       f"=C{rv['Implied steady-state revenue']}/Assumptions!{ref['rev26']}", NUM2)
rvline("Implied 10-yr revenue CAGR to get there",
       f"=(C{rv['Implied revenue ÷ FY26 revenue (×)']})^(1/10)-1", PCT1, bold=True)
dr += 1
put(D, f"A{dr}", "Read-through: CMP embeds FCFF generation far above what the explicit "
    "model produces — the market is pricing a structural step-change in cash conversion / scale.",
    font=F_RAT, align=WRAP)
D.merge_cells(f"A{dr}:N{dr}")

print("DCF sheet built.")

# =====================================================================
#  COVER SHEET  (first)
# =====================================================================
C = wb.create_sheet("Cover", 0)
C.sheet_view.showGridLines = False
C.column_dimensions["A"].width = 3
for cc in ["B","C","D","E","F"]:
    C.column_dimensions[cc].width = 22
C.column_dimensions["G"].width = 3

put(C, "B2", "THANGAMAYIL JEWELLERY LIMITED", font=Font(size=20, bold=True, color=WHITE))
put(C, "B3", "Buy-Side Equity DCF Valuation", font=Font(size=12, color=WHITE, italic=True))
for rr in (2, 3):
    for cc in ["A","B","C","D","E","F","G"]:
        C[f"{cc}{rr}"].fill = FILL_COVER
C.merge_cells("B2:F2"); C.merge_cells("B3:F3")
C["B2"].alignment = LEFT; C["B3"].alignment = LEFT

meta = [
    ("NSE Ticker", "THANGAMAYL"),
    ("BSE Code", "533158"),
    ("Sector", "Consumer Durables — Jewellery Retail"),
    ("Valuation date", "25-Jun-2026"),
    ("Methodology", "FCFF, 10-yr explicit + GGM terminal"),
]
rr = 5
for k, v in meta:
    put(C, f"B{rr}", k, font=F_LBLB, align=LEFT)
    put(C, f"C{rr}", v, font=F_LBL, align=LEFT)
    C.merge_cells(f"C{rr}:F{rr}")
    rr += 1
put(C, f"B{rr}", "Current Market Price", font=F_LBLB, align=LEFT)
put(C, f"C{rr}", f"=DCF!{vcols['Base']}{val['Current Market Price (₹)']}", fmt=RS,
    font=F_GREEN, align=LEFT); rr += 2

# ---- Scenario summary (green links only) ----
put(C, f"B{rr}", "SCENARIO SUMMARY", font=F_HDR, fill=FILL_HDR)
for cc in ["C","D","E"]:
    put(C, f"{cc}{rr}", None, fill=FILL_HDR)
C.merge_cells(f"B{rr}:E{rr}")
rr += 1
hdrr = rr
put(C, f"B{hdrr}", "", font=F_LBLB)
for j, s in enumerate(SCN):
    put(C, f"{col(3+j)}{hdrr}", s, font=F_LBLB, fill=SCN_FILL[s], align=CENTER, border=BORDER)
rr += 1
def cover_line(label, dcf_row, fmt, *, key=False):
    global rr
    put(C, f"B{rr}", label, font=F_LBL, align=LEFT)
    for j, s in enumerate(SCN):
        c = put(C, f"{col(3+j)}{rr}", f"=DCF!{vcols[s]}{dcf_row}", fmt=fmt,
                font=F_GREEN, align=RIGHT, border=BORDER)
        if key: c.fill = FILL_KEY
    rr += 1
cover_line("WACC", val["WACC"], PCT2)
cover_line("Terminal growth (g)", val["Terminal growth (g)"], PCT1)
cover_line("Enterprise Value (₹ Cr)", val["Enterprise Value (EV)"], NUM)
cover_line("Equity Value (₹ Cr)", val["Equity Value"], NUM)
cover_line("Implied value / share (₹)", IMPLIED_ROW, RS, key=True)
cover_line("Upside / (Downside) %", UPSIDE_ROW, PCT1, key=True)
rr += 1

# ---- Observations ----
put(C, f"B{rr}", "KEY OBSERVATIONS", font=F_HDR, fill=FILL_HDR)
for cc in ["C","D","E"]:
    put(C, f"{cc}{rr}", None, fill=FILL_HDR)
C.merge_cells(f"B{rr}:E{rr}")
rr += 1
obs = [
    "• FY26 revenue (₹8,514 Cr, +73% YoY) was amplified by record gold prices; forecasts "
    "normalise growth toward terminal rates.",
    "• The stock rose ~200% in 12 months and trades at ~49x earnings; the exchange sought a "
    "price-movement clarification in Jun-2026.",
    "• Jewellery is structurally low-margin (EBITDA ~7%) and working-capital heavy (gold ~142 "
    "inventory-days), so FCFF conversion is modest.",
    "• Company is in NET DEBT (~₹789 Cr), which reduces equity value below EV.",
    "• All three DCF scenarios imply intrinsic value well below CMP; the reverse DCF shows the "
    "market is pricing FCFF far above the explicit model.",
    "• Inputs are sourced from public filings/aggregators; FY26 cash balance and beta are "
    "flagged [ESTIMATED]. Tune blue cells on Assumptions to test views.",
]
for o in obs:
    put(C, f"B{rr}", o, font=F_LBL, align=WRAP)
    C.merge_cells(f"B{rr}:F{rr}")
    C.row_dimensions[rr].height = 30
    rr += 1
rr += 1

# ---- Colour legend ----
put(C, f"B{rr}", "COLOUR LEGEND", font=F_HDR, fill=FILL_HDR)
for cc in ["C","D","E"]:
    put(C, f"{cc}{rr}", None, fill=FILL_HDR)
C.merge_cells(f"B{rr}:E{rr}")
rr += 1
legend = [
    (BLUE,  "Blue font", "Hardcoded input (Assumptions sheet only)"),
    (BLACK, "Black font", "Formula referencing the same sheet"),
    (GREEN, "Green font", "Cross-sheet link"),
    (None,  "Yellow fill", "Key output cell"),
]
for clr, name, desc in legend:
    if clr:
        put(C, f"B{rr}", name, font=Font(size=10, bold=True, color=clr), align=LEFT)
    else:
        c = put(C, f"B{rr}", name, font=F_LBLB, align=LEFT); c.fill = FILL_KEY
    put(C, f"C{rr}", desc, font=F_LBL, align=LEFT)
    C.merge_cells(f"C{rr}:F{rr}")
    rr += 1
put(C, f"B{rr}", "Negatives shown in (parentheses); zeros shown as “–”.", font=F_RAT, align=LEFT)
C.merge_cells(f"B{rr}:F{rr}"); rr += 2

# ---- Sources ----
put(C, f"B{rr}", "SOURCES & FLAGS", font=F_HDR, fill=FILL_HDR)
for cc in ["C","D","E"]:
    put(C, f"{cc}{rr}", None, fill=FILL_HDR)
C.merge_cells(f"B{rr}:E{rr}")
rr += 1
sources = [
    "Financials: screener.in / ETMoney / Rediff Money (standalone, FY25 & FY26, ₹ Cr).",
    "FY2025 Annual Report is the latest filed on BSE; FY26 figures from announced results.",
    "Rf: India 10-yr G-Sec 6.77% (TradingEconomics, 25-Jun-2026).",
    "ERP: Damodaran India total ERP 8.49% (Jan-2026 update).",
    "Beta: [ESTIMATED] — Yahoo 5Y-monthly 0.98 used as proxy for 2-yr weekly vs Nifty.",
    "FY26 Cash ₹124 Cr: [ESTIMATED] — FY25 close ₹88.6 Cr + FY26 net cash flow +₹36 Cr.",
    "CMP ₹5,594: NSE/BSE close 25-Jun-2026.",
]
for sline in sources:
    put(C, f"B{rr}", "• " + sline, font=F_RAT, align=WRAP)
    C.merge_cells(f"B{rr}:F{rr}")
    rr += 1

print("Cover sheet built.")

# force Excel / LibreOffice / Google Sheets to recalculate all formulas on open
try:
    wb.calculation.fullCalcOnLoad = True
except Exception:
    from openpyxl.workbook.properties import CalcProperties
    wb.calculation = CalcProperties(fullCalcOnLoad=True)

wb.save("/projects/sandbox/Thangamayil_DCF.xlsx")
print("Saved Thangamayil_DCF.xlsx")
