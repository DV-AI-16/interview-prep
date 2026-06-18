# S&P GLOBAL — DATA CONSULTANT INTERVIEW
# COMPLETE VALUATION, FINANCIAL MODELLING & CONCEPTS REPORT
### Prepared for: Apoorva Singh | Companies: Infosys · HUL · HDFC Bank

---

## HOW TO USE THIS REPORT

Read it in order. Part 1–3 build your foundation (macro, terms, valuation logic). Parts 4–6 are the three company deep-dives. Parts 7–9 are interview Q&A and mock prep. Everything you say from this is TRUE because you will have genuinely understood it.

**Your interviewer** is a Senior Manager at S&P Global with a Master's in Finance. This means:
- Expect **conceptual depth**, not just definitions. He'll ask "why," not just "what."
- He'll **follow up** 2–3 layers deep. Know the logic behind each formula.
- Use **precise terminology** (constant currency, capital-structure neutral, justified P/B).
- It's OK to say "my understanding is..." — intellectual honesty beats bluffing with a finance expert.

### NIGHT-BEFORE TOP PRIORITIES
1. The 3 valuation methods and WHEN to use each (DCF / Comps / DDM-P-B).
2. Why banks are valued differently (deposits = raw material).
3. EV, EBITDA, P/E, EV/EBITDA — the *intuition*, not just formulas.
4. The connection between the 3 financial statements + depreciation walk-through.
5. Your honest HDFC story (tried DCF → learned banks differ → studied the right framework).
6. Current macro: RBI repo 5.25%, FY27 GDP ~6.6%, inflation ~5.1%.

---

# PART 1 — TOP-DOWN ("FUNDAMENTAL MACRO-DRIVEN") ANALYSIS

This term = **top-down analysis**: start broad (economy), narrow to industry, then company, then valuation.

```
MACRO (economy) → INDUSTRY → COMPANY (fundamentals) → VALUATION
```

| Level | What you examine |
|---|---|
| Macro | GDP, inflation, interest rates, currency, government policy |
| Industry | Growth rate, competition, regulation, demand drivers |
| Company | Revenue, margins, ROE/ROCE, debt, management, moat |
| Valuation | DCF, comps, P/E, P/B — cheap or expensive? |

## CURRENT INDIA MACRO (as of June 2026) — memorize this
- **RBI repo rate: 5.25%** (held at the June 5, 2026 MPC meeting; neutral stance). Governor: Sanjay Malhotra.
- **GDP growth FY27 forecast: 6.6%** (cut from 6.9% due to West Asia conflict, elevated oil prices, monsoon risk).
- **Inflation FY27 forecast: 5.1%** (raised from 4.6%). India had briefly seen historic-low inflation (~0.25% in Oct 2025) and strong Q2 FY26 GDP of ~8.2%, but risks have since risen ("Goldilocks moment dimming").
- **Key risks:** geopolitical (West Asia), oil prices, weaker rupee, global slowdown affecting IT exports.

**How macro connects to your 3 companies:**
- **Infosys (IT):** Depends on US/Europe client spending + USD/INR. Weak rupee = good (earns in $). Global slowdown / rate environment = risk to discretionary IT spend.
- **HUL (FMCG):** Depends on domestic consumption, rural demand recovery, inflation (input costs like palm oil). Lower inflation helps margins; rural recovery helps volumes.
- **HDFC Bank:** Depends on interest rate cycle (affects NIM), credit growth, deposit competition. Rate cuts can pressure margins short-term but boost loan demand.

---

# PART 2 — GLOSSARY: EVERY TERM YOU NEED

## A. Income Statement (P&L) terms — top to bottom
- **Revenue / Sales / Turnover** — total money earned from selling goods/services. "Top line."
- **COGS (Cost of Goods Sold)** — direct costs to produce what you sold.
- **Gross Profit** = Revenue − COGS. Profit before operating overheads.
- **Operating Expenses (SG&A)** — Selling, General & Administrative costs (salaries, rent, marketing).
- **EBITDA** — Earnings Before Interest, Tax, Depreciation, Amortization. Proxy for operating cash earnings (see Part 3).
- **Depreciation** — spreading the cost of a tangible asset (machine) over its life. Non-cash.
- **Amortization** — same idea for intangible assets (patents, goodwill). Non-cash.
- **EBIT / Operating Profit** = EBITDA − D&A. Profit from core operations.
- **Interest Expense** — cost of debt.
- **EBT (Pre-tax profit)** = EBIT − Interest.
- **Tax** — corporate income tax.
- **Net Income / PAT (Profit After Tax)** — "bottom line." What's left for shareholders.
- **EPS (Earnings Per Share)** = Net income / shares outstanding.

## B. Balance Sheet terms (Assets = Liabilities + Equity)
- **Assets** — what the company owns. Current (cash, receivables, inventory) + Non-current (PP&E, intangibles).
- **PP&E** — Property, Plant & Equipment (fixed assets).
- **Liabilities** — what it owes. Current (payables, short-term debt) + Non-current (long-term debt).
- **Equity / Shareholders' Funds** — owners' stake = share capital + retained earnings.
- **Retained Earnings** — accumulated profits not paid as dividends.
- **Working Capital** = Current Assets − Current Liabilities. Short-term operating liquidity.
- **Book Value** — equity value on the balance sheet (assets − liabilities).
- **Goodwill** — premium paid above fair value in an acquisition (intangible).

## C. Cash Flow Statement terms (3 sections)
- **CFO (Operating)** — cash from core business; starts with net income, adds back non-cash items (depreciation), adjusts working capital.
- **CFI (Investing)** — buying/selling long-term assets; includes **CapEx** (capital expenditure).
- **CFF (Financing)** — raising/repaying capital; debt, equity issuance, dividends.
- **Free Cash Flow (FCF)** = CFO − CapEx. Cash truly available to investors.

## D. Profitability & return ratios
- **Gross Margin** = Gross Profit / Revenue.
- **Operating (EBIT) Margin** = EBIT / Revenue.
- **Net Margin** = Net Income / Revenue.
- **ROE (Return on Equity)** = Net Income / Shareholders' Equity. Return on owners' money.
- **ROA (Return on Assets)** = Net Income / Total Assets.
- **ROCE (Return on Capital Employed)** = EBIT / Capital Employed. Return on all long-term capital.
- **Asset Turnover** = Revenue / Total Assets. Efficiency of asset use.
- **DuPont Analysis** — breaks ROE into: Net Margin × Asset Turnover × Financial Leverage. Shows WHAT drives ROE.

## E. Leverage & liquidity ratios
- **Debt-to-Equity** = Total Debt / Equity. Leverage level.
- **Interest Coverage** = EBIT / Interest Expense. Ability to service debt. >3 healthy.
- **Current Ratio** = Current Assets / Current Liabilities. Short-term solvency.
- **Quick Ratio** = (Current Assets − Inventory) / Current Liabilities.

## F. Valuation terms
- **Market Cap** = Share price × shares outstanding. Equity value only.
- **Enterprise Value (EV)** = Market Cap + Debt − Cash. Whole-business value (see Part 3).
- **P/E Ratio** = Price / EPS. Price paid per ₹1 of earnings.
- **P/B Ratio** = Price / Book Value per share. Used for banks.
- **EV/EBITDA** — capital-structure-neutral valuation multiple.
- **EV/Sales** — used for loss-making companies.
- **PEG Ratio** = P/E ÷ growth rate. P/E adjusted for growth (~1 = fair).
- **WACC** — Weighted Average Cost of Capital. Blended cost of debt + equity; the DCF discount rate.
- **CAPM** — Cost of Equity = Rf + β(ERP). Rf = risk-free rate, β = beta, ERP = equity risk premium.
- **Terminal Value** — value of all cash flows beyond the forecast period.
- **Constant Currency (CC)** — growth stripped of FX effects; shows real underlying growth.

## G. Banking-specific terms (for HDFC)
- **NII (Net Interest Income)** = Interest earned − Interest paid.
- **NIM (Net Interest Margin)** = NII / Average interest-earning assets. Core lending profitability.
- **CASA Ratio** = (Current + Savings deposits) / Total deposits. Higher = cheaper funding.
- **CD Ratio (Credit-Deposit)** = Loans / Deposits. Liquidity/aggressiveness gauge.
- **GNPA / NNPA** — Gross / Net Non-Performing Assets %. Asset quality.
- **Provisions** — money set aside for expected loan losses.
- **PCR (Provision Coverage Ratio)** — % of bad loans covered by provisions.
- **CAR / CRAR (Capital Adequacy Ratio)** = Capital / Risk-Weighted Assets. Regulatory cushion.
- **Slippage** — loans turning into NPAs.

---

# PART 3 — VALUATION METHODS & MULTIPLES (THE INTUITION)

## A. The three approaches
1. **DCF (intrinsic):** value = present value of future free cash flows. Bottom-up, based on the company's own economics.
2. **Comps (relative):** value the company like its peers, using multiples (P/E, EV/EBITDA).
3. **DDM / P-B (for banks):** value equity directly via dividends or book value × ROE logic.

## B. EBITDA — the concept
EBITDA strips out the "noise" of **financing (interest), taxes, and accounting (depreciation/amortization)** to show the **raw operating earning power** of a business. Two identical bakeries with different debt, tax rates, and oven ages will have very different net profit but similar EBITDA — letting you compare the operations themselves.
- **Weakness:** ignores real CapEx needs and debt. Depreciation IS a real economic cost. So EBITDA flatters capital-heavy firms; it's a comparison tool, not "true profit."

## C. Enterprise Value (EV) — the concept
EV = the **all-in cost to buy the whole business.** Market cap is only the equity. If you buy a company you also **take on its debt** and **keep its cash**:
**EV = Market Cap + Debt − Cash.**
*Home analogy:* a flat "worth" ₹1cr with a ₹40L loan and ₹10L cash inside truly costs you 100 + 40 − 10 = ₹1.3cr to own outright. EV is **capital-structure neutral** — that's its power.

## D. EV/EBITDA — why we pair them
- EV = value to ALL investors (debt + equity).
- EBITDA = earnings to ALL investors (before interest paid to debt).
- They're a **matched pair**, both measured *before* the effect of debt → apples-to-apples regardless of how a company is financed.
**Use it for:** companies with different debt levels, different tax regimes, capital-intensive sectors, and M&A.

## E. P/E Ratio — the concept
Three ways to understand it:
1. "How much do I pay for ₹1 of profit?" (P/E 25 = ₹25 per ₹1 earnings).
2. Rough "payback period" in years if earnings stayed flat.
3. **Expectations gauge** — high P/E = market expects strong, durable growth and low risk.
**Key nuance:** a high P/E isn't automatically expensive; a quality, fast-growing, low-risk firm *deserves* a higher P/E. Compare to peers and own history. **Use PEG** (P/E ÷ growth) to adjust for growth.
**Weakness:** distorted by debt and one-offs; meaningless if earnings are negative.

## F. Which multiple when?
| Situation | Multiple |
|---|---|
| Same-industry equity comparison | P/E |
| Different debt levels / capital-intensive / M&A | EV/EBITDA |
| Loss-making / pre-profit | EV/Sales |
| Banks & financials | P/B and P/E (NOT EV/EBITDA) |

## G. DCF — the mechanics
1. Project Free Cash Flow (5–10 yrs).
2. Discount rate = WACC. (CAPM for cost of equity: Ke = Rf + β·ERP.)
3. Discount each year's FCF to present value.
4. Terminal Value = FCF×(1+g)/(WACC−g), then discount it back.
5. Sum PVs = Enterprise Value → minus net debt = Equity Value → ÷ shares = intrinsic price.
6. Sanity-check vs market price.

## H. Comparable Company Analysis (Comps) — the 5 steps
1. Select peer group (same industry, size, growth, margins, geography).
2. Gather financials (Capital IQ, annual reports).
3. Calculate each peer's multiples (P/E, EV/EBITDA).
4. Take the **median** (robust to outliers — say this!).
5. Apply median multiple to target's metric → implied value.
DCF answers "what *should* it be worth?"; Comps answers "what is the market *paying* for peers?" Use both and triangulate.

---

# PART 4 — INFOSYS (IT SERVICES) — FULL REPORT

## A. Business model
India's #2 IT services firm. Earns from software development, consulting, digital & AI services. Clients mostly in **US (~60%) and Europe**, billed largely in **USD**. **Asset-light** (people-driven), generates large free cash flow → ideal DCF candidate.

## B. Macro & industry context
- IT demand tied to global (esp. US/Europe) corporate tech spending. Discretionary spend is soft amid global uncertainty.
- **AI is the swing factor:** GenAI is both an opportunity (new deals) and a risk (pricing pressure on traditional work).
- Weak rupee benefits reported revenue/margins.

## C. FY26 actuals (year ended March 2026)
- **Revenue: $20,158 mn** (+3.1% constant currency) — crossed $20bn for the first time.
- **Operating margin: 20.3% reported (21.0% adjusted).**
- **Net profit: ₹29,440 cr**; EPS ~₹71.6.
- **Large deal wins (TCV): $14.9 bn**; **Free Cash Flow: $3.7 bn.**
- **FY27 guidance: revenue growth 1.5%–3.5% CC, operating margin 20%–22%.**
- Note: Q3 FY26 had a one-off ₹1,289 cr charge from new labour codes (gratuity/leave provisions).
- (Source: Infosys FY26 results, April 23, 2026; figures rephrased for compliance.)

## D. DCF valuation (worked illustration)
Base FCF ≈ ₹31,000–34,500 cr. Assume ~8% growth, WACC 12% (near debt-free, so WACC≈Ke = 6.5% + 0.9×6% = 12%), terminal growth 5%.

| Year | FCF (₹cr) | DF@12% | PV (₹cr) |
|---|---|---|---|
| 1 | 37,260 | 0.893 | 33,275 |
| 2 | 40,241 | 0.797 | 32,072 |
| 3 | 43,460 | 0.712 | 30,943 |
| 4 | 46,937 | 0.636 | 29,852 |
| 5 | 50,692 | 0.567 | 28,742 |
| | | Sum PV | ≈154,884 |

Terminal Value = 50,692×1.05/(0.12−0.05) ≈ ₹760,000cr; PV = ×0.567 ≈ ₹431,000cr.
EV ≈ 154,884 + 431,000 = **₹586,000cr**; + net cash (~₹35,000cr) → equity ≈ ₹621,000cr ÷ ~414cr shares ≈ **₹1,500/share**. Sanity check: trades ~₹1,500–1,600. ✅

## E. Comps (IT peers — P/E and EV/EBITDA)
| Company | ~P/E | ~EV/EBITDA |
|---|---|---|
| TCS | 25–28× | 16–18× |
| Infosys | 24–26× | 15–17× |
| HCLTech | 22–24× | 13–15× |
| Wipro | 19–22× | 11–13× |
| Tech Mahindra | 20–24× | 11–13× |
| **Median** | **~23×** | **~14×** |
Apply ~23× to EPS ~₹71.6 → ~₹1,650/share implied. (Verify live multiples on screener.in.)

## F. Earnings call transcript — what to look for & recent themes
Structure: safe harbor → management remarks → analyst Q&A (the gold). For Infosys watch:
- **Revenue growth guidance (CC)** — most-watched. FY27 set at 1.5–3.5%.
- **Operating margin band** (20–22%).
- **Large deal TCV** — pipeline of future revenue ($14.9bn FY26).
- **Attrition** — wage pressure signal.
- **Vertical commentary** — BFSI, retail, manufacturing demand.
- **AI/GenAI** — deal impact, productivity, pricing.
Recent narrative: resilient but modest growth, AI-led positioning, cautious-but-improving demand, strong cash generation.

## G. Annual report — key sections
MD&A (strategy/outlook), segment revenue by geography & vertical, margin walk, cash flow (confirm FCF), capital allocation (Infosys returns ~85% of FCF via dividends + buybacks).

## H. Infosys Q&A
- **Why DCF for Infosys?** Asset-light, stable, predictable FCF → reliable intrinsic value.
- **Biggest risk to the valuation?** Slower revenue growth (soft discretionary spend), margin pressure (wages/AI pricing).
- **Weak rupee effect?** Positive — earns in USD, reports in INR.
- **What is constant currency?** Growth excluding FX effects → real underlying business growth.
- **What does $14.9bn TCV signal?** Strong future revenue visibility.

---

# PART 5 — HUL (FMCG) — FULL REPORT

## A. Business model
India's largest FMCG company — everyday products (Home Care, Beauty & Wellbeing, Personal Care, Foods & Refreshment). **Stable, recurring demand**, high margins, **virtually debt-free**, asset-light. Growth = **volume + price/mix**. Clean DCF candidate.

## B. Macro & industry context
- Tied to domestic consumption, especially **rural demand** recovery.
- **Input costs** (palm oil, crude derivatives) drive gross margin; lower inflation helps.
- Theme: **premiumization** (shift to higher-value products) and rural revival.

## C. FY25 actuals (year ended March 2025)
- **Turnover: ₹60,680 cr** (+2%); FY26 ~₹63,763 cr.
- **PAT: ₹10,644 cr** (+5%), net margin ~17.5%.
- **EBITDA margin: ~23%.** **ROCE: ~108%** (asset-light, brand-driven).
- **CFO: ₹13,789 cr.** **Debt: ~zero.** EPS ~₹45.3, DPS ₹53.
- (Source: HUL FY25 results; figures rephrased for compliance.)

## D. DCF valuation (worked illustration)
FCF ≈ CFO ₹13,789cr − capex ~₹1,300cr ≈ ₹12,500cr. Growth ~9%, WACC ~11% (Ke = 6.5% + 0.65×6% ≈ 10.4%, defensive low beta), terminal g 5.5%.

| Year | FCF (₹cr) | DF@11% | PV (₹cr) |
|---|---|---|---|
| 1 | 13,625 | 0.901 | 12,275 |
| 2 | 14,851 | 0.812 | 12,059 |
| 3 | 16,188 | 0.731 | 11,833 |
| 4 | 17,645 | 0.659 | 11,628 |
| 5 | 19,233 | 0.593 | 11,405 |
| | | Sum PV | ≈59,200 |

TV = 19,233×1.055/(0.11−0.055) ≈ ₹369,000cr; PV ≈ ₹219,000cr. EV ≈ **₹278,000cr**.
**Key insight:** HUL's actual market cap (~₹5.3 lakh cr) is far higher than this base-case DCF. That's because the market prices in a longer high-growth runway, premium brand moat, and very low risk for a quality compounder. **Lesson: DCF is assumption-sensitive and can understate quality franchises — complement it with relative valuation (P/E).**

## E. Comps (FMCG peers)
| Company | ~P/E | ~EV/EBITDA |
|---|---|---|
| Nestlé India | 60–65× | 40–45× |
| HUL | 50–55× | 35–38× |
| Britannia | 50–55× | ~35× |
| Dabur | 45–50× | ~32× |
| Marico | 45–50× | ~33× |
| **Median** | **~50×** | **~35×** |
FMCG trades far above IT (~24×) due to predictable demand, asset-light models, ROCE >100%, low risk. Market pays a premium for **quality and predictability.**

## F. Earnings call transcript — what to look for
- **UVG (Underlying Volume Growth)** — THE key FMCG metric (are people buying more units?).
- **USG (Underlying Sales Growth)** = volume + price.
- **Rural vs urban demand** commentary.
- **Gross margin / raw material** cost trends.
- **A&P spend** (advertising & promotion).
- **Premiumization** progress.
Recent narrative: modest volume growth, gradual rural recovery, margin management amid input costs.

## G. Annual report — key sections
Segment performance (4 divisions), volume-vs-price split, distribution & digital reach, high dividend payout.

## H. HUL Q&A
- **Why might DCF undervalue HUL?** A 5-yr DCF with conservative growth can't capture HUL's durable growth, brand moat, and low risk; the market assigns a premium multiple.
- **Most important FMCG metric?** Underlying volume growth — real demand, independent of price hikes.
- **Why is ROCE so high?** Asset-light, brand-driven → large profits on small capital base.

---

# PART 6 — HDFC BANK — FULL REPORT (BANKS ARE DIFFERENT)

## A. Why banks need a different framework
For a bank, **deposits (debt) are the raw material**, not a financing choice, and interest is a core operating item. So **FCF and EV/EBITDA are meaningless.** Value the **equity directly** using:
1. **DDM (Dividend Discount Model)**
2. **Excess Return / Residual Income model**
3. **Justified P/B** based on ROE vs cost of equity.

## B. Business model
India's largest private bank. Earns mainly **Net Interest Income** (loan interest − deposit interest) + fee income. HDFC Ltd (the mortgage parent) merged into the bank in July 2023, making it much larger and elevating its CD ratio.

## C. Key metrics (recent) — KNOW THESE
| Metric | Meaning | HDFC Bank |
|---|---|---|
| **NIM** | Lending profitability | ~3.4–3.5% (recent quarters; improved toward ~3.35–3.5%) |
| **CASA ratio** | Low-cost deposit share | **~34%** (declined from ~38% — deposit competition; a key challenge) |
| **CD ratio** | Loans/Deposits | Brought down to **~96%** from ~110% at merger; targeting lower |
| **Deposits** | — | ₹27.15 lakh cr (FY25, +14.1%) — grew 2.5× faster than loans |
| **Advances** | — | ₹26.43 lakh cr (FY25, +5.4%) |
| **GNPA / NNPA** | Asset quality | ~1.3% / ~0.4% (very clean) |
| **ROA** | — | ~1.8–1.9% (excellent for a bank) |
| **ROE** | — | ~14–17% |
| **CAR** | Capital cushion | ~19% (well above ~11.5% minimum) |
- Q4FY25 net profit ₹17,616 cr (+6.7% YoY), NII +10%.
- **Big story:** deliberately growing deposits faster than loans to normalize CD ratio post-merger; CEO sees faster loan growth by FY27.
- (Sources: HDFC Bank FY25/Q-updates; figures rephrased for compliance.)

## D. Dividend Discount Model (DDM)
Value per share = D₁ / (Ke − g).
- **Ke (CAPM):** 6.5% + 1.0×6% = ~12.5–13% (bank beta ~1.0).
- **g = ROE × retention ratio.**
- **Catch:** HDFC's g (~12–14%) approaches Ke (~13%), which breaks single-stage Gordon (denominator → ~0). **So use a two-stage DDM** (high growth 5–7 yrs, then stable terminal). Mentioning this shows real understanding.

## E. Justified P/B — the core bank valuation tool
**P/B = (ROE − g) / (Ke − g).**
Example: ROE 16%, g 10%, Ke 13% → (0.16−0.10)/(0.13−0.10) = 2.0×.
**Logic:** a bank earning ROE > cost of equity should trade above book (P/B > 1). Higher ROE vs Ke → higher justified P/B. HDFC trades ~2.5–2.8× book — premium for clean book, strong franchise.

## F. Comps (bank peers — P/B and P/E, NOT EV/EBITDA)
| Bank | ~P/B | ~P/E | ROE |
|---|---|---|---|
| ICICI Bank | ~3.0× | ~18× | ~17% |
| HDFC Bank | ~2.5–2.8× | ~18–20× | ~15–17% |
| Kotak Mahindra | ~2.5× | ~18× | ~14% |
| Axis Bank | ~1.8–2.0× | ~13× | ~16% |
| SBI | ~1.3–1.5× | ~9–10× | ~16% |
P/B differences are **explained by ROE differences** and franchise quality. SBI (PSU) trades near book; HDFC/ICICI command premiums.

## G. Earnings call transcript — what to look for
- **NIM trajectory** (rate-cycle dependent).
- **CD ratio reduction progress** (the post-merger headline).
- **CASA growth** (deposit mobilization — top priority).
- **Loan/deposit growth guidance.**
- **Asset quality** (slippages, GNPA trend).
- **Credit costs / provisions.**

## H. Annual report — key sections
Advances & deposits growth, asset quality tables (GNPA/NNPA/PCR), CAR, retail-vs-wholesale mix, post-merger integration commentary.

## I. HDFC / banking Q&A
- **Why can't you DCF a bank?** Deposits are raw material; interest is core operating; FCF/EV meaningless. Use DDM / residual income / justified P/B.
- **What is NIM?** (Interest earned − paid)/avg earning assets. Core lending profitability (~3.4–3.5%).
- **High CASA tells you?** Cheaper funding → supports NIM. HDFC ~34%, growing it is a priority.
- **Why did CD ratio spike?** HDFC Ltd merger added loans without matching deposits; bank is normalizing it (~96% now).
- **Why does a bank trade above book value?** Because ROE > cost of equity — justified P/B = (ROE−g)/(Ke−g).

---

# PART 7 — COMPREHENSIVE INTERVIEW Q&A BANK

## A. Financial statements
- **Connect the 3 statements.** Net income → retained earnings (BS) + top of CF. Ending cash (CF) → cash (BS). Depreciation links IS→BS via CF. Assets = Liabilities + Equity always.
- **Depreciation +₹100 (30% tax), walk through.** IS: net income −₹70. CF: −70 +100 add-back = cash +₹30. BS: cash +30, PP&E −100 (net −70); retained earnings −70 → balances.
- **Where does CapEx go?** Investing. **Dividends?** Financing. **Depreciation?** Operating (add-back).
- **If depreciation rises, does asset value fall?** Yes — net book value = cost − accumulated depreciation falls.

## B. Valuation & multiples
- **DCF vs Comps?** Intrinsic vs relative; complementary; triangulate.
- **Why EV/EBITDA over P/E?** Capital-structure & tax neutral; matches whole-company value to whole-company earnings.
- **P/E of 70 — overvalued?** Not necessarily; reflects growth + low risk; check vs peers, history, PEG.
- **Why median, not mean, in comps?** Robust to outliers.
- **What is WACC?** Blended cost of debt + equity; DCF discount rate.
- **Most sensitive DCF inputs?** WACC and terminal growth rate.
- **What is terminal value?** Value of cash flows beyond forecast; often 60–80% of DCF value.

## C. Ratios
- **EPS** = (Net income − pref div)/weighted avg shares. Basic vs diluted (diluted ≤ basic).
- **Interest coverage** = EBIT/Interest. >3 healthy.
- **ROE vs ROA vs ROCE** — equity vs total assets vs total capital employed.
- **DuPont:** ROE = Net Margin × Asset Turnover × Leverage.

## D. Markets & instruments (from earlier HR list)
- **Bond:** debt IOU; lender gets coupon + principal at maturity. Price moves inverse to rates.
- **Derivatives:** value derived from an underlying; for hedging/speculation. Types: forwards, futures, options, swaps.
- **Financial assets:** intangible claims (cash, stocks, bonds, derivatives) vs physical assets.
- **Equity & FX:** ownership shares; foreign-exchange currency market.
- **Capital IQ (CIQ):** S&P Global Market Intelligence's flagship data platform. **CIQ Estimates** = aggregated analyst consensus forecasts (revenue, EPS, EBITDA).
- **Debt vs Equity capital structure:** debt = borrowed (interest, tax-deductible, must repay, lower cost, higher risk); equity = ownership (no repayment, dividends, higher cost). Optimal mix minimizes WACC.

---

# PART 8 — BEHAVIORAL, GAP & SENIOR-LEVEL QUESTIONS

## A. Introduction (memorize)
"I'm Apoorva Singh, MBA in Finance & Business Analytics. I began as an Associate Analyst in EY's Strategy & Transaction team, working on market intelligence and financial analysis using tools like Capital IQ and Factiva. Since then I've deepened my valuation skills through independent financial research — building DCF models and analyzing companies across IT, FMCG, and banking. I'm drawn to this role because it combines financial data with precision and quality — and I've actually used S&P's own platforms like Capital IQ, so I understand why accurate data matters from the user's side."

## B. The gap (brief, confident, pivot to what you did)
"My EY role gave me a strong analytical foundation. After that I stepped back from full-time work for personal reasons, but I deliberately kept my skills sharp through independent valuation research — going deep on DCF and comparable analysis across sectors. I'm now fully ready and very motivated to bring those sharpened skills back into a corporate setting, and this role is the ideal fit."

## C. "Overqualified for an entry contract role — why?"
"I see this as the right way to re-enter a domain I'm passionate about with a global leader. I can ramp up fast and add value from day one, and I'm committed to the 12-month engagement and growing within S&P."

## D. Why S&P / Why this role
"S&P is the global leader in essential financial intelligence — ratings, indices like the S&P 500, and analytics. I've used its products as an analyst and respect the data quality. I want to contribute to and grow within that ecosystem."

## E. Strengths / weakness
Strength: attention to detail, financial data fluency, analytical rigor, fast learner. Weakness: "I can be a perfectionist about accuracy — I've learned to balance it by respecting deadlines and prioritizing."

## F. Senior-manager-level (expect these from a Finance master)
- "Walk me through how depreciation flows through all three statements." (Know cold — Part 7A.)
- "Why would a DCF and a comps valuation diverge, and which would you trust?" → Different assumptions vs market sentiment; reconcile both, investigate the gap.
- "How does a rate cut affect a bank's NIM?" → Short-term margin compression (loans reprice faster than deposits), but can boost loan demand.
- "Why do consumer staples trade at higher multiples than IT?" → Predictability, durability, low cyclicality, high ROCE.
- "What's the link between ROE and P/B for a bank?" → Justified P/B = (ROE−g)/(Ke−g).
- "If you had to value a bank, what would you NOT use and why?" → Not DCF/EV-EBITDA — deposits are raw material.

## G. The HDFC honesty story (use this — it's authentic and impressive)
"I started building a DCF for HDFC Bank and realized the FCF-based approach doesn't fit banks, because deposits are their raw material and interest is core to operations. That led me to learn the bank-specific framework — dividend discount and residual income models, and justified price-to-book against ROE, plus metrics like NIM, CASA, and CD ratio. It taught me to match the valuation method to the business model rather than apply one blindly."

## H. Smart questions to ASK them
- "Which vertical would I likely be placed in given my background?"
- "What does success look like in the first 3–6 months?"
- "Are there pathways from this contract role to a permanent position at S&P?"
- "Which datasets and tools would I primarily work with?"

---

# PART 9 — MOCK INTERVIEW SCRIPT (practice out loud)

1. Tell me about yourself. → (Part 8A)
2. Why the gap / short EY tenure? → (Part 8B)
3. Why S&P and why this entry-level role? → (Part 8C/D)
4. What is fundamental macro-driven analysis? → (Part 1)
5. Walk me through a DCF. → (Part 3G)
6. How would you value Infosys? → DCF (Part 4D) + comps.
7. Why might HUL's DCF be below its market cap? → (Part 5H)
8. How would you value HDFC Bank, and why differently? → (Part 6A/E)
9. What is NIM / CASA / CD ratio? → (Part 6C)
10. Explain EV, EBITDA, and why EV/EBITDA. → (Part 3B–D)
11. What does a high P/E mean? → (Part 3E)
12. Connect the 3 financial statements. → (Part 7A)
13. What is Capital IQ? → S&P's platform; CIQ Estimates = consensus forecasts.
14. Any questions for us? → (Part 8H)

---

## FINAL MINDSET
You are a skilled finance professional who has used S&P's own products, choosing to re-enter through this role. Lead with substance, stay calm, and let your genuine understanding show. Everything in this report is true once you've studied it — so speak with quiet confidence. Good luck, Apoorva.
