# Random date between two dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/random-date-between-two-dates

---

[Skip to main content](https://exceljet.net/formulas/random-date-between-two-dates#main-content)

[](https://exceljet.net/formulas/random-date-between-two-dates#)

*   [Previous](https://exceljet.net/formulas/project-complete-percentage)
    
*   [Next](https://exceljet.net/formulas/random-number-between-two-numbers)
    

[Random](https://exceljet.net/formulas#Random)

Random date between two dates
=============================

by Dave Bruns · Updated 19 May 2024

Related functions 
------------------

[RANDBETWEEN](https://exceljet.net/functions/randbetween-function)

[WORKDAY](https://exceljet.net/functions/workday-function)

![Excel formula: Random date between two dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/random%20date%20between%20two%20dates.png "Excel formula: Random date between two dates")

Summary
-------

To generate random dates between two dates, you can use the [RANDBETWEEN function](https://exceljet.net/functions/randbetween-function)
, together with the [DATE function](https://exceljet.net/functions/date-function)
. In the example shown, the formula in B5 is:

    =RANDBETWEEN(DATE(2016,1,1),DATE(2016,12,31))
    

This formula is then copied down from B5 to B11. The result is random dates between Jan 1, 2016 and Dec 31, 2016 (random dates in the year 2016).

Generic formula
---------------

    =RANDBETWEEN(date1,date2)

Explanation 
------------

The RANDBETWEEN function takes two numbers, a bottom and top number, and generates a random integer in between. Dates in Excel are serial numbers, so you can use the DATE function to create the lower number and the upper number. RANDBETWEEN then generates a number that falls between these two date values.

Notes:

1.  The result of this formula must be formatted as a date to display correctly.
2.  The RANDBETWEEN function is [volatile](https://exceljet.net/glossary/volatile-function)
     and will generate new numbers whenever a change occurs on the worksheet. That includes any edits to the worksheet, or simply _opening_ the workbook.
3.  To prevent random numbers from being calculated again, copy the formulas, then use Paste Special > Values to replace the formulas with their calculated values.

### Random workdays

To generate random workdays, you can add the WORKDAY function like this:

    =WORKDAY(RANDBETWEEN(date1,date2)-1,1)
    

The WORKDAY function ensures that the date returned is a work day and not a weekend or holiday. Note that WORKDAY will shift dates that fall on weekends or holidays to the _next_ working day, so you may see dates that extend beyond date2.

Related formulas
----------------

[![Excel formula: Random number between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20between%20two%20numbers.png "Excel formula: Random number between two numbers")](https://exceljet.net/formulas/random-number-between-two-numbers)

### [Random number between two numbers](https://exceljet.net/formulas/random-number-between-two-numbers)

The Excel RANDBETWEEN function returns a random integer between given numbers. In the example shown, the formula in B5 is: =RANDBETWEEN(1,100) This formula is then copied down from B5 to B11. The result is random numbers between 1-100. RANDBETWEEN is a volatile function that recalculates when a...

[![Excel formula: Random text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20text%20values.png "Excel formula: Random text values")](https://exceljet.net/formulas/random-text-values)

### [Random text values](https://exceljet.net/formulas/random-text-values)

The CHOOSE function provides the framework for this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are using four values:...

[![Excel formula: Random value from list or table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20value%20from%20list%20or%20table.png "Excel formula: Random value from list or table")](https://exceljet.net/formulas/random-value-from-list-or-table)

### [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)

Note: this formula uses the named range "data" (B5:E104) for readability and convenience. If you don't want to use a named range, substitute $B$5:$E$104 instead. To pull a random value out of a list or table, we'll need a random row number. For that, we'll use the RANDBETWEEN function, which...

[![Excel formula: Random number from fixed set of options](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20from%20fixed%20set%20of%20options.png "Excel formula: Random number from fixed set of options")](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)

### [Random number from fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)

The CHOOSE function does most of the work in this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are providing four...

[![Excel formula: Random date between two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20date%20between%20two%20dates.png "Excel formula: Random date between two dates")](https://exceljet.net/formulas/random-date-between-two-dates)

### [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)

The RANDBETWEEN function takes two numbers, a bottom and top number, and generates a random integer in between. Dates in Excel are serial numbers, so you can use the DATE function to create the lower number and the upper number. RANDBETWEEN then generates a number that falls between these two date...

Related functions
-----------------

[![Excel RANDBETWEEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rand%20function_0.png "Excel RANDBETWEEN function")](https://exceljet.net/functions/randbetween-function)

### [RANDBETWEEN Function](https://exceljet.net/functions/randbetween-function)

The Excel RANDBETWEEN function returns a random integer between two given numbers. RANDBETWEEN recalculates each time a worksheet is opened or changed.

[![Excel WORKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday%20function.png "Excel WORKDAY function")](https://exceljet.net/functions/workday-function)

### [WORKDAY Function](https://exceljet.net/functions/workday-function)

The Excel WORKDAY function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. You can use the WORKDAY function to calculate things like start dates, delivery dates, and completion dates...

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

*   [Random number between two numbers](https://exceljet.net/formulas/random-number-between-two-numbers)
    
*   [Random text values](https://exceljet.net/formulas/random-text-values)
    
*   [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)
    
*   [Random number from fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)
    
*   [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)
    

### Functions

*   [RANDBETWEEN Function](https://exceljet.net/functions/randbetween-function)
    
*   [WORKDAY Function](https://exceljet.net/functions/workday-function)
    

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