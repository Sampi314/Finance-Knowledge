# Sum if multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/sum-if-multiple-criteria#main-content)

[](https://exceljet.net/formulas/sum-if-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/sum-if-multiple-columns)
    
*   [Next](https://exceljet.net/formulas/sum-if-not-blank)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if multiple criteria
========================

by Dave Bruns · Updated 22 Dec 2022

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel formula: Sum if multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_multiple_criteria.png "Excel formula: Sum if multiple criteria")

Summary
-------

To sum numbers based on multiple criteria, you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. In the example shown, the formula in I6 is:

    =SUMIFS(F5:F16,C5:C16,"red",D5:D16,"tx")
    

The result is $88.00, the sum of the Total in F5:F16 when the Color in C5:C16 is "Red" and the State in D5:D16 is "TX". Note that the SUMIFS function is _not_ case-sensitive.

Generic formula
---------------

    =SUMIFS(sum_range,range1,criteria1,range2,criteria2)

Explanation 
------------

In this example, the goal is to sum the values in F5:F16 when the Color in C5:C16 is "Red" and the State in D5:D16 is "TX". This is an example of a conditional sum with multiple criteria and the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 is the easiest way to solve this problem.

### SUMIFS function

The SUMIFS function sums cells in a [range](https://exceljet.net/glossary/range)
 that meet one or more conditions, referred to as _criteria_. To apply criteria, the SUMIFS function supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. The syntax for the SUMIFS function depends on the number of conditions needed. Each separate condition will require a _range_ and a _criteria_. The generic syntax for SUMIFS looks like this:

    =SUMIFS(sum_range,range1,criteria1) // 1 condition
    =SUMIFS(sum_range,range1,criteria1,range2,criteria2) // 2 conditions

The first [argument](https://exceljet.net/glossary/function-argument)
, _sum\_range_, is the range of cells to sum, which should contain numeric values. Notice the conditions (called _criteria_) are entered in _pairs_. Each new condition requires a separate _range_ and _criteria_.

### Example - Red and TX

We start off with sum\_range, which is the range F5:F16:

    =SUMIFS(F5:F16,

Next, we add the first condition, which is that the Color in C5:C16 is "Red":

    =SUMIFS(F5:F16,C5:C16,"red"

The range is C5:C16, and the criteria is "red". Note that SUMIFS is not case-sensitive, so "red" will match "Red", "RED", and "red". Next, we need to add the second condition, which is that the State in D5:D16 is "TX". Again, we need to supply both a range and a criteria:

    =SUMIFS(F5:F16,C5:C16,"red",D5:D16,"tx")

When the formula is entered, the result is $88.00, the sum of the Total in F5:F16 when the Color in C5:C16 is "Red" and the State in D5:D16 is "TX".

### Example - Red and >20

Next, the goal is to sum the Total in F5:F16 when the color is "red" and the value of Total is _greater than_ $20. This means we need to include the [logical operator](https://exceljet.net/glossary/logical-operators)
 (>) in the second criteria. The formula in I7 is:

    =SUMIFS(F5:F16,C5:C16,"red",F5:F16,">20")

To read more about the syntax needed to apply logical operators and use wildcards with the SUMIFS function, [see this page](https://exceljet.net/functions/sumifs-function)
.

Related formulas
----------------

[![Excel formula: Sum if x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_x_or_y.png "Excel formula: Sum if x or y")](https://exceljet.net/formulas/sum-if-x-or-y)

### [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)

In this example, the goal is to sum Total when the corresponding Color is either "Red" or "Blue". For convenience, all data is in an Excel Table named data . This is a tricky problem, because the solution is not obvious. The go-to function for conditional sums is the SUMIFS function . However, when...

[![Excel formula: Sum if date is between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_date_is_between.png "Excel formula: Sum if date is between")](https://exceljet.net/formulas/sum-if-date-is-between)

### [Sum if date is between](https://exceljet.net/formulas/sum-if-date-is-between)

In this example, the goal is to sum amounts in column C when the date in column B is between two given dates. The start date is provided in cell E5, and the end date is provided in cell F5. The date range should be inclusive - both the start date and end date should be included in the final result...

[![Excel formula: Sum last 30 days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_last_30_days.png "Excel formula: Sum last 30 days")](https://exceljet.net/formulas/sum-last-30-days)

### [Sum last 30 days](https://exceljet.net/formulas/sum-last-30-days)

In this example, the goal is to calculate total amounts in column C that occur in the last 30 days, based on a current date of December 30, 2022. There are three basic approaches to solving this problem: (1) a traditional approach based on the SUMIFS function , (2) a more flexible approach that...

[![Excel formula: Sum by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_by_month.png "Excel formula: Sum by month")](https://exceljet.net/formulas/sum-by-month)

### [Sum by month](https://exceljet.net/formulas/sum-by-month)

In this example, the goal is to sum the amounts shown in column C by month using the dates in column B. The article below explains two approaches. One approach is based on the SUMIFS function , which can sum numeric values based on multiple criteria. The second approach is based on the SUMPRODUCT...

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

[![Excel formula: Count if two criteria match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20if%20two%20criteria%20match.png "Excel formula: Count if two criteria match")](https://exceljet.net/formulas/count-if-two-criteria-match)

### [Count if two criteria match](https://exceljet.net/formulas/count-if-two-criteria-match)

In this example, the goal is to count orders where the color is "blue" and the quantity is greater than 15. All data is in the range B5:B15. There are two primary ways to solve this problem, one with the COUNTIFS function, the other with the SUMPRODUCT function. Both approaches are explained below...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20SUMIFS%20with%20an%20Excel%20Table-Thumb.png)](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)

### [How to use SUMIFS with an Excel Table](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)

In this video, we'll look at how to use the SUMIFS function with an Excel Table. On this worksheet, I have two identical sets of order data. I'm going to walk through the process of constructing a summary of sales by item for both sets of data. With the data on the left, I'll use standard formulas...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)
    
*   [Sum if date is between](https://exceljet.net/formulas/sum-if-date-is-between)
    
*   [Sum last 30 days](https://exceljet.net/formulas/sum-last-30-days)
    
*   [Sum by month](https://exceljet.net/formulas/sum-by-month)
    
*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    
*   [Count if two criteria match](https://exceljet.net/formulas/count-if-two-criteria-match)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    
*   [How to use SUMIFS with an Excel Table](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

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