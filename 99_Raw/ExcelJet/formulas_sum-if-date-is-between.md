# Sum if date is between - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-date-is-between

---

[Skip to main content](https://exceljet.net/formulas/sum-if-date-is-between#main-content)

[](https://exceljet.net/formulas/sum-if-date-is-between#)

*   [Previous](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    
*   [Next](https://exceljet.net/formulas/sum-if-date-is-greater-than)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if date is between
======================

by Dave Bruns · Updated 5 Oct 2023

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[DATE](https://exceljet.net/functions/date-function)

![Excel formula: Sum if date is between](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_date_is_between.png "Excel formula: Sum if date is between")

Summary
-------

To sum values between a given start and end date, you can use the [SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
. In the example shown, the formula in cell G5 is:

    =SUMIFS(C5:C16,B5:B16,">="&E5,B5:B16,"<="&F5)
    

The result is $13,500, the sum of Amounts in the range C5:C16 when the date in B5:B16 is between 15-Sep-22 and 15-Oct-22, inclusive.

Generic formula
---------------

    =SUMIFS(values,dates,">="&A1,dates,"<="&B1)

Explanation 
------------

In this example, the goal is to sum amounts in column C when the date in column B is between two given dates. The start date is provided in cell E5, and the end date is provided in cell F5. The date range should be inclusive - both the start date and end date should be included in the final result. A good way to solve this problem is with the [SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
.

_Note: for SUMIFS to work correctly, the worksheet must use [valid Excel dates](https://exceljet.net/glossary/excel-date)
. All dates in Excel have a numeric value underneath, and this is what allows SUMIFS to apply the logical criteria described below._

### SUMIFS with a date range

The generic syntax for using SUMIFS with a date range looks like this:

    =SUMIFS(sum_range,criteria_range1,criteria1,criteria_range2,criteria2)

Where the arguments above have the following meaning:

*   _sum\_range_ - the range that contains values to sum
*   _criteria\_range1_ - a range that contains the dates 
*   _criteria1_ - logic to target dates greater than the start date
*   _criteria\_range2_ - a range that contains the dates 
*   _criteria2_ - logic to target dates less than the end date

In the worksheet shown, we already have a start date entered in cell E5 (15-Sep-2022) and an end date in F5 (15-Oct-2022), so we will need to use those cell references as we enter criteria into SUMIFS. We start off with the sum range, which contains the amounts in C5:C16:

    =SUMIFS(C5:C16,

Note that values in this range must be _numeric_. Next, we need to add the logic needed to target dates greater than or equal to the date in cell E5. We do this by entering two arguments: _criteria\_range1_ and _criteria1_. We first add the range that contains the dates (B5:B16), then we add the criteria, which we enter as ">="&E5:

    =SUMIFS(C5:C16,B5:B16,">="&E5,

This tricky syntax is a quirk of all the [RACON functions in Excel](https://exceljet.net/articles/excels-racon-functions)
. Notice that we need to enclose the [operator](https://exceljet.net/glossary/logical-operators)
 in double quotes (">="), and [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the cell reference E5 with an ampersand (&). ​​​​​​If we enter this formula as-is, we get a sum of all amounts in C5:C16 that are greater than or equal to 15-Sep-2022, which is $32,050:

    =SUMIFS(C5:C16,B5:B16,">="&E5) // returns 32050

This is a valid result, but we aren't done yet, because we still need to add the second criteria for the end date in cell F5. We do this in the same way, by adding two more arguments: _criteria\_range2_ and _criteria2_. We first add the date range (B5:B16):

    =SUMIFS(C5:C16,B5:B16,">="&E5,B5:B16,

Then we add the criteria:

    =SUMIFS(C5:C16,B5:B16,">="&E5,B5:B16,"<="&F5)

Notice we use the _same date range_ (B5:B16) for _criteria\_range2_ and, as before, we need to enclose the operator in double quotes ("<=") and concatenate cell F5 with an ampersand (&). When we enter the formula, SUMIFS returns $13,500, the total of Amounts in C5:C16 that are between 15-Sep-2022 and 15-Oct-2022, inclusive. If the dates in cell E5 or cell F5 are changed, the formula will immediately calculate a new result.

### With hard-coded dates

In general, it is a best practice to enter the dates you want to use in a formula directly on the worksheet. This makes the worksheet more "transparent" because you can easily see the dates being used, and easily change the dates when needed. It also reduces the problem of Excel incorrectly interpreting a date, since you can see at a glance if dates on the worksheet are displayed correctly. That said, there may be times when you need to hardcode dates directly into a formula. The safest way to do this is to use the [DATE function](https://exceljet.net/functions/date-function)
, which creates a valid date with separate _year_, _month_, and _day_ arguments like this:

    =DATE(year,month,day)

In this example, we can adapt the SUMIFS function above to use hardcoded dates by incorporating the DATE function inside the SUMIFS function like this:

    =SUMIFS(C5:C16,B5:B16,">="&DATE(2022,9,15),B5:B16,"<="&DATE(2022,10,15))

*   _sum\_range_ - C5:C16
*   _criteria\_range1_ - B5:B16
*   _criteria1_ - ">="&DATE(2022,9,15)
*   _criteria\_range2_ - B5:B16
*   _criteria1_ - "<="&DATE(2022,10,15)

Notice we still need to concatenate the logical operators to the DATE function using an ampersand (&).

Related formulas
----------------

[![Excel formula: Sum if date is greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_date_is_greater_than.png "Excel formula: Sum if date is greater than")](https://exceljet.net/formulas/sum-if-date-is-greater-than)

### [Sum if date is greater than](https://exceljet.net/formulas/sum-if-date-is-greater-than)

In this example, the goal is to sum amounts C5:C16 when the date in B5:B16 is greater than the date provided in cell E5. A good way to solve this problem is with the SUMIFS function . Note: for SUMIFS to work correctly, the worksheet must use valid Excel dates . All dates in Excel have a numeric...

[![Excel formula: Sum if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_not_blank.png "Excel formula: Sum if not blank")](https://exceljet.net/formulas/sum-if-not-blank)

### [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)

In this example, the goal is to sum the Amounts in C5:C16 when the Lead in D5:D16 is not blank (i.e., not empty). A good way to solve this problem is to use the SUMIFS function . However, you can also use the SUMPRODUCT function or the FILTER function , as explained below. Because SUMPRODUCT and...

[![Excel formula: Sum if cells are equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_equal_to.png "Excel formula: Sum if cells are equal to")](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

### [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when cells in the range C5:C15 contain "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only a single condition. SUMIFS on the other...

[![Excel formula: Sum if cells are not equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_not_equal_to.png "Excel formula: Sum if cells are not equal to")](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

### [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when corresponding cells in the range C5:C15 are not equal to "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only one criteria...

[![Excel formula: Sum if x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_x_or_y.png "Excel formula: Sum if x or y")](https://exceljet.net/formulas/sum-if-x-or-y)

### [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)

In this example, the goal is to sum Total when the corresponding Color is either "Red" or "Blue". For convenience, all data is in an Excel Table named data . This is a tricky problem, because the solution is not obvious. The go-to function for conditional sums is the SUMIFS function . However, when...

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum if date is greater than](https://exceljet.net/formulas/sum-if-date-is-greater-than)
    
*   [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)
    
*   [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)
    
*   [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)
    
*   [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)
    
*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    

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