# Excel RAND function | Exceljet

**Source:** https://exceljet.net/functions/rand-function

---

[Skip to main content](https://exceljet.net/functions/rand-function#main-content)

[](https://exceljet.net/functions/rand-function#)

*   [Previous](https://exceljet.net/functions/quotient-function)
    
*   [Next](https://exceljet.net/functions/randbetween-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

RAND Function
=============

by Dave Bruns · Updated 12 Feb 2023

Related functions 
------------------

[RANDBETWEEN](https://exceljet.net/functions/randbetween-function)

[RANDARRAY](https://exceljet.net/functions/randarray-function)

![Excel RAND function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20rand%20function.png "Excel RAND function")

Summary
-------

The Excel RAND function returns a random number between 0 and 1. For example, =RAND() will generate a number like 0.422245717. RAND recalculates when a worksheet is opened or changed.

Purpose 
--------

Get a random number between 0 and 1

Return value 
-------------

A number between 1 and 0

Syntax
------

    =RAND()

Using the RAND function 
------------------------

The RAND function returns a random decimal number between 0 and 1. For example, =RAND() will generate a number like 0.422245717. The RAND function takes no [arguments](https://exceljet.net/glossary/function-argument)
. RAND recalculates when a worksheet is opened or changed.

> RAND is a [volatile function](https://exceljet.net/glossary/volatile-function)
> , and can cause performance issues in large or complex worksheets.

### Examples

RAND takes no arguments:

    =RAND() // returns number like 0.073979356
    =RAND() // returns number like 0.080313118
    

### Automatic recalculation

The RAND function will calculate a new result each time a worksheet is edited. To stop random numbers from being updated, copy the cells that contain RAND to the clipboard, then use [Paste Special > Values](https://exceljet.net/videos/shortcuts-for-paste-special)
 to convert to a static result.

To get a single random number that doesn't change when the worksheet is calculated, enter =RAND() in the formulas bar and then press F9 to convert the formula into its result.

### Multiple random numbers

To generate a set of random numbers in multiple cells, select the cells, enter =RAND() and press [control + enter.](https://exceljet.net/shortcuts/enter-same-data-in-multiple-cells)
 

### Random number between

To generate a random number between a and b, you can use a formula like this:

    RAND()*(b-a)+a
    

For example, to generate a random number between 1 and 9:

    RAND()*(9-1)+1
    

The [RANDBETWEEN function](https://exceljet.net/functions/randbetween-function)
 can generate random integers between to numbers:

    =RANDBETWEEN(1,9) // random number between 1-9
    

_Note: In [Excel 365](https://exceljet.net/glossary/excel-365)
, the [RANDARRAY function](https://exceljet.net/functions/randarray-function)
 is another way to generate multiple random numbers, and to generate random numbers between two values._

### Notes

*   The RAND function takes no arguments.
*   RAND recalculates whenever a worksheet is opened or changed.

RAND function examples
----------------------

[![Excel formula: Randomly assign people to groups](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/randomly_assign_people_to_groups.png "Excel formula: Randomly assign people to groups")](https://exceljet.net/formulas/randomly-assign-people-to-groups)

### [Randomly assign people to groups](https://exceljet.net/formulas/randomly-assign-people-to-groups)

In this example, the goal is to randomly assign the names in column B to three groups of equal size. The group names are "A", "B", and "C", and these values appear in the named range groups (F5:F7). The solution should automatically count the number of groups to assign and attempt to generate the...

[![Excel formula: Random times at specific intervals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20times%20at%20specific%20intervals.png "Excel formula: Random times at specific intervals")](https://exceljet.net/formulas/random-times-at-specific-intervals)

### [Random times at specific intervals](https://exceljet.net/formulas/random-times-at-specific-intervals)

The RAND function generates a decimal number between zero and 1. So, you might get output like this from RAND() in three cells: 0.54739314 0.919767722 0.633760119 Dates in Excel are defined as simple numbers, where 1 = 1 day. This means you can simply divide 1 by the decimal value of time to get a...

[![Excel formula: Random number weighted probability](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Random%20number%20weighted%20probability.png "Excel formula: Random number weighted probability")](https://exceljet.net/formulas/random-number-weighted-probability)

### [Random number weighted probability](https://exceljet.net/formulas/random-number-weighted-probability)

This formula relies on the helper table visible in the range B4:D10. Column B contains the six numbers we want as a final result. Column C contains the probability weight assigned to each number, entered as a percentage. Column D contains the cumulative probability, created with this formula in D5...

RAND function videos
--------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20generate%20random%20values_Thumb.png)](https://exceljet.net/videos/how-to-generate-random-values)

### [How to generate random values](https://exceljet.net/videos/how-to-generate-random-values)

In this video we'll look at a few ways to generate random values with the RANDBETWEEN function. The RANDBETWEEN function is a simple function you can use to generate random numbers. For example, I can enter RANDBETWEEN with a bottom value of 1 and a top value of 100. When I press Enter, I get a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20pick%20names%20out%20of%20a%20hat%20with%20Excel.png)](https://exceljet.net/videos/how-to-pick-names-out-of-a-hat-with-excel)

### [How to pick names out of a hat with Excel](https://exceljet.net/videos/how-to-pick-names-out-of-a-hat-with-excel)

Have you ever had to select the winners in a contest? It's easy when you draw names out of a hat, but how would you do it in Excel? In this video we'll show you a simple way to do it using the RAND function . Here's a list of names that represent entries in a contest. Suppose we'd like to pick five...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20perform%20a%20random%20sort-Play_0.png)](https://exceljet.net/videos/how-to-perform-a-random-sort)

### [How to perform a random sort](https://exceljet.net/videos/how-to-perform-a-random-sort)

In this video, we’ll look at how to perform a random sort with the SORTBY function , with help from the RANDARRAY function . In this worksheet, we have the first 10 letters in the alphabet in the range B5:B14. How can we sort this data in random order? One way to do this is to add a helper column...

Related functions
-----------------

[![Excel RANDBETWEEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rand%20function_0.png "Excel RANDBETWEEN function")](https://exceljet.net/functions/randbetween-function)

### [RANDBETWEEN Function](https://exceljet.net/functions/randbetween-function)

The Excel RANDBETWEEN function returns a random integer between two given numbers. RANDBETWEEN recalculates each time a worksheet is opened or changed.

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

*   [Random times at specific intervals](https://exceljet.net/formulas/random-times-at-specific-intervals)
    
*   [Random number weighted probability](https://exceljet.net/formulas/random-number-weighted-probability)
    
*   [Randomly assign people to groups](https://exceljet.net/formulas/randomly-assign-people-to-groups)
    

### Videos

*   [How to pick names out of a hat with Excel](https://exceljet.net/videos/how-to-pick-names-out-of-a-hat-with-excel)
    
*   [How to generate random values](https://exceljet.net/videos/how-to-generate-random-values)
    
*   [How to perform a random sort](https://exceljet.net/videos/how-to-perform-a-random-sort)
    

### Functions

*   [RANDBETWEEN Function](https://exceljet.net/functions/randbetween-function)
    
*   [RANDARRAY Function](https://exceljet.net/functions/randarray-function)
    

### Links

*   [Microsoft RAND function documentation](https://support.office.com/en-us/article/rand-function-4cbfa695-8869-4788-8d90-021ea9f5be73)
    

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