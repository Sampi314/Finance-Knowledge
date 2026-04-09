# Expense begins on specific month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/expense-begins-on-specific-month

---

[Skip to main content](https://exceljet.net/formulas/expense-begins-on-specific-month#main-content)

[](https://exceljet.net/formulas/expense-begins-on-specific-month#)

*   [Previous](https://exceljet.net/formulas/easy-bundle-pricing-with-sumproduct)
    
*   [Next](https://exceljet.net/formulas/extract-unique-items-from-a-list)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Expense begins on specific month
================================

by Dave Bruns · Updated 29 Oct 2019

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Expense begins on specific month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/expense%20begins%20on%20specific%20month.png "Excel formula: Expense begins on specific month")

Summary
-------

To start an expense on a specific month, you can use a formula based on the IF function. In the example shown, the formula in cell E5 (copied down and across) is:

    =IF($D5<=E$4,$C5,0)
    

where the values in column D (start) and the range E4:J4 are valid [Excel dates](https://exceljet.net/glossary/excel-date)
.

Generic formula
---------------

    =IF(start<=month,expense,0)

Explanation 
------------

The first thing this formula does is check the date in column D against the date in the header (E4:J4).

    =IF($D5<=E$4
    

_Translated: if the date in column D is less than or equal to the date in row E._

Note these are [mixed references](https://exceljet.net/glossary/mixed-reference)
. The column in $D5 is locked, and the row in E$4 is locked. This allows the formula to be copied across the table.

If the result of this test is TRUE, the IF function returns the expense from column C, otherwise IF returns zero (0).

    =IF($D5<=E$4,$C5,0)
    

Again note the reference to $C5 is has the column locked, so the expense is always picked up from column C.

As the formula is copied across the table, expenses begin on the correct month. In months where the expense is not yet valid, the result is zero.

### With boolean logic

Using [boolean logic](https://exceljet.net/glossary/boolean-logic)
, the formula could be re-written like as below, for a simpler formula:

    =$C5*($D5<=E$4)
    

Here the logical expression is used to "cancel out" expenses in months where they have not yet started.

Related formulas
----------------

[![Excel formula: Fixed value every N columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/fixed%20value%20every%20N%20months.png "Excel formula: Fixed value every N columns")](https://exceljet.net/formulas/fixed-value-every-n-columns)

### [Fixed value every N columns](https://exceljet.net/formulas/fixed-value-every-n-columns)

The core of this formula is the MOD function. MOD takes a number and divisor, and returns the remainder after division, which makes it useful for formulas that need to do something every nth time. In this case, the number is created with the COLUMN function, which return the column number of cell...

[![Excel formula: Sum every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20nth%20column.png "Excel formula: Sum every nth column")](https://exceljet.net/formulas/sum-every-nth-column)

### [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)

In this example, the goal is to sum every nth value by column in a range of data, as seen in the worksheet above. For example, if n =2, we want to sum every second value by column, if n =3, we want to sum every third value by column, and so on. All data is in the range B5:J16 and n is entered into...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

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
    
*   [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    

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