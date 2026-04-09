# Compare two strings - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/compare-two-strings

---

[Skip to main content](https://exceljet.net/formulas/compare-two-strings#main-content)

[](https://exceljet.net/formulas/compare-two-strings#)

*   [Previous](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)
    
*   [Next](https://exceljet.net/formulas/conditional-message-with-rept-function)
    

[Text](https://exceljet.net/formulas#Text)

Compare two strings
===================

by Dave Bruns · Updated 30 Sep 2020

Related functions 
------------------

[EXACT](https://exceljet.net/functions/exact-function)

![Excel formula: Compare two strings](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/compare%20two%20strings.png "Excel formula: Compare two strings")

Summary
-------

To compare two text strings in Excel to determine if they're equal, you can use the [EXACT function](https://exceljet.net/functions/exact-function)
. In the example shown, the formula in D5 is:

    =EXACT(B5,C5)
    

Generic formula
---------------

    =EXACT(text1, text2)

Explanation 
------------

By default, Excel is _not_ case-sensitive.  For example, with "APPLE" in  A1, and "apple" in A2, the following formula will return TRUE:

    =A1=A2 // returns TRUE
    

To compare text strings in a case-sensitive way, you can use the [EXACT function](https://exceljet.net/functions/exact-function)
. The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not.

If we use EXACT to compare A1 and A2 as above, the result is FALSE:

    =EXACT(A1,A2) // returns FALSE
    

### EXACT with IF

You can use this result inside the [IF function](https://exceljet.net/videos/the-if-function)
 to display a message or make a conditional calculation. For example, to display the message "Yes" for a match and "No" if not, you can use a formula like this:

    =IF(EXACT(A2,A2),"Yes","No")
    

Related formulas
----------------

[![Excel formula: Case sensitive lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case%20sensitive%20lookup.png "Excel formula: Case sensitive lookup")](https://exceljet.net/formulas/case-sensitive-lookup)

### [Case sensitive lookup](https://exceljet.net/formulas/case-sensitive-lookup)

In this example, the goal is to perform a case-sensitive lookup on the name in column B, based on a lookup value entered in cell E5. By default, Excel is not case-sensitive. This means that standard lookup functions like VLOOKUP , XLOOKUP , and INDEX and MATCH are also not case-sensitive. These...

[![Excel formula: Count cells equal to case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20case%20sensitive.png "Excel formula: Count cells equal to case sensitive")](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)

### [Count cells equal to case sensitive](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)

In this example, the goal is to count codes in a case-sensitive way. The COUNTIF function and the COUNTIFS function are both good options for counting text values, but neither is case-sensitive, so they can't be used to solve this problem. The solution is to use the EXACT function to compare codes...

[![Excel formula: SUMPRODUCT case-sensitive lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMPRODUCT_case_sensitive_lookup.png "Excel formula: SUMPRODUCT case-sensitive lookup")](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)

### [SUMPRODUCT case-sensitive lookup](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)

The SUMPRODUCT function multiplies arrays together and returns the sum of products. If only one array is supplied, SUMPRODUCT will simply sum the items in the array. For example, if we give SUMPRODUCT one array in the form of the data\[Qty\] column: =SUMPRODUCT(data\[Qty\]) // returns 54 SUMPRODUCT...

Related functions
-----------------

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Case sensitive lookup](https://exceljet.net/formulas/case-sensitive-lookup)
    
*   [Count cells equal to case sensitive](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)
    
*   [SUMPRODUCT case-sensitive lookup](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)
    

### Functions

*   [EXACT Function](https://exceljet.net/functions/exact-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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