# Excel TBILLPRICE function | Exceljet

**Source:** https://exceljet.net/functions/tbillprice-function

---

[Skip to main content](https://exceljet.net/functions/tbillprice-function#main-content)

[](https://exceljet.net/functions/tbillprice-function#)

*   [Previous](https://exceljet.net/functions/tbilleq-function)
    
*   [Next](https://exceljet.net/functions/tbillyield-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

TBILLPRICE Function
===================

by Dave Bruns · Updated 6 Feb 2019

Related functions 
------------------

[TBILLPRICE](https://exceljet.net/functions/tbillprice-function)

[TBILLEQ](https://exceljet.net/functions/tbilleq-function)

[TBILLYIELD](https://exceljet.net/functions/tbillyield-function)

![Excel TBILLPRICE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_%20tbillprice_function.png "Excel TBILLPRICE function")

Summary
-------

The Excel TBILLPRICE function returns the price per $100 face value for a Treasury bill.

Purpose 
--------

Get price per $100 Treasury bill

Return value 
-------------

Price per $100

Syntax
------

    =TBILLPRICE(settlement,maturity,discount)

*   _settlement_ - Settlement date of the security.
*   _maturity_ - Maturity date of the security.
*   _discount_ - The discount rate for the security.

Using the TBILLPRICE function 
------------------------------

The TBILLPRICE function returns the price per $100 face value for a Treasury bill, based on a settlement date, a maturity date, and a discount. In the example shown, the settlement date is 5-Feb-2019, the maturity date is 1-Feb-2020, and the discount is 2.45%. The formula in F5 is:

    =TBILLPRICE(C6,C7,C8)
    

With these inputs, the TBILLPRICE function returns a price per $100 of $97.54, with currency [number format](https://exceljet.net/articles/custom-number-formats)
 applied.

To convert the face value of $1000 in cell C5 to a price using the value returned by TBILLPRICE, F6 contains this formula:

    =F5/100*C5
    

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. To enter valid dates directly inside a function, the [DATE function](https://exceljet.net/functions/date-function)
 is the best option.

### About treasury bills

A treasury bill (also called a T-Bill) is a short-term debt obligation issued by the US Treasury Department. T-Bills are sold in increments of $100, and have terms that range from a few days up to 52 weeks. Backed by US government, T-Bills are considered a low risk investment.

T-Bills are typically sold at a discount from par amount (face value), and the discount rate is determined at auction. However, T-bills can also be sold at a premium, when the price is greater than the par amount.

T-Bills do not offer regular interest payments like a coupon bond. However, when a T-Bill matures, the owner is paid it's par amount, or face value.  When the par amount is greater than the purchase price, the difference (par value less purchase price) is the interest earned.

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

*   [Microsoft TBILLPRICE function documentation](https://support.office.com/en-us/article/tbillprice-function-eacca992-c29d-425a-9eb8-0513fe6035a2)
    
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