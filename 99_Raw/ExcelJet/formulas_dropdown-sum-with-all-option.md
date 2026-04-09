# Dropdown sum with all option - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/dropdown-sum-with-all-option

---

[Skip to main content](https://exceljet.net/formulas/dropdown-sum-with-all-option#main-content)

[](https://exceljet.net/formulas/dropdown-sum-with-all-option#)

*   [Previous](https://exceljet.net/formulas/display-sorted-values-with-helper-column)
    
*   [Next](https://exceljet.net/formulas/easy-bundle-pricing-with-sumproduct)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Dropdown sum with all option
============================

by Dave Bruns · Updated 17 Jul 2019

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUM](https://exceljet.net/functions/sum-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Dropdown sum with all option](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/dropdown%20sum%20with%20all%20option.png "Excel formula: Dropdown sum with all option")

Summary
-------

To enable a dropdown with an "all" option you can use [data validation for the dropdown list](https://exceljet.net/articles/excel-data-validation-guide)
, and a formula based on IF, SUM, and SUMIF functions to calculate a conditional sum. In the example shown the formula in G5 is:

    =IF(F5="all",SUM(qty),SUMIF(color,F5,qty))
    

where "color" (C5:C15) and "qty" (D5:D15) are [named ranges](https://exceljet.net/glossary/named-range)
.

### Example

When F5 is selected, the following dropdown appears:

![Dropdown sum with all option in action](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/dropdown%20sum%20with%20all%20option%20in%20action.png?itok=gb4GFIPI "Dropdown sum with all option in action")

When the user makes a selection, the correct sum is returned.

Generic formula
---------------

    =IF(F5="all",SUM(D:D),SUMIF(C:C,A1,D:D))

Explanation 
------------

The dropdown is set up with a simple [data validation](https://exceljet.net/articles/excel-data-validation-guide)
 rule based on a "list":

    Red,Blue,Green,All
    

The [named ranges](https://exceljet.net/glossary/named-range)
 "color" (C5:C15) and "qty" (D5:D15) are for convenience only.

The formula in G5 performs a conditional sum based on the current dropdown selection in F5. The outermost function is an IF statement, which checks if the selection is "all":

    =IF(F5="all",SUM(qty)
    

If so, the formula returns the sum of quantity column as a final result.

If F5 is any value except "all" (i.e. "red", "blue", or "green"), the logical test returns FALSE and IF routes the formula to the SUMIF function:

    SUMIF(color,F5,qty)
    

SUMIF calculates a conditional sum based on the value in F5 and returns the result.

Related formulas
----------------

[![Excel formula: Sum if cells are equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_equal_to.png "Excel formula: Sum if cells are equal to")](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

### [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when cells in the range C5:C15 contain "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only a single condition. SUMIFS on the other...

Related functions
-----------------

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

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

*   [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)
    

### Functions

*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
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