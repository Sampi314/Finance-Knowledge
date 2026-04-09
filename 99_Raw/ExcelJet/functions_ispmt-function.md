# Excel ISPMT function | Exceljet

**Source:** https://exceljet.net/functions/ispmt-function

---

[Skip to main content](https://exceljet.net/functions/ispmt-function#main-content)

[](https://exceljet.net/functions/ispmt-function#)

*   [Previous](https://exceljet.net/functions/irr-function)
    
*   [Next](https://exceljet.net/functions/mduration-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

ISPMT Function
==============

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[IPMT](https://exceljet.net/functions/ipmt-function)

![Excel ISPMT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_ispmt_function.png "Excel ISPMT function")

Summary
-------

The Excel ISPMT function calculates the interest paid during a given period of an investment where principal payments are equal. The given period is specified as a zero-based number instead of a 1-based number.

Purpose 
--------

Get interest paid for specific period

Return value 
-------------

Interest amount in given period

Syntax
------

    =ISPMT(rate,per,nper,pv)

*   _rate_ - Interest rate.
*   _per_ - Period (starts with zero, not 1).
*   _nper_ - Number of periods.
*   _pv_ - Present value.

Using the ISPMT function 
-------------------------

The ISPMT function calculates the amount of interest in a given period of an investment where principal payments are equal. The given period is specified as a zero-based number instead of a 1-based number. For example, to calculate the interest amount in payments for a loan where the amount is $10,000, the interest rate is 10%, and there are 5 periods in which the principal payment is constant (even), you can use:

    =ISPMT(10%,0,5,-10000) // interest in period 1
    =ISPMT(10%,1,5,-10000) // interest in period 2
    =ISPMT(10%,2,5,-10000) // interest in period 3
    =ISPMT(10%,3,5,-10000) // interest in period 4
    =ISPMT(10%,4,5,-10000) // interest in period 5
    

In the example shown, the formula in H11, copied down, is:

    =ISPMT($C$6,B11-1,$C$7,-$C$5)
    

Note ISPMT assumes principal amounts are equal, but the payment is variable. For a loan where the payment is a fixed amount, see the [IPMT function](https://exceljet.net/functions/ipmt-function)
.

### Notes

1.  Be consistent with the units. For a 3 year loan with monthly payments and an annual interest rate of 10%, enter _rate_ as 10%/12. Enter _nper_ as 3\*12.
    
2.  ISPMT uses a zero-based index for period (_per_). Use 0 for period 1, 1 for period 2, etc.
    
3.  The PPMT function is for loans with even principal payments. For a loan with even periodic payments, use the IPMT function.
    

Related functions
-----------------

[![Excel IPMT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_ipmt_function.png "Excel IPMT function")](https://exceljet.net/functions/ipmt-function)

### [IPMT Function](https://exceljet.net/functions/ipmt-function)

The Excel IPMT function is a financial function used to calculate the interest payment for a given period of an investment or a loan, based on constant periodic payments and a constant interest rate. For example, you can use IPMT to get the interest amount of a loan payment for the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [IPMT Function](https://exceljet.net/functions/ipmt-function)
    

### Links

*   [Microsoft ISPMT function documentation](https://support.office.com/en-us/article/ispmt-function-fa58adb6-9d39-4ce0-8f43-75399cea56cc)
    

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