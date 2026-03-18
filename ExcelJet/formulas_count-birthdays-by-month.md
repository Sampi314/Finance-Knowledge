# Count birthdays by month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-birthdays-by-month

---

[Skip to main content](https://exceljet.net/formulas/count-birthdays-by-month#main-content)

[](https://exceljet.net/formulas/count-birthdays-by-month#)

*   [Previous](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime)
    
*   [Next](https://exceljet.net/formulas/count-calls-at-specific-times)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Count birthdays by month
========================

by Dave Bruns · Updated 1 Apr 2021

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[MONTH](https://exceljet.net/functions/month-function)

![Excel formula: Count birthdays by month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20birthdays%20by%20month.png "Excel formula: Count birthdays by month")

Summary
-------

To count the number of birthdays in a list, by month, you can use a formula based on the [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 and [MONTH](https://exceljet.net/functions/month-function)
 functions. In the example shown, E5 contains this formula:

    =SUMPRODUCT(--(MONTH(birthdays)=MONTH(D5&1)))
    

where birthdays is the [named range](https://exceljet.net/glossary/named-range)
 (B5:B104), which contains 100 random birthdays. As the formula is copied down, it returns the total count of birthdays in each month as listed.

Generic formula
---------------

    =SUMPRODUCT(--(MONTH(birthdays)=MONTH("name"&1)))

Explanation 
------------

You would think you could use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 to count birthdays, but the trouble is [COUNTIF only works with ranges](https://exceljet.net/articles/excels-racon-functions)
, and won't let you use something like MONTH to extract just the month number from dates. So, we use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 with custom logic instead.

Inside SUMPRODUCT, we have this expression:

    MONTH(birthdays)=MONTH(D5&1)
    

On the right, the [MONTH function](https://exceljet.net/functions/month-function)
 extracts the month for each date in the [named range](https://exceljet.net/glossary/named-range)
 "birthdays". On the right, the MONTH function is used to get a number for each month name shown in the table. This is a standard number between 1-12, and the details of this formula are [explained here](https://exceljet.net/formulas/month-number-from-name)
.

The results from these two expressions are then compared. Because we are working with 100 birthdays, the result is an array of 100 TRUE / FALSE values, where each TRUE represents a date where month numbers from the birthdays are the same as the month number from the name in column D. Next, the TRUE FALSE values are then converted to ones and zeros with the [double negative (--)](https://exceljet.net/glossary/double-unary)
.

In cell E5, the resulting array looks like this inside SUMPRODUCT:

    =SUMPRODUCT({0;0;1;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;1;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0})
    

SUMPRODUCT then sums these numbers and returns a final result, in this case, 9. As the formula is copied down, it returns the total count of birthdays in each month as listed.

### Dealing with empty cells

If you have blank cells in the list of birthdays, you will get incorrect results, since MONTH (0) returns 1. To handle blank cells, you can adjust the formula as follows:

    =SUMPRODUCT((MONTH(birthdays)=MONTH(D5&1))*(birthdays<>""))
    

Multiplying by the expression (birthdays<>"") effectively cancels out values for empty cells. See the [SUMPRODUCT page](https://exceljet.net/functions/sumproduct-function)
 for more information about how [logical expressions](https://exceljet.net/glossary/logical-test)
 work inside SUMPRODUCT.

### Pivot table solution

A pivot table is an [excellent solution for this problem](https://exceljet.net/pivot-tables/pivot-table-count-birthdays-by-month)
 as well.

Related formulas
----------------

[![Excel formula: Count cells between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20cells%20between%20two%20numbers_0.png "Excel formula: Count cells between two numbers")](https://exceljet.net/formulas/count-cells-between-two-numbers)

### [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)

In this example, the goal is to count numbers that fall within specific ranges. The lower value comes from the "Start" column, and the upper value comes from the "End" column. For each range, we want to include both the lower value and the upper value. For convenience, the numbers being counted are...

[![Excel formula: Summary count by month with COUNTIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20by%20month%20with%20COUNTIFS_0.png "Excel formula: Summary count by month with COUNTIFS")](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

### [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

In this example, we have a list of 100 issues in Columns B to D. Each issue has a date and priority. We are also using the named range dates for C5:C104 and priorities for D5:D105. Starting in column F, we have a summary table that shows a total count per month, followed by a total count per month...

[![Excel formula: Count dates by day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20dates%20by%20day%20of%20week.png "Excel formula: Count dates by day of week")](https://exceljet.net/formulas/count-dates-by-day-of-week)

### [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)

You might wonder why we aren't using COUNTIF or COUNTIFS . These functions seem like the obvious solution. However, without adding a helper column that contains a weekday value, there is no way to create criteria for COUNTIF to count weekdays in a range of dates. Instead, we use the versatile...

[![Excel formula: Month number from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/month%20number%20from%20name.png "Excel formula: Month number from name")](https://exceljet.net/formulas/month-number-from-name)

### [Month number from name](https://exceljet.net/formulas/month-number-from-name)

In this example, the goal is to return a number, 1-12, for any month name of the year. For example, given the string "January" we want to return 1, "February" should return 2, and so on. If we had a valid Excel date , we could use a number format for this task, but because we are starting with a...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)
    
*   [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)
    
*   [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)
    
*   [Month number from name](https://exceljet.net/formulas/month-number-from-name)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    

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