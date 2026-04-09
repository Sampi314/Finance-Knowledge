# Fixed value every N columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/fixed-value-every-n-columns

---

[Skip to main content](https://exceljet.net/formulas/fixed-value-every-n-columns#main-content)

[](https://exceljet.net/formulas/fixed-value-every-n-columns#)

*   [Previous](https://exceljet.net/formulas/filter-values-in-array-formula)
    
*   [Next](https://exceljet.net/formulas/flag-first-duplicate-in-a-list)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Fixed value every N columns
===========================

by Dave Bruns · Updated 12 Jun 2020

Related functions 
------------------

[MOD](https://exceljet.net/functions/mod-function)

[COLUMN](https://exceljet.net/functions/column-function)

![Excel formula: Fixed value every N columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/fixed%20value%20every%20N%20months.png "Excel formula: Fixed value every N columns")

Summary
-------

To generate a fixed value every N columns (for example, a fixed expense every 3 months, a fixed payment every 6 months, etc.) you can use a formula based on the MOD function.

In the example shown, generate a value of 60 every 3 months. The formula in B8 is:

    =IF(MOD(COLUMN(B8)-1,3)=0,$B$5,0)
    

Which returns 60 every 3rd month and zero for other months.

Generic formula
---------------

    =IF(MOD(COLUMN(A1)-offset,N)=0,amount,0)

Explanation 
------------

The core of this formula is the MOD function. MOD takes a number and divisor, and returns the remainder after division, which makes it useful for formulas that need to do something every nth time.

In this case, the number is created with the COLUMN function, which return the column number of cell B8, the number 2, minus 1, which is supplied as an "offset". We use an offset, because we want to make sure we start counting at 1, regardless of the actual column number.

The divisor is hardcoded as 3, since we want to do something every 3rd month. By testing for a zero remainder, this expression will return TRUE at the 3rd, 6th, 9th, and 12th months:

    MOD(COLUMN(B8)-1,3)=0
    

Finally, IF simply evaluates the MOD expression and returns value in B5 (coded as an absolute reference to prevent changes as the formula is copied) when TRUE and zero when FALSE.

### Working with a date

If you need to repeat a value every n months, and you are working directly with dates, [see this example](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)
.

Related formulas
----------------

[![Excel formula: Repeat fixed value every 3 months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/repeat%20value%20every%20n%20months.png "Excel formula: Repeat fixed value every 3 months")](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)

### [Repeat fixed value every 3 months](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)

The first thing this formula does is check the date in column B against the start date: =IF(B4>=start If the date is not greater than the start date, the formula returns zero. If the date is greater than or equal to the start date, the IF function runs this snippet: (MOD(DATEDIF(start,B4,"m")+n,...

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

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Repeat fixed value every 3 months](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)
    
*   [Highlight every other row](https://exceljet.net/formulas/highlight-every-other-row)
    
*   [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)
    
*   [Copy value from every nth row](https://exceljet.net/formulas/copy-value-from-every-nth-row)
    

### Functions

*   [MOD Function](https://exceljet.net/functions/mod-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    

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