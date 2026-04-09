# VLOOKUP calculate grades - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/vlookup-calculate-grades

---

[Skip to main content](https://exceljet.net/formulas/vlookup-calculate-grades#main-content)

[](https://exceljet.net/formulas/vlookup-calculate-grades#)

*   [Previous](https://exceljet.net/formulas/vlookup-by-date)
    
*   [Next](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)
    

[Lookup](https://exceljet.net/formulas#Lookup)

VLOOKUP calculate grades
========================

by Dave Bruns · Updated 27 Mar 2023

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")

Summary
-------

This example shows how to use the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 to calculate the correct grade for a given score using a table that holds the thresholds for each available grade. This requires an "approximate match" since in most cases the actual score will not exist in the table. The formula in cell D5 is:

    =VLOOKUP(C5,key,2,TRUE)
    

where **key** (F5:G9) is a [named range](https://exceljet.net/glossary/named-range)
. In cell D5, the formula returns "C", the correct grade for a score of 79. As the formula is copied down, a grade is returned for each score in the list.

Generic formula
---------------

    =VLOOKUP(score,key,2,TRUE)
    

Explanation 
------------

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been [named](https://exceljet.net/glossary/named-range)
 **key**. This is a classic "approximate-match" lookup problem because it is not likely that a given score will be found in the lookup table. The desired behavior is to match the largest value in the table that is _less than or equal to the score_. In this way, the table acts to group scores into buckets, where each bucket is a particular grade. 

### VLOOKUP function

VLOOKUP is an Excel function to get data from a table organized _vertically_. Lookup values must appear in the _first column_ of the table provided to VLOOKUP, and the information to retrieve is specified by column number. For a complete introduction to VLOOKUP with many examples and video links see:

*   [How to use VLOOKUP](https://exceljet.net/functions/vlookup-function)
     - overview with examples and video

### VLOOKUP solution

In the worksheet shown, the formula in cell D5 is:

    =VLOOKUP(C5,key,2,TRUE)

VLOOKUP requires lookup values to be in the _first_ column of the lookup table. To retrieve the correct grade for any given score, VLOOKUP is configured like this:

*   The _lookup\_value_ comes from cell C5
*   The _table\_array_ is the [named range](https://exceljet.net/glossary/named-range)
     **key** (F5:G9)
*   The _col\_index\_num_ is 2 since grades are in the second column
*   The _range\_lookup_ argument is set to TRUE = approximate match

In approximate match mode, VLOOKUP assumes the table is sorted by the values in the _first column_. With a score provided as a lookup value, VLOOKUP will scan the first column of the table. If it finds an exact match, it will return the grade in that row. If VLOOKUP does not find an exact match, it will continue scanning until it finds a value greater than the lookup value, then it will "step back", and return the grade in the previous row. As the formula is copied down column D, the VLOOKUP function looks up each score in column C and returns the correct grade in column D

### Named range optional

The named range in this example is optional and used for convenience only because it makes the formula easier to read and means that the tax rate does not need to be locked. To avoid using a named range, use an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 like this:

    =VLOOKUP(C5,$F$5:$G$9,2,TRUE)

### VLOOKUP match modes

VLOOKUP has two match modes: exact match and approximate match, controlled by an optional fourth argument called _range\_lookup_. When _range\_lookup_ is omitted, it defaults to TRUE and VLOOKUP performs an approximate match. This means we _could_ leave out the _range\_lookup_ and get the same result with this formula:

    =VLOOKUP(C5,key,2)

However, I recommend you always provide a value for _range\_lookup_ because it forces you to consider what you want. Providing a value for range\_lookup acts as a reminder to you and others of the intended behavior.

_Notes: (1) If the score is less than the first entry in the table, VLOOKUP will return the #N/A error. In the example shown, we use zero in cell F5 to make sure this does not occur. (2) You can use [INDEX and MATCH to solve this same problem](https://exceljet.net/formulas/index-and-match-approximate-match)
._

Related formulas
----------------

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

[![Excel formula: Self-contained VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/self-contained%20VLOOKUP%20formula2.png "Excel formula: Self-contained VLOOKUP")](https://exceljet.net/formulas/self-contained-vlookup)

### [Self-contained VLOOKUP](https://exceljet.net/formulas/self-contained-vlookup)

The goal in this example is to create a self-contained lookup formula to assign a grade to the score in cell E7, based on the table in B6:C10. However, instead of providing B6:B10 as a reference for the table\_array argument, the table is provided as a constant . Normally, the second argument for...

[![Excel formula: VLOOKUP calculate shipping cost](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_shipping_cost.png "Excel formula: VLOOKUP calculate shipping cost")](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)

### [VLOOKUP calculate shipping cost](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)

This example shows how to use the VLOOKUP function to calculate the total shipping cost for an item in one formula, where the cost per kilogram (kg) varies according to weight. This requires an "approximate match" since in most cases the actual weight will not appear in the shipping cost table. For...

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: Get employee information with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_employee_information_with_VLOOKUP.png "Excel formula: Get employee information with VLOOKUP")](https://exceljet.net/formulas/get-employee-information-with-vlookup)

### [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)

The goal is to look up and retrieve employee information in a table that contains unique id values in the first column. The VLOOKUP function is straightforward to use with data in this format, but you can easily use the XLOOKUP function as well. See below for a detailed explanation of both...

[![Excel formula: Merge tables with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20calculated%20column.png "Excel formula: Merge tables with VLOOKUP")](https://exceljet.net/formulas/merge-tables-with-vlookup)

### [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)

This is a standard "exact match" VLOOKUP formula with one exception: the column index is calculated using the COLUMN function. When the COLUMN function is used without any arguments, it returns a number that corresponds to the current column. In this case, the first instance of the formula in...

[![Excel formula: Score quiz answers with key](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/score%20quiz%20answers%20with%20key.png "Excel formula: Score quiz answers with key")](https://exceljet.net/formulas/score-quiz-answers-with-key)

### [Score quiz answers with key](https://exceljet.net/formulas/score-quiz-answers-with-key)

This formula uses the named range key (C4:G4) for convenience only. Without the named range, you'll want to use an absolute reference so the formula can be copied. In cell I7, we have this formula: =SUM(--(C7:G7=key)) working from the inside-out, this expression is evaluated first: C7:G7=key //...

[![Excel formula: INDEX and MATCH approximate match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_approximate_match.png "Excel formula: INDEX and MATCH approximate match")](https://exceljet.net/formulas/index-and-match-approximate-match)

### [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table to the right. For convenience only, grade (G5:G9) and score (F5:F9) are named ranges . This is a classic "approximate-match" lookup problem because it is unlikely that a...

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

*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    
*   [Self-contained VLOOKUP](https://exceljet.net/formulas/self-contained-vlookup)
    
*   [VLOOKUP calculate shipping cost](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)
    
*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [Score quiz answers with key](https://exceljet.net/formulas/score-quiz-answers-with-key)
    
*   [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)
    
*   [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)
    

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    
*   [Danger: beware VLOOKUP defaults](https://exceljet.net/articles/danger-beware-vlookup-defaults)
    

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