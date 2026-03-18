# VLOOKUP calculate shipping cost - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/vlookup-calculate-shipping-cost

---

[Skip to main content](https://exceljet.net/formulas/vlookup-calculate-shipping-cost#main-content)

[](https://exceljet.net/formulas/vlookup-calculate-shipping-cost#)

*   [Previous](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [Next](https://exceljet.net/formulas/vlookup-case-sensitive)
    

[Lookup](https://exceljet.net/formulas#Lookup)

VLOOKUP calculate shipping cost
===============================

by Dave Bruns · Updated 28 Mar 2023

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[MAX](https://exceljet.net/functions/max-function)

![Excel formula: VLOOKUP calculate shipping cost](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/VLOOKUP_calculate_shipping_cost.png "Excel formula: VLOOKUP calculate shipping cost")

Summary
-------

This example shows how to use the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 to calculate the total shipping cost for an item in one formula, where the cost per kilogram (kg) varies according to weight. This requires an "approximate match" since in most cases the actual weight will not appear in the shipping cost table. The formula in cell C5 is:

    =VLOOKUP(B5,cost_table,2,TRUE)*B5

where **cost\_table** (E5:F9) is a [named range](https://exceljet.net/glossary/named-range)
. In cell C5, the formula returns $14.00, the correct cost to ship an item that weighs 1 kilogram. As the formula is copied down, a cost is returned for each weight in the list.

Generic formula
---------------

    =VLOOKUP(weight,cost_table,column,TRUE)*weight

Explanation 
------------

This example shows how to use the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 to calculate the total shipping cost for an item in one formula, where the cost per kilogram (kg) varies according to weight. This requires an "approximate match" since in most cases the actual weight will not appear in the shipping cost table.  For convenience, the range E5:F9 is [named](https://exceljet.net/glossary/named-range)
 **cost\_table**. This is an "approximate-match" lookup problem because it is not likely that a given weight will be found in the cost table. As a result, the formula needs to match the largest weight in the table that is _less than or equal to the given weight_. Finally, the result of the lookup operation should multiply the cost per kilogram returned by VLOOKUP by the weight in column B to get a final cost.

### VLOOKUP function

VLOOKUP is an Excel function to get data from a table organized _vertically_. Lookup values must appear in the _first column_ of the table provided to VLOOKUP, and the information to retrieve is specified by column number. If you are new to VLOOKUP, see:

*   [How to use VLOOKUP](https://exceljet.net/functions/vlookup-function)
     - overview with examples and video links

### VLOOKUP solution

In the worksheet shown, the formula in cell C5 is:

    =VLOOKUP(B5,cost_table,2,TRUE)*B5

where **cost\_table** (E5:F9) is a [named range](https://exceljet.net/glossary/named-range)
. VLOOKUP requires lookup values to be in the _first_ column of the lookup table. To retrieve the correct cost per kilogram for a given weight, VLOOKUP is configured like this:

*   The _lookup\_value_ comes from cell B5
*   The _table\_array_ is the [named range](https://exceljet.net/glossary/named-range)
     **cost\_table** (E5:F9)
*   The _col\_index\_num_ is 2 since the cost appears in the second column of the table
*   The _range\_lookup_ argument is set to TRUE = approximate match

With a score provided as a lookup value, VLOOKUP will scan the first column of the table. If it finds an exact match, it will return the cost in that row. If VLOOKUP does not find an exact match, it will continue scanning until it finds a value greater than the lookup value, then it will "step back", and return the cost in the previous row. As the formula is copied down column C, the VLOOKUP function looks up each weight in column B and returns the correct cost per kilogram (kg). Finally, the result from VLOOKUP is multiplied by the original weight in column B to get a total shipping cost.

_Notes: (1) In approximate match mode, VLOOKUP assumes the table is sorted by the values in the first column. This means the cost table must be sorted in ascending order by weight. (2) As an alternative, you could add a [helper column](https://exceljet.net/glossary/helper-column)
 that contains only the VLOOKUP part of the formula to calculate the cost per kilogram, then perform the multiplication separately._

### Named range optional

The named range in this example is optional and used for convenience only because it makes the formula easier to read and means that the cost table does not need to be locked when the formula is copied down column C. To avoid using a named range, use an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 like this:

    =VLOOKUP(B5,$E$5:$F$9,2,TRUE)*B5

### VLOOKUP match modes

VLOOKUP has two match modes: exact match and approximate match, controlled by an optional fourth argument called _range\_lookup_. When _range\_lookup_ is omitted, it defaults to TRUE and VLOOKUP performs an approximate match. This means we _could_ leave out the _range\_lookup_ and get the same result with this formula:

    =VLOOKUP(B5,cost_table,2)*B5

However, I recommend that you always provide a value for _range\_lookup_ because it makes you consider the behavior you want. In other words, giving a value for _range\_lookup_ acts as a reminder to you and others of the intended behavior.

_Notes: If the weight is less than the first entry in the table, VLOOKUP will return the #N/A error. In the example shown, we use zero in cell E5 to make sure this does not occur._

### Adding a minimum cost

To modify the formula to return a minimum cost of $15, regardless of weight, you can nest the original formula inside the [MAX function](https://exceljet.net/functions/max-function)
 like so:

    =MAX(VLOOKUP(B5,cost_table,2,TRUE)*B5,15)
    

After the original formula runs and returns a calculated total cost, the MAX function will return whichever is greater - the result of the formula or 15.

Related formulas
----------------

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

[![Excel formula: Get employee information with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_employee_information_with_VLOOKUP.png "Excel formula: Get employee information with VLOOKUP")](https://exceljet.net/formulas/get-employee-information-with-vlookup)

### [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)

The goal is to look up and retrieve employee information in a table that contains unique id values in the first column. The VLOOKUP function is straightforward to use with data in this format, but you can easily use the XLOOKUP function as well. See below for a detailed explanation of both...

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: Merge tables with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20calculated%20column.png "Excel formula: Merge tables with VLOOKUP")](https://exceljet.net/formulas/merge-tables-with-vlookup)

### [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)

This is a standard "exact match" VLOOKUP formula with one exception: the column index is calculated using the COLUMN function. When the COLUMN function is used without any arguments, it returns a number that corresponds to the current column. In this case, the first instance of the formula in...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20for%20approximate%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

### [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

In a lot of cases, you'll use VLOOKUP to find exact matches based on some kind of unique id, but there are many situations where you'll want to use VLOOKUP to find non-exact matches. A classic case is using VLOOKUP to find a commission rate based on a sales number. Let's take a look. Here we have...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Why%20VLOOKUP%20is%20better%20than%20nested%20IFs-thumb.png)](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

### [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

In this video we look at a few reasons why VLOOKUP is a better option than nested IF statements. In our last video, we used nested IF statements to calculate a commission rate based on a sales number. As a quick recap: The first formula is created with nested IF statements normally. The second...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)
    
*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)
    
*   [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)
    

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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