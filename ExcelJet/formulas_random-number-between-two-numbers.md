# Random number between two numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/random-number-between-two-numbers

---

[Skip to main content](https://exceljet.net/formulas/random-number-between-two-numbers#main-content)

[](https://exceljet.net/formulas/random-number-between-two-numbers#)

*   [Previous](https://exceljet.net/formulas/random-date-between-two-dates)
    
*   [Next](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)
    

[Random](https://exceljet.net/formulas#Random)

Random number between two numbers
=================================

by Dave Bruns · Updated 19 May 2024

Related functions 
------------------

[RANDBETWEEN](https://exceljet.net/functions/randbetween-function)

[RANDARRAY](https://exceljet.net/functions/randarray-function)

![Excel formula: Random number between two numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/random%20number%20between%20two%20numbers.png "Excel formula: Random number between two numbers")

Summary
-------

To generate a random number between two numbers, you can use the [RANDBETWEEN function](https://exceljet.net/functions/randbetween-function)
. In the example shown, the formula in B5 is:

    =RANDBETWEEN(1,100)
    

As the formula is copied down, it returns a random integer between 1 and 100.

Generic formula
---------------

    =RANDBETWEEN(lower,upper)

Explanation 
------------

The Excel [RANDBETWEEN function](https://exceljet.net/functions/randbetween-function)
 returns a random integer between given numbers.  In the example shown, the formula in B5 is:

    =RANDBETWEEN(1,100)
    

This formula is then copied down from B5 to B11. The result is random numbers between 1-100.

RANDBETWEEN is a [volatile function](https://exceljet.net/glossary/volatile-function)
 that recalculates when a worksheet is opened or changed. This includes any edits to the worksheet, or simply opening the workbook. To prevent random numbers from being recalculated again, you can replace the formulas with the values last calculated:

1.  Select the random numbers
2.  Copy the formulas to the clipboard with Control + C.
3.  Open the [Paste Special](https://exceljet.net/videos/shortcuts-for-paste-special)
     Window and select "Values"
4.  Click OK to replace the formulas with static values.

### Notes

1.  The [RAND function](https://exceljet.net/functions/rand-function)
     can generate random decimal values.
2.  The [RANDARRAY function](https://exceljet.net/functions/randarray-function)
     (new in [Excel 365](https://exceljet.net/glossary/excel-365)
    ) can generate random numeric arrays. 

Related formulas
----------------

[![Excel formula: Random number from fixed set of options](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20from%20fixed%20set%20of%20options.png "Excel formula: Random number from fixed set of options")](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)

### [Random number from fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)

The CHOOSE function does most of the work in this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are providing four...

[![Excel formula: Random date between two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20date%20between%20two%20dates.png "Excel formula: Random date between two dates")](https://exceljet.net/formulas/random-date-between-two-dates)

### [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)

The RANDBETWEEN function takes two numbers, a bottom and top number, and generates a random integer in between. Dates in Excel are serial numbers, so you can use the DATE function to create the lower number and the upper number. RANDBETWEEN then generates a number that falls between these two date...

[![Excel formula: Randomly assign data to groups](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/randomly_assign_data_to_groups.png "Excel formula: Randomly assign data to groups")](https://exceljet.net/formulas/randomly-assign-data-to-groups)

### [Randomly assign data to groups](https://exceljet.net/formulas/randomly-assign-data-to-groups)

In this example, the goal is to return a random group ("A", "B", or "C") at each new row. The simplest way to do this is to use the RANDBETWEEN function with the CHOOSE function. In the current version of Excel, it is also possible to generate all random groups in one step with the RANDARRAY...

[![Excel formula: Random text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20text%20values.png "Excel formula: Random text values")](https://exceljet.net/formulas/random-text-values)

### [Random text values](https://exceljet.net/formulas/random-text-values)

The CHOOSE function provides the framework for this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are using four values:...

[![Excel formula: Random value from list or table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20value%20from%20list%20or%20table.png "Excel formula: Random value from list or table")](https://exceljet.net/formulas/random-value-from-list-or-table)

### [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)

Note: this formula uses the named range "data" (B5:E104) for readability and convenience. If you don't want to use a named range, substitute $B$5:$E$104 instead. To pull a random value out of a list or table, we'll need a random row number. For that, we'll use the RANDBETWEEN function, which...

Related functions
-----------------

[![Excel RANDBETWEEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rand%20function_0.png "Excel RANDBETWEEN function")](https://exceljet.net/functions/randbetween-function)

### [RANDBETWEEN Function](https://exceljet.net/functions/randbetween-function)

The Excel RANDBETWEEN function returns a random integer between two given numbers. RANDBETWEEN recalculates each time a worksheet is opened or changed.

[![Excel RANDARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_randarray_function.png "Excel RANDARRAY function")](https://exceljet.net/functions/randarray-function)

### [RANDARRAY Function](https://exceljet.net/functions/randarray-function)

The Excel RANDARRAY function generates an array of random numbers between two values. The size or the array is specified by _rows_ and _columns_ arguments. The generated values can be either decimals or whole numbers.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20pick%20names%20out%20of%20a%20hat%20with%20Excel.png)](https://exceljet.net/videos/how-to-pick-names-out-of-a-hat-with-excel)

### [How to pick names out of a hat with Excel](https://exceljet.net/videos/how-to-pick-names-out-of-a-hat-with-excel)

Have you ever had to select the winners in a contest? It's easy when you draw names out of a hat, but how would you do it in Excel? In this video we'll show you a simple way to do it using the RAND function . Here's a list of names that represent entries in a contest. Suppose we'd like to pick five...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Random number from fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)
    
*   [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)
    
*   [Randomly assign data to groups](https://exceljet.net/formulas/randomly-assign-data-to-groups)
    
*   [Random text values](https://exceljet.net/formulas/random-text-values)
    
*   [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)
    

### Functions

*   [RANDBETWEEN Function](https://exceljet.net/functions/randbetween-function)
    
*   [RANDARRAY Function](https://exceljet.net/functions/randarray-function)
    

### Videos

*   [How to pick names out of a hat with Excel](https://exceljet.net/videos/how-to-pick-names-out-of-a-hat-with-excel)
    

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