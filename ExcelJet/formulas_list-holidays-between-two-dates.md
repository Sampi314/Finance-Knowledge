# List holidays between two dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/list-holidays-between-two-dates

---

[Skip to main content](https://exceljet.net/formulas/list-holidays-between-two-dates#main-content)

[](https://exceljet.net/formulas/list-holidays-between-two-dates#)

*   [Previous](https://exceljet.net/formulas/last-updated-date-stamp)
    
*   [Next](https://exceljet.net/formulas/month-number-from-name)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

List holidays between two dates
===============================

by Dave Bruns · Updated 26 Nov 2019

Related functions 
------------------

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: List holidays between two dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/list%20holidays%20between%20two%20dates.png "Excel formula: List holidays between two dates")

Summary
-------

To list holidays that occur between two dates, you can use a formula based on the [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
 and IF functions.

In the example shown, the formula in F8 is:

    {=TEXTJOIN(", ",TRUE,IF(B4:B12>=F5,IF(B4:B12<=F6,C4:C12,""),""))}
    

_This is an array formula and must be entered with control + shift + enter._

Generic formula
---------------

    {=TEXTJOIN(", ",TRUE,IF(dates>=start,IF(dates<=end,holidays,""),""))}

Explanation 
------------

At a high level, this formula uses a nested IF function to return an array of holidays between two dates. This array is then processed by the TEXTJOIN function, which converts the array to text using a comma as the delimiter.

Working from the inside out, we generate the array of matching holidays using a nested IF:

    IF(B4:B12>=F5,IF(B4:B12<=F6,C4:C12,""),"")
    

If the dates in B4:B12 are greater than or equal the start date in F5, and if the dates in B4:B12 are less than or equal the end date in F6, then IF returns a an array of holidays. In the example shown, the list looks like this:

{"";"";"Presidents Day";"Memorial Day";"";"";"";"";""}

This array is then delivered to the TEXTJOIN function as the **text1** argument, where the **delimiter** is set to ", " and **ignore\_empty** is TRUE. The TEXT JOIN function processes the items in the array and returns a string where every non-empty item is separated by a comma plus space.

_Note: the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
 is a new function available in Office 365 and Excel 2019._

Related formulas
----------------

[![Excel formula: Count holidays between two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20holidays%20between%20two%20dates.png "Excel formula: Count holidays between two dates")](https://exceljet.net/formulas/count-holidays-between-two-dates)

### [Count holidays between two dates](https://exceljet.net/formulas/count-holidays-between-two-dates)

This formula uses two expressions in a single array inside the SUMPRODUCT function. The first expression tests every holiday date to see if it's greater than or equal to the start date in F5: (B4:B12>=F5) This returns an array of TRUE/FALSE values like this: {FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;...

Related functions
-----------------

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

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

*   [Count holidays between two dates](https://exceljet.net/formulas/count-holidays-between-two-dates)
    

### Functions

*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

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