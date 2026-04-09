# Show formula text with formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/show-formula-text-with-formula

---

[Skip to main content](https://exceljet.net/formulas/show-formula-text-with-formula#main-content)

[](https://exceljet.net/formulas/show-formula-text-with-formula#)

*   [Previous](https://exceljet.net/formulas/send-email-with-formula)
    
*   [Next](https://exceljet.net/formulas/simple-currency-conversion)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Show formula text with formula
==============================

by Dave Bruns · Updated 4 Aug 2022

Related functions 
------------------

[FORMULATEXT](https://exceljet.net/functions/formulatext-function)

[IFERROR](https://exceljet.net/functions/iferror-function)

[ISFORMULA](https://exceljet.net/functions/isformula-function)

![Excel formula: Show formula text with formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/show%20formula%20text%20with%20formula.png "Excel formula: Show formula text with formula")

Summary
-------

To show the text of one formula with another formula, you can use the [FORMULATEXT](https://exceljet.net/functions/formulatext-function)
 function. In the example shown, the formula in D5, copied down, is:

    =FORMULATEXT(C5)
    

Generic formula
---------------

    =FORMULATEXT(A1)

Explanation 
------------

The FORMULATEXT is fully automatic. When given the reference of a cell that contains a formula, it will return the entire formula as text. In the example as shown, the formula:

    =FORMULATEXT(C5)
    

returns the text "=IF(B5>=70,"Pass","Fail")".

### Dealing with errors

The FORMULATEXT function will return the #N/A error when a cell does not contain a formula. To trap this error and display nothing when a cell does not contain a formula, you can use the IFERROR function like this:

    =IFERROR(FORMULATEXT(A1),"")
    

Alternately, you can use ISFORMULA and IF like this:

    =IF(ISFORMULA(A1),FORMULATEXT(A1),"")
    

### Checking for specific text

To check a formula for a specific text, you can use the ISNUMBER and SEARCH functions. In the formula below, we are checking a formula in A1 to see if it contains "apple":

    =ISNUMBER(SEARCH("apple",FORMULATEXT(A1)))
    

The result is either TRUE or FALSE. See [this page](https://exceljet.net/formulas/cell-contains-specific-text)
 for a full explanation.

Related functions
-----------------

[![Excel FORMULATEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20formulatext%20function.png "Excel FORMULATEXT function")](https://exceljet.net/functions/formulatext-function)

### [FORMULATEXT Function](https://exceljet.net/functions/formulatext-function)

The Excel FORMULATEXT function returns a formula as a text string from a given reference. You can use FORMULATEXT to extract the formula as text from a cell. If you use FORMULATEXT on a cell that doesn't contain a formula, it returns #N/A.

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

[![Excel ISFORMULA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isformula%20function.png "Excel ISFORMULA function")](https://exceljet.net/functions/isformula-function)

### [ISFORMULA Function](https://exceljet.net/functions/isformula-function)

The Excel ISFORMULA function returns TRUE if a cell contains a formula, and FALSE if not. When a cell contains a formula ISFORMULA will return TRUE regardless of the formula's output or error conditions.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [FORMULATEXT Function](https://exceljet.net/functions/formulatext-function)
    
*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    
*   [ISFORMULA Function](https://exceljet.net/functions/isformula-function)
    

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