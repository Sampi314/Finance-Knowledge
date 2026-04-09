# Randomly assign data to groups - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/randomly-assign-data-to-groups

---

[Skip to main content](https://exceljet.net/formulas/randomly-assign-data-to-groups#main-content)

[](https://exceljet.net/formulas/randomly-assign-data-to-groups#)

*   [Previous](https://exceljet.net/formulas/random-value-from-list-or-table)
    
*   [Next](https://exceljet.net/formulas/randomly-assign-people-to-groups)
    

[Random](https://exceljet.net/formulas#Random)

Randomly assign data to groups
==============================

by Dave Bruns · Updated 4 Apr 2024

Related functions 
------------------

[RANDBETWEEN](https://exceljet.net/functions/randbetween-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

[RANDARRAY](https://exceljet.net/functions/randarray-function)

[ROWS](https://exceljet.net/functions/rows-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8258/download?token=6yJGMtq1)
 (25.11 KB)

![Excel formula: Randomly assign data to groups](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/randomly_assign_data_to_groups.png "Excel formula: Randomly assign data to groups")

Summary
-------

To randomly assign rows of data to arbitrary groups, you can use the [RANDBETWEEN function](https://exceljet.net/functions/randbetween-function)
 with the [CHOOSE function](https://exceljet.net/functions/choose-function)
. In the example shown, the formula in F5 is:

    =CHOOSE(RANDBETWEEN(1,3),"A","B","C")
    

As the formula is copied down the column, it will return a random group ("A", "B", or "C") at each new row.

_Note: this approach will create groups of different sizes. If you need to assign random groups with a fixed size, see [this formula](https://exceljet.net/formulas/randomly-assign-people-to-groups)
._

Generic formula
---------------

    =CHOOSE(RANDBETWEEN(1,3),"A","B","C")

Explanation 
------------

In this example, the goal is to return a random group ("A", "B", or "C") at each new row. The simplest way to do this is to use the RANDBETWEEN function with the CHOOSE function. In the current version of Excel, it is also possible to generate all random groups in one step with the RANDARRAY function. Both approaches are explained below.

### The CHOOSE function

The [CHOOSE function](https://exceljet.net/functions/choose-function)
 returns a value from a list of values using an index number. The index number is provided as the first argument, and the values to be selected follow. For example, if we have a list of three colors ("red", "blue", and "green"), we can configure CHOOSE to return each color in turn with the following formulas:

    CHOOSE(1,"red","blue","green") // returns "red"
    CHOOSE(2,"red","blue","green") // returns "blue"
    CHOOSE(3,"red","blue","green") // returns "green"

Notice that CHOOSE uses the index number to select the "nth" value from the list of values. The values can be customized in any way you like and the only requirement is that the index number be valid for the number of values provided. Of course, in this example, we don't want to _hardcode_ an index number into CHOOSE, we want a random index number. For this, we can use the RANDBETWEEN function.

### The RANDBETWEEN function

The [RANDBETWEEN function](https://exceljet.net/functions/randbetween-function)
 generates a random number between two integers, provided as the _bottom_ and the _top_. For example, to generate a random number between 1 and 10, you can use RANDBETWEEN like this:

    =RANDBETWEEN(1,10) // returns a random number between 1 and 10

When Excel's calculation engine updates a worksheet, RANDBETWEEN will generate a random number between 1 and 10.

### CHOOSE with RANDBETWEEN

The behavior of RANDBETWEEN will work perfectly for this problem. We have three possible groups ("A","B","C") so we need a random number between 1 and 3, which we can get like this:

    =RANDBETWEEN(1,3) // returns a random number between 1 and 3

The final step is to embed RANDBETWEEN into the CHOOSE function as the index number like this:

    =CHOOSE(RANDBETWEEN(1,3),"A","B","C")

This is the formula that appears in cell F5 in the example shown. When the formula is copied down the column, RANDBETWEEN returns a random number between 1 and 3. This number is delivered directly to the CHOOSE function as the index number, and CHOOSE returns the corresponding color as a final result. You can use this approach whenever you need to assign random text values to each row in a data set. Just be sure to adjust the second argument in RANDBETWEEN, _top_, to match the number of values provided.

### Stopping automatic recalculation

Be aware that RANDBETWEEN is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and will recalculate whenever there is _any change_ to a workbook, or even when a workbook is opened. To force a recalculation, you can press the F9 key. Once you have a set of random assignments, you may want to stop the formula from returning new results. The classic way to do this is to use Paste Special:

1.  Select all cells that contain the CHOOSE and RANDBETWEEN formula.
2.  Copy to the clipboard with Control + C.
3.  Open the Paste Special window with the [shortcut](https://exceljet.net/shortcuts)
     Control + Alt + V.
4.  Select "Values" and click OK:

![Select Values in the Paste Special window](https://exceljet.net/sites/default/files/images/formulas/inline/randomly_assign_data_to_groups_paste_special_window.png "Select Values in the Paste Special window")

After you press OK, all formulas will be replaced with static values.

### Dynamic array formula

In the current version of Excel (Excel 2021 or later) you can use a single [dynamic array](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 formula to generate all random values at once. One option is to use the [RANDARRAY function](https://exceljet.net/functions/randarray-function)
 with CHOOSE like this:

    =CHOOSE(RANDARRAY(ROWS(B5:B104),,1,3,TRUE),"A","B","C")

The core idea of this formula is the same as the original formula above. However, instead of RANDBETWEEN, we use RANDARRAY, which can generate an _array_ of random numbers in one step. To figure out how many random numbers to generate, we use the [ROWS function](https://exceljet.net/functions/rows-function)
 on a range corresponding to the first column of the data. This saves us the step of telling RANDARRAY how many rows we need. In this case, ROWS returns 100, because there are 100 rows in the range B5:B104. Simplifying, we now have:

    =CHOOSE(RANDARRAY(100,,1,3,TRUE),"A","B","C")

Next, RANDARRAY generates an array of 100 random numbers between 1 and 3. The result is returned to CHOOSE as the _index\_num_ argument, and CHOOSE uses the random numbers to return an array that contains 100 random groups. This array lands in cell F5 and [spills](https://exceljet.net/glossary/spill)
 into the range F5:F104.

> RANDARRAY is a volatile function and will recalculate with each worksheet change.

### INDEX alternative

It is also possible to use the [INDEX function](https://exceljet.net/functions/index-function)
 instead of CHOOSE in a formula like this:

    =INDEX({"A","B","C"},RANDBETWEEN(1,3))

Like CHOOSE, INDEX retrieves a value based on an index number. INDEX however accepts the values all at once in the first argument, called _array_. In the formula above, the values "A", "B", and "C" are provided as an [array constant](https://exceljet.net/glossary/array-constant)
 to INDEX as the _array_, and RANDBETWEEN is used as before to generate a random number between 1 and 3.  The RANDARRAY version of the formula with INDEX looks like this:

    =INDEX({"A","B","C"},RANDARRAY(ROWS(B5:B104),,1,3,TRUE))

One advantage of INDEX is that the array constant can be replaced with a range on the worksheet. In other words, you can enter group names into a range and provide that range to INDEX. The CHOOSE function will not accept a range of values; it requires that values be provided separately.

_Note: the formulas on this page will create completely random groups. One result is that the total number of rows assigned to each group will vary. If you need to assign random groups with a fixed size (i.e. randomly assign people to teams of 6), see the example on [this page](https://exceljet.net/formulas/randomly-assign-people-to-groups)
._

Related formulas
----------------

[![Excel formula: Randomly assign people to groups](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/randomly_assign_people_to_groups.png "Excel formula: Randomly assign people to groups")](https://exceljet.net/formulas/randomly-assign-people-to-groups)

### [Randomly assign people to groups](https://exceljet.net/formulas/randomly-assign-people-to-groups)

In this example, the goal is to randomly assign the names in column B to three groups of equal size. The group names are "A", "B", and "C", and these values appear in the named range groups (F5:F7). The solution should automatically count the number of groups to assign and attempt to generate the...

[![Excel formula: Random number between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20between%20two%20numbers.png "Excel formula: Random number between two numbers")](https://exceljet.net/formulas/random-number-between-two-numbers)

### [Random number between two numbers](https://exceljet.net/formulas/random-number-between-two-numbers)

The Excel RANDBETWEEN function returns a random integer between given numbers. In the example shown, the formula in B5 is: =RANDBETWEEN(1,100) This formula is then copied down from B5 to B11. The result is random numbers between 1-100. RANDBETWEEN is a volatile function that recalculates when a...

[![Excel formula: Random date between two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20date%20between%20two%20dates.png "Excel formula: Random date between two dates")](https://exceljet.net/formulas/random-date-between-two-dates)

### [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)

The RANDBETWEEN function takes two numbers, a bottom and top number, and generates a random integer in between. Dates in Excel are serial numbers, so you can use the DATE function to create the lower number and the upper number. RANDBETWEEN then generates a number that falls between these two date...

[![Excel formula: Random text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20text%20values.png "Excel formula: Random text values")](https://exceljet.net/formulas/random-text-values)

### [Random text values](https://exceljet.net/formulas/random-text-values)

The CHOOSE function provides the framework for this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are using four values:...

[![Excel formula: Random value from list or table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20value%20from%20list%20or%20table.png "Excel formula: Random value from list or table")](https://exceljet.net/formulas/random-value-from-list-or-table)

### [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)

Note: this formula uses the named range "data" (B5:E104) for readability and convenience. If you don't want to use a named range, substitute $B$5:$E$104 instead. To pull a random value out of a list or table, we'll need a random row number. For that, we'll use the RANDBETWEEN function, which...

[![Excel formula: Random number from fixed set of options](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20from%20fixed%20set%20of%20options.png "Excel formula: Random number from fixed set of options")](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)

### [Random number from fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)

The CHOOSE function does most of the work in this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are providing four...

Related functions
-----------------

[![Excel RANDBETWEEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rand%20function_0.png "Excel RANDBETWEEN function")](https://exceljet.net/functions/randbetween-function)

### [RANDBETWEEN Function](https://exceljet.net/functions/randbetween-function)

The Excel RANDBETWEEN function returns a random integer between two given numbers. RANDBETWEEN recalculates each time a worksheet is opened or changed.

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

[![Excel RANDARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_randarray_function.png "Excel RANDARRAY function")](https://exceljet.net/functions/randarray-function)

### [RANDARRAY Function](https://exceljet.net/functions/randarray-function)

The Excel RANDARRAY function generates an array of random numbers between two values. The size or the array is specified by _rows_ and _columns_ arguments. The generated values can be either decimals or whole numbers.

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20pick%20names%20out%20of%20a%20hat%20with%20Excel.png)](https://exceljet.net/videos/how-to-pick-names-out-of-a-hat-with-excel)

### [How to pick names out of a hat with Excel](https://exceljet.net/videos/how-to-pick-names-out-of-a-hat-with-excel)

Have you ever had to select the winners in a contest? It's easy when you draw names out of a hat, but how would you do it in Excel? In this video we'll show you a simple way to do it using the RAND function . Here's a list of names that represent entries in a contest. Suppose we'd like to pick five...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20randomly%20assign%20people%20to%20teams-Play.png)](https://exceljet.net/videos/how-to-randomly-assign-people-to-teams)

### [How to randomly assign people to teams](https://exceljet.net/videos/how-to-randomly-assign-people-to-teams)

In this video, we'll look at a way to use basic formulas to randomly assign people to teams. Here we have a list of 36 people. Let's say we want to randomly assign each person to a team of 4 people so that we have a total of 9 teams with 4 people in each. I'm going to solve this problem in small...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Randomly assign people to groups](https://exceljet.net/formulas/randomly-assign-people-to-groups)
    
*   [Random number between two numbers](https://exceljet.net/formulas/random-number-between-two-numbers)
    
*   [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)
    
*   [Random text values](https://exceljet.net/formulas/random-text-values)
    
*   [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)
    
*   [Random number from fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)
    

### Functions

*   [RANDBETWEEN Function](https://exceljet.net/functions/randbetween-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    
*   [RANDARRAY Function](https://exceljet.net/functions/randarray-function)
    
*   [ROWS Function](https://exceljet.net/functions/rows-function)
    

### Videos

*   [How to pick names out of a hat with Excel](https://exceljet.net/videos/how-to-pick-names-out-of-a-hat-with-excel)
    
*   [How to randomly assign people to teams](https://exceljet.net/videos/how-to-randomly-assign-people-to-teams)
    

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