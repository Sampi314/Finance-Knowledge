# Sum by month ignore year - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-by-month-ignore-year

---

[Skip to main content](https://exceljet.net/formulas/sum-by-month-ignore-year#main-content)

[](https://exceljet.net/formulas/sum-by-month-ignore-year#)

*   [Previous](https://exceljet.net/formulas/sum-by-month)
    
*   [Next](https://exceljet.net/formulas/sum-by-month-in-columns)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum by month ignore year
========================

by Dave Bruns · Updated 11 Nov 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[MONTH](https://exceljet.net/functions/month-function)

![Excel formula: Sum by month ignore year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20by%20month%20ignore%20year.png "Excel formula: Sum by month ignore year")

Summary
-------

To sum data by month while ignoring year values you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 and the [MONTH function](https://exceljet.net/functions/month-function)
. In the example shown, the formula in F5 is:

    =SUMPRODUCT((MONTH(date)=MONTH(E5&1))*amount)
    

where **amount** (C5:C16) and **date** (B5:B16) are [named ranges](https://exceljet.net/glossary/named-range)
. The result in F5 is 225, the sum of amounts in January for both 2022 and 2023.  As the formula is copied down, we get a sum of amount by month that ignores years.

Generic formula
---------------

    =SUMPRODUCT((MONTH(date)=number)*amount)

Explanation 
------------

In this example, the goal is to sum numeric values by month while ignoring the year that contains the date. The solution below is based on the SUMPRODUCT function, the MONTH function, and [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
. For convenience, **amount** (C5:C16) and **date** (B5:B16) are [named ranges](https://exceljet.net/glossary/named-range)
.

### Basic concept

The basic concept in this formula is to extract just the month number from all dates and test this number against the month number of interest. For example, to extract the month number of the dates in date, we can use the MONTH function like this:

    MONTH(date)
    

Because the named range **date** contains 12 dates, the result from MONTH is an [array](https://exceljet.net/glossary/array)
 with 12 numbers like this:

    {1;2;2;3;3;3;1;2;2;3;3;3}
    

These twelve numbers correspond to the month numbers of the dates seen in column B. If we want to test these numbers for dates in _January_ (which is the first month in the year), we can write a formula like this:

    =MONTH(date)=1
    

This formula returns an array with 12 TRUE and FALSE values like this:

    {TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

Notice there are two TRUE values in this array, which correspond to the two dates that occur in January: one in 2022 and one in 2023. All remaining values are FALSE, since other dates do not occur in January.

To use this array of Boolean values to sum amounts in January, we can write a formula like this:

    =SUMPRODUCT((MONTH(date)=1)*amount)
    

After the first expression runs, we have the array of TRUE and FALSE values we looked at above:

    =SUMPRODUCT({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}*amount)
    

Next, the math operation of multiplying the two arrays together automatically coerces the TRUE and FALSE values into 1s and 0s, which we can visualize like this:

    =SUMPRODUCT({1;0;0;0;0;0;1;0;0;0;0;0}*amount)
    

Now you can see how the logic works. When the two arrays are multiplied together, the 1s return the corresponding value in **amount**, while the 0s "cancel out" the other amounts. We are left with a single array in SUMPRODUCT like this:

    =SUMPRODUCT({100;0;0;0;0;0;125;0;0;0;0;0})
    

With just one array to process, SUMPRODUCT sums the array and returns 225 as the final result for January. By altering the month number, we can do the same thing for other months:

    =SUMPRODUCT((MONTH(date)=1)*amount) // January
    =SUMPRODUCT((MONTH(date)=2)*amount) // February
    =SUMPRODUCT((MONTH(date)=3)*amount) // March
    

In each case, the year values of the dates being tested are completely ignored.

### Dynamic month

As seen above, we can hardcode month numbers into the formula and get correct results, but how can we make the formula dynamic, so that it will _automatically_ apply the correct month number for each month seen in column F? In the worksheet, the values in F5:F7 are simply text values like "Jan", "Feb", and "Mar". One way to get a month number from a month name is to [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the month name to the number 1, and feed the result into MONTH like this:

    =MONTH(E5&1) // returns 1
    

The result inside of MONTH is the string "Jan1", which Excel interprets as the [date](https://exceljet.net/glossary/excel-date)
 January 1 of the current year, and MONTH returns 1. We can do the same thing with E6 and E7:

    =MONTH(E6&1) // returns 2
    =MONTH(E7&1) // returns 3
    

For a more detailed explanation, [see this example](https://exceljet.net/formulas/month-number-from-name)
.

### Putting it all together

The last step is to combine the ideas above into one formula:

    =SUMPRODUCT((MONTH(date)=MONTH(E5&1))*amount)
    

This is the formula in F5 of the worksheet shown. As the formula is copied down, the month changes at each new row, and SUMPRODUCT calculates the sum of amounts for each month, ignoring year values.

### Count by month ignoring year

Using the same ideas explained above, you can get a count by month like this:

    =SUMPRODUCT(--(MONTH(date)=MONTH(E5&1)))
    

In this formula, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is used to coerce TRUE and FALSE values to 1s and 0s. This step is necessary because we don't have a math operation doing this conversion automatically.

Video: [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

Related formulas
----------------

[![Excel formula: Sum by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_by_month.png "Excel formula: Sum by month")](https://exceljet.net/formulas/sum-by-month)

### [Sum by month](https://exceljet.net/formulas/sum-by-month)

In this example, the goal is to sum the amounts shown in column C by month using the dates in column B. The article below explains two approaches. One approach is based on the SUMIFS function , which can sum numeric values based on multiple criteria. The second approach is based on the SUMPRODUCT...

[![Excel formula: Summary count by month with COUNTIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20by%20month%20with%20COUNTIFS_0.png "Excel formula: Summary count by month with COUNTIFS")](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

### [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

In this example, we have a list of 100 issues in Columns B to D. Each issue has a date and priority. We are also using the named range dates for C5:C104 and priorities for D5:D105. Starting in column F, we have a summary table that shows a total count per month, followed by a total count per month...

[![Excel formula: Count birthdays by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20birthdays%20by%20month.png "Excel formula: Count birthdays by month")](https://exceljet.net/formulas/count-birthdays-by-month)

### [Count birthdays by month](https://exceljet.net/formulas/count-birthdays-by-month)

You would think you could use the COUNTIF function to count birthdays, but the trouble is COUNTIF only works with ranges , and won't let you use something like MONTH to extract just the month number from dates. So, we use the SUMPRODUCT function with custom logic instead. Inside SUMPRODUCT, we have...

[![Excel formula: Average by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_by_month.png "Excel formula: Average by month")](https://exceljet.net/formulas/average-by-month)

### [Average by month](https://exceljet.net/formulas/average-by-month)

In this example, the goal is to calculate a monthly average for the amounts shown in column C using the dates in column B. The article below explains two approaches. One approach is based on the AVERAGEIFS function , which is designed to calculate averages using multiple criteria. The second...

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

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20summary%20table-thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

### [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

In this video, I want to show you how to build a quick summary table using the COUNTIF and SUMIF functions. Here we have a sample set of data that shows t-shirt sales. You can see we have columns for date, item, color, and amount. So let's break this data down by color. Now, before we start, I want...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20operations%20in%20array%20formulas-Play.png)](https://exceljet.net/videos/boolean-operations-in-array-formulas)

### [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

In this video, we'll look at why boolean operations are important in array formulas. Boolean operations are a key building block in the world of dynamic array formulas. To illustrate, let's look at some simple order data. Given the data shown, how can we total orders from Texas using an array...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum by month](https://exceljet.net/formulas/sum-by-month)
    
*   [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)
    
*   [Count birthdays by month](https://exceljet.net/formulas/count-birthdays-by-month)
    
*   [Average by month](https://exceljet.net/formulas/average-by-month)
    
*   [Month number from name](https://exceljet.net/formulas/month-number-from-name)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    

### Videos

*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    
*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    

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