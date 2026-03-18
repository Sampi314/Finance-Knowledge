# Position of max value in list - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/position-of-max-value-in-list

---

[Skip to main content](https://exceljet.net/formulas/position-of-max-value-in-list#main-content)

[](https://exceljet.net/formulas/position-of-max-value-in-list#)

*   [Previous](https://exceljet.net/formulas/position-of-first-partial-match)
    
*   [Next](https://exceljet.net/formulas/quantity-based-discount)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Position of max value in list
=============================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[MAX](https://exceljet.net/functions/max-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Position of max value in list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/position%20of%20max%20value%20in%20list.png "Excel formula: Position of max value in list")

Summary
-------

To get the position of the maximum value in a range (i.e. a list, table, or row), you can use the [MAX function](https://exceljet.net/functions/max-function)
 together with the [MATCH function](https://exceljet.net/functions/match-function)
. In the example shown, the formula in I5 is:

    =MATCH(MAX(C3:C11),C3:C11,0)
    

Which returns the number 4, representing the position of the most expensive property in the list.

Generic formula
---------------

    =MATCH(MAX(range),range,0)

Explanation 
------------

In this formula, the goal is to return the numeric position of the most expensive property in the list. The formula in cell I5 is:

    =MATCH(MAX(C3:C11),C3:C11,0)
    

The MAX function extracts the maximum value from the range C3:C11. In this case, that value is 849900. This number is then supplied to the MATCH function as the lookup value. The _lookup\_array_ is the same range (C3:C11), and the _match\_type_ is set to "exact" with 0. With those arguments, MATCH finds the maximum value inside the range and returns the relative position of the value in that range.

To retrieve information about the most expensive property in the list, we need to add the [INDEX function](https://exceljet.net/functions/index-function)
 to the mix. See this example for details: [Information about the max value](https://exceljet.net/formulas/get-information-about-max-value)
.

_Notes: (1) In this case, the position corresponds to a relative row number, but in a horizontal range, the position would correspond to a relative column number. (2) In case of duplicates (i.e. two or more max values that are the same) this formula will return the position of the first match, the default behavior of the MATCH function._

Related formulas
----------------

[![Excel formula: Get information about max value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_information_corresponding_to_max_value.png "Excel formula: Get information about max value")](https://exceljet.net/formulas/get-information-about-max-value)

### [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)

An interesting problem in Excel is how to look up information related to the maximum value in a set of data. For example, if you have a dataset of property listings and prices, you might want to find details about the property with the highest price. The best way to solve this problem depends on...

[![Excel formula: Get next scheduled event](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20next%20scheduled%20event.png "Excel formula: Get next scheduled event")](https://exceljet.net/formulas/get-next-scheduled-event)

### [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)

The first part of the solution uses the MIN and TODAY functions to find the "next date" based on the date today. This is done by filtering the dates through the IF function: IF((date>=TODAY()),date) The logical test generates an array of TRUE / FALSE values, where TRUE corresponds to dates greater...

Related functions
-----------------

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)
    
*   [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)
    

### Functions

*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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