# Random times at specific intervals - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/random-times-at-specific-intervals

---

[Skip to main content](https://exceljet.net/formulas/random-times-at-specific-intervals#main-content)

[](https://exceljet.net/formulas/random-times-at-specific-intervals#)

*   [Previous](https://exceljet.net/formulas/random-text-values)
    
*   [Next](https://exceljet.net/formulas/random-value-from-list-or-table)
    

[Random](https://exceljet.net/formulas#Random)

Random times at specific intervals
==================================

by Dave Bruns · Updated 16 Nov 2021

Related functions 
------------------

[RAND](https://exceljet.net/functions/rand-function)

![Excel formula: Random times at specific intervals](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/random%20times%20at%20specific%20intervals.png "Excel formula: Random times at specific intervals")

Summary
-------

To generate random times in at specific intervals you can use the RAND function with the FLOOR function. In the example shown, the formula in B6 is:

    =FLOOR(RAND(),"0:15")
    

which generates a random time at a 15-minute interval.

Generic formula
---------------

    =FLOOR(RAND(),"0:15")

Explanation 
------------

The RAND function generates a decimal number between zero and 1. So, you might get output like this from RAND() in three cells:

0.54739314  
0.919767722  
0.633760119

Dates in Excel are defined as simple numbers, where 1 = 1 day. This means you can simply divide 1 by the decimal value of time to get a value that corresponds to time as Excel sees it, for example:

1/12 = 12 hours = .5 days  
1/6 = 6 hours = .25 days  
1/8 = 8 hours = .333 days

This means we can use RAND() to generate a decimal value between 1 and 0, then round that number down with FLOOR to the nearest interval. FLOOR takes an argument called _significance_ as the rounding multiple, and it recognizes time intervals expressed like this:

"0:10" - 10 minutes  
"0:15" - 15 minutes  
"0:30" - 30 minutes  
"0:45" - 45 minutes

### Setting and upper and lower time

If you want to limit the hours used by RAND, you can use this general formula force RAND to output a number between an upper and lower value:

    =RAND()*(upper-lower)+lower
    

Because Excel can recognize time values, you can get times between 8 AM and 12 PM, with a formula like this:

    =RAND()*("12:00"-"8:00")+"8:00"
    

_Note: the formula above is general and will work with other numbers too, not just times._

Related formulas
----------------

[![Excel formula: Random number between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20between%20two%20numbers.png "Excel formula: Random number between two numbers")](https://exceljet.net/formulas/random-number-between-two-numbers)

### [Random number between two numbers](https://exceljet.net/formulas/random-number-between-two-numbers)

The Excel RANDBETWEEN function returns a random integer between given numbers. In the example shown, the formula in B5 is: =RANDBETWEEN(1,100) This formula is then copied down from B5 to B11. The result is random numbers between 1-100. RANDBETWEEN is a volatile function that recalculates when a...

[![Excel formula: Random date between two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20date%20between%20two%20dates.png "Excel formula: Random date between two dates")](https://exceljet.net/formulas/random-date-between-two-dates)

### [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)

The RANDBETWEEN function takes two numbers, a bottom and top number, and generates a random integer in between. Dates in Excel are serial numbers, so you can use the DATE function to create the lower number and the upper number. RANDBETWEEN then generates a number that falls between these two date...

[![Excel formula: Random text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20text%20values.png "Excel formula: Random text values")](https://exceljet.net/formulas/random-text-values)

### [Random text values](https://exceljet.net/formulas/random-text-values)

The CHOOSE function provides the framework for this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are using four values:...

Related functions
-----------------

[![Excel RAND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rand%20function.png "Excel RAND function")](https://exceljet.net/functions/rand-function)

### [RAND Function](https://exceljet.net/functions/rand-function)

The Excel RAND function returns a random number between 0 and 1. For example, =RAND() will generate a number like 0.422245717. RAND recalculates when a worksheet is opened or changed.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20generate%20random%20values_Thumb.png)](https://exceljet.net/videos/how-to-generate-random-values)

### [How to generate random values](https://exceljet.net/videos/how-to-generate-random-values)

In this video we'll look at a few ways to generate random values with the RANDBETWEEN function. The RANDBETWEEN function is a simple function you can use to generate random numbers. For example, I can enter RANDBETWEEN with a bottom value of 1 and a top value of 100. When I press Enter, I get a...

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
    
*   [Random text values](https://exceljet.net/formulas/random-text-values)
    

### Functions

*   [RAND Function](https://exceljet.net/functions/rand-function)
    

### Videos

*   [How to generate random values](https://exceljet.net/videos/how-to-generate-random-values)
    

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