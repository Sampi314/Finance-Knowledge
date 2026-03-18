# IFERROR Excel Shortcut to Wrap All Formulas, a VBA alternative

**Source:** https://macabacus.com/blog/iferror-excel-formula-shortcut

---

IFERROR Excel Shortcut: How to Error-Wrap Your Formulas
=======================================================

[![iferror screenshot](https://macabacus.com/assets/2023/09/iferror-screenshot.png)](https://macabacus.com/assets/2023/09/iferror-screenshot.png)

Excel often contains many interconnected formulas that can produce errors if a cell contains an invalid value. These errors can crash the model and make it unusable. The IFERROR function provides an easy way to handle potential errors and prevent them from breaking your spreadsheets.

Build Financial Models in Minutes
---------------------------------

**Enterprise-Grade Financial Modeling** used by 80,000+ professionals across Investment Banking, Private Equity, and Corporate Finance. Ensure consistency, accuracy, and efficiency across your entire organization.

[Get Started](https://macabacus.com/start-trial)
[Book a Demo](https://macabacus.com/demo-request)

**What is IFERROR?**
--------------------

IFERROR is an Excel function that allows you to capture potential errors in a formula and replace the error with a value you specify. The syntax is: **\=IFERROR(value,value\_if\_error)**

Where:

*   Value is the formula that may produce an error
*   Value\_if\_error is the value to return if an error occurs

IFERROR checks if the first argument returns an error. If it does, it will return the second argument. If not, it will return the first argument.

**Where to Use IFERROR in Excel Models**
----------------------------------------

IFERROR is useful whenever errors need to be contained to preserve model stability. Some common examples include:

*   **Division** – Wrapping divisors in IFERROR prevents #DIV/0! errors. =IFERROR(100/B12,0)

*   **VLOOKUP** – Lookup functions may fail if data changes. IFERROR displays a message. =IFERROR(VLOOKUP(A3,$D$2:$E$100,2,FALSE),”No match”)

*   **External links** – Links to other workbooks may break if locations change. =IFERROR(‘\[\\Sales.xlsx\]Sheet1’!A1,”Sales unavailable”)

*   **Data validation** – If inputs are restricted via Data Validation, errors can appear if invalid entries occur. =IFERROR(A1,””)

*   **Interim calculations** – Prevent errors in interim formulas from spreading through the model. =IFERROR(B4\*B5,0)

*   **Error checking** – Purposefully generate errors to test downstream impacts. =IFERROR(1/0,”Divide by zero error”)

**Best Practices When Using IFERROR**
-------------------------------------

Follow these tips when using IFERROR to help you create clean models and debug for accuracy.

*   **Be descriptive** – Use clear messages that indicate the error reason and any action needed.
*   **Use judiciously** – Don’t overuse IFERROR just to hide errors. Fix the root cause when feasible.
*   **Nest multiple IFERRORs** – You can nest IFERRORs to handle different potential errors. =IFERROR(IFERROR(A1/B1,0), “Error”)
*   **Place at start** – Put IFERROR at the start of a formula containing many operations. =IFERROR((A1+A2+A3…),0)
*   **Use on final outputs** – No need to use on intermediate calculations, only final error-sensitive outputs.
*   **Keep formulas simple** – Complex nested formulas are harder to debug. Break formulas into steps.
*   **Test thoroughly** – Rigorously test all error scenarios to ensure proper handling.

**Using Macabacus to Easily Add IFERROR Protection**
----------------------------------------------------

Adding IFERROR protection across large models with thousands of formulas can take a very long time. Creating a VBA script is an option, but you’ll then need to manage that script and your own VBA library. Fortunately, Macabacus, a popular Excel add-in for financial modeling, can make this process run a lot smoother.

With Macabacus, you can select a range of cells and instantly wrap every formula with IFERROR. Just select the target cells, open the Macabacus Formula Audit ribbon tab, choose Wrap Formulas with IFERROR, and specify the value to return on error.

Here’s a quick video demonstrating that:

Macabacus will scan all selected cells, identify those containing formulas, and wrap them with IFERROR. This makes it fast and easy to protect your model’s key outputs. Macabacus also includes model debugging tools to visualize errors, perform mass error checking, break formula circularities, and more. Combined with IFERROR wrapping, Macabacus provides a robust solution to error-proof models.

[**Try Macabacus today**](https://macabacus.com/start-trial)
 for free and experience the ease of wrapping your formulas with IFERROR.

Discover more topics
--------------------

[Webinar: The AI Edge in Investment Banking](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

Join experts from Macabacus & LSEG to learn practical insights about AI’s influence on the future of banking.

[Read more](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

[DCF Excel Template](https://macabacus.com/excel/templates/discounted-cash-flow)

Elevate your investment analysis with our free DCF model template. Understand discounted cash flow principles and perform accurate valuations in Excel.

[Read more](https://macabacus.com/excel/templates/discounted-cash-flow)

[Operating Model Excel Template](https://macabacus.com/excel/templates/operating-model)

Download our free operating model Excel template. Forecast revenue, expenses, and key financial metrics for better decision-making.

[Read more](https://macabacus.com/excel/templates/operating-model)

[LBO Excel Model](https://macabacus.com/excel/templates/lbo-model-short)

Try LBO modeling with our comprehensive Excel template. Understand key concepts, calculate returns, and gain actionable insights.

[Read more](https://macabacus.com/excel/templates/lbo-model-short)