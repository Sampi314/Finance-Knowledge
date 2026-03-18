# Random text values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/random-text-values

---

[Skip to main content](https://exceljet.net/formulas/random-text-values#main-content)

[](https://exceljet.net/formulas/random-text-values#)

*   [Previous](https://exceljet.net/formulas/random-number-weighted-probability)
    
*   [Next](https://exceljet.net/formulas/random-times-at-specific-intervals)
    

[Random](https://exceljet.net/formulas#Random)

Random text values
==================

by Dave Bruns · Updated 27 Jun 2018

Related functions 
------------------

[CHOOSE](https://exceljet.net/functions/choose-function)

[RANDBETWEEN](https://exceljet.net/functions/randbetween-function)

![Excel formula: Random text values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/random%20text%20values.png "Excel formula: Random text values")

Summary
-------

To quickly fill a range of cells with random text values, you can use a formula based on the CHOOSE and RANDBETWEEN functions.

In the example shown, the formula in C5 is:

    =CHOOSE(RANDBETWEEN(1,4),"Red","Blue","Green","Pink")
    

Which returns a random color from the values provided.

Generic formula
---------------

    =CHOOSE(RANDBETWEEN(1,3),"Value1","Value2","Value3")

Explanation 
------------

The CHOOSE function provides the framework for this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index.

In this case, we are using four values: Red, Blue, Green, and Pink, so we need to give CHOOSE a number between 1 and 4.

To generate this number, we use RANDBETWEEN, a function that returns a random integer between a bottom and top value. Since we are only working with 4 values in CHOOSE, we supply 1 for the bottom number and 4 for the top number.

When this formula is copied down, it will return one of the four colors.

_Note that RANDBETWEEN will calculate a new value whenever the worksheet is changed. Once you have values in the range, you may want to replace the formulas with values to prevent further changes._

Related formulas
----------------

[![Excel formula: Random number between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20between%20two%20numbers.png "Excel formula: Random number between two numbers")](https://exceljet.net/formulas/random-number-between-two-numbers)

### [Random number between two numbers](https://exceljet.net/formulas/random-number-between-two-numbers)

The Excel RANDBETWEEN function returns a random integer between given numbers. In the example shown, the formula in B5 is: =RANDBETWEEN(1,100) This formula is then copied down from B5 to B11. The result is random numbers between 1-100. RANDBETWEEN is a volatile function that recalculates when a...

[![Excel formula: Random date between two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20date%20between%20two%20dates.png "Excel formula: Random date between two dates")](https://exceljet.net/formulas/random-date-between-two-dates)

### [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)

The RANDBETWEEN function takes two numbers, a bottom and top number, and generates a random integer in between. Dates in Excel are serial numbers, so you can use the DATE function to create the lower number and the upper number. RANDBETWEEN then generates a number that falls between these two date...

[![Excel formula: Random value from list or table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20value%20from%20list%20or%20table.png "Excel formula: Random value from list or table")](https://exceljet.net/formulas/random-value-from-list-or-table)

### [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)

Note: this formula uses the named range "data" (B5:E104) for readability and convenience. If you don't want to use a named range, substitute $B$5:$E$104 instead. To pull a random value out of a list or table, we'll need a random row number. For that, we'll use the RANDBETWEEN function, which...

Related functions
-----------------

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

[![Excel RANDBETWEEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rand%20function_0.png "Excel RANDBETWEEN function")](https://exceljet.net/functions/randbetween-function)

### [RANDBETWEEN Function](https://exceljet.net/functions/randbetween-function)

The Excel RANDBETWEEN function returns a random integer between two given numbers. RANDBETWEEN recalculates each time a worksheet is opened or changed.

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
    
*   [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)
    
*   [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)
    

### Functions

*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    
*   [RANDBETWEEN Function](https://exceljet.net/functions/randbetween-function)
    

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