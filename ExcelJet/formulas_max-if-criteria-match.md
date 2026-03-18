# Max if criteria match - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/max-if-criteria-match

---

[Skip to main content](https://exceljet.net/formulas/max-if-criteria-match#main-content)

[](https://exceljet.net/formulas/max-if-criteria-match#)

*   [Previous](https://exceljet.net/formulas/match-next-highest-value)
    
*   [Next](https://exceljet.net/formulas/merge-tables-with-vlookup)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Max if criteria match
=====================

by Dave Bruns · Updated 10 Dec 2019

Related functions 
------------------

[MAX](https://exceljet.net/functions/max-function)

[IF](https://exceljet.net/functions/if-function)

[MAXIFS](https://exceljet.net/functions/maxifs-function)

![Excel formula: Max if criteria match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/max%20if%20criteria%20match.png "Excel formula: Max if criteria match")

Summary
-------

To find the maximum value in a range with specific criteria, you can use a basic [array formula](https://exceljet.net/glossary/array-formula)
 based on the IF function and MAX function. In the example shown, the formula in cell H8 is:

    {=MAX(IF(B5:B9391=H7,E5:E9391))}
    

which returns the maximum temperature on the date in H7.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter_

Generic formula
---------------

    {=MAX(IF(criteria_range=criteria,value_range))}

Explanation 
------------

The example shown contains almost 10,000 rows of data. The data represents temperature readings taken every 2 minutes over a period of days. For any given date (provided in cell H7), we want to get the maximum temperature on that date.

Inside the [IF function](https://exceljet.net/videos/the-if-function)
, logical test is entered as B5:B9391=H7. Because we're comparing the value in H7 against a range of cells (an array), the result will be an [array](https://exceljet.net/glossary/array)
 of results, where each item in the array is either TRUE or FALSE. The TRUE values represent dates that match H7.

For the value if true, we provide the range E5:E9391, which fetches all the full set of temperatures in Fahrenheit. This returns an array of values the same size as the first array.

The IF function acts as a filter. Because we provide IF with an array for the logical test, IF returns an _array of results_. Where the date matches H7, the array contains a temperature value. In all other cases, the array contains FALSE. In other words, only temperatures associated with the date in H7 survive the trip through the IF function.

The array result from the IF function is delivered directly to the [MAX function](https://exceljet.net/functions/max-function)
, which returns the maximum value in the array.

### With MAXIFS

In Excel O365 and Excel 2019, the new [MAXIFS function](https://exceljet.net/functions/maxifs-function)
 can find the maximum value with one or more criteria without the need for an array formula. With MAXIFS, the equivalent formula for the this example is:

    =MAXIFS(E5:E9391,B5:B9391,H7)
    

Related formulas
----------------

[![Excel formula: Maximum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value_if.png "Excel formula: Maximum value if")](https://exceljet.net/formulas/maximum-value-if)

### [Maximum value if](https://exceljet.net/formulas/maximum-value-if)

In this example, the goal is to get the maximum value for each group in the data as shown. The easiest way to solve this problem is with the MAXIFS function. However, there are actually several options. If you need more flexibility (i.e. you need to work with arrays and not ranges), you can use the...

[![Excel formula: Maximum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_if_multiple_criteria.png "Excel formula: Maximum if multiple criteria")](https://exceljet.net/formulas/maximum-if-multiple-criteria)

### [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)

In this example, the goal is to get the maximum value for a given group below a specific temperature. In other words, we want the max value after applying multiple criteria. The easiest way to solve this problem is with the MAXIFS function. However, if you need more flexibility (i.e., you need to...

[![Excel formula: Get next scheduled event](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20next%20scheduled%20event.png "Excel formula: Get next scheduled event")](https://exceljet.net/formulas/get-next-scheduled-event)

### [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)

The first part of the solution uses the MIN and TODAY functions to find the "next date" based on the date today. This is done by filtering the dates through the IF function: IF((date>=TODAY()),date) The logical test generates an array of TRUE / FALSE values, where TRUE corresponds to dates greater...

[![Excel formula: Find closest match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_closest_match_0.png "Excel formula: Find closest match")](https://exceljet.net/formulas/find-closest-match)

### [Find closest match](https://exceljet.net/formulas/find-closest-match)

In this example, the goal is to find the closest match to a target value entered in cell E5. Although it may not look like it, this is essentially a look-up problem. The easiest way to solve this problem is with the XLOOKUP function . However in older versions of Excel without the XLOOKUP function...

Related functions
-----------------

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel MAXIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20maxifs%20function.png "Excel MAXIFS function")](https://exceljet.net/functions/maxifs-function)

### [MAXIFS Function](https://exceljet.net/functions/maxifs-function)

The Excel MAXIFS function returns the largest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MAXIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers, and...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Maximum value if](https://exceljet.net/formulas/maximum-value-if)
    
*   [Maximum if multiple criteria](https://exceljet.net/formulas/maximum-if-multiple-criteria)
    
*   [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)
    
*   [Find closest match](https://exceljet.net/formulas/find-closest-match)
    

### Functions

*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [MAXIFS Function](https://exceljet.net/functions/maxifs-function)
    

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