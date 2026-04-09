# Count dates in given year - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-dates-in-given-year

---

[Skip to main content](https://exceljet.net/formulas/count-dates-in-given-year#main-content)

[](https://exceljet.net/formulas/count-dates-in-given-year#)

*   [Previous](https://exceljet.net/formulas/count-dates-by-day-of-week)
    
*   [Next](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)
    

[Count](https://exceljet.net/formulas#Count)

Count dates in given year
=========================

by Dave Bruns · Updated 25 Sep 2022

Related functions 
------------------

[YEAR](https://exceljet.net/functions/year-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count dates in given year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20dates%20in%20given%20year.png "Excel formula: Count dates in given year")

Summary
-------

To count dates in a given year, you can use the [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 and [YEAR](https://exceljet.net/functions/year-function)
 functions. In the example shown, the formula in E5 is:

    =SUMPRODUCT(--(YEAR(dates)=D5))
    

where **dates** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15.

Generic formula
---------------

    =SUMPRODUCT(--(YEAR(dates)=year))

Explanation 
------------

The [YEAR function](https://exceljet.net/functions/year-function)
 extracts the year from a valid [Excel date](https://exceljet.net/glossary/excel-date)
. For example:

    =YEAR("15-Jun-2021") // returns 2021
    

In this case, we are giving YEAR and array of dates in the [named range](https://exceljet.net/glossary/named-range)
  **dates**:

    YEAR(dates)
    

Because dates contains 11 cells, we get back 11 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {2018;2017;2019;2019;2017;2019;2017;2019;2019;2018;2018}
    

Each date is compared to the year in column D, which creates a new array of TRUE FALSE values:

    {FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE}
    

In this array, TRUE corresponds to dates in the year 2017, and FALSE corresponds to dates in different years. Next, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to coerce the TRUE FALSE values to 1's and 0's. Inside SUMPRODUCT, we now have:

    =SUMPRODUCT({0;1;0;0;1;0;1;0;0;0;0})
    

Finally, with only one array to work with, SUMPRODUCT sums the items in the array and returns a result, 3.

_Note: The SUMPRODUCT formula above is an example of using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 in an [array operation](https://exceljet.net/videos/boolean-operations-in-array-formulas)
. This is a powerful and flexible approach to solving many problems in Excel. It is also an important skill with new functions like [FILTER](https://exceljet.net/functions/filter-function)
 and [XLOOKUP](https://exceljet.net/functions/xlookup-function)
, which often use this technique to apply multiple criteria ([FILTER example](https://exceljet.net/videos/filter-with-boolean-logic)
, [XLOOKUP example](https://exceljet.net/formulas/xlookup-with-logical-criteria)
)_

Related formulas
----------------

[![Excel formula: Count dates in current month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20dates%20in%20current%20month.png "Excel formula: Count dates in current month")](https://exceljet.net/formulas/count-dates-in-current-month)

### [Count dates in current month](https://exceljet.net/formulas/count-dates-in-current-month)

At the core, this formula uses the COUNTIFS function to count dates that are greater than or equal to the first day of the current month, and less than the first day of the next month. The EOMONTH function is used to create both dates based on the current date, which is supplied by the TODAY...

[![Excel formula: Count dates by day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20dates%20by%20day%20of%20week.png "Excel formula: Count dates by day of week")](https://exceljet.net/formulas/count-dates-by-day-of-week)

### [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)

You might wonder why we aren't using COUNTIF or COUNTIFS . These functions seem like the obvious solution. However, without adding a helper column that contains a weekday value, there is no way to create criteria for COUNTIF to count weekdays in a range of dates. Instead, we use the versatile...

[![Excel formula: Highlight dates in same month and year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20in%20same%20month%20and%20year.png "Excel formula: Highlight dates in same month and year")](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)

### [Highlight dates in same month and year](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)

This formula uses the TEXT function to concatenate the month and year of each date. Then, the two dates are tested for equality. TEXT is a useful function that allows you to convert a number to text in the text format of your choice. In this case the format is the custom date format "myyyy", which...

[![Excel formula: Count birthdays by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20birthdays%20by%20month.png "Excel formula: Count birthdays by month")](https://exceljet.net/formulas/count-birthdays-by-month)

### [Count birthdays by month](https://exceljet.net/formulas/count-birthdays-by-month)

You would think you could use the COUNTIF function to count birthdays, but the trouble is COUNTIF only works with ranges , and won't let you use something like MONTH to extract just the month number from dates. So, we use the SUMPRODUCT function with custom logic instead. Inside SUMPRODUCT, we have...

Related functions
-----------------

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count dates in current month](https://exceljet.net/formulas/count-dates-in-current-month)
    
*   [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)
    
*   [Highlight dates in same month and year](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)
    
*   [Count birthdays by month](https://exceljet.net/formulas/count-birthdays-by-month)
    

### Functions

*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

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