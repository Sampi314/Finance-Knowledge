# Payment for annuity - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/payment-for-annuity

---

[Skip to main content](https://exceljet.net/formulas/payment-for-annuity#main-content)

[](https://exceljet.net/formulas/payment-for-annuity#)

*   [Previous](https://exceljet.net/formulas/npv-formula-for-net-present-value)
    
*   [Next](https://exceljet.net/formulas/present-value-of-annuity)
    

[Financial](https://exceljet.net/formulas#Financial)

Payment for annuity
===================

by Dave Bruns · Updated 3 Oct 2020

Related functions 
------------------

[PMT](https://exceljet.net/functions/pmt-function)

[PV](https://exceljet.net/functions/pv-function)

[FV](https://exceljet.net/functions/fv-function)

![Excel formula: Payment for annuity](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/annuity%20payment%20amount.png "Excel formula: Payment for annuity")

Summary
-------

To solve for an annuity payment, you can use the PMT function. In the example shown, C9 contains this formula:

    =PMT(C6,C7,C4,C5,0)
    

Generic formula
---------------

    =PMT(rate,nper,pv,fv,type)

Explanation 
------------

The [PMT function](https://exceljet.net/functions/pmt-function)
 is a financial function that returns the periodic payment for a loan. You can use the PMT function to figure out payments for a loan, given the loan amount, number of periods, and interest rate. An annuity is a series of equal cash flows, spaced equally in time.

The goal in this example is to have 100,000 at the end of 10 years, with an interest rate of 5%. Payments are made annually, at the end of each year. The formula in cell C9 is:

    =PMT(C6,C7,C4,C5,0)
    

where:

*   **rate** - from cell C6, 5%.
*   **nper** - from cell C7, 25.
*   **pv** - from cell C4, 0.
*   **fv** - from cell C5, 100000.
*   **type** - 0, payment at end of period (regular annuity).

With this information, the PMT function returns -$7,950.46. The value is negative because it represents a cash outflow.

### Annuity due

With an annuity due, payments are made at the _beginning_ of the period, instead of the _end_. To calculate the payment for an annuity due, use 1 for the _type_ argument. In the example shown, the formula in C11 is:

    =PMT(C6,C7,C4,C5,1)
    

which returns -$7,571.86 as the payment amount. Notice the only difference in this formula is type = 1.

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

Related functions
-----------------

[![Excel PMT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_pmt.png "Excel PMT function")](https://exceljet.net/functions/pmt-function)

### [PMT Function](https://exceljet.net/functions/pmt-function)

The Excel PMT function is a financial function that returns the periodic payment for a loan. You can use the PMT function to figure out payments for a loan, given the loan amount, number of periods, and interest rate.

[![Excel PV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20pv%20function.png "Excel PV function")](https://exceljet.net/functions/pv-function)

### [PV Function](https://exceljet.net/functions/pv-function)

The Excel PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate.

[![Excel FV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_fv.png "Excel FV function")](https://exceljet.net/functions/fv-function)

### [FV Function](https://exceljet.net/functions/fv-function)

The Excel FV function is a financial function that returns the future value of an investment. You can use the FV function to get the future value of an investment assuming periodic, constant payments with a constant interest rate.

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
    

### Functions

*   [PMT Function](https://exceljet.net/functions/pmt-function)
    
*   [PV Function](https://exceljet.net/functions/pv-function)
    
*   [FV Function](https://exceljet.net/functions/fv-function)
    

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