# Sum if cells contain an asterisk - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-cells-contain-an-asterisk

---

[Skip to main content](https://exceljet.net/formulas/sum-if-cells-contain-an-asterisk#main-content)

[](https://exceljet.net/formulas/sum-if-cells-contain-an-asterisk#)

*   [Previous](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)
    
*   [Next](https://exceljet.net/formulas/sum-if-cells-contain-both-x-and-y)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if cells contain an asterisk
================================

by Dave Bruns · Updated 18 Jan 2023

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[FIND](https://exceljet.net/functions/find-function)

[FILTER](https://exceljet.net/functions/filter-function)

![Excel formula: Sum if cells contain an asterisk](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_cells_contain_an_asterisk.png "Excel formula: Sum if cells contain an asterisk")

Summary
-------

To sum numbers when corresponding cells contain an asterisk (\*), you can use the SUMIFS function with criteria that uses the tilde (~) as an escape character. In the example shown, cell G6 contains this formula:

    =SUMIFS(C5:C16,B5:B16,"*~**")
    

This formula sums the Price in column C when the Item name in column B contains an asterisk ("\*").

Generic formula
---------------

    =SUMIFS(sum_range,range,"*~**")

Explanation 
------------

The goal in this example is to sum Prices in column C when the Items in column B contain an asterisk (\*). The challenge is that the asterisk (\*) is reserved as a wildcard in functions like the SUMIFS function, so you can't match a literal occurrence of this character without using a special syntax.

### Wildcards

Excel functions like SUMIF and SUMIFS support the [wildcard](https://exceljet.net/glossary/wildcard)
 characters "?" (any one character) and "\*" (zero or more characters), which can be used in criteria. Wildcards allow you to create criteria to target cells that "begin with", "end with", "contain 3 characters" and so on. The table below shows some examples. For this problem, we want to use the "Cells that contain text in xyz" pattern, which uses two asterisks (\*), one before and one after the search string like this "\*xyz\*".

| Target | Criteria |
| --- | --- |
| Cells with 3 characters | "???" |
| Cells equal to "xyz", "xaz", "xbz", etc | "x?z" |
| Cells that begin with "xyz" | "xyz\*" |
| Cells that end with "xyz" | "\*xyz" |
| Cells that contain "xyz" | "\*xyz\*" |
| Cells that contain text in A1 | "\*"&A1&"\*" |

Because asterisks and question marks are themselves wildcards, if you want to search for these characters specifically, you'll need to escape them with a tilde (~). The tilde causes Excel to handle the next character _literally_.

### SUMIFS solution

To sum Prices in column C when the Items in column B contain an asterisk (\*), the formula in cell F5 is:

    =SUMIFS(C5:C16,B5:B16,"*~**")

In this case we are using "~\*" to match a literal asterisk, but this is surrounded by asterisks on either side, in order to match an asterisk _anywhere in the cell_. If you just want to match an asterisk at the end of a cell, you can use "\*~\*" for the criteria. To sum Prices for Item names that do not contain an asterisk ("\*"), the formula in cell F6 is:

    =SUMIFS(C5:C16,B5:B16,"<>*~**")

This formula simply prepends the not equal to [operator](https://exceljet.net/glossary/logical-operators)
 ("<>")  to the existing criteria. For more details about using other operators in the SUMIFS function, [see this page](https://exceljet.net/functions/sumifs-function)
.

### SUMIF solution

This problem can also be solved with the older [SUMIF function](https://exceljet.net/functions/sumif-function)
, which only supports a single condition. The equivalent formulas based on SUMIF look like this:

    =SUMIF(B5:B16,"*~**",C5:C16) // contains *
    =SUMIF(B5:B16,"<>*~**",C5:C16) // does not contain *

### Other options

In Excel, there is _always_ another way to skin the cat. If you don't like the fiddly syntax needed to escape wildcards above, you can use a formula based on the [FIND function](https://exceljet.net/functions/find-function)
 to search for an asterisk directly. One option that will work in any version of Excel is [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 + FIND:

    =SUMPRODUCT(ISNUMBER(FIND("*",B5:B16))*C5:C16)

This works because, unlike the [SEARCH function](https://exceljet.net/functions/search-function)
, the FIND function _does not_ support wildcards.  Another option in newer versions of Excel is to use the [SUM function](https://exceljet.net/functions/sum-function)
 with the [FILTER function](https://exceljet.net/functions/filter-function)
:

    =SUM(FILTER(C5:C16,ISNUMBER(FIND("*",B5:B16)),0))

Note that both of these functions use the same logic to locate text that contains an asterisk: ISNUMBER + FIND. To read more about how this part of the formula works, [see this example](https://exceljet.net/formulas/cell-contains-specific-text)
.

Related formulas
----------------

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

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

Related functions
-----------------

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

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

*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    
*   [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)
    
*   [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)
    
*   [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)
    
*   [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)
    
*   [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)
    

### Functions

*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

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