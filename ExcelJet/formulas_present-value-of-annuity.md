# Present value of annuity - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/present-value-of-annuity

---

[Skip to main content](https://exceljet.net/formulas/present-value-of-annuity#main-content)

[](https://exceljet.net/formulas/present-value-of-annuity#)

*   [Previous](https://exceljet.net/formulas/payment-for-annuity)
    
*   [Next](https://exceljet.net/formulas/required-recovery-rate)
    

[Financial](https://exceljet.net/formulas#Financial)

Present value of annuity
========================

by Dave Bruns · Updated 3 Oct 2020

Related functions 
------------------

[PV](https://exceljet.net/functions/pv-function)

[FV](https://exceljet.net/functions/fv-function)

![Excel formula: Present value of annuity](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/present%20value%20of%20annuity.png "Excel formula: Present value of annuity")

Summary
-------

To get the present value of an annuity, you can use the PV function. In the example shown, the formula in C9 is:

    =PV(C5,C6,C4,0,0)
    

Generic formula
---------------

    =PV(rate,periods,payment,0,0)

Explanation 
------------

The [PV function](https://exceljet.net/functions/pv-function)
 is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate. An annuity is a series of equal cash flows, spaced equally in time

In this example, an annuity pays 10,000 per year for the next 25 years, with an interest rate (discount rate) of 7%. The PV function is configured as follows in cell C9:

    =PV(C5,C6,C4,0,0)
    

The inputs to PV are as follows:

*   **rate** - the value from cell C7, 7%.
*   **nper** - the value from cell C8, 25.
*   **pmt** - the value from cell C6, 100000.
*   **fv** - 0.
*   **type** - 0, payment at end of period (regular annuity).

With this information, the present value of the annuity is $116,535.83. Note payment is entered as a negative number, so the result is positive.

### Annuity due

With an annuity due, payments are made at the beginning of the period, instead of the end. To calculate present value for an annuity due, use 1 for the _type_ argument. In the example shown, the formula in F9 is:

    =PV(F7,F8,-F6,0,1)
    

Note the inputs (which come from column F) are the same as the original formula. The only difference is _type_ = 1.

Related formulas
----------------

[![Excel formula: Future value of annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/future%20value%20of%20annuity.png "Excel formula: Future value of annuity")](https://exceljet.net/formulas/future-value-of-annuity)

### [Future value of annuity](https://exceljet.net/formulas/future-value-of-annuity)

The FV function is a financial function that returns the future value of an investment. You can use the FV function to get the future value of an investment assuming periodic, constant payments with a constant interest rate. An annuity is a series of equal cash flows, spaced equally in time. In...

[![Excel formula: Future value vs. Present value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/future%20value%20vs%20present%20value%20arrows.png "Excel formula: Future value vs. Present value")](https://exceljet.net/formulas/future-value-vs.-present-value)

### [Future value vs. Present value](https://exceljet.net/formulas/future-value-vs.-present-value)

The FV function is a financial function that returns the future value of an investment, given periodic, constant payments with a constant interest rate. The PV function returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future...

[![Excel formula: Bond valuation example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Bond%20valuation%20example.png "Excel formula: Bond valuation example")](https://exceljet.net/formulas/bond-valuation-example)

### [Bond valuation example](https://exceljet.net/formulas/bond-valuation-example)

In the example shown, we have a 3-year bond with a face value of $1,000. The coupon rate is 7% so the bond will pay 7% of the $1,000 face value in interest every year, or $70. However, because interest is paid semiannually in two equal payments, there will be 6 coupon payments of $35 each. The $1,...

Related functions
-----------------

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
    
*   [Bond valuation example](https://exceljet.net/formulas/bond-valuation-example)
    

### Functions

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