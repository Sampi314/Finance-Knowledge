# Random value from list or table - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/random-value-from-list-or-table

---

[Skip to main content](https://exceljet.net/formulas/random-value-from-list-or-table#main-content)

[](https://exceljet.net/formulas/random-value-from-list-or-table#)

*   [Previous](https://exceljet.net/formulas/random-times-at-specific-intervals)
    
*   [Next](https://exceljet.net/formulas/randomly-assign-data-to-groups)
    

[Random](https://exceljet.net/formulas#Random)

Random value from list or table
===============================

by Dave Bruns · Updated 28 Jun 2019

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[RANDBETWEEN](https://exceljet.net/functions/randbetween-function)

[ROWS](https://exceljet.net/functions/rows-function)

![Excel formula: Random value from list or table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/random%20value%20from%20list%20or%20table.png "Excel formula: Random value from list or table")

Summary
-------

To get a random value from a table or list in Excel, you can use the INDEX function with help from the RANDBETWEEN and ROWS functions.

In the example shown, the formula in G7 is:

    =INDEX(data,RANDBETWEEN(1,ROWS(data)),1)
    

Generic formula
---------------

    =INDEX(data,RANDBETWEEN(1,ROWS(data)),1)

Explanation 
------------

_Note: this formula uses the named range "data" (B5:E104) for readability and convenience. If you don't want to use a named range, substitute $B$5:$E$104 instead._

To pull a random value out of a list or table, we'll need a random row number. For that, we'll use the RANDBETWEEN function, which generates a random integer between two given values - an upper value and lower value.

For the lower value, we use the number 1, and for the upper value we use the ROWS function to get count the total rows in the table or list:

    =RANDBETWEEN(1,ROWS(data))
    

RANDBETWEEN will return a random number between 1 and the count of rows in the data, and this result is fed into the INDEX function for the rows argument. For the columns argument, we simply use 1, since we want a name from the first column.

So, assuming that RANDBETWEEN returns 7 (as in the example) the formula reduces to:

    =INDEX(data,7,1)
    

Which returns the name "Tim Moore", in row 7 of the table.

Note that RANDBETWEEN will recalculate whenever a worksheet is changed or opened.

Related formulas
----------------

[![Excel formula: Random number between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20between%20two%20numbers.png "Excel formula: Random number between two numbers")](https://exceljet.net/formulas/random-number-between-two-numbers)

### [Random number between two numbers](https://exceljet.net/formulas/random-number-between-two-numbers)

The Excel RANDBETWEEN function returns a random integer between given numbers. In the example shown, the formula in B5 is: =RANDBETWEEN(1,100) This formula is then copied down from B5 to B11. The result is random numbers between 1-100. RANDBETWEEN is a volatile function that recalculates when a...

[![Excel formula: Random date between two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20date%20between%20two%20dates.png "Excel formula: Random date between two dates")](https://exceljet.net/formulas/random-date-between-two-dates)

### [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)

The RANDBETWEEN function takes two numbers, a bottom and top number, and generates a random integer in between. Dates in Excel are serial numbers, so you can use the DATE function to create the lower number and the upper number. RANDBETWEEN then generates a number that falls between these two date...

[![Excel formula: Randomly assign data to groups](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/randomly_assign_data_to_groups.png "Excel formula: Randomly assign data to groups")](https://exceljet.net/formulas/randomly-assign-data-to-groups)

### [Randomly assign data to groups](https://exceljet.net/formulas/randomly-assign-data-to-groups)

In this example, the goal is to return a random group ("A", "B", or "C") at each new row. The simplest way to do this is to use the RANDBETWEEN function with the CHOOSE function. In the current version of Excel, it is also possible to generate all random groups in one step with the RANDARRAY...

[![Excel formula: Random text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20text%20values.png "Excel formula: Random text values")](https://exceljet.net/formulas/random-text-values)

### [Random text values](https://exceljet.net/formulas/random-text-values)

The CHOOSE function provides the framework for this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are using four values:...

[![Excel formula: Random number from fixed set of options](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20from%20fixed%20set%20of%20options.png "Excel formula: Random number from fixed set of options")](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)

### [Random number from fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)

The CHOOSE function does most of the work in this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are providing four...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel RANDBETWEEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rand%20function_0.png "Excel RANDBETWEEN function")](https://exceljet.net/functions/randbetween-function)

### [RANDBETWEEN Function](https://exceljet.net/functions/randbetween-function)

The Excel RANDBETWEEN function returns a random integer between two given numbers. RANDBETWEEN recalculates each time a worksheet is opened or changed.

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

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
    
*   [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)
    
*   [Randomly assign data to groups](https://exceljet.net/formulas/randomly-assign-data-to-groups)
    
*   [Random text values](https://exceljet.net/formulas/random-text-values)
    
*   [Random number from fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [RANDBETWEEN Function](https://exceljet.net/functions/randbetween-function)
    
*   [ROWS Function](https://exceljet.net/functions/rows-function)
    

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