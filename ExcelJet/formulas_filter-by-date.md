# Filter by date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-by-date

---

[Skip to main content](https://exceljet.net/formulas/filter-by-date#main-content)

[](https://exceljet.net/formulas/filter-by-date#)

*   [Previous](https://exceljet.net/formulas/filter-by-column-sort-by-row)
    
*   [Next](https://exceljet.net/formulas/filter-case-sensitive)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Filter by date
==============

by Dave Bruns · Updated 27 Jan 2026

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[MONTH](https://exceljet.net/functions/month-function)

[YEAR](https://exceljet.net/functions/year-function)

[DATE](https://exceljet.net/functions/date-function)

![Excel formula: Filter by date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter_by_date.png "Excel formula: Filter by date")

Summary
-------

To filter data to include data based on dates, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 with one or more of Excel's date functions. In the example shown, we are filtering by month with the [MONTH function](https://exceljet.net/functions/month-function)
. The formula in E5 is:

    =FILTER(B5:C16,MONTH(B5:B16)=11,"No data")
    

The result returned by FILTER includes only rows where the date falls in November. See below for other filter-by-date examples.

Generic formula
---------------

    =FILTER(range,MONTH(dates)=n,"No data")

Explanation 
------------

This example shows how to filter dates using Excel's FILTER function. Several common date-based filtering patterns are shown below, including filtering by month, filtering by a specific date, and filtering by month and year.

### Filter by month

In the worksheet below, the goal is to filter the data to include only rows where the date falls in November. The formula in cell E5 is:

    =FILTER(B5:C16,MONTH(B5:B16)=11,"No data")
    

Note that the month is hardcoded as the number 11. The result returned by FILTER includes only rows where the date falls in November:

![FILTER by MONTH example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/filter_by_date_by_month.png "FILTER by MONTH example")

This formula relies on the [FILTER function](https://exceljet.net/functions/filter-function)
 to retrieve data based on a logical test created with the [MONTH function](https://exceljet.net/functions/month-function)
. The _array_ argument is B5:C16, which contains the full set of data without headers. The _include_ argument is constructed with the MONTH function:

    MONTH(B5:B16)=11
    

Here, MONTH receives the range B5:B16. Since the range contains 12 cells, MONTH returns an [array](https://exceljet.net/glossary/array)
 with 12 results representing each date's month number:

    {10;10;10;10;11;11;11;11;12;12;12;12}
    

Each result is then compared to 11 (November), and this operation creates an array of 12 TRUE and FALSE values, which is delivered to the FILTER function as the _include_ argument:

    {FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE}
    

FILTER uses this array to select specific rows. Only rows where the result is TRUE make it into the final output. The _if\_empty_ argument is set to "No data" in case no matching data is found.

### Filter by specific date

To filter by a specific date, use the [DATE function](https://exceljet.net/functions/date-function)
 to construct the date value for comparison. You can see how this works in the worksheet below, where the formula in E5 is:

    =FILTER(B5:C16,B5:B16=DATE(2026,11,24),"No data")
    

![FILTER by specific DATE example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/filter_by_date_specific_date.png "FILTER by specific DATE example")

The DATE function creates a proper [Excel date](https://exceljet.net/glossary/excel-date)
 from the year (2026), month (11), and day (24). This is compared against each date in the range B5:B16. Only the row matching November 24, 2026 is returned.

### Filter by month and year

To filter by both month and year, you can construct a formula using [boolean logic](https://exceljet.net/glossary/boolean-logic)
 that combines the [YEAR function](https://exceljet.net/functions/year-function)
 and [MONTH function](https://exceljet.net/functions/month-function)
:

    =FILTER(B5:C16,(YEAR(B5:B16)=2026)*(MONTH(B5:B16)=12),"No results")
    

![FILTER by specific MONTH and YEAR example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/filter_by_date_by_month_and_year.png "FILTER by specific MONTH and YEAR example")

The multiplication operator (\*) acts as an AND condition—both the year must equal 2026 and the month must equal 12 (December) for a row to be included. This returns all four December 2026 dates from the source data.

Although the values for month and year are hardcoded in this example (the year is 2026 and the month is 12), these values can easily be replaced with cell references to make the formula more flexible.

### Summary

The FILTER function can extract data by date in different ways using Excel's date functions:

*   Use MONTH, YEAR, DAY, or WEEKDAY to extract date components
*   Compare extracted values to target values to create a Boolean array
*   Combine multiple criteria with multiplication (AND logic)
*   Use cell references instead of hardcoded values for flexibility

For filtering between two dates, see [Filter data between dates](https://exceljet.net/formulas/filter-data-between-dates)
.

Related formulas
----------------

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: Filter data between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter_data_between_dates.png "Excel formula: Filter data between dates")](https://exceljet.net/formulas/filter-data-between-dates)

### [Filter data between dates](https://exceljet.net/formulas/filter-data-between-dates)

The goal is to extract records with dates that are greater than or equal to a start date in F5 and less than or equal to an end date in G5. You might think we can use the AND function inside FILTER to solve this problem. However, because AND returns just a single value, this won't work. Instead, we...

[![Excel formula: Filter with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter_with_multiple_criteria.png "Excel formula: Filter with multiple criteria")](https://exceljet.net/formulas/filter-with-multiple-criteria)

### [Filter with multiple criteria](https://exceljet.net/formulas/filter-with-multiple-criteria)

In this example, the goal is to filter data based on multiple criteria with the FILTER function. Specifically, we want to select data where (1) the group = "A" and (2) the Score is greater than 80. At first glance, it's not obvious how to do this with the FILTER function. Unlike older functions...

[![Excel formula: FILTER with complex multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20complex%20multiple%20criteria.png "Excel formula: FILTER with complex multiple criteria")](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)

### [FILTER with complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)

In this example, we need to construct logic that filters data to include: account begins with "x" AND region is "east", and month is NOT April. The filtering logic of this formula (the include argument) is created by chaining together three expressions that use boolean logic on arrays in the data...

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

[![Excel formula: Filter on dates expiring soon](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20on%20dates%20expiring%20soon.png "Excel formula: Filter on dates expiring soon")](https://exceljet.net/formulas/filter-on-dates-expiring-soon)

### [Filter on dates expiring soon](https://exceljet.net/formulas/filter-on-dates-expiring-soon)

In this example, the goal is to filter data to show rows where dates have expired or will be expiring soon. In the table to the left, we have equipment that needs to be replaced every x months, where x appears in the "Months" column. The "Replaced" column shows the date equipment was replaced. The...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20data%20between%20two%20dates-Play.png)](https://exceljet.net/videos/filter-data-between-two-dates)

### [FILTER data between two dates](https://exceljet.net/videos/filter-data-between-two-dates)

In this video, we’ll look at a couple ways to use the FILTER function to extract data between dates. In this worksheet, we have sample order data that contains a date field. Let's set up the FILTER function to extract data between two dates. Before we begin, I want to remind you that Excel dates...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20algebra%20in%20Excel-Play.png)](https://exceljet.net/videos/boolean-algebra-in-excel)

### [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)

In this video, we’ll look at how boolean algebra is used for AND and OR logic in formulas. In Boolean algebra, there are only two possible results for a math operation: 1 or 0, which, as we know, correspond to the logical values TRUE and FALSE. AND logic corresponds to multiplication . Anything...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [Filter data between dates](https://exceljet.net/formulas/filter-data-between-dates)
    
*   [Filter with multiple criteria](https://exceljet.net/formulas/filter-with-multiple-criteria)
    
*   [FILTER with complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)
    
*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [Filter on dates expiring soon](https://exceljet.net/formulas/filter-on-dates-expiring-soon)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [FILTER data between two dates](https://exceljet.net/videos/filter-data-between-two-dates)
    
*   [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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