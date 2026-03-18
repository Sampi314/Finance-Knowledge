# Random number weighted probability - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/random-number-weighted-probability

---

[Skip to main content](https://exceljet.net/formulas/random-number-weighted-probability#main-content)

[](https://exceljet.net/formulas/random-number-weighted-probability#)

*   [Previous](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)
    
*   [Next](https://exceljet.net/formulas/random-text-values)
    

[Random](https://exceljet.net/formulas#Random)

Random number weighted probability
==================================

by Dave Bruns · Updated 27 Jun 2018

Related functions 
------------------

[RAND](https://exceljet.net/functions/rand-function)

[MATCH](https://exceljet.net/functions/match-function)

[INDEX](https://exceljet.net/functions/index-function)

![Excel formula: Random number weighted probability](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Random%20number%20weighted%20probability.png "Excel formula: Random number weighted probability")

Summary
-------

To generated a random number, weighted with a given probability, you can use a helper table together with a formula based on the RAND and MATCH functions.

In the example shown, the formula in F5 is:

    =MATCH(RAND(),D$5:D$10)
    

Generic formula
---------------

    =MATCH(RAND(),cumulative_probability)

Explanation 
------------

This formula relies on the helper table visible in the range B4:D10. Column B contains the six numbers we want as a final result. Column C contains the probability weight assigned to each number, entered as a percentage. Column D contains the cumulative probability, created with this formula in D5, copied down:

    =SUM(D4,C4)
    

Notice, we are intentionally shifting the cumulative probability down one row, so that the value in D5 is zero. This is to make sure MATCH is able to find a position for all values down to zero as explained below.

To generate a random value, using the weighted probability in the helper table, F5 contains this formula, copied down:

    =MATCH(RAND(),D$5:D$10)
    

Inside MATCH, the lookup value is provided by the RAND function. RAND generates a random value between zero and 1. The lookup array is the range D5:D10, [locked](https://exceljet.net/glossary/absolute-reference)
 so it won't change as the formula is copied down the column.

The third argument for MATCH, match type, is omitted. When match type is omitted, MATCH will return the position of the largest value less than or equal to the lookup value\*. In practical terms, this means the MATCH function travels along the values in D5:D10 until a larger value is encountered, then "steps back" to the previous position. When MATCH encounters a value larger than the largest last value in D5:D10 (.7 in the example), it returns the last position (6 in the example). As mentioned above, the first value in D5:D10 is deliberately zero to ensure that values below .1 are "caught" by the lookup table and return a position of 1.

_\*Values in the lookup range must be sorted in ascending order._

### Random weighted text value

To return a random weighted text value (i.e. a non-numeric value), you can enter text values in the range B5:B10, then add INDEX to return a value in that range, based on the position returned by MATCH:

    =INDEX($B$5:$B$10,MATCH(RAND(),D$5:D$10))
    

### Notes

1.  I ran into this approach in a [forum post on mrexcel.com](http://www.mrexcel.com/forum/excel-questions/513950-weighted-randbetween.html)
    
2.  RAND is a [volatile function](https://exceljet.net/glossary/volatile-function)
     and will recalculate with every worksheet change
3.  Once you have random value(s), use paste special > values to replace the formula if needed

Related formulas
----------------

[![Excel formula: Random number between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20between%20two%20numbers.png "Excel formula: Random number between two numbers")](https://exceljet.net/formulas/random-number-between-two-numbers)

### [Random number between two numbers](https://exceljet.net/formulas/random-number-between-two-numbers)

The Excel RANDBETWEEN function returns a random integer between given numbers. In the example shown, the formula in B5 is: =RANDBETWEEN(1,100) This formula is then copied down from B5 to B11. The result is random numbers between 1-100. RANDBETWEEN is a volatile function that recalculates when a...

[![Excel formula: Randomly assign data to groups](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/randomly_assign_data_to_groups.png "Excel formula: Randomly assign data to groups")](https://exceljet.net/formulas/randomly-assign-data-to-groups)

### [Randomly assign data to groups](https://exceljet.net/formulas/randomly-assign-data-to-groups)

In this example, the goal is to return a random group ("A", "B", or "C") at each new row. The simplest way to do this is to use the RANDBETWEEN function with the CHOOSE function. In the current version of Excel, it is also possible to generate all random groups in one step with the RANDARRAY...

[![Excel formula: Random value from list or table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20value%20from%20list%20or%20table.png "Excel formula: Random value from list or table")](https://exceljet.net/formulas/random-value-from-list-or-table)

### [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)

Note: this formula uses the named range "data" (B5:E104) for readability and convenience. If you don't want to use a named range, substitute $B$5:$E$104 instead. To pull a random value out of a list or table, we'll need a random row number. For that, we'll use the RANDBETWEEN function, which...

Related functions
-----------------

[![Excel RAND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rand%20function.png "Excel RAND function")](https://exceljet.net/functions/rand-function)

### [RAND Function](https://exceljet.net/functions/rand-function)

The Excel RAND function returns a random number between 0 and 1. For example, =RAND() will generate a number like 0.422245717. RAND recalculates when a worksheet is opened or changed.

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Random number between two numbers](https://exceljet.net/formulas/random-number-between-two-numbers)
    
*   [Randomly assign data to groups](https://exceljet.net/formulas/randomly-assign-data-to-groups)
    
*   [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)
    

### Functions

*   [RAND Function](https://exceljet.net/functions/rand-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

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