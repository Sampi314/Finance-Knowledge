# GROUPBY with monthly totals - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/groupby-with-monthly-totals

---

[Skip to main content](https://exceljet.net/formulas/groupby-with-monthly-totals#main-content)

[](https://exceljet.net/formulas/groupby-with-monthly-totals#)

*   [Previous](https://exceljet.net/formulas/get-row-totals)
    
*   [Next](https://exceljet.net/formulas/groupby-with-survey-results)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

GROUPBY with monthly totals
===========================

by Dave Bruns · Updated 3 Jul 2025

Related functions 
------------------

[GROUPBY](https://exceljet.net/functions/groupby-function)

[HSTACK](https://exceljet.net/functions/hstack-function)

[CHOOSECOLS](https://exceljet.net/functions/choosecols-function)

[TEXT](https://exceljet.net/functions/text-function)

[MONTH](https://exceljet.net/functions/month-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9247/download?token=yAKXlxA0)
 (44.7 KB)

![Excel formula: GROUPBY with monthly totals](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/groupby_with_monthly_totals.png "Excel formula: GROUPBY with monthly totals")

Summary
-------

To generate monthly totals using the [GROUPBY](https://exceljet.net/functions/groupby-function)
 function, you can use a formula that integrates several functions in Excel, including [GROUPBY](https://exceljet.net/functions/groupby-function)
, [CHOOSECOLS](https://exceljet.net/functions/choosecols-function)
, [HSTACK](https://exceljet.net/functions/hstack-function)
, [TEXT](https://exceljet.net/functions/text-function)
, [MONTH](https://exceljet.net/functions/month-function)
, and [SUM](https://exceljet.net/functions/sum-function)
. In the worksheet shown, the formula in cell G5 is:

    =CHOOSECOLS(GROUPBY(HSTACK(TEXT(data[Date],"mmm"),MONTH(data[Date])),data[Total],SUM,,,2,,1),{1,3})
    

The source data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data** in the range B4:E179, which contains daily sales data for the first 6 months of 2025. The result is a total for each month in columns G and H. This is a fully dynamic solution. If the source data in the table changes, the monthly totals will recalculate as needed.

> After I published this article, I got an email from a reader suggesting what I think is an even better approach. The core idea is to leave all of the dates as dates, but to remap them to the first day of each month, then group. See details below under [Formula Alternative #2](https://exceljet.net/formulas/groupby-with-monthly-totals#alternative-formula2)
> .

Explanation 
------------

In this example, the goal is to generate monthly totals using the [GROUPBY](https://exceljet.net/functions/groupby-function)
 function. This is a tricky problem in Excel because typically, source data contains a regular date field and not a separate field with month names. In addition, the GROUPBY function will, by default, sort everything in alphabetical order. This means when we add month names, they will sort A-Z and end up in the wrong order. Part of the challenge is figuring out the best way to sort the month names as part of the GROUPBY formula. To explain how this all works, let's build the solution step by step.

### Table of contents

*   [Excel data for source data](https://exceljet.net/formulas/groupby-with-monthly-totals#excel-data-for-source-data)
    
*   [The core GROUPBY formula](https://exceljet.net/formulas/groupby-with-monthly-totals#the-core-groupby-formula)
    
*   [GROUPBY sort options](https://exceljet.net/formulas/groupby-with-monthly-totals#groupby-sort-options)
    
*   [Adding the month numbers to sort by](https://exceljet.net/formulas/groupby-with-monthly-totals#adding-the-month-numbers-to-sort-by)
    
*   [Sorting the table by month number](https://exceljet.net/formulas/groupby-with-monthly-totals#sorting-the-table-by-month-number)
    
*   [Removing the month numbers](https://exceljet.net/formulas/groupby-with-monthly-totals#removing-the-month-numbers)
    
*   [Summary of steps](https://exceljet.net/formulas/groupby-with-monthly-totals#summary-of-steps)
    
*   [Alternative formula #1](https://exceljet.net/formulas/groupby-with-monthly-totals#alternative-formula1)
    
*   [Alternative formula #2](https://exceljet.net/formulas/groupby-with-monthly-totals#alternative-formula2)
    
*   [Formula for older versions of Excel](https://exceljet.net/formulas/groupby-with-monthly-totals#formula-for-older-versions-of-excel)
    
*   [Final thoughts](https://exceljet.net/formulas/groupby-with-monthly-totals#final-thoughts)
    

### Excel data for source data

The source data is in an Excel Table named data in the range B4:E179, which contains daily sales data for the first 6 months of 2025. It's not necessary to use an Excel table to solve this problem, but it makes the formula a bit easier to read and understand. Plus, it means that the solution is dynamic - if the source data is added or removed, the monthly subtotals will recalculate as needed.

![The source data is in an Excel Table named "data"](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/groupby_with_monthly_totals_source_data.png "The source data is in an Excel Table named "data"")

> Note: The source data contains only the first 6 months of 2025. This is to keep the example simple. The solution will work with any number of months.

### The core GROUPBY formula

The [GROUPBY](https://exceljet.net/functions/groupby-function)
 function excels at grouping data. In this example, we're going to use GROUPBY to group the data by month. The main challenge initially is that we don't have month names in the data. We only have the raw dates. This means we need to create our own month names in the formula. An easy way to do that is to use the [TEXT](https://exceljet.net/functions/text-function)
 function, which allows us to generate month names any way we like using Excel's [custom number format](https://exceljet.net/articles/custom-number-formats)
 codes. In this case, we will abbreviate the month names using the format code "mmm". For example, with a date like 12-Jan-2025 in cell A1, TEXT would return "Jan":

    =TEXT("12-Jan-2025","mmm") // returns "Jan"
    

The complete formula in cell G5 below looks like this:

    =GROUPBY(TEXT(data[Date],"mmm"),data[Total],SUM)

![Excel worksheet showing GROUPBY results with monthly totals, but months are sorted alphabetically (Apr, Feb, Jan, Mar, May, Jun) instead of chronologically](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/groupby_with_monthly_totals_default_sort.png "Excel worksheet showing GROUPBY results with monthly totals, but months are sorted alphabetically (Apr, Feb, Jan, Mar, May, Jun) instead of chronologically")

*   The first argument to GROUPBY is the data to group. Here we use the TEXT function to create the month names as shown above, with the code `=TEXT(data[Date],"mmm")`. The result is a new column of month names derived directly from the dates. This column doesn't actually exist in the source data, but we can use it as a row field in the GROUPBY function.
*   The second argument to GROUPBY is the data to aggregate. In this case, we want to aggregate the sales numbers in the Total column, so we use data\[Total\].
*   The third argument to GROUPBY is the function to use to aggregate the data. Because we want total sales per month, we want to use the [SUM](https://exceljet.net/functions/sum-function)
     function.

This formula works nicely. You can see that we get a clean breakdown by month for the first six months of 2025. However, there is a problem. Notice that the month names do not appear in chronological order. Instead, they are sorted alphabetically. This is because the GROUPBY function sorts grouped values in alphabetical order by default.

### GROUPBY sort options

By default, the GROUPBY function will sort values in standard ascending (A-Z) order, beginning with the leftmost row field. The result is that the month names are sorted alphabetically, starting with "Apr". To override the default sort order, we can provide a value for the [sort\_order argument](https://exceljet.net/functions/groupby-function#sort-options)
, which is given as an index number that can be positive (A-Z) or negative (Z-A). The number itself corresponds to the columns in the table, starting with 1 for the first column. For example, to sort the table by month name in descending (Z-A) order, we can provide -1 for _sort\_order_ in the GROUPBY function, like this:

    =GROUPBY(TEXT(data[Date],"mmm"),data[Total],SUM,,,-1)
    

However, as you can see, that doesn't help. The month names are still sorted alphabetically, but in reverse order, so now the first month name is "May" instead of "Apr":

![Excel worksheet showing GROUPBY results with reverse alphabetical sorting, now starting with "May" instead of "Apr" but still not in chronological order](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/groupby_with_monthly_totals_reverse_sort.png "Excel worksheet showing GROUPBY results with reverse alphabetical sorting, now starting with "May" instead of "Apr" but still not in chronological order")

We'll need to use a different approach.

### Adding the month numbers to sort by

To sort the month names in chronological order, we need a different approach. The core problem is that we only have the month names as text, but what we need to sort in chronological order are _month numbers_. To get the month numbers, we can use the [MONTH](https://exceljet.net/functions/month-function)
 function, which returns the month number for a given date. For example, with a date like 12-Mar-2025, MONTH would return 3:

    =MONTH("12-Mar-2025") // returns 3
    

We can get month numbers for all dates in the source data like this:

    =MONTH(data[Date]) // returns 1-12 for all dates
    

Because there are 175 dates in the source data, this MONTH returns an [array](https://exceljet.net/glossary/array)
 of 175 month numbers. Like the month names, this column does not exist in the source data, but we can add it as a second row field using the [HSTACK](https://exceljet.net/functions/hstack-function)
 function. HSTACK stacks arrays horizontally, which lets us work around the limitation that GROUPBY only allows one row field. We can use it to add the month numbers as a second row field like this:

    =GROUPBY(HSTACK(TEXT(data[Date],"mmm"),MONTH(data[Date])),data[Total],SUM)
    

As you can see, this adds the month numbers as a second row field. The first row field is the month name, and the second row field is the month number.

![GROUPBY results with month numbers added as a second column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/groupby_with_monthly_totals_adding_month_numbers.png "GROUPBY results with month numbers added as a second column")

Notice I've also removed the sort order setting, so we are back to an alphabetical sort. The month numbers appear as a second row field, but the table is still being sorted by the left-most row field, which is the month name.

> Note: We don't really want the month numbers in the table, and we'll get rid of them in a another step below.

### Sorting the table by month number

We are now at the point where we can finally sort the table by month number. To do that, we need to specify the column to sort by as an index number. Because we've added a column, we need to sort by column 2, the month number. We can do that by adding a _sort\_order_ argument to the GROUPBY function like this:

    =GROUPBY(HSTACK(TEXT(data[Date],"mmm"),MONTH(data[Date])),data[Total],SUM,,,2)
    

Unfortunately, this doesn't work. Why? The problem is that GROUPBY uses a hierarchical relationship between row fields by default. This means the month names override the month numbers, because they appear first in the table:

![GROUPBY results where sorting by month number column doesn't work due to hierarchical relationship](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/groupby_with_monthly_totals_sort_by_month_number_not_working.png "GROUPBY results where sorting by month number column doesn't work due to hierarchical relationship")

We need a way to unlink the month names from the month numbers for sorting. We can do that by supplying 1 for the last argument, which is called _field\_relationship_. This tells GROUPBY to use a table relationship instead of a hierarchy relationship:

    =GROUPBY(HSTACK(TEXT(data[Date],"mmm"),MONTH(data[Date])),data[Total],SUM,,,2,,1)
    

![GROUPBY results successfully sorted by month number in chronological order](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/groupby_with_monthly_totals_sort_by_month_number_working.png "GROUPBY results successfully sorted by month number in chronological order")

This works! The month names are no longer overriding the month numbers, and the table is sorted by month number.

> Note: you might wonder about adding the month numbers as the first row field instead of the second. This also works. But one consequence is that the word "Total" will be removed from the table when we remove the month number column in the next step. In the end, I decided to keep the month numbers as the second row field because it makes a good example of how the field relationship argument works. See the [Alternative formula](https://exceljet.net/formulas/groupby-with-monthly-totals#alternative-formula)
>  section below for more details.

### Removing the month numbers

The last step in the problem is to remove the month numbers from the table that displays on the worksheet. We still need the month numbers for sorting, so we need to do this outside of the GROUPBY function. The tool we use for this is the [CHOOSECOLS](https://exceljet.net/functions/choosecols-function)
 function, which is designed to get specific columns from a set of data. In this case, we have three columns total, but we only want to keep columns 1 and 3. Assuming we have a three-column array, we can do that with a generic syntax like this:

    =CHOOSECOLS(array,{1,3}) // keep columns 1 and 3
    

Where array represents the table, and {1,3} is an array of column indices to keep. The final step is to wrap the GROUPBY formula in the CHOOSECOLS function like this:

    =CHOOSECOLS(GROUPBY(HSTACK(TEXT(data[Date],"mmm"),MONTH(data[Date])),data[Total],SUM,,,2,,1),{1,3})
    

You can see the final result in the worksheet below:

![GROUPBY results with months in chronological order and month numbers removed using CHOOSECOLS](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/groupby_with_monthly_totals_final_result.png "GROUPBY results with months in chronological order and month numbers removed using CHOOSECOLS")

We now have data grouped by month with the month names in chronological order.

### Summary of steps

Here's a quick recap of the steps we took:

1.  Started with a basic [GROUPBY](https://exceljet.net/functions/groupby-function)
     using `TEXT(data[Date],"mmm")` to create month names from the dates. Works fine, but the sort order is alphabetical (Apr, Feb, Jan...) instead of chronological.
2.  Tried reversing the sort with `sort_order = -1` but that just flipped the alphabetical order backwards, which still wasn't what we wanted.
3.  Added month numbers using the [HSTACK function](https://exceljet.net/functions/hstack-function)
     because we needed actual numbers (1-12) to sort chronologically.
4.  Set `sort_order = 2` to sort by the month numbers, but this didn't work because GROUPBY was still prioritizing the month names due to its default hierarchical behavior.
5.  Fixed the sorting issue by adding `field_relationship = 1` to break the hierarchy and let the month numbers control the sort order.
6.  Used the [CHOOSECOLS function](https://exceljet.net/functions/choosecols-function)
     to remove the month numbers from the final result since we only need them for sorting, not for display.

### Alternative formula #1

As mentioned above, another way to manage the hierarchy is to reorder the row fields so that the month numbers are the _first_ column:

    =CHOOSECOLS(GROUPBY(HSTACK(MONTH(data2[Date]),TEXT(data2[Date],"mmm")),data2[Total],SUM),{2,3})
    

This formula is a bit simpler because we don't need to use the field relationship at all. However, one consequence of moving the month numbers to the first column and then using CHOOSECOLS to remove the first column is that the word "Total" is also removed:

![Alternative formula #1 with month numbers in the first column and month names in the second column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/groupby_with_monthly_totals_alternative_formula1.png "Alternative formula #1 with month numbers in the first column and month names in the second column")

### Alternative formula #2

After I published this article, I got an email from a reader with what I think is an even better idea. It is certainly simpler. The basic idea is to leave all of the dates as dates, but to remap them to the first day of each month. The GROUPBY function still groups the data by month as before. The big advantage is that there is no need to sort manually. Because the dates that represent month names are valid dates, they sort naturally in chronological order. You can see this approach in the worksheet below, where the formula in G5 looks like this:

    =GROUPBY(EOMONTH(+data3[Date],-1)+1,data3[Total],SUM)

Inside the GROUPBY function, the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 is used to [get the first day of the month](https://exceljet.net/formulas/get-first-day-of-month)
. The effect is to remap all dates to the first of the month so that GROUPBY can group by month as before. As you can see, this formula is much simpler, but there is one extra step: we need to format the month names with the custom date format "mmm".

![Alternative formula #2 - force all dates to "first of month", then group by month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/groupby_with_monthly_totals_alternative_formula2.png "Alternative formula #2 - force all dates to "first of month", then group by month")

Because of its simplicity, I think this is the best solution to this problem. However, I think the learning process that the rest of the article goes through is valuable, especially because it shows an example of when the field relationship argument is important. 

> What is that `+` doing in the EOMONTH formula? Some Excel functions, like [EOMONTH](https://exceljet.net/functions/eomonth-function)
> , resist [spilling](https://exceljet.net/glossary/spill)
>  when provided a range — they won't automatically spill results without extra help. Adding an operator like `+` in front of the range reference forces Excel to evaluate the expression first, which turns the range into an array of values, which EOMONTH can then process. For more details and a list of functions that have this problem, see: [Why some functions won't spill](https://exceljet.net/articles/why-some-excel-functions-wont-spill)
> .

### Formula for older versions of Excel

The GROUPBY formula only works in the latest version of Excel, which contains dynamic array functions like GROUPBY, HSTACK, and CHOOSECOLS. If you are using an older version of Excel, you will need to use a different approach. I think the easiest approach overall is to enter the month names in column G manually. Then you can use a formula based on [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 in column H to get a monthly total like this:

    =SUMPRODUCT(--(TEXT(data2[Date],"mmm")=G5),data2[Total])
    

![Legacy Excel formula based on SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/groupby_with_monthly_totals_formula_for_legacy_excel.png "Legacy Excel formula based on SUMPRODUCT function")

In this worksheet, data2 is the source data in an [Excel Table](https://exceljet.net/articles/excel-tables)
, and G5 is the abbreviated month name. As the formula is copied down, it will return the total for each month. You will then need to calculate a grand total with the SUM function:

    =SUM(H5:H10)
    

This is a fairly simple approach, but it does require manually entering the month names in column G, and the month names will not dynamically update if the source data changes. For more details on how this formula works, see the [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 function page.

### Final thoughts

I've been looking for an example where the field relationship argument in the GROUPBY function is needed, and this is a good one. Even after we add the month numbers for sorting, we still can't sort the months chronologically because of the hierarchy that GROUPBY imposes on row fields. We need to set the field relationship argument to 1 to break the hierarchy and let the month numbers control the sort order. It's worth noting also that the core GROUPBY formula is quite simple. It's the process of sorting the months in the correct order that adds complexity.

Related formulas
----------------

[![Excel formula: GROUPBY with survey results](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/groupby_with_survey_results.png "Excel formula: GROUPBY with survey results")](https://exceljet.net/formulas/groupby-with-survey-results)

### [GROUPBY with survey results](https://exceljet.net/formulas/groupby-with-survey-results)

In May 2025, I ran a survey asking Exceljet newsletter subscribers what version of Excel they use most. This is an important question for Excel learning because the new dynamic array engine has completely changed how many formulas are written. These changes started rolling out after Excel 2019, so...

[![Excel formula: Sum by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_by_month.png "Excel formula: Sum by month")](https://exceljet.net/formulas/sum-by-month)

### [Sum by month](https://exceljet.net/formulas/sum-by-month)

In this example, the goal is to sum the amounts shown in column C by month using the dates in column B. The article below explains two approaches. One approach is based on the SUMIFS function , which can sum numeric values based on multiple criteria. The second approach is based on the SUMPRODUCT...

Related functions
-----------------

[![Excel GROUPBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_groupby_function.png "Excel GROUPBY function")](https://exceljet.net/functions/groupby-function)

### [GROUPBY Function](https://exceljet.net/functions/groupby-function)

The Excel GROUPBY function is designed to summarize data by grouping rows and aggregating values. The result is a summary table created with a single formula.

[![Excel HSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hstack%20function.png "Excel HSTACK function")](https://exceljet.net/functions/hstack-function)

### [HSTACK Function](https://exceljet.net/functions/hstack-function)

The Excel HSTACK function combines arrays horizontally into a single array. Each subsequent array is appended to the right of the previous array....

[![Excel CHOOSECOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choosecols%20function.png "Excel CHOOSECOLS function")](https://exceljet.net/functions/choosecols-function)

### [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)

The Excel CHOOSECOLS function returns specific columns from an array or range. The columns to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a column in the given array.

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [GROUPBY with survey results](https://exceljet.net/formulas/groupby-with-survey-results)
    
*   [Sum by month](https://exceljet.net/formulas/sum-by-month)
    

### Functions

*   [GROUPBY Function](https://exceljet.net/functions/groupby-function)
    
*   [HSTACK Function](https://exceljet.net/functions/hstack-function)
    
*   [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
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