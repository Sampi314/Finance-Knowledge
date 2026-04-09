# Conditional mode with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/conditional-mode-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/conditional-mode-with-criteria#main-content)

[](https://exceljet.net/formulas/conditional-mode-with-criteria#)

*   [Previous](https://exceljet.net/formulas/conditional-median-with-criteria)
    
*   [Next](https://exceljet.net/formulas/convert-column-letter-to-number)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Conditional mode with criteria
==============================

by Dave Bruns · Updated 25 Mar 2019

Related functions 
------------------

[MODE](https://exceljet.net/functions/mode-function)

![Excel formula: Conditional mode with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/conditional%20mode%20with%20criteria.png "Excel formula: Conditional mode with criteria")

Summary
-------

To calculate a conditional mode with one or more criteria you can use an array formula based on the IF and MODE functions. In the example shown, the formula in F5 is:

    {=MODE(IF(group=E5,data))}
    

where "group" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B14, and "data" is the named range C5:C14.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter._

Generic formula
---------------

    {=MODE(IF(criteria,data))}

Explanation 
------------

The MODE function has no built-in way to apply criteria. Given a range, it will return the most frequently occurring number in that range.

To apply criteria, we use the IF function inside MODE to filter values in a range. In this example, the IF function filters values by group with an expression like this:

    IF(group=E5,data)
    

This compares each value in the named range "group" against the value in E5, which is "A". Because the logical test is applied to an array with multiple values, the result is an array of TRUE FALSE values:

    {TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE}
    

where each TRUE corresponds to a row where the group is "A". This array becomes a filter. For each TRUE, IF returns the corresponding value in the named range "data". FALSE values remain unchanged. The final result of IF is this array:

    {3;FALSE;3;FALSE;5;FALSE;1;FALSE;2;FALSE}
    

Notice only values in group A have survived, group B values are now FALSE. This array is returned to the MODE function, which automatically ignores FALSE values and returns the most frequently occurring number, which is 3.

_Note: when IF is used this way to filter values with an array operation, the formula must be entered with control + shift + enter._

### Additional criteria

To apply more than one criteria, you can nest another IF inside the first IF:

    {=MODE(IF(criteria1,IF(criteria2,data)))}
    

Related formulas
----------------

[![Excel formula: Most frequently occurring number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/most%20frequently%20occurring%20number.png "Excel formula: Most frequently occurring number")](https://exceljet.net/formulas/most-frequently-occurring-number)

### [Most frequently occurring number](https://exceljet.net/formulas/most-frequently-occurring-number)

The MODE function is fully automatic and will return the most frequently occurring number in a set of numbers. For example: =MODE(1,2,4,4,5,5,5,6) // returns 5 In the example shown, we give MODE the range B4:K4, so the formula is solved like this: =MODE(B4:K4) =MODE({1,2,2,1,1,2,2,2,1,1}) =2

[![Excel formula: List most frequently occurring numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20most%20frequently%20occuring%20numbers.png "Excel formula: List most frequently occurring numbers")](https://exceljet.net/formulas/list-most-frequently-occurring-numbers)

### [List most frequently occurring numbers](https://exceljet.net/formulas/list-most-frequently-occurring-numbers)

The core of this formula is the MODE function, which returns the most frequently occurring number in a range or array. The rest of the formula just constructs a filtered array for MODE to use in each row. The expanding range $D$4:D4 works to exclude numbers already output in $D$4:D4. Working from...

[![Excel formula: Most frequently occurring text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/most%20frequent%20text2.png "Excel formula: Most frequently occurring text")](https://exceljet.net/formulas/most-frequently-occurring-text)

### [Most frequently occurring text](https://exceljet.net/formulas/most-frequently-occurring-text)

Working from the inside out, the MATCH function matches the range against itself. That is, we give the MATCH function the same range for lookup value and lookup array (B5:F5). Because the lookup value contains more than one value (an array), MATCH returns an array of results, where each number...

Related functions
-----------------

[![Excel MODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mode%20function.png "Excel MODE function")](https://exceljet.net/functions/mode-function)

### [MODE Function](https://exceljet.net/functions/mode-function)

The Excel MODE function returns the most frequently occurring number in a numeric data set. For example, =MODE(1,2,4,4,5,5,5,6) returns 5.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Most frequently occurring number](https://exceljet.net/formulas/most-frequently-occurring-number)
    
*   [List most frequently occurring numbers](https://exceljet.net/formulas/list-most-frequently-occurring-numbers)
    
*   [Most frequently occurring text](https://exceljet.net/formulas/most-frequently-occurring-text)
    

### Functions

*   [MODE Function](https://exceljet.net/functions/mode-function)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    
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