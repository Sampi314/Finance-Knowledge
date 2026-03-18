# Repeat fixed value every 3 months - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/repeat-fixed-value-every-3-months

---

[Skip to main content](https://exceljet.net/formulas/repeat-fixed-value-every-3-months#main-content)

[](https://exceljet.net/formulas/repeat-fixed-value-every-3-months#)

*   [Previous](https://exceljet.net/formulas/range-contains-specific-text)
    
*   [Next](https://exceljet.net/formulas/repeat-range-of-values)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Repeat fixed value every 3 months
=================================

by Dave Bruns · Updated 24 Oct 2023

Related functions 
------------------

[MOD](https://exceljet.net/functions/mod-function)

[DATEDIF](https://exceljet.net/functions/datedif-function)

![Excel formula: Repeat fixed value every 3 months](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/repeat%20value%20every%20n%20months.png "Excel formula: Repeat fixed value every 3 months")

Summary
-------

To repeat a fixed value every 3 months, you can use a formula based on the [DATEDIF](https://exceljet.net/functions/datedif-function)
 and [MOD](https://exceljet.net/functions/mod-function)
 functions. In the example shown, the formula in C4, copied down, is:

    =IF(B4>=start,(MOD(DATEDIF(start,B4,"m")+n,n)=0)*value,0)
    

where "start" is the [named range](https://exceljet.net/glossary/named-range)
 F6, "n" is F4, and "value" is F5.

Generic formula
---------------

    =IF(A1>=start,(MOD(DATEDIF(start,A1,"m")+n,n)=0)*value,0)

Explanation 
------------

The first thing this formula does is check the date in column B against the start date:

    =IF(B4>=start
    

If the date is not greater than the start date, the formula returns zero. If the date is greater than or equal to the start date, the IF function runs this snippet:

    (MOD(DATEDIF(start,B4,"m")+n,n)=0)*value
    

Inside MOD, the DATEDIF function is used to get the number of months between the start date and the date in B4. When the date in B4 equals the start date, DATEDIF returns zero. On the next month, DATEDIF returns 1, and so on.

To this result, we add the value for the named range "n", which is 3 in the example. This effectively starts the numbering pattern at 3 instead of zero.

The MOD function is used to check each value, with n as the divisor:

    MOD(DATEDIF(start,B4,"m")+n,n)=0
    

If the remainder is zero, we are working with a month that requires a value. Instead of nesting another IF function, we use [boolean logic](https://exceljet.net/glossary/boolean-logic)
 to multiply the result of the expression above by "value".

In months where there should be a value, MOD returns zero, the expression is TRUE, and value is returned. In other months, MOD returns a non-zero result, the expression is FALSE, and the value is forced to zero.

Related formulas
----------------

[![Excel formula: Fixed value every N columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/fixed%20value%20every%20N%20months.png "Excel formula: Fixed value every N columns")](https://exceljet.net/formulas/fixed-value-every-n-columns)

### [Fixed value every N columns](https://exceljet.net/formulas/fixed-value-every-n-columns)

The core of this formula is the MOD function. MOD takes a number and divisor, and returns the remainder after division, which makes it useful for formulas that need to do something every nth time. In this case, the number is created with the COLUMN function, which return the column number of cell...

[![Excel formula: Highlight every other row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20every%20other%20row.png "Excel formula: Highlight every other row")](https://exceljet.net/formulas/highlight-every-other-row)

### [Highlight every other row](https://exceljet.net/formulas/highlight-every-other-row)

When you use a formula to apply conditional formatting, the formula is evaluated for every cell in the selection. In this case, there are no addresses in the formula, so, for every cell in the data, the ROW and ISEVEN functions are run. ROW returns the row number of the cell, and ISEVEN returns...

[![Excel formula: Sum every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20nth%20column.png "Excel formula: Sum every nth column")](https://exceljet.net/formulas/sum-every-nth-column)

### [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)

In this example, the goal is to sum every nth value by column in a range of data, as seen in the worksheet above. For example, if n =2, we want to sum every second value by column, if n =3, we want to sum every third value by column, and so on. All data is in the range B5:J16 and n is entered into...

[![Excel formula: Copy value from every nth row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20row_0.png "Excel formula: Copy value from every nth row")](https://exceljet.net/formulas/copy-value-from-every-nth-row)

### [Copy value from every nth row](https://exceljet.net/formulas/copy-value-from-every-nth-row)

In this example, the goal is to copy every nth value from column B, where n is a variable that can be changed as needed. In Excel, it's difficult to create formulas that skip rows following a certain pattern, because the references in the formula will automatically change as the formula is copied...

Related functions
-----------------

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

[![Excel DATEDIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_datedif_function_0.png "Excel DATEDIF function")](https://exceljet.net/functions/datedif-function)

### [DATEDIF Function](https://exceljet.net/functions/datedif-function)

The Excel DATEDIF function returns the difference between two date values in years, months, or days. DATEDIF supports six unit codes that let you calculate complete years, complete months, total days, and partial intervals. DATEDIF is a "compatibility" function inherited from Lotus 1-2-3....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Fixed value every N columns](https://exceljet.net/formulas/fixed-value-every-n-columns)
    
*   [Highlight every other row](https://exceljet.net/formulas/highlight-every-other-row)
    
*   [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)
    
*   [Copy value from every nth row](https://exceljet.net/formulas/copy-value-from-every-nth-row)
    

### Functions

*   [MOD Function](https://exceljet.net/functions/mod-function)
    
*   [DATEDIF Function](https://exceljet.net/functions/datedif-function)
    

### Articles

*   [How to use the MOD function to repeat values](https://exceljet.net/articles/how-to-use-the-mod-function-to-repeat-values)
    

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