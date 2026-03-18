# Get earliest and latest project dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-earliest-and-latest-project-dates

---

[Skip to main content](https://exceljet.net/formulas/get-earliest-and-latest-project-dates#main-content)

[](https://exceljet.net/formulas/get-earliest-and-latest-project-dates#)

*   [Previous](https://exceljet.net/formulas/get-days-months-and-years-between-dates)
    
*   [Next](https://exceljet.net/formulas/get-first-day-of-month)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get earliest and latest project dates
=====================================

by Dave Bruns · Updated 29 Jul 2022

Related functions 
------------------

[MINIFS](https://exceljet.net/functions/minifs-function)

[MAXIFS](https://exceljet.net/functions/maxifs-function)

[MIN](https://exceljet.net/functions/min-function)

[MAX](https://exceljet.net/functions/max-function)

[IF](https://exceljet.net/functions/if-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6131/download?token=V_ue0xam)
 (15.6 KB)

![Excel formula: Get earliest and latest project dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20earliest%20and%20latest%20project%20dates.png "Excel formula: Get earliest and latest project dates")

Summary
-------

This example shows how to retrieve the earliest and latest dates associated with a project. In the example shown, the formulas in H5 and I5 are:

    =MINIFS(data[Start],data[Project],G5) // earliest
    =MAXIFS(data[End],data[Project],G5) // latest
    

where "data" is an [Excel table](https://exceljet.net/glossary/excel-table)
 as shown, and project names in column G match those in column B.

_Note: MINIFS and MAXIFS are available only in [Excel 365](https://exceljet.net/glossary/excel-365)
 and Excel 2019. In other versions of Excel, you can use a simple array formula, as explained below._

### Introduction

The task here is to find the earliest and latest dates associated with a given project. The earliest dates come from the **Start** column, and latest dates come from the **End** column.

You might be tempted to use a lookup function like [VLOOKUP](https://exceljet.net/functions/vlookup-function)
, [XLOOKUP](https://exceljet.net/functions/xlookup-function)
, or [INDEX and MATCH.](https://exceljet.net/articles/index-and-match)
 However, since each project has more than one entry, and entries may not always be sorted by date, this becomes challenging.

A better approach is to use process of elimination: discard dates for other projects, and work only with the dates that are left.

Explanation 
------------

The [MINIFS function](https://exceljet.net/functions/minifs-function)
 returns the _smallest_ numeric value that meets supplied criteria, and the [MAXIFS function](https://exceljet.net/functions/maxifs-function)
 returns the _largest_ numeric value that meets supplied criteria.

Like COUNTIFS and SUMIFS, these functions use range/criteria "pairs" to apply conditions. For both formulas, we need just one condition: the project name must equal the name in column G:

    data[Project],G5 // condition
    

To get the _earliest_ start date, we use:

    =MINIFS(data[Start],data[Project],G5) // earliest date
    

Here, MINIFS returns the _minimum_ value in the **Start** column where the project is equal to "Omega" (from cell G5). Since [Excel dates are just numbers](https://exceljet.net/glossary/excel-date)
, the minimum date is the same as the earliest date.

To get the _latest_ end date, we use:

    =MAXIFS(data[End],data[Project],G5) // latest date
    

Here, MAXIFS returns the _maximum_ value in the **End** column where the project is equal to "Omega". As above, the maximum value is the same as the latest date.

### Array formula alternative

If you don't have MINIFS and MAXIFS, you can use simple array formulas, based on the [MIN](https://exceljet.net/functions/min-function)
 and [MAX](https://exceljet.net/functions/max-function)
 functions, to get the same result. For the earliest start date:

    {=MIN(IF(data[Project]=G5,data[Start]))}
    

For the latest end date:

    {=MAX(IF(data[Project]=G5,data[End]))}
    

_Note: both formulas are [array formulas](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, in Excel 2019 or earlier. With Excel 365, you can enter the formulas normally, [since array formulas are native](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
._

In both cases, the [IF function](https://exceljet.net/videos/the-if-function)
 is used to "filter" date values like this:

    IF(data[Project]=G5,data[End]) // filter dates by project
    

When G5 is "Omega", IF returns the end date. Otherwise, IF returns FALSE. Since we are testing all project names in the table at the same time, the result is an array of values like this:

    {43936;43983;43990;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

The large serial numbers are Excel dates associated with project Omega. The other values are FALSE, since the project is not Omega. Because MIN and MAX are programmed to ignore the logical values TRUE and FALSE, they only operate on the remaining values. MIN returns the smallest (earliest) date, and MAX returns the largest (latest) date.

Related formulas
----------------

[![Excel formula: Get project start date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20project%20start%20date.png "Excel formula: Get project start date")](https://exceljet.net/formulas/get-project-start-date)

### [Get project start date](https://exceljet.net/formulas/get-project-start-date)

This formula is uses the WORKDAY function, which returns a date in the future or past, based on start date and required work days. WORKDAY automatically excludes weekends, and can also exclude holidays if provided as a range of dates. In the example shown, the project end date is in column C, and...

[![Excel formula: Get project midpoint](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20project%20midpoint2.png "Excel formula: Get project midpoint")](https://exceljet.net/formulas/get-project-midpoint)

### [Get project midpoint](https://exceljet.net/formulas/get-project-midpoint)

The WORKDAY function returns a date in the future or past, based on a start date, workdays, and optional holidays. WORKDAY automatically excludes weekends, and counts only Monday through Friday as workdays. In the example shown, WORKDAY is configured to get a project midpoint date by adding half of...

[![Excel formula: Project complete percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/project%20complete%20percentage_0.png "Excel formula: Project complete percentage")](https://exceljet.net/formulas/project-complete-percentage)

### [Project complete percentage](https://exceljet.net/formulas/project-complete-percentage)

In this example if a task is marked "Done", then it is considered complete. The goal is to calculate the percent complete for the project by showing the ratio of complete tasks to total tasks, expressed as a percentage. The formula in F6 is: =COUNTA(C5:C11)/COUNTA(B5:B11) At the core, this formula...

[![Excel formula: Sum time by week and project](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20time%20by%20week%20and%20project.png "Excel formula: Sum time by week and project")](https://exceljet.net/formulas/sum-time-by-week-and-project)

### [Sum time by week and project](https://exceljet.net/formulas/sum-time-by-week-and-project)

In this example, the sum range is the named range "time", entered as an Excel time in hh:mm format. The first criteria inside SUMIFS includes dates that are greater than or equal to week date in column F: date,">="...

Related functions
-----------------

[![Excel MINIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_minifs.png "Excel MINIFS function")](https://exceljet.net/functions/minifs-function)

### [MINIFS Function](https://exceljet.net/functions/minifs-function)

The Excel MINIFS function returns the smallest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MINIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers,...

[![Excel MAXIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20maxifs%20function.png "Excel MAXIFS function")](https://exceljet.net/functions/maxifs-function)

### [MAXIFS Function](https://exceljet.net/functions/maxifs-function)

The Excel MAXIFS function returns the largest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MAXIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers, and...

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get project start date](https://exceljet.net/formulas/get-project-start-date)
    
*   [Get project midpoint](https://exceljet.net/formulas/get-project-midpoint)
    
*   [Project complete percentage](https://exceljet.net/formulas/project-complete-percentage)
    
*   [Sum time by week and project](https://exceljet.net/formulas/sum-time-by-week-and-project)
    

### Functions

*   [MINIFS Function](https://exceljet.net/functions/minifs-function)
    
*   [MAXIFS Function](https://exceljet.net/functions/maxifs-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

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