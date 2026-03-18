# VLOOKUP with multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/vlookup-with-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/vlookup-with-multiple-criteria#main-content)

[](https://exceljet.net/formulas/vlookup-with-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/vlookup-with-2-lookup-tables)
    
*   [Next](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced)
    

[Lookup](https://exceljet.net/formulas#Lookup)

VLOOKUP with multiple criteria
==============================

by Dave Bruns · Updated 10 May 2024

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

![Excel formula: VLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/VLOOKUP%20with%20muliple%20criteria.png "Excel formula: VLOOKUP with multiple criteria")

Summary
-------

The VLOOKUP function does not handle multiple criteria natively. However, if you have control over source data, you can use a [helper column](https://exceljet.net/glossary/helper-column)
 to join multiple fields together, and use these fields like multiple criteria inside VLOOKUP. In the example shown, Column B is a helper column that concatenates first and last names together, and VLOOKUP does the same to build a lookup value. The formula in I6 is:

    =VLOOKUP(I4&I5,data,4,0)
    

where "data" is the [named range](https://exceljet.net/glossary/named-range)
 B4:F104

_Note: This approach is simple, but limited. For a more powerful solution that does not require a helper column, see [this advanced formula based on Boolean logic](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced)
. Also consider a more direct approach based on [INDEX and MATCH](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
 or [XLOOKUP](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
._

Generic formula
---------------

    =VLOOKUP(val1&val2,data,column,0)

Explanation 
------------

In the example shown, we want to look up employee departments and groups using VLOOKUP by matching the first and last name of an employee.

One limitation of VLOOKUP is that it only handles one condition: the lookup\_value, which is matched against the _first column_ in the table. This makes it difficult to use VLOOKUP to find a value using multiple criteria. However, if you have control over the source data, you can add a helper column that concatenates 2 or more fields together, and then give VLOOKUP a lookup value that does the same.

The helper column joins field values from columns that are used as criteria, and it must be the first column of the table. Inside the VLOOKUP function, the lookup value itself is also created by joining the same criteria.

In the example shown, the formula in I6 is:

    =VLOOKUP(I4&I5,data,4,0)
    

Once I4 and I5 are joined, we have:

    =VLOOKUP("JonVictor",data,4,0)
    

VLOOKUP locates "JonVictor" on the 5th row in "data", and returns the value in the 4th column, "Marketing".

### Setting things up

To set up a multiple criteria VLOOKUP, follow these 3 steps:

1.  Add a helper column and concatenate (join) values from the columns you want to use for your criteria.
2.  Set up VLOOKUP to refer to a table that includes the helper column. The helper column must be the first column in the table.
3.  For the lookup value, join the same values in the same order to match the values in the helper column.
4.  Make sure VLOOKUP is set to perform an exact match.

Related formulas
----------------

[![Excel formula: VLOOKUP with multiple criteria advanced](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20multiple%20criteria%20advanced.png "Excel formula: VLOOKUP with multiple criteria advanced")](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced)

### [VLOOKUP with multiple criteria advanced](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced)

In this example, the goal is to use VLOOKUP to retrieve the price for a given item based on three criteria: name, size, and color, which are entered in H5:H7. For example, for a Blue Medium T-shirt, VLOOKUP should return $16.00. The VLOOKUP function does not handle multiple criteria natively...

[![Excel formula: INDEX and MATCH with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX%20and%20MATCH%20with%20multiple%20criteria.png "Excel formula: INDEX and MATCH with multiple criteria")](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

### [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

This is a more advanced formula. For basics, see How to use INDEX and MATCH . Normally, an INDEX MATCH formula is configured with MATCH set to look through a one-column range and provide a match based on given criteria. Without concatenating values in a helper column , or in the formula itself,...

[![Excel formula: VLOOKUP with 2 lookup tables](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20two%20lookup%20tables.png "Excel formula: VLOOKUP with 2 lookup tables")](https://exceljet.net/formulas/vlookup-with-2-lookup-tables)

### [VLOOKUP with 2 lookup tables](https://exceljet.net/formulas/vlookup-with-2-lookup-tables)

Working from the inside out, the IF function in this formula, which is entered as the "table\_array" argument in VLOOKUP, runs a logical test on the value in column C "Years", which represents the number of years a salesperson has been with a company. If C5 is less than 2, then table1 is returned as...

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

Related videos
--------------

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

*   [VLOOKUP with multiple criteria advanced](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced)
    
*   [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
    
*   [VLOOKUP with 2 lookup tables](https://exceljet.net/formulas/vlookup-with-2-lookup-tables)
    
*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    

### Videos

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