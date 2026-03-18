# Sum if cells contain both x and y - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-cells-contain-both-x-and-y

---

[Skip to main content](https://exceljet.net/formulas/sum-if-cells-contain-both-x-and-y#main-content)

[](https://exceljet.net/formulas/sum-if-cells-contain-both-x-and-y#)

*   [Previous](https://exceljet.net/formulas/sum-if-cells-contain-an-asterisk)
    
*   [Next](https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if cells contain both x and y
=================================

by Dave Bruns · Updated 28 Apr 2025

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel formula: Sum if cells contain both x and y](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_cells_contain_both_x_and_y.png "Excel formula: Sum if cells contain both x and y")

Summary
-------

To sum numbers if cells contain both x and y (i.e., contain "red" _and_ "blue") you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. In the example shown, the formula in F5 is:

    =SUMIFS(C5:C16,B5:B16,"*red*",B5:B16,"*blue*")
    

The result is 6, the sum of the numbers in column C when the text in column B contains both "red" and "blue" in any order. Note that SUMIFS is _not_ case-sensitive.

Generic formula
---------------

    =SUMIFS(sum_range,range,"*red*",range,"*blue*")

Explanation 
------------

In this example, the goal is to sum the numbers in column C when the text in column B contains specific pairs of colors. For example, the formula should sum a number when the text contains both "red" and "blue". Order is not important; the two colors can appear anywhere in the cell. However, both colors must appear in the same cell. This problem can be solved with the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
, which is designed to sum numbers based on multiple criteria.

### SUMIFS function

The SUMIFS function sums cells in a [range](https://exceljet.net/glossary/range)
 that meet one or more conditions, referred to as _criteria_. The syntax for the SUMIFS function depends on the number of conditions needed. Each separate condition will require a _range_ and _criteria_. The generic syntax for SUMIFS looks like this:

    =SUMIFS(sum_range,range1,criteria1) // 1 condition
    =SUMIFS(sum_range,range1,criteria1,range2,criteria2) // 2 conditions

In this case, we need two conditions, one to test for "red", and one to test for "blue". This means both criteria will be applied to the same range, the text in B5:B16. We start with the _sum\_range_, which is the numbers in the range C5:C16:

    =SUMIFS(C5:C16,

Then we add the first range/criteria pair to test for "red":

    =SUMIFS(C5:C16,B5:B16,"*red*",

Note that we surround "red" with an asterisk (\*) on either side. The asterisk (\*) is a [wildcard](https://exceljet.net/glossary/wildcard)
 available in the SUMIFS function, which means "zero or more characters". We use a wildcard in this case to match "red" occurring _anywhere_ in the text. Next, we add a second range/criteria pair to test for "blue" to complete the formula:

    =SUMIFS(C5:C16,B5:B16,"*red*",B5:B16,"*blue*")

Again, we use two asterisks (\*) as wildcards to match "blue" in any location. Notice we are applying two _different criteria_ to the _same range_, B5:B15. This is intentional. The SUMIFS function applies criteria based on AND logic, which means that both conditions must be true for SUMIFS to include a value in the final result. In other words, both "red" and "blue" must exist in the text. Note that SUMIFS is _not_ case-sensitive. Using "\*red\*" for criteria will match "Red", "RED", and "red" in any location.

### Other combinations

The other color combinations in the worksheet shown use the same pattern. To test for "pink" and "purple", and "green" and "blue", the formulas in F6 and F7 are as follows:

    =SUMIFS(C5:C16,B5:B16,"*pink*",B5:B16,"*purple*")
    =SUMIFS(C5:C16,B5:B16,"*green*",B5:B16,"*blue*")

Related formulas
----------------

[![Excel formula: Sum if cells contain either x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_either_x_or_y.png "Excel formula: Sum if cells contain either x or y")](https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y)

### [Sum if cells contain either x or y](https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y)

In this example, the goal is to sum numbers in the range C5:C16 when text in the range B5:B16 contains the substring "red" OR the substring "blue". In other words, if the text in B5:B16 contains either of these two text values in any location, the corresponding number in C5:C16 should be included...

[![Excel formula: Sum if x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_x_or_y.png "Excel formula: Sum if x or y")](https://exceljet.net/formulas/sum-if-x-or-y)

### [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)

In this example, the goal is to sum Total when the corresponding Color is either "Red" or "Blue". For convenience, all data is in an Excel Table named data . This is a tricky problem, because the solution is not obvious. The go-to function for conditional sums is the SUMIFS function . However, when...

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

[![Excel formula: Count cells that contain either x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20either%20x%20or%20y.png "Excel formula: Count cells that contain either x or y")](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

### [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

In this example, the goal is to count cells in the range B5:B15 that contain either "x" or "y", where x and y are both text strings . When you count cells with "OR logic", you need to be careful not to double count. For example, if you are counting cells that contain "blue" or "green", you can't...

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

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum if cells contain either x or y](https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y)
    
*   [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)
    
*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    
*   [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

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