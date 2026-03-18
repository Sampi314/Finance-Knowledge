# Excel RANDARRAY function | Exceljet

**Source:** https://exceljet.net/functions/randarray-function

---

[Skip to main content](https://exceljet.net/functions/randarray-function#main-content)

[](https://exceljet.net/functions/randarray-function#)

*   [Previous](https://exceljet.net/functions/pivotby-function)
    
*   [Next](https://exceljet.net/functions/reduce-function)
    

Excel 2021

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

RANDARRAY Function
==================

by Dave Bruns · Updated 10 May 2024

Related functions 
------------------

[RAND](https://exceljet.net/functions/rand-function)

[RANDBETWEEN](https://exceljet.net/functions/randbetween-function)

![Excel RANDARRAY function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_randarray_function.png "Excel RANDARRAY function")

Summary
-------

The Excel RANDARRAY function generates an array of random numbers between two values. The size or the array is specified by _rows_ and _columns_ arguments. The generated values can be either decimals or whole numbers.

Purpose 
--------

Get array of random numbers

Return value 
-------------

Array of random values

Syntax
------

    =RANDARRAY([rows],[columns],[min],[max],[integer])

*   _rows_ - \[optional\] Row count. Default = 1.
*   _columns_ - \[optional\] Column count. Default = 1.
*   _min_ - \[optional\] Minimum value. Default = 0.
*   _max_ - \[optional\] Maximum value. Default = 1.
*   _integer_ - \[optional\] Whole numbers. Boolean, TRUE or FALSE. Default = FALSE.

Using the RANDARRAY function 
-----------------------------

The RANDARRAY function generates an array of random numbers between two values. The size or the array is determined by _rows_ and _columns_ arguments. By default, RANDARRAY returns an array of random numbers between 0 and 1. However, RANDARRAY will generate whole numbers when the _integer_ argument is set to TRUE. When RANDARRAY returns multiple results in a worksheet, results will [spill](https://exceljet.net/glossary/spill)
 into adjacent cells.

> RANDARRAY is a [volatile function](https://exceljet.net/glossary/volatile-function)
> , and can cause performance issues in large or complex worksheets.

The RANDARRAY function takes five arguments, none of which are required: _rows_, _columns_, _min_, _max_, and _integer_. By default, _rows_, _columns_, and _max_ default to 1, while _min_ defaults to zero and _integer_ defaults to FALSE. Without any arguments, RANDARRAY will return a decimal value between 0 and 1:

    RANDARRAY() // returns number like 0.098419132
    

Use _rows_ and _columns_ to control the number of values returned:

    =RANDARRAY(10,1) //  10 random values in rows
    =RANDARRAY(1,10) //  10 random values in columns
    

Use _min_ and max _to_ set a lower and upper threshold for values. For example, to generate 3 random decimal values in rows between 1 and 5:

    =RANDARRAY(3,1,1,5) // 3 decimal between 1-5
    

Set _integers_ to TRUE to return whole numbers. For example, to generate 3 random whole numbers in rows between 1 and 100:

    =RANDARRAY(3,1,1,100,TRUE) // 3 whole numbers between 1-100
    

### Examples

In the example shown, RANDARRAY is used to generate 50 values in a range of 10 rows by 5 columns. The formula in B4 is:

    =RANDARRAY(10,5)
    

To return a random array of integers, 5 rows by 2 columns,  between 1 and 10, you can use a formula like this:

    =RANDARRAY(5,2,1,10,TRUE)
    

### Random text

To generate a random letter between A-Z you can use the [CHAR function](https://exceljet.net/functions/char-function)
 with RANDARRAY:

    =CHAR(RANDARRAY(1,1,65,90,TRUE))
    

You can also [generate random text strings](https://exceljet.net/formulas/generate-random-text-strings)
 with RANDARRAY.

### Random dates

To generate 5 random dates in the next year, you can use a formula that combines RANDARRAY with the [EDATE](https://exceljet.net/functions/edate-function)
 and [TODAY](https://exceljet.net/functions/today-function)
 functions:

    =RANDARRAY(5,1,TODAY(),EDATE(TODAY(),12),TRUE)
    

RANDARRAY function examples
---------------------------

[![Excel formula: Random numbers without duplicates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20numbers%20without%20duplicates.png "Excel formula: Random numbers without duplicates")](https://exceljet.net/formulas/random-numbers-without-duplicates)

### [Random numbers without duplicates](https://exceljet.net/formulas/random-numbers-without-duplicates)

In this example, the goal is to generate a list of random numbers without duplicates. This involves jumping through a few hoops because although the RANDARRAY function can easily generate a list of random integers, there is no guarantee that the numbers will be unique. In the explanation below, we'...

[![Excel formula: Random sort](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random_sort.png "Excel formula: Random sort")](https://exceljet.net/formulas/random-sort)

### [Random sort](https://exceljet.net/formulas/random-sort)

In this example, the goal is to perform a random sort of the data in B5:B16 with a formula. This can be done with the SORTBY function and the RANDARRAY function . SORTBY function The SORTBY function sorts provided values by one or more "sort by" arrays. The sort by arrays make it possible to sort...

[![Excel formula: Randomly assign data to groups](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/randomly_assign_data_to_groups.png "Excel formula: Randomly assign data to groups")](https://exceljet.net/formulas/randomly-assign-data-to-groups)

### [Randomly assign data to groups](https://exceljet.net/formulas/randomly-assign-data-to-groups)

In this example, the goal is to return a random group ("A", "B", or "C") at each new row. The simplest way to do this is to use the RANDBETWEEN function with the CHOOSE function. In the current version of Excel, it is also possible to generate all random groups in one step with the RANDARRAY...

[![Excel formula: Random number between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20between%20two%20numbers.png "Excel formula: Random number between two numbers")](https://exceljet.net/formulas/random-number-between-two-numbers)

### [Random number between two numbers](https://exceljet.net/formulas/random-number-between-two-numbers)

The Excel RANDBETWEEN function returns a random integer between given numbers. In the example shown, the formula in B5 is: =RANDBETWEEN(1,100) This formula is then copied down from B5 to B11. The result is random numbers between 1-100. RANDBETWEEN is a volatile function that recalculates when a...

[![Excel formula: Randomly assign people to groups](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/randomly_assign_people_to_groups.png "Excel formula: Randomly assign people to groups")](https://exceljet.net/formulas/randomly-assign-people-to-groups)

### [Randomly assign people to groups](https://exceljet.net/formulas/randomly-assign-people-to-groups)

In this example, the goal is to randomly assign the names in column B to three groups of equal size. The group names are "A", "B", and "C", and these values appear in the named range groups (F5:F7). The solution should automatically count the number of groups to assign and attempt to generate the...

[![Excel formula: Generate random text strings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/generate%20random%20strings.png "Excel formula: Generate random text strings")](https://exceljet.net/formulas/generate-random-text-strings)

### [Generate random text strings](https://exceljet.net/formulas/generate-random-text-strings)

The new dynamic array formulas in Excel 365 make it much easier to solve certain tricky problems with formulas. In this example, the goal is to generate a list of random 6-character codes. The randomness is handled by the RANDARRAY function , a new function in Excel 365. RANDARRAY returns 6 random...

[![Excel formula: Random list of names](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random-list-of-names.png "Excel formula: Random list of names")](https://exceljet.net/formulas/random-list-of-names)

### [Random list of names](https://exceljet.net/formulas/random-list-of-names)

In this example, the goal is to create a list of 10 random names from a larger list of 100 names. In other words, we want to select a random subset of names from a larger list. The names to select from are in column B, starting in row 5. The formula should handle any number of names in the input...

RANDARRAY function videos
-------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20generate%20random%20times-PLAY.png)](https://exceljet.net/videos/how-to-generate-random-times)

### [How to generate random times](https://exceljet.net/videos/how-to-generate-random-times)

In this video, we'll look at how to create a list of random times. In this worksheet, let's generate 20 random times between 7:00 AM and 6:00 PM. To do this, we'll use the RANDARRAY function . Now, RANDARRAY can generate both integers and decimal values. For Times, we want decimal values, because...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20perform%20a%20random%20sort-Play_0.png)](https://exceljet.net/videos/how-to-perform-a-random-sort)

### [How to perform a random sort](https://exceljet.net/videos/how-to-perform-a-random-sort)

In this video, we’ll look at how to perform a random sort with the SORTBY function , with help from the RANDARRAY function . In this worksheet, we have the first 10 letters in the alphabet in the range B5:B14. How can we sort this data in random order? One way to do this is to add a helper column...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/New%20dynamic%20array%20functions%20in%20Excel-Play.png)](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

### [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

In this video, we'll quickly review new Dynamic Array functions in Excel. With the introduction of dynamic array formulas, Excel includes 6 brand new functions that directly leverage dynamic array behavior. Each of these functions is covered in more detail later in the course, so this is just a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20generate%20random%20dates-Play_0.png)](https://exceljet.net/videos/how-to-generate-random-dates)

### [How to generate random dates](https://exceljet.net/videos/how-to-generate-random-dates)

In this video, we'll look at how to create a list of random dates. One of the nice things about the RANDARRAY function is that it makes it easy to generate a list of random dates. In this worksheet, let's generate 20 random dates between May 1 and May 30, 2020. Now, to use the RANDARRAY function...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20generate%20random%20text%20values-Play.png)](https://exceljet.net/videos/how-to-generate-random-text-values)

### [How to generate random text values](https://exceljet.net/videos/how-to-generate-random-text-values)

In this video, we'll look at how to create a list of random text values. As we've already seen, the RANDARRAY function can be used to generate random dates and times, which are numeric values. How can we generate random values that aren't numeric? One way is to use this is to use the RANDARRAY...

Related functions
-----------------

[![Excel RAND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rand%20function.png "Excel RAND function")](https://exceljet.net/functions/rand-function)

### [RAND Function](https://exceljet.net/functions/rand-function)

The Excel RAND function returns a random number between 0 and 1. For example, =RAND() will generate a number like 0.422245717. RAND recalculates when a worksheet is opened or changed.

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
    
*   [Randomly assign people to groups](https://exceljet.net/formulas/randomly-assign-people-to-groups)
    
*   [Random numbers without duplicates](https://exceljet.net/formulas/random-numbers-without-duplicates)
    
*   [Generate random text strings](https://exceljet.net/formulas/generate-random-text-strings)
    
*   [Random list of names](https://exceljet.net/formulas/random-list-of-names)
    
*   [Random sort](https://exceljet.net/formulas/random-sort)
    
*   [Randomly assign data to groups](https://exceljet.net/formulas/randomly-assign-data-to-groups)
    

### Videos

*   [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)
    
*   [How to perform a random sort](https://exceljet.net/videos/how-to-perform-a-random-sort)
    
*   [How to generate random dates](https://exceljet.net/videos/how-to-generate-random-dates)
    
*   [How to generate random times](https://exceljet.net/videos/how-to-generate-random-times)
    
*   [How to generate random text values](https://exceljet.net/videos/how-to-generate-random-text-values)
    

### Functions

*   [RAND Function](https://exceljet.net/functions/rand-function)
    
*   [RANDBETWEEN Function](https://exceljet.net/functions/randbetween-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    

### Links

*   [Microsoft RANDARRAY function documentation](https://support.office.com/en-us/article/randarray-function-21261e55-3bec-4885-86a6-8b0a47fd4d33)
    

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