# Excel RANDBETWEEN function | Exceljet

**Source:** https://exceljet.net/functions/randbetween-function

---

[Skip to main content](https://exceljet.net/functions/randbetween-function#main-content)

[](https://exceljet.net/functions/randbetween-function#)

*   [Previous](https://exceljet.net/functions/rand-function)
    
*   [Next](https://exceljet.net/functions/roman-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

RANDBETWEEN Function
====================

by Dave Bruns · Updated 12 Feb 2023

Related functions 
------------------

[RAND](https://exceljet.net/functions/rand-function)

[RANDARRAY](https://exceljet.net/functions/randarray-function)

![Excel RANDBETWEEN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20rand%20function_0.png "Excel RANDBETWEEN function")

Summary
-------

The Excel RANDBETWEEN function returns a random integer between two given numbers. RANDBETWEEN recalculates each time a worksheet is opened or changed.

Purpose 
--------

Get a random integer between two values

Return value 
-------------

An integer

Syntax
------

    =RANDBETWEEN(bottom,top)

*   _bottom_ - An integer representing the lower value of the range.
*   _top_ - An integer representing the upper value of the range.

Using the RANDBETWEEN function 
-------------------------------

The RANDBETWEEN function returns a random integer between two numbers. The result from RANDBETWEEN is automatic, and a new random number will be recalculated each time a worksheet is opened or changed.

> RANDBETWEEN is a [volatile function](https://exceljet.net/glossary/volatile-function)
> , and can cause performance issues in large or complex worksheets.

The RANDBETWEEN function takes two [arguments](https://exceljet.net/glossary/function-argument)
: _bottom_ and _top_. _Bottom_ represents the lower bound for a random number, and _top_ represents the upper bound. RANDBETWEEN includes both _top_ and _bottom_ values in the range of integers that may be returned. 

### Examples

Below are basic examples of RANDBETWEEN formulas:

    =RANDBETWEEN(1,9) // random number between 1 and 9
    =RANDBETWEEN(10,100) // random number between 10 and 100
    =RANDBETWEEN(-10,0) // random number between -10 and zero
    

### Multiple results

To generate _multiple_ random numbers in _multiple_ cells, select the target cells, enter the RANDBETWEEN function, and press [control + enter](https://exceljet.net/shortcuts/enter-same-data-in-multiple-cells)
 to enter the same formula in all cells at once.

### Static results

RANDBETWEEN returns a new random value each time the worksheet is recalculated, including changes made to unrelated cells in the same workbook. To stop random numbers from changing, copy the cells that contain RANDBETWEEN to the clipboard, then use [Paste Special > Values](https://exceljet.net/videos/shortcuts-for-paste-special)
 to convert to text. To get a single random number that doesn't change, enter RANDBETWEEN in the [formula bar](https://exceljet.net/glossary/formula-bar)
, press F9 to convert the formula to a static result, and press Enter to enter the value in the cell.

_Note: in [Excel 365](https://exceljet.net/glossary/excel-365)
, the [RANDARRAY function](https://exceljet.net/functions/randarray-function)
 is a more flexible alternative. RANDARRAY can generate random decimal numbers and random integers, and can also return more than one random value at the same time._

### Notes

*   RANDBETWEEN recalculates whenever a worksheet is opened or changed.
*   RANDBETWEEN returns integers. Use the [RAND function](https://exceljet.net/functions/rand-function)
     to return random decimal values.

RANDBETWEEN function examples
-----------------------------

[![Excel formula: Random text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20text%20values.png "Excel formula: Random text values")](https://exceljet.net/formulas/random-text-values)

### [Random text values](https://exceljet.net/formulas/random-text-values)

The CHOOSE function provides the framework for this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are using four values:...

[![Excel formula: Random date between two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20date%20between%20two%20dates.png "Excel formula: Random date between two dates")](https://exceljet.net/formulas/random-date-between-two-dates)

### [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)

The RANDBETWEEN function takes two numbers, a bottom and top number, and generates a random integer in between. Dates in Excel are serial numbers, so you can use the DATE function to create the lower number and the upper number. RANDBETWEEN then generates a number that falls between these two date...

[![Excel formula: Random number between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20between%20two%20numbers.png "Excel formula: Random number between two numbers")](https://exceljet.net/formulas/random-number-between-two-numbers)

### [Random number between two numbers](https://exceljet.net/formulas/random-number-between-two-numbers)

The Excel RANDBETWEEN function returns a random integer between given numbers. In the example shown, the formula in B5 is: =RANDBETWEEN(1,100) This formula is then copied down from B5 to B11. The result is random numbers between 1-100. RANDBETWEEN is a volatile function that recalculates when a...

[![Excel formula: Randomly assign data to groups](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/randomly_assign_data_to_groups.png "Excel formula: Randomly assign data to groups")](https://exceljet.net/formulas/randomly-assign-data-to-groups)

### [Randomly assign data to groups](https://exceljet.net/formulas/randomly-assign-data-to-groups)

In this example, the goal is to return a random group ("A", "B", or "C") at each new row. The simplest way to do this is to use the RANDBETWEEN function with the CHOOSE function. In the current version of Excel, it is also possible to generate all random groups in one step with the RANDARRAY...

[![Excel formula: Random number from fixed set of options](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20from%20fixed%20set%20of%20options.png "Excel formula: Random number from fixed set of options")](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)

### [Random number from fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)

The CHOOSE function does most of the work in this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are providing four...

[![Excel formula: Random value from list or table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20value%20from%20list%20or%20table.png "Excel formula: Random value from list or table")](https://exceljet.net/formulas/random-value-from-list-or-table)

### [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)

Note: this formula uses the named range "data" (B5:E104) for readability and convenience. If you don't want to use a named range, substitute $B$5:$E$104 instead. To pull a random value out of a list or table, we'll need a random row number. For that, we'll use the RANDBETWEEN function, which...

RANDBETWEEN function videos
---------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20generate%20random%20values_Thumb.png)](https://exceljet.net/videos/how-to-generate-random-values)

### [How to generate random values](https://exceljet.net/videos/how-to-generate-random-values)

In this video we'll look at a few ways to generate random values with the RANDBETWEEN function. The RANDBETWEEN function is a simple function you can use to generate random numbers. For example, I can enter RANDBETWEEN with a bottom value of 1 and a top value of 100. When I press Enter, I get a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20convert%20formulas%20to%20values-thumb_1.png)](https://exceljet.net/videos/how-to-convert-formulas-to-values)

### [How to convert formulas to values](https://exceljet.net/videos/how-to-convert-formulas-to-values)

As you start to work with more formulas in Excel, you'll find you often want to replace formulas with the values they generate. One common situation is that your formula has calculated a result, and you want to stop Excel from calculating a new result. Let's take a look. To illustrate converting...

Related functions
-----------------

[![Excel RAND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rand%20function.png "Excel RAND function")](https://exceljet.net/functions/rand-function)

### [RAND Function](https://exceljet.net/functions/rand-function)

The Excel RAND function returns a random number between 0 and 1. For example, =RAND() will generate a number like 0.422245717. RAND recalculates when a worksheet is opened or changed.

[![Excel RANDARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_randarray_function.png "Excel RANDARRAY function")](https://exceljet.net/functions/randarray-function)

### [RANDARRAY Function](https://exceljet.net/functions/randarray-function)

The Excel RANDARRAY function generates an array of random numbers between two values. The size or the array is specified by _rows_ and _columns_ arguments. The generated values can be either decimals or whole numbers.

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
    
*   [Random number from fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)
    
*   [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)
    
*   [Random text values](https://exceljet.net/formulas/random-text-values)
    
*   [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)
    

### Videos

*   [How to convert formulas to values](https://exceljet.net/videos/how-to-convert-formulas-to-values)
    
*   [How to generate random values](https://exceljet.net/videos/how-to-generate-random-values)
    

### Functions

*   [RAND Function](https://exceljet.net/functions/rand-function)
    
*   [RANDARRAY Function](https://exceljet.net/functions/randarray-function)
    

### Links

*   [Microsoft RANDBETWEEN function documentation](https://support.office.com/en-us/article/randbetween-function-4cc7f0d1-87dc-4eb7-987f-a469ab381685)
    

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