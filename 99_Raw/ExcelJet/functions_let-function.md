# Excel LET function | Exceljet

**Source:** https://exceljet.net/functions/let-function

---

[Skip to main content](https://exceljet.net/functions/let-function#main-content)

[](https://exceljet.net/functions/let-function#)

*   [Previous](https://exceljet.net/functions/lambda-function)
    
*   [Next](https://exceljet.net/functions/makearray-function)
    

Excel 2021

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

LET Function
============

by Dave Bruns · Updated 11 Dec 2025

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[LET](https://exceljet.net/functions/let-function)

[MAP](https://exceljet.net/functions/map-function)

[SCAN](https://exceljet.net/functions/scan-function)

[REDUCE](https://exceljet.net/functions/reduce-function)

[MAKEARRAY](https://exceljet.net/functions/makearray-function)

[BYCOL](https://exceljet.net/functions/bycol-function)

[BYROW](https://exceljet.net/functions/byrow-function)

![Excel LET function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_let.png "Excel LET function")

Summary
-------

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write.

Purpose 
--------

Assign variables inside formula

Return value 
-------------

Normal formula result

Syntax
------

    =LET(name1,value1,[name2/value2],...,result)

*   _name1_ - First name to assign. Must begin with a letter.
*   _value1_ - The value or calculation to assign to name 1.
*   _name2/value2_ - \[optional\] Second name and value. Entered as a pair of arguments.
*   _result_ - A calculation or a variable previously calculated.

Using the LET function 
-----------------------

The LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write. Once a variable is named, it can be assigned a static value or a value based on a calculation. The formula can then refer to a variable by name as many times as needed, while the value of the variable is defined in one place only.

[Example 1](https://exceljet.net/functions/let-function#example1)
 | [Example 2](https://exceljet.net/functions/let-function#example2)
 | [Example 3](https://exceljet.net/formulas/detailed-let-function-example)
 | [Example 4](https://exceljet.net/formulas/get-days-months-and-years-between-dates)
 | [More examples](https://exceljet.net/functions/let-function#related-info)

Variables are named and assigned values in pairs, separated by commas (name1,value1, name2,value2, etc). LET can handle up to 126 name/value pairs, but only the first name/value pair is required. The scope of each variable is the current LET function and nested functions below. The final result is a calculation or a variable previously calculated. The result from LET always appears as the _last argument_ to the function. 

The names used in LET must begin with a letter and are not case-sensitive. You can use names that contain numbers like "count1", "count2", etc., but names like "ct1" and "ct2" will fail because Excel will interpret the names as a cell reference. Space characters and punctuation symbols are not allowed in names, but the underscore character (\_) can be used.

The LET function is often combined with the [LAMBDA function](https://exceljet.net/functions/lambda-function)
 as a way to make a complex formula easier to use. LAMBDA provides a way to name a formula and reuse it in a worksheet like a custom function. [Example here](https://exceljet.net/formulas/lambda-append-range)
.

### Key Benefits

The LET function provides three key benefits:

1.  **Clarity** - naming variables used in a formula can make a complex formula much easier to read and understand.
2.  **Simplification** - naming and defining variables in just one place helps eliminate redundancy and the errors that arise from having the same code in more than one place.
3.  **Performance** - elimination of redundant code means less calculation time overall since expensive calculations only need to occur once.

### Example #1

Below is the general form of the LET function with one variable:

    =LET(x,10,x+1) // returns 11
    

With a second variable:

    =LET(x,10,y,5,x+y) // returns 15
    

After x and y have been declared and assigned values, the calculation provided in the 5th argument returns 15.

### Example #2

A chief benefit of the LET function is simplification by eliminating redundancy. For example, the screenshot above shows a formula that uses the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 to generate all dates between May 1, 2020 and May 15, 2020, which are then filtered by the [FILTER function](https://exceljet.net/functions/filter-function)
 to include only weekdays. The formula in E5 is:

    =LET(dates,SEQUENCE(C5-C4+1,1,C4,1),FILTER(dates,WEEKDAY(dates,2)<6))
    

The first argument declares the variable **dates** and the second argument assigns the output from SEQUENCE to **dates**:

    =LET(dates,SEQUENCE(C5-C4+1,1,C4,1)
    

Notice the start and end dates come from cells C4 and C5, respectively. Once **dates** has been assigned a value, it can be used in the final calculation, which is based on the FILTER function:

    FILTER(dates,WEEKDAY(dates,2)<6)) // filter out weekends
    

Notice **dates** is used twice in this snippet: once by FILTER, once by the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
. In the first instance, the raw dates from SEQUENCE are passed into the FILTER function as the array to filter. In the second instance, the dates from SEQUENCE are passed into the WEEKDAY function, which tests for weekdays (i.e. not Sat or Sun). The result from WEEKDAY is the logic used to filter the original dates.

Without the LET function, SEQUENCE would need to appear twice in the formula, both times with the same (redundant) configuration. The LET function allows the SEQUENCE function to appear and be configured just once in the formula.

### More examples

*   For an example of how LET can make a tricky formula easier to follow, [see this page](https://exceljet.net/formulas/get-nth-day-of-week-in-month)
    .
*   For a more complex example of how LET can eliminate redundancy, [see this example](https://exceljet.net/formulas/combine-ranges)
    .

LET function examples
---------------------

[![Excel formula: Get days, months, and years between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20months%20and%20years%20between%20dates.png "Excel formula: Get days, months, and years between dates")](https://exceljet.net/formulas/get-days-months-and-years-between-dates)

### [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)

In this example, the goal is to output the time between a start date and an end date as a text string that lists years, months, and days separately. For example, given a start date of 1-Jan-2018 and an end date of 1-Jul-2018, the result should be a string like this: "1 years, 6 months, 0 days"...

[![Excel formula: List all dates in a month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_all_dates_in_a_month.png "Excel formula: List all dates in a month")](https://exceljet.net/formulas/list-all-dates-in-a-month)

### [List all dates in a month](https://exceljet.net/formulas/list-all-dates-in-a-month)

In this example, we'll use SEQUENCE to generate all dates in a given month. Creating a complete list of dates for a specific month is a common Excel task with many practical applications, from building project timelines and work schedules to generating calendar views and tracking daily data. The...

[![Excel formula: Maximum change](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_change.png "Excel formula: Maximum change")](https://exceljet.net/formulas/maximum-change)

### [Maximum change](https://exceljet.net/formulas/maximum-change)

In the example shown, the goal is to calculate the maximum difference between the "High" values in column C and the "Low" values in column D. Because the difference between High and Low is not part of the data, the calculation must occur in the formula itself. This is a classic example of an array...

[![Excel formula: LAMBDA append range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20append%20range.png "Excel formula: LAMBDA append range")](https://exceljet.net/formulas/lambda-append-range)

### [LAMBDA append range](https://exceljet.net/formulas/lambda-append-range)

Note: this example was created before the VSTACK function and HSTACK function were introduced to Excel. VSTACK combines ranges vertically and HSTACK combines ranges horizontally. These functions are a much easier way to append ranges, but this example is still useful as a way to understand how to...

[![Excel formula: Sum numbers with text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20numbers%20with%20text.png "Excel formula: Sum numbers with text")](https://exceljet.net/formulas/sum-numbers-with-text)

### [Sum numbers with text](https://exceljet.net/formulas/sum-numbers-with-text)

In this example, one goal is to sum the numbers that appear in the range B5:B16. A second more challenging goal is to create the table of results seen in E7:F12. For convenience, data is the named range B5:B16. Total sum To sum all the numbers that appear in B5:B16, ignoring text, the formula in E5...

[![Excel formula: LAMBDA strip characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20strip%20characters.png "Excel formula: LAMBDA strip characters")](https://exceljet.net/formulas/lambda-strip-characters)

### [LAMBDA strip characters](https://exceljet.net/formulas/lambda-strip-characters)

This is an experimental formula to strip characters from text. The experimental part is using character codes instead of regular characters as a way to make the formula case-sensitive, and providing a way to reverse the logic of the formula with the "keep" input parameter. Unlike the formula...

[![Excel formula: LAMBDA contains which things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20contains%20which%20strings.png "Excel formula: LAMBDA contains which things")](https://exceljet.net/formulas/lambda-contains-which-things)

### [LAMBDA contains which things](https://exceljet.net/formulas/lambda-contains-which-things)

The goal in this example is to use a formula to report which things exist in a cell. The list of things to check for is in the named range things (E5:E9). The result is returned as a comma separated text string. The first step in creating a custom function with the LAMBDA function is to verify the...

[![Excel formula: Strip numeric characters from cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip%20numeric%20characters%20from%20cell_0.png "Excel formula: Strip numeric characters from cell")](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

### [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

Excel doesn't have a way to cast the letters in a text string to an array directly in a formula. As a workaround, this formula uses the MID function, with help from the ROW and INDIRECT functions to achieve the same result. The formula in C5, copied down, is: =TEXTJOIN("",TRUE,IF(ISERR(MID(B5,ROW(...

[![Excel formula: Two-way summary count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Two-way%20summary%20count.png "Excel formula: Two-way summary count")](https://exceljet.net/formulas/two-way-summary-count)

### [Two-way summary count](https://exceljet.net/formulas/two-way-summary-count)

In this example, the goal is to count the people shown in the table by both Department (Dept) and Group as shown in the worksheet. A simple way to do this is with the COUNTIFS function. COUNTIFS function The COUNTIFS function is designed to count things based on more than one condition. Conditions...

[![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")](https://exceljet.net/formulas/sum-by-year)

### [Sum by year](https://exceljet.net/formulas/sum-by-year)

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an Excel Table called data in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem...

[![Excel formula: List upcoming birthdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20upcoming%20birthdays.png "Excel formula: List upcoming birthdays")](https://exceljet.net/formulas/list-upcoming-birthdays)

### [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)

In this example, the goal is to list the next n upcoming birthdays from a larger set of 25 birthdays based on the current date. The set of birthdays are in an Excel Table named data in the range B5:C29. In the example shown, we are using 7 for n , so the result will be the next 7 upcoming birthdays...

[![Excel formula: Income tax bracket calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/income%20tax%20bracket%20calculation_0.png "Excel formula: Income tax bracket calculation")](https://exceljet.net/formulas/income-tax-bracket-calculation)

### [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)

In this example, the goal is to calculate the total income tax owed in a progressive tax system with multiple tax brackets, as shown in the worksheet. The article below first reviews how taxes are computed in a progressive system. Next, it shows how to accomplish this task in Excel using two...

[![Excel formula: XLOOKUP return blank if blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20if%20blank%20return%20blank.png "Excel formula: XLOOKUP return blank if blank")](https://exceljet.net/formulas/xlookup-return-blank-if-blank)

### [XLOOKUP return blank if blank](https://exceljet.net/formulas/xlookup-return-blank-if-blank)

When XLOOKUP can't find a value in a lookup array, it returns an #N/A error. You can use the IFNA function or IFERROR function to trap this error and return a different result. However, when the result is an empty cell , XLOOKUP does not throw an error. Instead, XLOOKUP returns an empty result,...

[![Excel formula: Count unique dates ignore time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20dates%20ignore%20time.png "Excel formula: Count unique dates ignore time")](https://exceljet.net/formulas/count-unique-dates-ignore-time)

### [Count unique dates ignore time](https://exceljet.net/formulas/count-unique-dates-ignore-time)

In this example, the goal is to count the unique dates in a range of timestamps (i.e. dates that contain dates and times). In addition, we also want to create the table of results seen in E7:F9. For convenience, data is the named range B5:B16. Basic count To get a count of individual dates that...

[![Excel formula: Get workbook name and path without sheet](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_workbook_name_and_path_without_sheet.png "Excel formula: Get workbook name and path without sheet")](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)

### [Get workbook name and path without sheet](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)

In this example, the goal is to get a normal path to the current workbook, without a sheet name, and without the square brackets ("\[ \]") that normally enclose the workbook name. This is a pretty simple problem in the latest version of Excel, which provides the TEXTBEFORE function . In older...

Related functions
-----------------

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel MAP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20map%20function.png "Excel MAP function")](https://exceljet.net/functions/map-function)

### [MAP Function](https://exceljet.net/functions/map-function)

The Excel MAP function "maps" a custom LAMBDA function to each value in a supplied [array](https://exceljet.net/glossary/array)
. The LAMBDA is applied to each value, and the result from MAP is an array of results with the same dimensions as the original array.

[![Excel SCAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20scan%20function.png "Excel SCAN function")](https://exceljet.net/functions/scan-function)

### [SCAN Function](https://exceljet.net/functions/scan-function)

The SCAN function applies a custom calculation to each element in a given array or range and returns an [array](https://exceljet.net/glossary/array)
 that contains the intermediate values created during the scan. SCAN can be used to generate running totals, running counts, and other...

[![Excel REDUCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20reduce%20function.png "Excel REDUCE function")](https://exceljet.net/functions/reduce-function)

### [REDUCE Function](https://exceljet.net/functions/reduce-function)

The Excel REDUCE function applies a custom LAMBDA function to each element in a given array and accumulates results to a single value.

[![Excel MAKEARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20makearray%20function.png "Excel MAKEARRAY function")](https://exceljet.net/functions/makearray-function)

### [MAKEARRAY Function](https://exceljet.net/functions/makearray-function)

The Excel MAKEARRAY function returns an array with specified rows and columns, based on a custom [LAMBDA calculation](https://exceljet.net/functions/lambda-function)
. MAKEARRAY can be used to create arrays with variable dimensions based on a calculation....

[![Excel BYCOL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20bycol%20function.png "Excel BYCOL function")](https://exceljet.net/functions/bycol-function)

### [BYCOL Function](https://exceljet.net/functions/bycol-function)

The Excel BYCOL function applies a function to each column in a given array and returns one result per column. BYCOL can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)
    
*   [LAMBDA contains which things](https://exceljet.net/formulas/lambda-contains-which-things)
    
*   [Dynamic summary count](https://exceljet.net/formulas/dynamic-summary-count)
    
*   [Get address of named range or table](https://exceljet.net/formulas/get-address-of-named-range-or-table)
    
*   [Get nth day of week in month](https://exceljet.net/formulas/get-nth-day-of-week-in-month)
    
*   [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)
    
*   [Sequence of leap years](https://exceljet.net/formulas/sequence-of-leap-years)
    
*   [Randomly assign people to groups](https://exceljet.net/formulas/randomly-assign-people-to-groups)
    
*   [Sum by quarter](https://exceljet.net/formulas/sum-by-quarter)
    
*   [LAMBDA strip characters](https://exceljet.net/formulas/lambda-strip-characters)
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [MAP Function](https://exceljet.net/functions/map-function)
    
*   [SCAN Function](https://exceljet.net/functions/scan-function)
    
*   [REDUCE Function](https://exceljet.net/functions/reduce-function)
    
*   [MAKEARRAY Function](https://exceljet.net/functions/makearray-function)
    
*   [BYCOL Function](https://exceljet.net/functions/bycol-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    

### Links

*   [Microsoft LET function documentation](https://support.microsoft.com/en-us/office/let-function-34842dd8-b92b-4d3f-b325-b8b8f9908999)
    

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