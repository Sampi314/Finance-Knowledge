# Sum if date is greater than - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-date-is-greater-than

---

[Skip to main content](https://exceljet.net/formulas/sum-if-date-is-greater-than#main-content)

[](https://exceljet.net/formulas/sum-if-date-is-greater-than#)

*   [Previous](https://exceljet.net/formulas/sum-if-date-is-between)
    
*   [Next](https://exceljet.net/formulas/sum-if-ends-with)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if date is greater than
===========================

by Dave Bruns · Updated 13 Jan 2023

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[SUMIF](https://exceljet.net/functions/sumif-function)

[DATE](https://exceljet.net/functions/date-function)

![Excel formula: Sum if date is greater than](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_date_is_greater_than.png "Excel formula: Sum if date is greater than")

Summary
-------

To sum values when corresponding dates are greater than a given date, you can use the [SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
. In the example shown, the formula in cell G5 is:

    =SUMIFS(C5:C16,B5:B16,">"&E5)
    

The result is $18,550, the sum of Amounts in the range C5:C16 when the date in B5:B16 is greater than 15-Oct-2022.

Generic formula
---------------

    =SUMIFS(values,dates,">="&A1)

Explanation 
------------

In this example, the goal is to sum amounts C5:C16 when the date in B5:B16 is _greater than_ the date provided in cell E5. A good way to solve this problem is with the [SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
.

_Note: for SUMIFS to work correctly, the worksheet must use [valid Excel dates](https://exceljet.net/glossary/excel-date)
. All dates in Excel have a numeric value underneath, and this is what allows SUMIFS to apply the logical criteria described below._

### SUMIFS function

The SUMIFS function sums cells in a [range](https://exceljet.net/glossary/range)
 that meet one or more conditions, referred to as _criteria_. The generic syntax for SUMIFS looks like this:

    =SUMIFS(sum_range,range1,criteria1) // 1 condition
    =SUMIFS(sum_range,range1,criteria1,range2,criteria2) // 2 conditions

In this problem, we need only one condition: the date in B5:B16 must be _greater than_ the date provided in cell E5. To apply criteria, the SUMIFS function supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. Each condition requires a separate _range_ and _criteria_, and operators need to be enclosed in double quotes (""). We start off with the sum range, which contains the amounts in C5:C16:

    =SUMIFS(C5:C16,

Next, we need to add criteria, which is provided in two parts. We add the range (B5:B16), then add the criteria (">="&E5):

    =SUMIFS(C5:C16,B5:B16,">"&E5)

Notice we need to enclose the [logical operator](https://exceljet.net/glossary/logical-operators)
 in double quotes (""), and join the text to the cell reference with [concatenation](https://exceljet.net/glossary/concatenation)
. This is a quirk of the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. When we enter this formula, we get a sum of all amounts in C5:C16 where corresponding dates in B5B16 are greater than 15-Oct-2022, which is $18,550. Notice we are _not_ including the start date in the result.

### SUMIF function

Because this problem only requires a single condition, another option is to use the SUMIF function, an older function in Excel. The syntax is similar, but the order of the [arguments](https://exceljet.net/glossary/function-argument)
 is different. In the SUMIF function, the _sum\_range_ always comes last:

    =SUMIF(B5:B16,">"&E5,C5:C16)

### With hard-coded dates

In the example shown, the start date is exposed on the worksheet in cell E5. This is a nice solution, because it makes the start date easy to change. However, there may be times when you want to hardcode a date into a formula. In that case, the safest way to hardcode a date into the SUMIFS function is to use the [DATE function](https://exceljet.net/functions/date-function)
, which generates a valid Excel date from the separate year, month, and day values. To sum amounts C5:C16 when the date in B5:B16 is _greater than_ 15-Oct-2022, where the date is hardcoded, you can use a formula like this:

    =SUMIFS(C5:C16,B5:B16,">"&DATE(2022,10,15))

Notice we still need to concatenate the logical operator ">" to the DATE function.

Related formulas
----------------

[![Excel formula: Sum if date is between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_date_is_between.png "Excel formula: Sum if date is between")](https://exceljet.net/formulas/sum-if-date-is-between)

### [Sum if date is between](https://exceljet.net/formulas/sum-if-date-is-between)

In this example, the goal is to sum amounts in column C when the date in column B is between two given dates. The start date is provided in cell E5, and the end date is provided in cell F5. The date range should be inclusive - both the start date and end date should be included in the final result...

[![Excel formula: Sum if begins with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_begins_with.png "Excel formula: Sum if begins with")](https://exceljet.net/formulas/sum-if-begins-with)

### [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)

In this example, the goal is to sum the Price in column C when the Product in column B begins with "sha". To solve this problem, you can use either the SUMIF function or the SUMIFS function with the asterisk (\*) wildcard, as explained below. Wildcards Certain Excel functions like SUMIF and SUMIFS...

[![Excel formula: Sum if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_not_blank.png "Excel formula: Sum if not blank")](https://exceljet.net/formulas/sum-if-not-blank)

### [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)

In this example, the goal is to sum the Amounts in C5:C16 when the Lead in D5:D16 is not blank (i.e., not empty). A good way to solve this problem is to use the SUMIFS function . However, you can also use the SUMPRODUCT function or the FILTER function , as explained below. Because SUMPRODUCT and...

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumif-function)

### [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)

In this video we'll look at how to use the SUMIF function to sum cells that meet a single criteria. Let's take a look. The SUMIF function sums cells that satisfy a single condition that you supply. It takes three arguments: range, criteria, and sum range. Note that sum range is optional. If you don...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum if date is between](https://exceljet.net/formulas/sum-if-date-is-between)
    
*   [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)
    
*   [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)
    
*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    
*   [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)
    

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