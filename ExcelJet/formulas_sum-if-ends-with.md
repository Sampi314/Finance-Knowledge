# Sum if ends with - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-ends-with

---

[Skip to main content](https://exceljet.net/formulas/sum-if-ends-with#main-content)

[](https://exceljet.net/formulas/sum-if-ends-with#)

*   [Previous](https://exceljet.net/formulas/sum-if-date-is-greater-than)
    
*   [Next](https://exceljet.net/formulas/sum-if-greater-than)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if ends with
================

by Dave Bruns · Updated 20 Dec 2022

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel formula: Sum if ends with](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_cells_end_with.png "Excel formula: Sum if ends with")

Summary
-------

To sum numbers when corresponding text values _end with_ specific text, you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 or the [SUMIF function](https://exceljet.net/functions/sumif-function)
. In the example shown, the formula in F5 is:

    =SUMIFS(C5:C16,B5:B16,"*small")
    

The result is 19, which is the sum of the quantities in the range C5:C16 when the corresponding item names in B5:B16 end with "small". Note the SUMIFS function is _not_ case-sensitive.

Generic formula
---------------

    =SUMIFS(sum_range,range,"*text")

Explanation 
------------

In this example, the goal is to sum the Quantity in C5:C16 when the Item in B5:B16 ends with "small". To solve this problem, you can use either the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 or the [SUMIF function](https://exceljet.net/functions/sumif-function)
 with the asterisk (\*) wildcard, as explained below.

### Wildcards

Certain Excel functions like SUMIFS and SUMIF support the [wildcard](https://exceljet.net/glossary/wildcard)
 characters "?" (any one character) and "\*" (zero or more characters), which can be used in criteria. These wildcards allow you to create criteria such as "begins with", "ends with", "contains 3 characters", etc. as shown in the table below:

| Target | Criteria |
| --- | --- |
| Cells with 3 characters | "???" |
| Cells like "bed", "bad", "bid", etc | "b?d" |
| Cells that begin with "xyz" | "xyz\*" |
| Cells that end with "xyz" | "\*xyz" |

Note that wildcards are enclosed in double quotes ("") when they appear in criteria.

### SUMIFS solution

The generic syntax for the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 with a single condition looks like this:

    =SUMIFS(sum_range,range1,criteria1)

Notice that the sum range always comes _first_ in the SUMIFS function. To use SUMIFS to sum the Quantity in C5:C16 when the Item in B5:B16 ends with "small", the formula in F5 looks like this:

    =SUMIFS(C5:C16,B5:B16,"*small")
    

The criteria "\*small" means match text that _ends with_ "small". Notice both the text and the wildcard must be enclosed in double quotes (""). Also note that SUMIFS is _not_ case-sensitive. The criteria "\*small" will match "Small", "SMALL", or "small".

### SUMIF function

You can also solve this problem with the SUMIF function, an older function in Excel that supports just one condition. The generic syntax for the [SUMIF function](https://exceljet.net/functions/sumif-function)
 looks like this:

    =SUMIF(range,criteria,sum_range)

Notice _sum\_range_ comes _last_ in the SUMIF function. To sum the Quantity in C5:C16 when the Item in B5:B16 ends with "small", the equivalent SUMIF formula is:

    =SUMIF(B5:B16,"*small",C5:C16)

Like the SUMIFS function, the SUMIF function is _not_ case-sensitive.

Related formulas
----------------

[![Excel formula: Sum if begins with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_begins_with.png "Excel formula: Sum if begins with")](https://exceljet.net/formulas/sum-if-begins-with)

### [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)

In this example, the goal is to sum the Price in column C when the Product in column B begins with "sha". To solve this problem, you can use either the SUMIF function or the SUMIFS function with the asterisk (\*) wildcard, as explained below. Wildcards Certain Excel functions like SUMIF and SUMIFS...

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

[![Excel formula: Sum if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_not_blank.png "Excel formula: Sum if not blank")](https://exceljet.net/formulas/sum-if-not-blank)

### [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)

In this example, the goal is to sum the Amounts in C5:C16 when the Lead in D5:D16 is not blank (i.e., not empty). A good way to solve this problem is to use the SUMIFS function . However, you can also use the SUMPRODUCT function or the FILTER function , as explained below. Because SUMPRODUCT and...

[![Excel formula: Sum if cells are not equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_not_equal_to.png "Excel formula: Sum if cells are not equal to")](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

### [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when corresponding cells in the range C5:C15 are not equal to "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only one criteria...

[![Excel formula: Sum if x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_x_or_y.png "Excel formula: Sum if x or y")](https://exceljet.net/formulas/sum-if-x-or-y)

### [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)

In this example, the goal is to sum Total when the corresponding Color is either "Red" or "Blue". For convenience, all data is in an Excel Table named data . This is a tricky problem, because the solution is not obvious. The go-to function for conditional sums is the SUMIFS function . However, when...

Related functions
-----------------

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumif-function)

### [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)

In this video we'll look at how to use the SUMIF function to sum cells that meet a single criteria. Let's take a look. The SUMIF function sums cells that satisfy a single condition that you supply. It takes three arguments: range, criteria, and sum range. Note that sum range is optional. If you don...

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

*   [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)
    
*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    
*   [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)
    
*   [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)
    
*   [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)
    

### Functions

*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

### Videos

*   [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)
    
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