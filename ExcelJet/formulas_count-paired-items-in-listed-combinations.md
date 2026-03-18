# Count paired items in listed combinations - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-paired-items-in-listed-combinations

---

[Skip to main content](https://exceljet.net/formulas/count-paired-items-in-listed-combinations#main-content)

[](https://exceljet.net/formulas/count-paired-items-in-listed-combinations#)

*   [Previous](https://exceljet.net/formulas/count-or-sum-whole-numbers-only)
    
*   [Next](https://exceljet.net/formulas/count-rows-that-contain-specific-values)
    

[Count](https://exceljet.net/formulas#Count)

Count paired items in listed combinations
=========================================

by Dave Bruns · Updated 21 Aug 2022

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[CONCAT](https://exceljet.net/functions/concat-function)

![Excel formula: Count paired items in listed combinations](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20paired%20items%20in%20listed%20combinations.png "Excel formula: Count paired items in listed combinations")

Summary
-------

To build a summary table with a count of paired items that appear in a list of existing combinations, you can use a helper column and a formula based on the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
. In the example shown the formula in cell H5 is:

    =IF($G5=H$4,"-",COUNTIFS(helper,"*"&$G5&"*",helper,"*"&H$4&"*"))
    

where **helper** is the [named range](https://exceljet.net/glossary/named-range)
 E5:E16.

_Note: this formula assumes items don't repeat in a given combination (i.e. AAB, EFE are not valid combinations)._

Generic formula
---------------

    =COUNTIFS(range,"*"&$item1&"*",range,"*"&item2&"*")

Explanation 
------------

We want to count how often items in columns B, C, and D appear together. For example, how often A appears with C, B appears with F, G appears with D, and so on. This would seem like a perfect use of COUNTIFS, but if we try to add criteria looking for 2 items across 3 columns, it isn't going to work.

A simple workaround is to join all items together in a single cell in a [helper column](https://exceljet.net/glossary/helper-column)
, then use COUNTIFS with a [wildcard](https://exceljet.net/glossary/wildcard)
 to count items. We do that with a [helper column](https://exceljet.net/glossary/helper-column)
 (E) that joins items in columns B, C, and D using the [CONCAT function](https://exceljet.net/functions/concat-function)
. The formula in E5, copied down, is:

    =CONCAT(B5:D5)
    

As an alternative, you can also [manually concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the values like this:

    =B5&C5&D5
    

Because repeated items are not allowed in a combination, the first part of the formula excludes matching items. If the two items are the same, the formula returns a hyphen or dash as text:

    =IF($G5=H$4,"-"
    

If items are different, a COUNTIFS function is run:

    COUNTIFS(helper,"*"&$G5&"*",helper,"*"&H$4&"*")
    

Here, the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 is configured to count "pairs" of items. Only when corresponding values from column G and row 4 appear together in the helper column is the pair counted. Because a letter may appear anywhere, the asterisk (\*) [wildcard](https://exceljet.net/glossary/wildcard)
 is [concatenated](https://exceljet.net/glossary/concatenation)
 to both sides of the value to ensure a match will be counted no matter where it appears in the cell. Note the references to G5 and H4 are [mixed references](https://exceljet.net/glossary/mixed-reference)
 in order to lock the column and row as needed when the formula is copied across the table.

Related formulas
----------------

[![Excel formula: Count if row meets internal criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20if%20row%20meets%20internal%20criteria.png "Excel formula: Count if row meets internal criteria")](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)

### [Count if row meets internal criteria](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)

In this example the goal is to count products (rows) where sales have increased and sales have decreased, where previous sales are in column C (Previous) and current sales are in column D (Current). In this case, we can't use COUNTIFS directly, because COUNTIFS is a range-based function and it won'...

[![Excel formula: Count if row meets multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20if%20row%20meets%20multiple%20criteria.png "Excel formula: Count if row meets multiple criteria")](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)

### [Count if row meets multiple criteria](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)

In this example, the goal is to count orders (rows) where the state is Texas ("TX"), the amount is greater than $100, and the month is March. In this case, we can't use COUNTIFS , because COUNTIFS is a range-based function and it won't accept a calculation for a range argument, which we need to...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel CONCAT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20concat%20function.png "Excel CONCAT function")](https://exceljet.net/functions/concat-function)

### [CONCAT Function](https://exceljet.net/functions/concat-function)

The Excel CONCAT function concatenates (joins) values supplied as references or constants. Unlike the [CONCATENATE function](https://exceljet.net/functions/concatenate-function)
 (which CONCAT replaces), CONCAT will accept a [range](https://exceljet.net/glossary/range)
 of cells to join, in addition to individual...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count if row meets internal criteria](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)
    
*   [Count if row meets multiple criteria](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [CONCAT Function](https://exceljet.net/functions/concat-function)
    

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