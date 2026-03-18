# Group times into unequal buckets - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/group-times-into-unequal-buckets

---

[Skip to main content](https://exceljet.net/formulas/group-times-into-unequal-buckets#main-content)

[](https://exceljet.net/formulas/group-times-into-unequal-buckets#)

*   [Previous](https://exceljet.net/formulas/group-times-into-3-hour-buckets)
    
*   [Next](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)
    

[Grouping](https://exceljet.net/formulas#Grouping)

Group times into unequal buckets
================================

by Dave Bruns · Updated 22 Sep 2020

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

![Excel formula: Group times into unequal buckets](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/group%20times%20into%20unequal%20buckets.png "Excel formula: Group times into unequal buckets")

Summary
-------

To group times into buckets that are _unequal_ (i.e. 12 AM-7 AM, 7 AM-12 PM, etc.) you can use  the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
. In the example shown, the formula n E5 is:

    =VLOOKUP(D5,buckets,2,1)
    

Generic formula
---------------

    =VLOOKUP(time,bucket_table,column,TRUE)

Explanation 
------------

If you need to group times into buckets that are not the same size (i.e. 12 AM-7 AM, 7 AM-12 PM, etc.) you can use the VLOOKUP function in approximate match mode.

### The problem

There are several ways to group times in Excel. If you just need to group times by the hour, a pivot table is very quick and easy. If you need to group times into other _equal_ buckets of multiple hours (i.e. 3 hours, 4 hours, etc.) a nice solution is to [use the FLOOR function](https://exceljet.net/formulas/group-times-into-3-hour-buckets)
. However, if you need to group times into _unequal_ buckets, you need to take a more custom approach. VLOOKUP, in its approximate match mode, allows you to group times into custom intervals of any size.

### The solution

The solution is to build a lookup table that "maps" each time into the right bucket. In the first column, enter the start time for the bucket. In column two, enter the name of the bucket you want to use. The table must be sorted by the start time, smallest to largest. Finally, configure the VLOOKUP function to look up each time in the bucket table with approximate match.

In the example shown, the formula n E5 is:

    =VLOOKUP(D5,buckets,2,1)
    

D5 is the lookup value, "buckets" is a named range for G5:H8, 2 is the column index, and 1 is a flag that enables approximate match. (You can also use TRUE). See [this page](https://exceljet.net/functions/vlookup-function)
 for a full explanation.

When VLOOKUP is in approximate match mode, it matches the nearest value that is _less than or equal to the lookup value_. In this way, you can think of the incoming lookup time as being "rounded down" into the right bucket.

This formula is a great example of how you can use VLOOKUP to group data in completely custom ways. I learned it from Jon Acampora, over at Excel Campus, in his article on [three ways to group times](http://www.excelcampus.com/charts/group-times-in-excel)
.

Related formulas
----------------

[![Excel formula: Group times into 3 hour buckets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/group%20times%20into%203%20hour%20buckets.png "Excel formula: Group times into 3 hour buckets")](https://exceljet.net/formulas/group-times-into-3-hour-buckets)

### [Group times into 3 hour buckets](https://exceljet.net/formulas/group-times-into-3-hour-buckets)

If you need to group times into buckets (i.e. group by 6 hours, group by 3 hours, etc.) you can do so with a rounding function called FLOOR. In the example shown, we have a number of transactions, each with a timestamp. Let's say you want to group these transactions into buckets of 3 hours like...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20for%20approximate%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

### [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

In a lot of cases, you'll use VLOOKUP to find exact matches based on some kind of unique id, but there are many situations where you'll want to use VLOOKUP to find non-exact matches. A classic case is using VLOOKUP to find a commission rate based on a sales number. Let's take a look. Here we have...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Group times into 3 hour buckets](https://exceljet.net/formulas/group-times-into-3-hour-buckets)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    

### Videos

*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)
    

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