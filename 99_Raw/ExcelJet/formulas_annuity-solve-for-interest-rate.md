# Annuity solve for interest rate - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/annuity-solve-for-interest-rate

---

[Skip to main content](https://exceljet.net/formulas/annuity-solve-for-interest-rate#main-content)

[](https://exceljet.net/formulas/annuity-solve-for-interest-rate#)

*   [Previous](https://exceljet.net/formulas/annual-compound-interest-schedule)
    
*   [Next](https://exceljet.net/formulas/bond-valuation-example)
    

[Financial](https://exceljet.net/formulas#Financial)

Annuity solve for interest rate
===============================

by Dave Bruns · Updated 1 Oct 2020

Related functions 
------------------

[RATE](https://exceljet.net/functions/rate-function)

![Excel formula: Annuity solve for interest rate](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/annuity%20solve%20for%20rate.png "Excel formula: Annuity solve for interest rate")

Summary
-------

To solve for an annuity interest rate, you can use the [RATE function](https://exceljet.net/functions/rate-function)
. In the example shown, C9 contains this formula:

    =RATE(C7,-C6,C4,C5)
    

Generic formula
---------------

    =RATE(nper,pmt,pv,fv)

Explanation 
------------

An annuity is a series of equal cash flows, spaced equally in time. The goal in this example is to have $100,000 at the end of 10 years, with an annual payment of $7,500 made at the end of each year. What interest rate is required?

To solve for the interest rate, the [RATE function](https://exceljet.net/functions/rate-function)
 is configured like this in cell C9:

    =RATE(C7,-C6,C4,C5)
    

**nper** - from cell C7, 10.  
**pmt** - from cell -C6, -7500  
**pv** - from cell C4, 0.  
**fv** - from cell C5, 100000

With this information, the RATE function returns 0.0624. When a percentage [number format](https://exceljet.net/articles/custom-number-formats)
 is applied, the result displays as 6.24%. Note payment is negative because it represents a cash outflow.

Related formulas
----------------

[![Excel formula: Future value of annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/future%20value%20of%20annuity.png "Excel formula: Future value of annuity")](https://exceljet.net/formulas/future-value-of-annuity)

### [Future value of annuity](https://exceljet.net/formulas/future-value-of-annuity)

The FV function is a financial function that returns the future value of an investment. You can use the FV function to get the future value of an investment assuming periodic, constant payments with a constant interest rate. An annuity is a series of equal cash flows, spaced equally in time. In...

[![Excel formula: Future value vs. Present value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/future%20value%20vs%20present%20value%20arrows.png "Excel formula: Future value vs. Present value")](https://exceljet.net/formulas/future-value-vs.-present-value)

### [Future value vs. Present value](https://exceljet.net/formulas/future-value-vs.-present-value)

The FV function is a financial function that returns the future value of an investment, given periodic, constant payments with a constant interest rate. The PV function returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future...

[![Excel formula: Present value of annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/present%20value%20of%20annuity.png "Excel formula: Present value of annuity")](https://exceljet.net/formulas/present-value-of-annuity)

### [Present value of annuity](https://exceljet.net/formulas/present-value-of-annuity)

The PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate. An annuity is a series of equal cash flows,...

[![Excel formula: Payment for annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/annuity%20payment%20amount.png "Excel formula: Payment for annuity")](https://exceljet.net/formulas/payment-for-annuity)

### [Payment for annuity](https://exceljet.net/formulas/payment-for-annuity)

The PMT function is a financial function that returns the periodic payment for a loan. You can use the PMT function to figure out payments for a loan, given the loan amount, number of periods, and interest rate. An annuity is a series of equal cash flows, spaced equally in time. The goal in this...

Related functions
-----------------

[![Excel RATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rate%20function.png "Excel RATE function")](https://exceljet.net/functions/rate-function)

### [RATE Function](https://exceljet.net/functions/rate-function)

The Excel RATE function is a financial function that returns the interest rate per period of an annuity. You can use RATE to calculate the periodic interest rate, then multiply as required to derive the annual interest rate. The RATE function calculates by iteration.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Future value of annuity](https://exceljet.net/formulas/future-value-of-annuity)
    
*   [Future value vs. Present value](https://exceljet.net/formulas/future-value-vs.-present-value)
    
*   [Present value of annuity](https://exceljet.net/formulas/present-value-of-annuity)
    
*   [Payment for annuity](https://exceljet.net/formulas/payment-for-annuity)
    

### Functions

*   [RATE Function](https://exceljet.net/functions/rate-function)
    

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)