# Excel TBILLEQ function | Exceljet

**Source:** https://exceljet.net/functions/tbilleq-function

---

[Skip to main content](https://exceljet.net/functions/tbilleq-function#main-content)

[](https://exceljet.net/functions/tbilleq-function#)

*   [Previous](https://exceljet.net/functions/syd-function)
    
*   [Next](https://exceljet.net/functions/tbillprice-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

TBILLEQ Function
================

by Dave Bruns · Updated 21 Sep 2021

Related functions 
------------------

[TBILLPRICE](https://exceljet.net/functions/tbillprice-function)

[TBILLEQ](https://exceljet.net/functions/tbilleq-function)

[TBILLYIELD](https://exceljet.net/functions/tbillyield-function)

![Excel TBILLEQ function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_%20tbilleq_function.png "Excel TBILLEQ function")

Summary
-------

The Excel TBILLEQ function returns the bond-equivalent yield for a Treasury bill.

Purpose 
--------

Get bond-equivalent yield for a Treasury bill

Return value 
-------------

Yield as percentage

Syntax
------

    =TBILLEQ(settlement,maturity,discount)

*   _settlement_ - Settlement date of the security.
*   _maturity_ - Maturity date of the security.
*   _discount_ - Discount rate of the security.

Using the TBILLEQ function 
---------------------------

The Excel TBILLEQ function returns the bond-equivalent yield for a Treasury bill, based on a _settlement_ date, a _maturity_ date, and a _discount_ rate. In the example shown, the settlement date is 5-Feb-2019, the maturity date is 1-Feb-2020, and the discount rate is 2.54%. The formula in F5 is:

    =TBILLEQ(C5,C6,C7)
    

With these inputs, the TBILLEQ function returns a yield of 2.53%, with [percentage number format](https://exceljet.net/articles/custom-number-formats)
 applied.

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. To enter valid dates directly inside a function, the [DATE function](https://exceljet.net/functions/date-function)
 is the best option.

### About treasury bills

A treasury bill (also called a T-Bill) is a short-term debt obligation issued by the US Treasury Department. T-Bills are sold in increments of $100, and have terms that range from a few days up to 52 weeks. Backed by US government, T-Bills are considered a low risk investment.

T-Bills are typically sold at a discount from par amount (face value), and the discount rate is determined at auction. However, T-bills can also be sold at a premium, when the price is greater than the par amount.

T-Bills do not offer regular interest payments like a coupon bond. However, when a T-Bill matures, the owner is paid it's par amount, or face value.  When the par value is greater than the purchase price, the difference is the interest earned.

Related functions
-----------------

[![Excel TBILLPRICE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20tbillprice_function.png "Excel TBILLPRICE function")](https://exceljet.net/functions/tbillprice-function)

### [TBILLPRICE Function](https://exceljet.net/functions/tbillprice-function)

The Excel TBILLPRICE function returns the price per $100 face value for a Treasury bill.

[![Excel TBILLEQ function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20tbilleq_function.png "Excel TBILLEQ function")](https://exceljet.net/functions/tbilleq-function)

### [TBILLEQ Function](https://exceljet.net/functions/tbilleq-function)

The Excel TBILLEQ function returns the bond-equivalent yield for a Treasury bill.

[![Excel TBILLYIELD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20tbillyield_function.png "Excel TBILLYIELD function")](https://exceljet.net/functions/tbillyield-function)

### [TBILLYIELD Function](https://exceljet.net/functions/tbillyield-function)

The Excel TBILLYIELD function returns the yield for a Treasury bill.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [TBILLPRICE Function](https://exceljet.net/functions/tbillprice-function)
    
*   [TBILLEQ Function](https://exceljet.net/functions/tbilleq-function)
    
*   [TBILLYIELD Function](https://exceljet.net/functions/tbillyield-function)
    

### Links

*   [Microsoft TBILLEQ function documentation](https://support.office.com/en-us/article/tbilleq-function-2ab72d90-9b4d-4efe-9fc2-0f81f2c19c8c)
    
*   [Tbills at a glance (treasurydirect.gov)](https://www.treasurydirect.gov/indiv/products/prod_tbills_glance.htm)
    

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