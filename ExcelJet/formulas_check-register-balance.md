# Check register balance - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/check-register-balance

---

[Skip to main content](https://exceljet.net/formulas/check-register-balance#main-content)

[](https://exceljet.net/formulas/check-register-balance#)

*   [Previous](https://exceljet.net/formulas/change-negative-numbers-to-positive)
    
*   [Next](https://exceljet.net/formulas/coefficient-of-variation)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Check register balance
======================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[AND](https://exceljet.net/functions/and-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

![Excel formula: Check register balance](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/check%20register%20balance.png "Excel formula: Check register balance")

Summary
-------

To set a check register formula that calculates a running balance, you can use a formula based on simple addition and subtraction. In the example shown, the formula in G6 is:

    =G5-E6+F6
    

Generic formula
---------------

    =balance-debit+credit

Explanation 
------------

The value in G5 is hard-coded. The formula picks up the value in G5, then subtracts the value (if any) in E6 and adds the value (if any) in F6. When the credit or debit values are empty, they behave like zero and have no effect on the result.

When this formula is copied down column G, it will continue to calculate a running balance in each row.

### Dealing with blank values

To display nothing in the balance column when the credit and debit columns are empty, you can use the IF function with AND and ISBLANK like this:

    =IF(AND(ISBLANK(E6),ISBLANK(F6)),"",G5-E6+F6)
    

This formula will return an [empty string](https://exceljet.net/glossary/empty-string)
 ("") when both credit and debit cells are empty, and returns the running balance if either number exists.

_Note: this only handles bank credit and debit values at the end of the table, not rows in between._

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")](https://exceljet.net/functions/isblank-function)

### [ISBLANK Function](https://exceljet.net/functions/isblank-function)

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    

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