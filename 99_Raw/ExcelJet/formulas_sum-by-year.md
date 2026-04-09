# Sum by year - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-by-year

---

[Skip to main content](https://exceljet.net/formulas/sum-by-year#main-content)

[](https://exceljet.net/formulas/sum-by-year#)

*   [Previous](https://exceljet.net/formulas/sum-by-weekday)
    
*   [Next](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum by year
===========

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[YEAR](https://exceljet.net/functions/year-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[DATE](https://exceljet.net/functions/date-function)

[LET](https://exceljet.net/functions/let-function)

[BYROW](https://exceljet.net/functions/byrow-function)

[UNIQUE](https://exceljet.net/functions/unique-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

[HSTACK](https://exceljet.net/functions/hstack-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7503/download?token=5lKxHDPD)
 (15.62 KB)

![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")

Summary
-------

To sum values by year, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 together with the [YEAR function](https://exceljet.net/functions/year-function)
. In the example shown, the formula in cell G5 is:

    =SUMPRODUCT((YEAR(data[Date])=F5)*data[Amount])
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:D16. As the formula is copied down, it returns a total for each year shown in column F.

Generic formula
---------------

    =SUMPRODUCT((YEAR(dates)=A1)*amounts)

Explanation 
------------

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 called **data** in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem is with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 using the formula seen in the worksheet above. The problem can also be solved with the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
, or with a [dynamic array formula](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. All three approaches are explained below.

### SUMPRODUCT function

In the example shown, the formula in cell G5 is:

    =SUMPRODUCT((YEAR(data[Date])=F5)*data[Amount])
    

Working from the inside out, the first step is to extract year values from the dates in column B, which is done with the YEAR function:

    YEAR(data[Date]) // get years
    

Because there are 12 dates in the column, YEAR returns 12 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {2020;2020;2021;2022;2020;2021;2021;2022;2020;2021;2022;2022}
    

Each year in this array corresponds to a date in **data\[Date\]**. Next, the year values are compared to the year in cell F5:

    YEAR(data[Date])=F5
    

The result is an array of 12 TRUE and FALSE values like this:

    {TRUE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE}
    

Notice TRUE values correspond to dates that occur in 2020, the value in F5. Next, this array is multiplied by the amounts in column D. The math operation automatically converts the TRUE and FALSE values to 1s and 0s, so we can visualize this operation like this:

    {1;1;0;0;1;0;0;0;1;0;0;0}*data[Amount]
    

Remember the 1s in the first array correspond to dates that occur in 2020, while 0s indicate dates in other years. The zeros in the first array effectively "cancel out" amounts in other years. The resulting array is returned to SUMPRODUCT like this:

    =SUMPRODUCT({1500;1250;0;0;1850;0;0;0;1250;0;0;0})
    

With only one array to process, SUMPRODUCT sums the array and returns a final result of 5850. As the formula is copied down, the cell reference F5, which is relative, changes at each new row, and we get the correct total for each year shown.

_Note: in the current version of Excel, you can replace the SUMPRODUCT function with the SUM function in the formula above. To read more about this topic, see [Why SUMPRODUCT](https://exceljet.net/articles/why-sumproduct)
?_

### SUMIFS function

Another way to solve this problem is with the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 and a formula like this:

    =SUMIFS(data[Amount],data[Date],">="&DATE(F5,1,1),data[Date],"<="&DATE(F5,12,31))
    

If you are new to SUMIFS, [this article](https://exceljet.net/functions/sumifs-function)
 covers the basics. This formula is more complicated than the SUMPRODUCT option because SUMIFS has no way to get at the year values directly. This limitation is [discussed in more detail here](https://exceljet.net/articles/excels-racon-functions)
. Instead, we need to create two dates for each year with the [DATE function](https://exceljet.net/functions/date-function)
, then test for dates between these two dates:

    DATE(F5,1,1) // start "Jan 1, 2020"
    DATE(F5,12,31) // end "Dec 31,2020"
    

For the start date, we simply hardcode 1 for _month_ and _day_ arguments to get a January 1 date. For the end date, we hardcode 12 for _month_ and 31 for _day_ to create a December 31 date. For both dates, _year_ comes from cell F5, which contains 2020. In summary, we use the DATE function to create a first-of-year date and a last-of-year date based on the year value in column F.

We also need logical operators to "bracket" each year. We [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the operators like this:

    ">="&DATE(F5,1,1) // start date
    "<="&DATE(F5,12,31) // end date
    

The requirement to concatenate operators like this is again a "feature" of the SUMIFS function, which shares this peculiar syntax with [eight other functions](https://exceljet.net/articles/excels-racon-functions)
.

After the DATE function is evaluated, and after concatenation is complete, we have:

    =SUMIFS(data[Amount],data[Date],">=43831",data[Date],"<=44196")
    

The number 43831 is the [Excel serial number date](https://exceljet.net/glossary/excel-date)
 for January 1, 2020. The number 44196 is the serial number for December 31, 2020. 

_Note: with either of the two options above, you could use the [UNIQUE function](https://exceljet.net/videos/the-unique-function)
 to fetch the unique years from the dates as an initial step, if you have a [modern version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
._

### Dynamic array solution

In the current version of Excel, which supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, it is possible to create a single all-in-one formula that builds the entire summary table, including headers, like this:

    =LET(
    years,YEAR(data[Date]),
    values,data[Amount],
    uyears,SORT(UNIQUE(years)),
    sums, BYROW(uyears, LAMBDA(r, SUM(--(years=r)*values))),
    VSTACK({"Year","Total"},HSTACK(uyears, sums))
    )
    

Because this formula is doing a lot more work, it is more complicated. At the highest level, the [LET function](https://exceljet.net/functions/let-function)
 is used to assign values to four variables: _years_, _values_, _uyears_, and _sums_. First, we assign values to _years_ and _values_ like this:

    =LET(
    years,YEAR(data[Date]),
    values,data[Amount],
    

Technically, we could just use the references for **data\[Date\]** and **data\[Amount\]** throughout the formula, but defining these variables up front makes the formula more portable. With a different set of data, only these two references need to be changed and the formula will continue to work.

The value for _years_ is created with the [YEAR function](https://exceljet.net/functions/year-function)
 like this:

    years,YEAR(data[Date]) // extract years
    

YEAR extracts just the year from all dates in **data\[Date\]**. Because the table contains 12 rows, the result is an [array](https://exceljet.net/glossary/array)
 with 12 year values like this:

    {2020;2020;2021;2022;2020;2021;2021;2022;2020;2021;2022;2022}
    

Next, _values_ is assigned like this:

    values,data[Amount]
    

As mentioned above, we do this to avoid repeating the reference elsewhere in the formula. In the following line, the value for _uyears_ (unique years) is created like this:

    SORT(UNIQUE(years)) // get and sort unique years
    

From the12 year values, the [UNIQUE function](https://exceljet.net/functions/unique-function)
 returns just 3 _unique_ years:

    {2020;2021;2022} // unique
    

This array is returned to the [SORT function,](https://exceljet.net/functions/sort-function)
 which sorts the array in ascending order:

    {2020;2021;2022} // sorted
    

_Note: In this example, it happens that the unique years are already in ascending order, so the SORT function does not change the result from UNIQUE. However, using the SORT function ensures that year values will always appear in order when source data is not sorted._

Next, the [BYROW function](https://exceljet.net/functions/byrow-function)
 is used to create a value for _sums_ for each year like this:

    sums,BYROW(uyears,LAMBDA(r,SUM(--(years=r)*values))) // sums
    

This is the core calculation in the formula. BYROW runs through the _uyears_ values row by row. At each row, it applies this calculation:

    LAMBDA(r,SUM(--(years=r)*values))
    

The value for _r_ is the year in the "current" row. Inside the [SUM function](https://exceljet.net/functions/sum-function)
, this value is compared to _years_. Since _years_ contains all 12 years, the result is an array with 12 TRUE and FALSE results. The TRUE and FALSE values are converted to 1s and 0s with the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--), and the resulting array is multiplied by _values_. The 0s in the first array effectively "cancel out" amounts not associated with the year of interest.

_Note: technically, the double negative (--) isn't needed here, because the math operation of multiplication automatically converts the TRUE and FALSE values to 1s and 0s. However, the double negative does no harm, and arguably makes the formula easier to read by clearly signaling an operation that cancels out values._

Next, the SUM function then sums the resulting array, which represents the total sum of values in the current year. Since there are 3 unique years, the result from BYROW is an array with 3 sums like this:

    {5850;7950;6500} // sums
    

Finally, the HSTACK and VSTACK functions are used to assemble a complete table:

    VSTACK({"Year","Total"},HSTACK(uyears, sums))
    

At the top of the table, the [array constant](https://exceljet.net/glossary/array-constant)
 {"Year","Total"} creates a header row. The [HSTACK function](https://exceljet.net/functions/hstack-function)
 combines _uyears_ and _sums_ horizontally, and the [VSTACK function](https://exceljet.net/functions/vstack-function)
 combines the header row and the data to make the final table. The result [spills](https://exceljet.net/glossary/spill)
 into multiple cells on the worksheet:

![All in one formula to sum by year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sum%20by%20year%20all%20in%20one%20formula.png?itok=AEHkvIGf "All in one formula to sum by year")

Related formulas
----------------

[![Excel formula: Sum if date is greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_date_is_greater_than.png "Excel formula: Sum if date is greater than")](https://exceljet.net/formulas/sum-if-date-is-greater-than)

### [Sum if date is greater than](https://exceljet.net/formulas/sum-if-date-is-greater-than)

In this example, the goal is to sum amounts C5:C16 when the date in B5:B16 is greater than the date provided in cell E5. A good way to solve this problem is with the SUMIFS function . Note: for SUMIFS to work correctly, the worksheet must use valid Excel dates . All dates in Excel have a numeric...

[![Excel formula: Sum if date is between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_date_is_between.png "Excel formula: Sum if date is between")](https://exceljet.net/formulas/sum-if-date-is-between)

### [Sum if date is between](https://exceljet.net/formulas/sum-if-date-is-between)

In this example, the goal is to sum amounts in column C when the date in column B is between two given dates. The start date is provided in cell E5, and the end date is provided in cell F5. The date range should be inclusive - both the start date and end date should be included in the final result...

[![Excel formula: Sum if begins with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_begins_with.png "Excel formula: Sum if begins with")](https://exceljet.net/formulas/sum-if-begins-with)

### [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)

In this example, the goal is to sum the Price in column C when the Product in column B begins with "sha". To solve this problem, you can use either the SUMIF function or the SUMIFS function with the asterisk (\*) wildcard, as explained below. Wildcards Certain Excel functions like SUMIF and SUMIFS...

[![Excel formula: Sum if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_not_blank.png "Excel formula: Sum if not blank")](https://exceljet.net/formulas/sum-if-not-blank)

### [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)

In this example, the goal is to sum the Amounts in C5:C16 when the Lead in D5:D16 is not blank (i.e., not empty). A good way to solve this problem is to use the SUMIFS function . However, you can also use the SUMPRODUCT function or the FILTER function , as explained below. Because SUMPRODUCT and...

[![Excel formula: Sum if cells are equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_equal_to.png "Excel formula: Sum if cells are equal to")](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

### [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when cells in the range C5:C15 contain "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only a single condition. SUMIFS on the other...

[![Excel formula: Sum if cells are not equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_not_equal_to.png "Excel formula: Sum if cells are not equal to")](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

### [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when corresponding cells in the range C5:C15 are not equal to "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only one criteria...

[![Excel formula: Sum if x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_x_or_y.png "Excel formula: Sum if x or y")](https://exceljet.net/formulas/sum-if-x-or-y)

### [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)

In this example, the goal is to sum Total when the corresponding Color is either "Red" or "Blue". For convenience, all data is in an Excel Table named data . This is a tricky problem, because the solution is not obvious. The go-to function for conditional sums is the SUMIFS function . However, when...

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

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

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

[![Excel HSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hstack%20function.png "Excel HSTACK function")](https://exceljet.net/functions/hstack-function)

### [HSTACK Function](https://exceljet.net/functions/hstack-function)

The Excel HSTACK function combines arrays horizontally into a single array. Each subsequent array is appended to the right of the previous array....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20summary%20table-thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

### [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

In this video, I want to show you how to build a quick summary table using the COUNTIF and SUMIF functions. Here we have a sample set of data that shows t-shirt sales. You can see we have columns for date, item, color, and amount. So let's break this data down by color. Now, before we start, I want...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum if date is greater than](https://exceljet.net/formulas/sum-if-date-is-greater-than)
    
*   [Sum if date is between](https://exceljet.net/formulas/sum-if-date-is-between)
    
*   [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)
    
*   [Sum if not blank](https://exceljet.net/formulas/sum-if-not-blank)
    
*   [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)
    
*   [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)
    
*   [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)
    
*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    
*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    
*   [HSTACK Function](https://exceljet.net/functions/hstack-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    
*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    

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