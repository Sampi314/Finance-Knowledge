# Excel PDURATION function | Exceljet

**Source:** https://exceljet.net/functions/pduration-function

---

[Skip to main content](https://exceljet.net/functions/pduration-function#main-content)

[](https://exceljet.net/functions/pduration-function#)

*   [Previous](https://exceljet.net/functions/oddlyield-function)
    
*   [Next](https://exceljet.net/functions/pmt-function)
    

Excel 2013

[Financial](https://exceljet.net/functions#Financial)

PDURATION Function
==================

by Dave Bruns · Updated 12 Feb 2019

Related functions 
------------------

[NPER](https://exceljet.net/functions/nper-function)

![Excel PDURATION function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_pduration_function2.png "Excel PDURATION function")

Summary
-------

The Excel PDURATION function returns the number of periods required for an investment to reach a desired value.

Purpose 
--------

Get periods required to reach given value

Return value 
-------------

Required time in periods

Syntax
------

    =PDURATION(rate,pv,fv)

*   _rate_ - Interest rate per period.
*   _pv_ - Present value of the investment.
*   _fv_ - Future value of the investment.

Using the PDURATION function 
-----------------------------

The PDURATION function calculates how much time is needed for an initial investment (present value) to reach a given amount (future value), assuming a constant annual interest rate. PDURATION returns an amount of time in periods, which is linked to the number of compounding periods per year. With one compounding period per year, periods = years. With 4 compounding periods per year, periods = quarters, and so on.

_Note: the [NPER function](https://exceljet.net/functions/nper-function)
 returns the number of periods for a series of cash flows (like a loan repayment schedule) whereas PDURATION returns the number of periods for a single sum to achieve a certain amount._

### Example

Assume you have $5,000 to invest at an annual rate of 5%. When interest is compounded monthly, how long will it take for the initial investment of $5,000 to reach $10,000? In the example shown, the formula in F5 is:

    =PDURATION(C5/C6,C7,C8)
    

Notice because rate must be provided as interest rate per period, it is given here as the annual interest rate divided by the number of compounding periods per year (12). With these inputs, PDURATION returns 166.70 periods. Since interest is compounded monthly, periods correspond to months. To convert to years, the formula in F6 is:

    =F5/C6
    

Related functions
-----------------

[![Excel NPER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_nper.png "Excel NPER function")](https://exceljet.net/functions/nper-function)

### [NPER Function](https://exceljet.net/functions/nper-function)

The Excel NPER function is a financial function that returns the number of periods for a loan or investment. You can use the NPER function to get the number of payment periods for a loan, given the amount, the interest rate, and periodic payment amount.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [NPER Function](https://exceljet.net/functions/nper-function)
    

### Links

*   [Microsoft PDURATION function documentation](https://support.office.com/en-us/article/pduration-function-44f33460-5be5-4c90-b857-22308892adaf)
    

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