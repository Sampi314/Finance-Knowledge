# Excel FVSCHEDULE function | Exceljet

**Source:** https://exceljet.net/functions/fvschedule-function

---

[Skip to main content](https://exceljet.net/functions/fvschedule-function#main-content)

[](https://exceljet.net/functions/fvschedule-function#)

*   [Previous](https://exceljet.net/functions/fv-function)
    
*   [Next](https://exceljet.net/functions/intrate-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

FVSCHEDULE Function
===================

by Dave Bruns · Updated 27 Aug 2021

Related functions 
------------------

[FV](https://exceljet.net/functions/fv-function)

[PV](https://exceljet.net/functions/pv-function)

![Excel FVSCHEDULE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_fvschedule_function.png "Excel FVSCHEDULE function")

Summary
-------

The Excel FVSCHEDULE function returns the future value of a single sum based on a schedule of given interest rates. FVSCHEDULE can be used to find the future value of an investment with a variable or adjustable rate.

Purpose 
--------

Get future value of principal compound interest

Return value 
-------------

Future value

Syntax
------

    =FVSCHEDULE(principal,schedule)

*   _principal_ - The initial investment sum.
*   _schedule_ - Schedule of interest rates, provided as range or array.

Using the FVSCHEDULE function 
------------------------------

The FVSCHEDULE function calculates the future value of a single sum based on a schedule of interest rates. The interest rates can vary in each period. As such, FVSCHEDULE can be used to find the future value of an investment with a variable or adjustable rate.

By contrast, the [FV function](https://exceljet.net/functions/fv-function)
 can also be used to find the future value of a sum based on a given interest rate, it can't handle different rates in different periods.

### Example

In the example shown, an initial sum of $1000 is invested for 4 years. In each year, the rate is different as shown below:

| Period | Rate |
| --- | --- |
| Year 1 | 2.00% |
| Year 2 | 3.00% |
| Year 3 | 4.00% |
| Year 4 | 5.00% |

In the example, the rates are entered in the range C8:C11. The formula in F5 is:

    =FVSCHEDULE(C5,C8:C11)
    

FVSCHEDULE returns $1,147.26, when [currency number format](https://exceljet.net/articles/custom-number-formats)
 is applied.

### Schedule

The values in _schedule_ can be provided as a range of cells (per the example) or an array constant. For example, the formula below provides the _principal_ as C5, but rates are hardcoded into an [array constant](https://exceljet.net/glossary/array-constant)
:

    =FVSCHEDULE(C5,{0.02;0.03;0.04;0.05})
    

The result is the same as above, $1,147.26.

### Notes

*   Blank cells in the _schedule_ are treated as zeros
*   FVSCHEDULE will return #VALUE if any values are non-numeric

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

### Functions

*   [FV Function](https://exceljet.net/functions/fv-function)
    
*   [PV Function](https://exceljet.net/functions/pv-function)
    

### Links

*   [Microsoft FVSCHEDULE function documentation](https://support.office.com/en-us/article/fvschedule-function-bec29522-bd87-4082-bab9-a241f3fb251d)
    

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