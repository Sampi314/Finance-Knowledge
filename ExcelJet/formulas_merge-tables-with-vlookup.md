# Merge tables with VLOOKUP - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/merge-tables-with-vlookup

---

[Skip to main content](https://exceljet.net/formulas/merge-tables-with-vlookup#main-content)

[](https://exceljet.net/formulas/merge-tables-with-vlookup#)

*   [Previous](https://exceljet.net/formulas/max-if-criteria-match)
    
*   [Next](https://exceljet.net/formulas/multi-criteria-lookup-and-transpose)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Merge tables with VLOOKUP
=========================

by Dave Bruns · Updated 23 Oct 2023

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

![Excel formula: Merge tables with VLOOKUP](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/VLOOKUP%20with%20calculated%20column.png "Excel formula: Merge tables with VLOOKUP")

Summary
-------

To merge tables, you can use the VLOOKUP function to lookup and retrieve data from one table to the other. To use VLOOKUP this way, both tables must share a common id or key.

This article explains how join tables using VLOOKUP and a calculated column index. This is one way to use the same basic formula to retrieve data across more than one column.

In the example shown, we are using VLOOKUP to pull Name and State into the invoice data table. The VLOOKUP formula used for both is identical:

    =VLOOKUP($C5,$H$5:$J$8,COLUMN()-3,0)
    

Generic formula
---------------

    =VLOOKUP($A1,table,COLUMN()-x,0)

Explanation 
------------

This is a standard "exact match" VLOOKUP formula with one exception: the column index is calculated using the COLUMN function. When the COLUMN function is used without any arguments, it returns a number that corresponds to the current column.

In this case, the first instance of the formula in column E returns 5, since column E is the 5th column in the worksheet. We don't actually want to retrieve data from the 5th column of the customer table (there are only 3 columns total) so we need to subtract 3 from 5 to get the number 2, which is used to retrieve Name from customer data:

    COLUMN()-3 = 2 // column E
    

When the formula is copied across to column F, the same formula yields the number 3:

    COLUMN()-3 = 3 // column F
    

As a result, the first instance gets Name from the customer table (column 2), and the 2nd instance gets State from the customer table (column 3).

You can use this same approach to write one VLOOKUP formula that you can copy across many columns to retrieve values from consecutive columns in another table.

### With two-way match

Another way to calculate a column index for VLOOKUP is to do a [two-way VLOOKUP using the MATCH function](https://exceljet.net/formulas/vlookup-two-way-lookup)
. With this approach, the MATCH function is used to figure out the column index needed for a given column in the second table.

Related formulas
----------------

[![Excel formula: Join tables with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join%20tables%20with%20INDEX%20and%20MATCH%202.png "Excel formula: Join tables with INDEX and MATCH")](https://exceljet.net/formulas/join-tables-with-index-and-match)

### [Join tables with INDEX and MATCH](https://exceljet.net/formulas/join-tables-with-index-and-match)

This formula pulls the customer name and state from the customer table into the order table. The MATCH function is used to locate the right customer and the INDEX function is used to retrieve the data. Retrieving customer name Working from the inside out, the MATCH function is used to get a row...

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

[![Excel formula: Get employee information with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_employee_information_with_VLOOKUP.png "Excel formula: Get employee information with VLOOKUP")](https://exceljet.net/formulas/get-employee-information-with-vlookup)

### [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)

The goal is to look up and retrieve employee information in a table that contains unique id values in the first column. The VLOOKUP function is straightforward to use with data in this format, but you can easily use the XLOOKUP function as well. See below for a detailed explanation of both...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20to%20merge%20tables-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-to-merge-tables)

### [How to use VLOOKUP to merge tables](https://exceljet.net/videos/how-to-use-vlookup-to-merge-tables)

In this video I'll demonstrate how you can use VLOOKUP to join data in separate tables. In this worksheet we have two tables. In the first table, we have order data. You can see that we've got a date, customer id, product, and total. In a second sheet we have customer data. We've got first and last...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20replace%20nested%20IFs%20with%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

### [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

You might build or inherit a worksheet that uses a series of nested IF statements to assign values of some kind. Many people use nested IF statements this way because the approach is easy once you get the hang of it. But nested IF statements can be difficult to maintain and debug. Let's look at how...

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

*   [Join tables with INDEX and MATCH](https://exceljet.net/formulas/join-tables-with-index-and-match)
    
*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    

### Videos

*   [How to use VLOOKUP to merge tables](https://exceljet.net/videos/how-to-use-vlookup-to-merge-tables)
    
*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    
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