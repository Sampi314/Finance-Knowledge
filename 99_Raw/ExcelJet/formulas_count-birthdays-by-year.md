# Count birthdays by year - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-birthdays-by-year

---

[Skip to main content](https://exceljet.net/formulas/count-birthdays-by-year#main-content)

[](https://exceljet.net/formulas/count-birthdays-by-year#)

*   [Previous](https://exceljet.net/formulas/count-between-dates-by-age-range)
    
*   [Next](https://exceljet.net/formulas/count-cells-between-dates)
    

[Count](https://exceljet.net/formulas#Count)

Count birthdays by year
=======================

by Dave Bruns · Updated 12 Aug 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[YEAR](https://exceljet.net/functions/year-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[BYROW](https://exceljet.net/functions/byrow-function)

[UNIQUE](https://exceljet.net/functions/unique-function)

[SORT](https://exceljet.net/functions/sort-function)

[LET](https://exceljet.net/functions/let-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7319/download?token=5obMttqh)
 (15.38 KB)

![Excel formula: Count birthdays by year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20birthdays%20by%20year_0.png "Excel formula: Count birthdays by year")

Summary
-------

To count the number of birthdays by year, you can use a formula based on the [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 and [YEAR](https://exceljet.net/functions/year-function)
 functions. In the example shown, E5 contains this formula:

    =SUMPRODUCT(--(YEAR(data[Birthday])=E5))
    

where **data** is an [Excel Table](https://exceljet.net/articles/excel-tables)
 in the range (C5:B16). As the formula is copied down, it returns a count of birthdays per year as shown. Video: [What is an Excel table](https://exceljet.net/videos/what-is-an-excel-table)
.

_Note: this example has been [updated below](https://exceljet.net/formulas/count-birthdays-by-year#dynamic_array)
 to show how to create an all-in-one formula with [dynamic arrays](https://exceljet.net/glossary/dynamic-array)
 in the latest version of Excel._

Generic formula
---------------

    =SUMPRODUCT(--(YEAR(dates)=year))

Explanation 
------------

In this example, the goal is to count birthdays by year. The source data is an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data** in the range C5:C16. The birthdays we want to count are in the Birthday column. In column E, the years of interest have been previously entered. The easiest way to solve this problem is with the SUMPRODUCT function, but it can also be solved with COUNTIFS as explained below.

### SUMPRODUCT function

The easiest way to solve this problem is to use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 together with the [YEAR function](https://exceljet.net/functions/year-function)
 like this in cell F5:

    =SUMPRODUCT(--(YEAR(data[Birthday])=E5))
    

Working from the inside out, we use the YEAR function to extract the year from each birthday:

    YEAR(data[Birthday]) // extract year
    

Because there are 12 dates in the list, the YEAR function returns 12 values in an [array](https://exceljet.net/glossary/array)
 like this:

    {1999;1999;2000;2000;2000;2000;2001;1999;2000;2001;2001;2002}
    

Next, each value in this array is compared against the year in E5, which is 1999. The result is a new array containing only TRUE and FALSE values:

    {TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE}
    

In this array, TRUE represents birth years equal to 1999 and FALSE represents birth years not equal to 1999. We want to count the TRUE values, but because SUMPRODUCT will ignore the logical values TRUE and FALSE, we need to convert these values to 1s and 0s first. To perform this conversion, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--). The result is an array that contains just 1s and 0s, which is returned directly to the SUMPRODUCT function like this:

    =SUMPRODUCT({1;1;0;0;0;0;0;1;0;0;0;0})
    

With only one array to process, SUMPRODUCT sums the array and returns a result of 3 in cell F5. As the formula is copied down, it returns a count of birthdays per year as seen in the worksheet.

_Note: The SUMPRODUCT formula above is an example of using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 in an [array operation](https://exceljet.net/videos/boolean-operations-in-array-formulas)
. This is a powerful and flexible approach to solving many problems in Excel. It is also an important skill with new functions like [FILTER](https://exceljet.net/functions/filter-function)
 and [XLOOKUP](https://exceljet.net/functions/xlookup-function)
, which often use this technique to apply multiple criteria ([FILTER example](https://exceljet.net/videos/filter-with-boolean-logic)
, [XLOOKUP example](https://exceljet.net/formulas/xlookup-with-logical-criteria)
)_

### COUNTIFS function

The [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 can also be used to solve this problem but the formula is more complicated, because [COUNTIF only works with ranges](https://exceljet.net/articles/excels-racon-functions)
, and you can't extract the years to use as the _range_ argument inside COUNTIFS. Instead, you must create a start and end date for each year. The formula looks like this:

    =COUNTIFS(data[Birthday],">="&DATE(E5,1,1),data[Birthday],"<="&DATE(E5,12,31))
    

In a nutshell, we create a first-of-year date (1-Jan-1999) and an end-of-year date (31-Jan-1999) using the year in E5 with the [DATE function](https://exceljet.net/functions/date-function)
:

    DATE(E5,1,1) // first day of year
    DATE(E5,12,31) // last day of year
    

The DATE function creates [Excel dates](https://exceljet.net/glossary/excel-date)
 with separate _year_, _month_, and _day_ arguments. In the example, _month_ and _day_ are hard-coded, and we get _year_ from column E. These dates are [concatenated](https://exceljet.net/articles/how-to-concatenate-in-excel)
 to the greater than or equals to [operator](https://exceljet.net/glossary/logical-operators)
 (>=) to make _criteria1_, and the less than or equals to operator (<=) to make _criteria2_. The range for both criteria is **data\[Birthday\]**. Notice the operators must be enclosed in double quotes ("").

As the formula is copied down column F, it returns a count of birthdays per year, same as the SUMPRODUCT formula.

### Dynamic array solution

In the latest version of Excel, which supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, it is possible to create a single all-in-one formula that builds the entire summary table, including headers, like this:

    =LET(
    years, YEAR(data[Birthday]),
    uyears,SORT(UNIQUE(years)),
    counts, BYROW(uyears, LAMBDA(r, SUM(--(years=r)))),
    VSTACK({"Year","Count"},HSTACK(uyears, counts))
    )
    

The [LET function](https://exceljet.net/functions/let-function)
 is used to assign three intermediate variables: _years_, _uyears,_ and _counts_. The value for _years_ is created like this:

    YEAR(data[Birthday]) // extract years
    

Here, the [YEAR function](https://exceljet.net/functions/year-function)
 is used to extract just the year from all dates in **data\[Birthday\]**. Because the table contains 12 rows, the result is an [array](https://exceljet.net/glossary/array)
 with 12 year values like this:

    {1999;1999;2000;2000;2000;2000;2001;1999;2000;2001;2001;2002}
    

Next, the value for _uyears_ (unique years) is created like this:

    SORT(UNIQUE(years)) // get and sort unique years
    

Out of 12 year values, the [UNIQUE function](https://exceljet.net/functions/unique-function)
 returns just 4 _unique_ years:

    {1999;2000;2001;2002} // unique
    

This array is returned to the [SORT function,](https://exceljet.net/functions/sort-function)
 which returns an array sorted in ascending order:

    ={1999;2000;2001;2002} // sorted
    

In this example, it happens that the unique years are _already_ in ascending order, so the SORT function does not change the result from UNIQUE. However, using the SORT function ensures that year values will always appear in order when source data is _not_ sorted.

Next, the [BYROW function](https://exceljet.net/functions/byrow-function)
 is used to create a value for _counts_ for each year like this:

    BYROW(uyears, LAMBDA(r, SUM(--(years=r)))) // counts
    

BYROW runs through the _uyears_ values row by row. At each row, it applies this calculation:

    LAMBDA(r, SUM(--(years=r)))
    

The value for r is the year in the "current" row. Inside the SUM function, this value is compared to _years_. Since _years_ contains all 12 years, the result is an array with 12 TRUE and FALSE results. The TRUE and FALSE values are converted to 1s and 0s with the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--), and the SUM function simply adds up the result, which is the count of birthdays associated with the current row. Since there are 4 unique years, the result from BYROW is an array with 4 counts like this:

    ={3;5;3;1} // counts
    

Finally the [HSTACK](https://exceljet.net/functions/hstack-function)
 and [VSTACK](https://exceljet.net/functions/vstack-function)
 functions are used to assemble a complete table:

    VSTACK({"Year","Count"},HSTACK(uyears, counts))
    

At the top of the table, the [array constant](https://exceljet.net/glossary/array-constant)
 {"Year","Count"} creates a header row. The HSTACK function combines _uyears_ and _counts_ horizontally, and VSTACK combines the header row and the data to make the final table. The result [spills](https://exceljet.net/glossary/spill)
 into multiple cells on the worksheet:

![A single all in one formula with dynamic arrays](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/count%20birthdays%20by%20year%20all%20in%20one.png?itok=hnSJpyRP "A single all in one formula with dynamic arrays")

### Pivot table solution

A [Pivot Table](https://exceljet.net/articles/excel-pivot-tables)
 is a good solution for this problem as well. [This example](https://exceljet.net/pivot-tables/pivot-table-count-birthdays-by-month)
 shows how to count birthdays by month with a Pivot Table.

Related formulas
----------------

[![Excel formula: Count birthdays by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20birthdays%20by%20month.png "Excel formula: Count birthdays by month")](https://exceljet.net/formulas/count-birthdays-by-month)

### [Count birthdays by month](https://exceljet.net/formulas/count-birthdays-by-month)

You would think you could use the COUNTIF function to count birthdays, but the trouble is COUNTIF only works with ranges , and won't let you use something like MONTH to extract just the month number from dates. So, we use the SUMPRODUCT function with custom logic instead. Inside SUMPRODUCT, we have...

[![Excel formula: Count cells between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20cells%20between%20two%20numbers_0.png "Excel formula: Count cells between two numbers")](https://exceljet.net/formulas/count-cells-between-two-numbers)

### [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)

In this example, the goal is to count numbers that fall within specific ranges. The lower value comes from the "Start" column, and the upper value comes from the "End" column. For each range, we want to include both the lower value and the upper value. For convenience, the numbers being counted are...

[![Excel formula: Count dates by day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20dates%20by%20day%20of%20week.png "Excel formula: Count dates by day of week")](https://exceljet.net/formulas/count-dates-by-day-of-week)

### [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)

You might wonder why we aren't using COUNTIF or COUNTIFS . These functions seem like the obvious solution. However, without adding a helper column that contains a weekday value, there is no way to create criteria for COUNTIF to count weekdays in a range of dates. Instead, we use the versatile...

[![Excel formula: Month number from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/month%20number%20from%20name.png "Excel formula: Month number from name")](https://exceljet.net/formulas/month-number-from-name)

### [Month number from name](https://exceljet.net/formulas/month-number-from-name)

In this example, the goal is to return a number, 1-12, for any month name of the year. For example, given the string "January" we want to return 1, "February" should return 2, and so on. If we had a valid Excel date , we could use a number format for this task, but because we are starting with a...

[![Excel formula: Get age from birthday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20age%20from%20birthdate.png "Excel formula: Get age from birthday")](https://exceljet.net/formulas/get-age-from-birthday)

### [Get age from birthday](https://exceljet.net/formulas/get-age-from-birthday)

The DATEDIF function (Date + Dif) is a bit of an anomaly in Excel. A compatibility function that comes originally from Lotus 1-2-3, Excel will not help supply arguments when the function is entered. However, DATEDIF works in all modern versions of Excel and is a useful function for calculating the...

[![Excel formula: List upcoming birthdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20upcoming%20birthdays.png "Excel formula: List upcoming birthdays")](https://exceljet.net/formulas/list-upcoming-birthdays)

### [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)

In this example, the goal is to list the next n upcoming birthdays from a larger set of 25 birthdays based on the current date. The set of birthdays are in an Excel Table named data in the range B5:C29. In the example shown, we are using 7 for n , so the result will be the next 7 upcoming birthdays...

[![Excel formula: Dynamic summary count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20summary%20count.png "Excel formula: Dynamic summary count")](https://exceljet.net/formulas/dynamic-summary-count)

### [Dynamic summary count](https://exceljet.net/formulas/dynamic-summary-count)

In this example, the goal is to build a simple summary count table with a formula. Once created, the summary table should automatically update to show new values and counts when data changes. The article below walks through several options, from simple to very advanced. The more advanced options...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count birthdays by month](https://exceljet.net/formulas/count-birthdays-by-month)
    
*   [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)
    
*   [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)
    
*   [Month number from name](https://exceljet.net/formulas/month-number-from-name)
    
*   [Get age from birthday](https://exceljet.net/formulas/get-age-from-birthday)
    
*   [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)
    
*   [Dynamic summary count](https://exceljet.net/formulas/dynamic-summary-count)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    
*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    

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