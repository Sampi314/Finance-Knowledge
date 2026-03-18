# Due date by category - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/due-date-by-category

---

[Skip to main content](https://exceljet.net/formulas/due-date-by-category#main-content)

[](https://exceljet.net/formulas/due-date-by-category#)

*   [Previous](https://exceljet.net/formulas/display-the-current-date-and-time)
    
*   [Next](https://exceljet.net/formulas/dynamic-calendar-formula)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Due date by category
====================

by Dave Bruns · Updated 25 Sep 2022

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[WORKDAY](https://exceljet.net/functions/workday-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6952/download?token=h6Muk3DC)
 (15.71 KB)

![Excel formula: Due date by category](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/due%20date%20by%20category.png "Excel formula: Due date by category")

Summary
-------

To calculate a due date based on category, where the category determines the due date, you can use a formula based on the [VLOOKUP function.](https://exceljet.net/functions/vlookup-function)
 In the example shown, the formula in E5 is:

    =D5+VLOOKUP(C5,categories,2,0)
    

Where **categories** is the [named range](https://exceljet.net/glossary/named-range)
 G5:H7, the result is a due date in column E that is based on the category assigned in column C. This kind of formula can be used to set due dates, shipping dates, and other end dates where a group or category determines how much time is allotted.

Generic formula
---------------

    =A1+VLOOKUP(category,table,column,0)

Explanation 
------------

In this example, the goal is to create a due date based on category, where each category has a different number of days allocated to complete a given task, issue, project, etc. The amount of time available to resolve each category is shown in column H, and **categories** is the [named range](https://exceljet.net/glossary/named-range)
 G5:H7. The named range is for convenience and readability only. You can also use the [absolute reference](https://exceljet.net/glossary/absolute-reference)
 $G$5:$H$7.

### Calculating days

The first task in this problem is to calculate the number of days to use for each category, as shown in the range G5:H7. One way to do it is to start adding IF statements like this:

    =IF(C5="A",1,IF(C5="B",3,IF(C5="C",7)))
    

This approach is called "[nested ifs](https://exceljet.net/articles/nested-ifs)
". However, note how this tangles up the formula with the category data. If the days per category changes, the formula will need to be edited. If more categories are added, more [IF functions](https://exceljet.net/videos/the-if-function)
 will need to be added. This is not an ideal way to solve the problem.

A better approach is to use the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 to retrieve the number of days for a given category directly from G5:H7, which is [named](https://exceljet.net/glossary/named-range)
 "categories" for convenience only. We can use VLOOKUP like this:

    =VLOOKUP("A",categories,2,0) // returns 1
    =VLOOKUP("B",categories,2,0) // returns 3
    =VLOOKUP("C",categories,2,0) // returns 7
    

In the above formulas, the _lookup\_value_ is temporarily hardcoded as "A", "B", or "C". The _table\_array_ is provided as **categories**, which is the named range G5:H7 and _column\_index\_num_ is 2, since we want days from the second column in. Finally, we use zero (0) for the _range\_lookup_ [argument](https://exceljet.net/glossary/function-argument)
 to force an exact match. To use this formula in the worksheet shown, we need to change _lookup\_value_ to C5:

    =VLOOKUP(C5,categories,2,0)
    

Now, VLOOKUP will use the category shown in column C to retrieve the correct number of days from G5:H7. If the number of days for a category is changed, or if additional categories are added to the named range **categories**, the VLOOKUP will continue to return the correct result.

So far, so good. At this point, we have a number we can use for days, but we don't have a due date.

### Creating a due date

The next task is to create the actual due date using the date given in column D. This is a simple problem, because [dates in Excel are just serial numbers](https://exceljet.net/glossary/excel-date)
 and can be added together like other numbers. To complete the formula, we only need to start with the date in D5, and add the VLOOKUP formula we created above:

    =D5+VLOOKUP(C5,categories,2,0)
    

This formula gets the date from D5, retrieves the correct number of days for the category in C5 with VLOOKUP, and adds the two values together. The result in E5 is 16-Sep-2021, since we start with 15-Sep-2021 and add 1 day for category "A".

### With XLOOKUP

For this problem, VLOOKUP works fine. However, you can also use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 if you prefer like this:

    =D5+XLOOKUP(C5,$G$5:$G$7,$H$5:$H$7)
    

Here we use [absolute references](https://exceljet.net/glossary/absolute-reference)
 since we can't use the [named range](https://exceljet.net/glossary/named-range)
 categories directly for _lookup\_array_ and _return\_array_. However, we can also get fancy and use the [INDEX function](https://exceljet.net/functions/index-function)
 with the named range like this:

    =D5+XLOOKUP(C5,INDEX(categories,0,1),INDEX(categories,0,2))
    

Here we use zero for the _row\_num_ in INDEX, which causes INDEX to return the entire column.

Note: using an [Excel Table](https://exceljet.net/articles/excel-tables)
 instead of a named range for G5:H7 would be a good approach for XLOOKUP or VLOOKUP.

### Workdays only

To create a due date based on workdays only you can alter the formula like this:

    =WORKDAY(D5,VLOOKUP(C5,categories,2,0))
    

In this version, the [WORKDAY function](https://exceljet.net/functions/workday-function)
 returns the final due date. The start date is the same and comes from column D. The VLOOKUP function is the same and returns days as before. The difference is that both values are returned directly to the WORKDAY function: D5 becomes the start\_date and the result from VLOOKUP becomes the _days_ argument.

WORKDAY uses the start date and _days_ to create a date in the future, automatically ignoring Saturday and Sunday. WORKDAY can also ignore holidays as well, if they are provided as a range with valid dates. See the [WORKDAY](https://exceljet.net/functions/workday-function)
 page for more information. If you need to customize the days treated as weekends, you can replace the WORKDAY function with the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
, which offers more control over non-working days.

### With hours

If you are using [datetimes](https://exceljet.net/glossary/excel-datetime)
 (i.e. date + time), you can adjust the **categories** table to show [Excel hours](https://exceljet.net/glossary/excel-time)
 (i.e. 8:00, 12:00, etc.) and use the same formula to determine a due date measured in hours. This works, because hours in Excel are [fractional parts of 1 day](https://exceljet.net/glossary/excel-time)
. You will also need to change the [number format](https://exceljet.net/glossary/number-format)
 used in column E to show date and time.

Related formulas
----------------

[![Excel formula: Calculate days open](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20days%20open.png "Excel formula: Calculate days open")](https://exceljet.net/formulas/calculate-days-open)

### [Calculate days open](https://exceljet.net/formulas/calculate-days-open)

In this example, the goal is to calculate the number of days a ticket/case/issue has been open. We start counting on the date a ticket was opened and stop counting on the date a ticket was closed. If there is no closed date, the ticket is still open. Because dates in Excel are just serial numbers...

[![Excel formula: Conditional formatting date past due](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20formatting%20date%20past%20due.png "Excel formula: Conditional formatting date past due")](https://exceljet.net/formulas/conditional-formatting-date-past-due)

### [Conditional formatting date past due](https://exceljet.net/formulas/conditional-formatting-date-past-due)

In this example, we want to apply three different colors, depending on how much the original date varies from the current date: Green if the variance is less than 3 days Yellow if the variance is between 3 and 10 days Red if the variance is greater than 10 days For each rule, we calculate a...

[![Excel formula: Get days, months, and years between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20months%20and%20years%20between%20dates.png "Excel formula: Get days, months, and years between dates")](https://exceljet.net/formulas/get-days-months-and-years-between-dates)

### [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)

In this example, the goal is to output the time between a start date and an end date as a text string that lists years, months, and days separately. For example, given a start date of 1-Jan-2018 and an end date of 1-Jul-2018, the result should be a string like this: "1 years, 6 months, 0 days"...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel WORKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday%20function.png "Excel WORKDAY function")](https://exceljet.net/functions/workday-function)

### [WORKDAY Function](https://exceljet.net/functions/workday-function)

The Excel WORKDAY function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. You can use the WORKDAY function to calculate things like start dates, delivery dates, and completion dates...

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Why%20VLOOKUP%20is%20better%20than%20nested%20IFs-thumb.png)](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

### [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

In this video we look at a few reasons why VLOOKUP is a better option than nested IF statements. In our last video, we used nested IF statements to calculate a commission rate based on a sales number. As a quick recap: The first formula is created with nested IF statements normally. The second...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)

### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)

In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Calculate days open](https://exceljet.net/formulas/calculate-days-open)
    
*   [Conditional formatting date past due](https://exceljet.net/formulas/conditional-formatting-date-past-due)
    
*   [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [WORKDAY Function](https://exceljet.net/functions/workday-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    

### Videos

*   [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)
    
*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    

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