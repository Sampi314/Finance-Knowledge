# Conditional median with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/conditional-median-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/conditional-median-with-criteria#main-content)

[](https://exceljet.net/formulas/conditional-median-with-criteria#)

*   [Previous](https://exceljet.net/formulas/coefficient-of-variation)
    
*   [Next](https://exceljet.net/formulas/conditional-mode-with-criteria)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Conditional median with criteria
================================

by Dave Bruns · Updated 25 Mar 2019

Related functions 
------------------

[MEDIAN](https://exceljet.net/functions/median-function)

![Excel formula: Conditional median with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/conditional%20median%20with%20criteria.png "Excel formula: Conditional median with criteria")

Summary
-------

To calculate a conditional median based on one or more criteria you can use an array formula that uses the MEDIAN and IF functions together. In the example shown, the formula in F5 is:

    =MEDIAN(IF(group=E5,data))
    

where "group" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B14, and "data" is the named range C5:C14.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter._

Generic formula
---------------

    {=MEDIAN(IF(criteria,range))}

Explanation 
------------

The MEDIAN function has no built-in way to apply criteria. Given a range, it will return the MEDIAN (middle) number in that range.

To apply criteria, we use the IF function inside MEDIAN to "filter" values. In this example, the IF function filters by group like this:

    IF(group=E5,data)
    

This expression compares each value in the named range "group" against the value in E5 ("A"). Because the criteria is applied to an array with multiple values, the result is an array of TRUE FALSE values like this:

    {TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

In this array each TRUE corresponds to a value in group A. The IF function evaluates these results and returns the corresponding value from the named range "data". The final result from IF is

    {1;2;3;3;5;FALSE;FALSE;FALSE;FALSE;FALSE}
    

Notice only values in group A have survived, and group B values are now FALSE. This array is returned to the MEDIAN function, which automatically ignores FALSE values and returns median value, 3.

_Note: when IF is used this way to filter values with an array operation, the formula must be entered with control + shift + enter._

### Additional criteria

To apply more than one criteria, you can nest another IF inside the first IF:

    {=MEDIAN(IF(criteria1,IF(criteria2,data)))}
    

To avoid extra nesting, you can also use [boolean logic in the criteria](https://exceljet.net/formulas/if-with-boolean-logic)
.

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

[![Excel MEDIAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20median%20function.png "Excel MEDIAN function")](https://exceljet.net/functions/median-function)

### [MEDIAN Function](https://exceljet.net/functions/median-function)

The Excel MEDIAN function returns the median (middle number) in the supplied set of data. For example, =MEDIAN(1,2,3,4,5) returns 3.

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

*   [MEDIAN Function](https://exceljet.net/functions/median-function)
    

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