# Sum if cells are equal to - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-cells-are-equal-to

---

[Skip to main content](https://exceljet.net/formulas/sum-if-cells-are-equal-to#main-content)

[](https://exceljet.net/formulas/sum-if-cells-are-equal-to#)

*   [Previous](https://exceljet.net/formulas/sum-if-cell-contains-text-in-another-cell)
    
*   [Next](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if cells are equal to
=========================

by Dave Bruns · Updated 16 Dec 2022

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel formula: Sum if cells are equal to](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_cells_are_equal_to.png "Excel formula: Sum if cells are equal to")

Summary
-------

To sum numbers when cells are equal to a specific value, you can use the SUMIF or SUMIFS functions. In the example shown, the formula in cell I5 is:

    =SUMIFS(F5:F16,C5:C16,"red")
    

When this formula is entered, the result is $192. This is the sum of numbers in the range F5:F16 when cells in C5:C15 contain "Red". Note that the SUMIFS function is _not_ case-sensitive.

Generic formula
---------------

    =SUMIFS(sum_range,range,"red")

Explanation 
------------

In this example the goal is to sum the numbers in the range F5:F16 when cells in the range C5:C15 contain "Red". To solve this problem, you can use either the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 or the [SUMIF function](https://exceljet.net/functions/sumif-function)
. The SUMIF function is an older function that supports only a single condition. SUMIFS on the other hand can be configured to apply multiple criteria. Both options are explained below.

### SUMIFS solution

 In the example shown, the solution is based on the SUMIFS function. The formula in cell I5 is:

    =SUMIFS(F5:F16,C5:C16,"red")
    

In this formula, _sum\_range_ is F5:F16, _criteria\_range1_ is C5:C16, and _criteria1_ is "red". The result ($192) is the sum of numbers in the range F5:F16 when cells in C5:C15 contain "Red". Note that the SUMIFS function is _not_ case-sensitive. With a criteria of "red", SUMIFS will match "RED", "Red", and "red". Also note that in the SUMIFS function, _sum\_range_ always comes _first_. To use SUMIFS to calculate a conditional sum when the state is Texas (state = "TX"), you can use a formula like this:

    =SUMIFS(F5:F16,D5:D16,"tx")

In this formula, _sum\_range_ is again F5:F16, _criteria\_range1_ is D5:D16, and _criteria1_ is "tx". For more information about using SUMIFS to apply multiple criteria with logical operators (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?), [see this page](https://exceljet.net/functions/sumifs-function)
.

### SUMIF solution

The SUMIF function is an older function in Excel that supports only a single condition. To solve this problem with the SUMIF function, you can use a formula like this:

    =SUMIF(C5:C16,"red",F5:F16)

In this formula, _range_ is D5:D16, _criteria_ is "tx", and _sum\_range_ is again F5:F16. Note that in the SUMIF function, _sum\_range_ always comes _last_. The result ($192) is the same as with the SUMIFS function above. For more information about using SUMIF to apply criteria with logical operators (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?), [see this page](https://exceljet.net/functions/sumif-function)
.

Whether you use SUMIFS or SUMIF is a matter of personal preference. SUMIFS was introduced in Excel 2007, so it's been around now for a long time.

### Notes

*   For a case-sensitive solution, [see this formula](https://exceljet.net/formulas/sum-if-case-sensitive)
    .
*   To match a _substring_ in a cell, [see this formula](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    .
*   To sum if _not equal to_, [see this formula](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)
    .

Related formulas
----------------

[![Excel formula: Sum if cells are not equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_not_equal_to.png "Excel formula: Sum if cells are not equal to")](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

### [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when corresponding cells in the range C5:C15 are not equal to "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only one criteria...

[![Excel formula: Sum if x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_x_or_y.png "Excel formula: Sum if x or y")](https://exceljet.net/formulas/sum-if-x-or-y)

### [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)

In this example, the goal is to sum Total when the corresponding Color is either "Red" or "Blue". For convenience, all data is in an Excel Table named data . This is a tricky problem, because the solution is not obvious. The go-to function for conditional sums is the SUMIFS function . However, when...

[![Excel formula: Sum if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_not_blank.png "Excel formula: Sum if not blank")](https://exceljet.net/formulas/sum-if-not-blank)

### [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)

In this example, the goal is to sum the Amounts in C5:C16 when the Lead in D5:D16 is not blank (i.e., not empty). A good way to solve this problem is to use the SUMIFS function . However, you can also use the SUMPRODUCT function or the FILTER function , as explained below. Because SUMPRODUCT and...

[![Excel formula: Sum if begins with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_begins_with.png "Excel formula: Sum if begins with")](https://exceljet.net/formulas/sum-if-begins-with)

### [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)

In this example, the goal is to sum the Price in column C when the Product in column B begins with "sha". To solve this problem, you can use either the SUMIF function or the SUMIFS function with the asterisk (\*) wildcard, as explained below. Wildcards Certain Excel functions like SUMIF and SUMIFS...

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

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

*   [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)
    
*   [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)
    
*   [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)
    
*   [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)
    
*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    

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