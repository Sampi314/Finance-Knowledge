# Future value of annuity - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/future-value-of-annuity

---

[Skip to main content](https://exceljet.net/formulas/future-value-of-annuity#main-content)

[](https://exceljet.net/formulas/future-value-of-annuity#)

*   [Previous](https://exceljet.net/formulas/estimate-mortgage-payment)
    
*   [Next](https://exceljet.net/formulas/future-value-vs.-present-value)
    

[Financial](https://exceljet.net/formulas#Financial)

Future value of annuity
=======================

by Dave Bruns · Updated 3 Oct 2020

Related functions 
------------------

[FV](https://exceljet.net/functions/fv-function)

[PV](https://exceljet.net/functions/pv-function)

![Excel formula: Future value of annuity](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/future%20value%20of%20annuity.png "Excel formula: Future value of annuity")

Summary
-------

To get the present value of an annuity, you can use the [FV function](https://exceljet.net/functions/fv-function)
. In the example shown, the formula in C7 is:

    =FV(C5,C6,-C4,0,0)
    

Generic formula
---------------

    =FV(rate,periods,payment)

Explanation 
------------

The [FV function](https://exceljet.net/functions/fv-function)
 is a financial function that returns the future value of an investment. You can use the FV function to get the future value of an investment assuming periodic, constant payments with a constant interest rate. An annuity is a series of equal cash flows, spaced equally in time.  

In this example, a $5000 payment is made each year for 25 years, with an interest rate of 7%. To calculate future value, the FV function is configured as follows like this in cell C7:

    =FV(C5,C6,-C4,0,0)
    

with the following inputs:

*   **rate** - the value from cell C5, 7%.
*   **nper** - the value from cell C6, 25.
*   **pmt** - negative value from cell C4, -100000
*   **pv** - 0.
*   **type** - 0, payment at end of period (regular annuity).

With this information, the FV function returns $316,245.19. Note payment is entered as a negative number, so the result is positive.

### Annuity due

An annuity due is a repeating payment made at the _beginning_ of each period, instead of at the _end_ of each period. To calculate an annuity due with the FV function, set the _type_ argument to 1:

    =FV(C5,C6,-C4,0,1)
    

With type set to 1, FV returns $338,382.35.

Related formulas
----------------

[![Excel formula: Present value of annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/present%20value%20of%20annuity.png "Excel formula: Present value of annuity")](https://exceljet.net/formulas/present-value-of-annuity)

### [Present value of annuity](https://exceljet.net/formulas/present-value-of-annuity)

The PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate. An annuity is a series of equal cash flows,...

[![Excel formula: Future value vs. Present value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/future%20value%20vs%20present%20value%20arrows.png "Excel formula: Future value vs. Present value")](https://exceljet.net/formulas/future-value-vs.-present-value)

### [Future value vs. Present value](https://exceljet.net/formulas/future-value-vs.-present-value)

The FV function is a financial function that returns the future value of an investment, given periodic, constant payments with a constant interest rate. The PV function returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future...

Related functions
-----------------

[![Excel FV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_fv.png "Excel FV function")](https://exceljet.net/functions/fv-function)

### [FV Function](https://exceljet.net/functions/fv-function)

The Excel FV function is a financial function that returns the future value of an investment. You can use the FV function to get the future value of an investment assuming periodic, constant payments with a constant interest rate.

[![Excel PV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20pv%20function.png "Excel PV function")](https://exceljet.net/functions/pv-function)

### [PV Function](https://exceljet.net/functions/pv-function)

The Excel PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Present value of annuity](https://exceljet.net/formulas/present-value-of-annuity)
    
*   [Future value vs. Present value](https://exceljet.net/formulas/future-value-vs.-present-value)
    

### Functions

*   [FV Function](https://exceljet.net/functions/fv-function)
    
*   [PV Function](https://exceljet.net/functions/pv-function)
    

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