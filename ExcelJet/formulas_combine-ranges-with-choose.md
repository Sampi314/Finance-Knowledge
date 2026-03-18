# Combine ranges with CHOOSE - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/combine-ranges-with-choose

---

[Skip to main content](https://exceljet.net/formulas/combine-ranges-with-choose#main-content)

[](https://exceljet.net/formulas/combine-ranges-with-choose#)

*   [Previous](https://exceljet.net/formulas/automatic-row-numbers)
    
*   [Next](https://exceljet.net/formulas/count-cells-in-range)
    

[Range](https://exceljet.net/formulas#Range)

Combine ranges with CHOOSE
==========================

by Dave Bruns · Updated 14 Jun 2022

Related functions 
------------------

[CHOOSE](https://exceljet.net/functions/choose-function)

![Excel formula: Combine ranges with CHOOSE](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/join%20ranges%20with%20choose.png "Excel formula: Combine ranges with CHOOSE")

Summary
-------

To combine ranges or [arrays](https://exceljet.net/glossary/array)
 horizontally, you can use the [CHOOSE function](https://exceljet.net/functions/choose-function)
 with an array constant. In the example shown, the formula in cell G5 is:

    =CHOOSE({1,2},B5:B16,D5:D16)
    

The result is that the range B5:B16 and range D5:D16 are joined together horizontally into a single range.

Generic formula
---------------

    =CHOOSE({1,2},range1,range2)

Explanation 
------------

In this example, the goal is to join two one-dimensional ranges together horizontally. This can be done with the CHOOSE function and [array constant](https://exceljet.net/glossary/array-constant)
.

### The CHOOSE function

The [CHOOSE function](https://exceljet.net/functions/choose-function)
 is used to select arbitrary values by numeric position. CHOOSE is a flexible function and accepts a list of text values, numbers, cell references, in any combination. For example, if we have the colors "red", "blue", and "green", we can use CHOOSE like this:

    =CHOOSE(1,"red", "blue", "green") // returns "red"
    =CHOOSE(2,"red", "blue", "green") // returns "blue"
    =CHOOSE(3,"red", "blue", "green") // returns "green"
    

If we give CHOOSE an array constant like {1,2}, CHOOSE will return the first and second values in an array at the same time:

    =CHOOSE({1,2}},"red", "blue", "green") // returns {"red","blue"}
    

The result is an array that contains two values and, in the [dynamic array version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, these values [spill](https://exceljet.net/glossary/spill)
 onto the worksheet into the range G5:H16.

### Applications

Traditionally, the use of CHOOSE function to combine ranges is used up in tricky [array formulas](https://exceljet.net/glossary/array-formula)
. The formulas below are good examples:

*   [VLOOKUP case-sensitive](https://exceljet.net/formulas/vlookup-case-sensitive)
    
*   [VLOOKUP multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)
    

In these formulas, the CHOOSE function is used to create a _new_ table (in memory) that can be used by the VLOOKUP function to workaround a difficult problem.

_Note: the forthcoming [HSTACK function](https://exceljet.net/functions/hstack-function)
 will make this use of CHOOSE unnecessary._

Related formulas
----------------

[![Excel formula: Combine ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/combine_ranges.png "Excel formula: Combine ranges")](https://exceljet.net/formulas/combine-ranges)

### [Combine ranges](https://exceljet.net/formulas/combine-ranges)

In this example, the goal is to combine ranges. With the introduction of the VSTACK function and the HSTACK function, this is quite a simple task. To combine ranges vertically, stacking one range on top of another, you can use the VSTACK function like this: =VSTACK(range1,range2) To combine ranges...

Related functions
-----------------

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Combine ranges](https://exceljet.net/formulas/combine-ranges)
    

### Functions

*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    

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