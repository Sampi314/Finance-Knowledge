# Sum if between - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-between

---

[Skip to main content](https://exceljet.net/formulas/sum-if-between#main-content)

[](https://exceljet.net/formulas/sum-if-between#)

*   [Previous](https://exceljet.net/formulas/sum-if-begins-with)
    
*   [Next](https://exceljet.net/formulas/sum-if-case-sensitive)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if between
==============

by Dave Bruns · Updated 20 Dec 2022

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel formula: Sum if between](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20if%20between.png "Excel formula: Sum if between")

Summary
-------

To sum numeric values that are between two numbers, you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. In the example shown, the formula in cell H5 is:

    =SUMIFS(data[Amount],data[Amount],">"&F5,data[Amount],"<="&G5)
    

Where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:D16.

_Note: With an Excel Table, the formula will automatically update if data is added or removed from the table._

Generic formula
---------------

    =SUMIFS(data,data,">"&start,data,"<="&end)

Explanation 
------------

In this example, the goal is to sum the amounts in the table using the "Start" and "End" values in columns F and G. For convenience, all data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 called **data**, which means we can use the [structured reference](https://exceljet.net/glossary/structured-reference)
 **data\[Amount\]** to refer to amounts. An easy way to solve this problem is to use the SUMIFS function, as explained below.

### SUMIFS function

The [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 can sum values in ranges based on multiple criteria. The basic function signature for SUMIFS looks like this:

    =SUMIFS(sum_range,range1,criteria1,range2,criteria2,...)
    

In this case, we need to configure SUMIFS to sum values in the Amount column based on two criteria:

1.  Amounts greater than zero (the value in cell F5)
2.  Amounts that are less than or equal to 500 (the value in E5)

Conditions are supplied to SUMIFS as range/criteria pairs, so each condition will be composed of two arguments.  To start off, we provide the _sum\_range_ to SUMIFS, which contains the values we want to sum:

    =SUMIFS(sum_range
    

Next, add the first condition, which is that amounts need to be greater than zero (the value in cell F5):

    =SUMIFS(data[Amount],data[Amount],">"&F5
    

Here we provide **data\[Amount\]** as _criteria\_range1_, and the  ">"&F5 for _criteria1_. Notice we need to [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the cell reference to the [logical operators](https://exceljet.net/glossary/logical-operators)
, and the operators are entered as text\*, enclosed in double quotes (""). Next, we need to add the second condition, for amounts less than or equal to 500 (the value in cell E5):

    =SUMIFS(data[Amount],data[Amount],">"&F5,data[Amount],"<="&G5)
    

As before, we need to concatenate the operator as text to cell C5. When we enter this formula, it returns 1400, the total of all amounts greater than 0 and less than or equal to 500.  As the formula is copied down, it returns a new total in each row, based on the values in columns F and G. The [structured reference](https://exceljet.net/videos/introduction-to-structured-references)
 **data\[Amount\]** behaves like an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 and does not change. The references to F5 and G5 are [relative](https://exceljet.net/glossary/relative-reference)
 and change at each new row.

_\* Note: SUMIFS is in a group of functions that split criteria into two parts. As a result, the syntax used for operators is different from other functions. [See this article for details](https://exceljet.net/articles/excels-racon-functions)
._

Related formulas
----------------

[![Excel formula: Sum if greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_greater_than.png "Excel formula: Sum if greater than")](https://exceljet.net/formulas/sum-if-greater-than)

### [Sum if greater than](https://exceljet.net/formulas/sum-if-greater-than)

In this example, the goal is to sum values in the range D5:D16 when they are greater than the value entered in cell F5. This problem can be easily solved with the SUMIF function or the SUMIFS function. The main challenge in this problem is the syntax needed for criteria that uses the value in cell...

[![Excel formula: Sum if less than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_less_than.png "Excel formula: Sum if less than")](https://exceljet.net/formulas/sum-if-less-than)

### [Sum if less than](https://exceljet.net/formulas/sum-if-less-than)

In this example, the goal is to sum values in the range D5:D16 when they are less than the value entered in cell F5. This problem can be easily solved with the SUMIF function or the SUMIFS function. The main challenge in this problem is the syntax needed for cell F5 in the criteria, which involves...

[![Excel formula: Sum if begins with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_begins_with.png "Excel formula: Sum if begins with")](https://exceljet.net/formulas/sum-if-begins-with)

### [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)

In this example, the goal is to sum the Price in column C when the Product in column B begins with "sha". To solve this problem, you can use either the SUMIF function or the SUMIFS function with the asterisk (\*) wildcard, as explained below. Wildcards Certain Excel functions like SUMIF and SUMIFS...

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

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum if greater than](https://exceljet.net/formulas/sum-if-greater-than)
    
*   [Sum if less than](https://exceljet.net/formulas/sum-if-less-than)
    
*   [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)
    
*   [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)
    
*   [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)
    
*   [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)
    
*   [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)
    
*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

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