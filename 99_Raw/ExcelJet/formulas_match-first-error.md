# Match first error - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/match-first-error

---

[Skip to main content](https://exceljet.net/formulas/match-first-error#main-content)

[](https://exceljet.net/formulas/match-first-error#)

*   [Previous](https://exceljet.net/formulas/match-first-does-not-begin-with)
    
*   [Next](https://exceljet.net/formulas/match-first-occurrence-does-not-contain)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Match first error
=================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[MATCH](https://exceljet.net/functions/match-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

![Excel formula: Match first error](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/match%20first%20error.png "Excel formula: Match first error")

Summary
-------

If you need to match the first error in a range of cells, you can use an array formula based on the MATCH and ISERROR functions. In the example shown, the formula is:

    {=MATCH(TRUE,ISERROR(B4:B11),0)}
    

This is an [array formula](https://exceljet.net/glossary/array-formula)
, and must be entered using Control + Shift + Enter (CSE).

Generic formula
---------------

    {=MATCH(TRUE,ISERROR(rng),0)}

Explanation 
------------

Working from the inside out, the ISERROR function returns TRUE when a value is a recognized error, and FALSE if not.

When given a range of cells (an array of cells) ISERROR function will return an array of TRUE/FALSE results. In the example, this resulting array looks like this:

{FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE}

Note that the 6th value (which corresponds to the 6th cell in the range) is TRUE, since cell B9 contains #N/A.

The MATCH function is configured to match TRUE in exact match mode. It finds the first TRUE in the array created by ISERROR and returns the position. If no match is found, the MATCH function itself returns #N/A.

### Finding the first NA error

The formula above will match any error. If you want to match the first #N/A error, just substitute ISNA for ISERROR:

    {=MATCH(TRUE,ISNA(B4:B11),0)}
    

Related formulas
----------------

[![Excel formula: Find missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_missing_values.png "Excel formula: Find missing values")](https://exceljet.net/formulas/find-missing-values)

### [Find missing values](https://exceljet.net/formulas/find-missing-values)

The goal is to identify invoice numbers in range D5:D11 that are missing in range B5:B16 (named list ). Two good ways to solve this problem in Excel are the COUNTIF function and the MATCH function . Both approaches are explained below. COUNTIF function COUNTIF counts cells in a range that meet a...

[![Excel formula: Count cells that contain errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20errors.png "Excel formula: Count cells that contain errors")](https://exceljet.net/formulas/count-cells-that-contain-errors)

### [Count cells that contain errors](https://exceljet.net/formulas/count-cells-that-contain-errors)

In this example, the goal is to count errors in the range B5:B15, which is named data for convenience. The article below explains several different approaches, depending on your needs. For background, this article: Excel Formula Errors . COUNTIF function One way to count individual errors is with...

Related functions
-----------------

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Find missing values](https://exceljet.net/formulas/find-missing-values)
    
*   [Count cells that contain errors](https://exceljet.net/formulas/count-cells-that-contain-errors)
    

### Functions

*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    

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