# Date is same month and year - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/date-is-same-month-and-year

---

[Skip to main content](https://exceljet.net/formulas/date-is-same-month-and-year#main-content)

[](https://exceljet.net/formulas/date-is-same-month-and-year#)

*   [Previous](https://exceljet.net/formulas/date-is-same-month)
    
*   [Next](https://exceljet.net/formulas/date-is-workday)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Date is same month and year
===========================

by Dave Bruns · Updated 24 Oct 2024

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[AND](https://exceljet.net/functions/and-function)

[MONTH](https://exceljet.net/functions/month-function)

[YEAR](https://exceljet.net/functions/year-function)

[TEXT](https://exceljet.net/functions/text-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8761/download?token=tYXQe-4F)
 (21.25 KB)

![Excel formula: Date is same month and year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/date_is_same_month_and_year.png "Excel formula: Date is same month and year")

Summary
-------

To test if two dates occur in the same month and year, you can use the [TEXT function](https://exceljet.net/functions/text-function)
. In the example shown, the formula in cell F5 is: 

    =IF(TEXT($B$5,"mmyyyy")=TEXT(D5,"mmyyyy"),"x","") 

As this formula is copied down column F, it returns an "x" when the date in column D occurs in October 2024, which matches the date in B5. The article below explains how this formula works and how it is derived from longer, more complicated solutions.

Generic formula
---------------

    =TEXT(date1,"mmyyyy")=TEXT(date2,"mmyyyy")

Explanation 
------------

In this example, the goal is to mark dates in column D with an "x" when they have the same year and month as the date in cell B5. We don't care at all about the day. At a high level, we can easily use the IF function to return "x" for qualifying dates, so the challenge is in creating a logical test we can use inside IF that will properly test the dates. We want this test to return TRUE when two dates are in the same month and year and FALSE if not.

This problem is an interesting example of how a longer formula can be shortened to a simpler formula by paying attention to how the formula works and looking for ways to accomplish the same thing with less code. This article explains three ways to solve this problem: (1) a classic long-form formula, (2) a medium-form alternative, and (3) the compact short-form formula above.

### Long-form with AND, YEAR, and MONTH

The classic long-form solution breaks each date into parts and uses a combination of the [AND](https://exceljet.net/functions/and-function)
, [YEAR](https://exceljet.net/functions/year-function)
, and [MONTH](https://exceljet.net/functions/month-function)
 functions to perform a logical test. We start with the logic we need: "Given two dates, if the year is the same, and if the month is the same, the result should be TRUE". We can translate this logic into an Excel formula like this:

    =AND(YEAR($B$5)=YEAR(D5),MONTH($B$5)=MONTH(D5))

The literal translation for this formula is: _If the year in B5 is equal to the year in D5 AND if the month in B5 is equal to the month in D5, return TRUE. Otherwise, return FALSE._ Notice that cell B5 is an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 to prevent it from changing as the formula is copied down the column. With 1-Oct-2024 in cell B5 and 11-Oct-2024 in cell D5, the formula evaluates like this:

    =AND(YEAR($B$5)=YEAR(D5),MONTH($B$5)=MONTH(D5))
    =AND(2024=2024,10=10)
    =AND(TRUE,TRUE)
    =TRUE

However, on the next row, where cell D6 contains the date 18-Sep-2024, the formula will evaluate like this:

    =AND(YEAR($B$5)=YEAR(D6),MONTH($B$5)=MONTH(D6))
    =AND(2024=2024,10=9)
    =AND(TRUE,FALSE)
    =FALSE

The last step is to include the logical test above in a formula that will mark dates that pass the test with an "x". We can easily do that with the [IF function](https://exceljet.net/functions/if-function)
 like this:

    =IF(AND(YEAR($B$5)=YEAR(D5),MONTH($B$5)=MONTH(D5)),"x","")

As the formula is copied down, $B$5 is an absolute reference and does not change, while D5 is relative and changes at each new row. The result is that each date in column D is tested against the date in cell B5. When the test returns TRUE, the IF function returns "x". When the test returns FALSE, IF returns an empty string (""). This formula does the job and works fine. However, with a bit of creativity, we can streamline things quite a lot.

### Medium-form with YEAR, MONTH, and concatenation

In the previous long-form formula, our logical test looks like this:

    =AND(YEAR($B$5)=YEAR(D5),MONTH($B$5)=MONTH(D5))

Notice we are using many function calls for a fairly simple problem. Let's see what we can do to shorten things up a bit. If you look at the code, you can see we are extracting the year and month from each date and comparing each pair separately. Then, we use AND to evaluate the two results. Can we compare year and month in one step and eliminate AND? Yes. One way to do it is to join the month and year for each date together and then test the two strings in one step like this:

    =MONTH($B$5)&YEAR($B$5)=MONTH(D5)&YEAR(D5)

This is a small improvement, but it is significant. We've reorganized the functions because we want the year and month for each date together. Because we are testing the year and month in one step, we no longer need the AND function. We combine the values with [concatenation](https://exceljet.net/articles/how-to-concatenate-in-excel)
 using the ampersand (&), creating a text string. For the date in D5, the code above evaluates like this:

    =MONTH($B$5)&YEAR($B$5)=MONTH(D5)&YEAR(D5)
    =10&2024=10&2024
    ="102024"="102024"
    =TRUE

It might seem strange to work with the month and year as a text string, but it creates a human-readable value that contains all the information we need. For example, for a date in October 2024, we'll end up with "102024". After we place this logic inside the IF function, the final medium-form formula looks like this:

    =IF(MONTH($B$5)&YEAR($B$5)=MONTH(D5)&YEAR(D5),"x","")

As with the original solution, this formula will mark all dates in the same month and year with an "x". Can we take this idea further and streamline the formula even more? Yes.

### Short-form with the TEXT function

In the medium-form formula, we've eliminated the AND function by concatenating the year and month for each date together. This gives us a simple text string for each date that we can compare, but we still need to call YEAR and MONTH twice, once for each date. The logical test looks like this:

    =MONTH($B$5)&YEAR($B$5)=MONTH(D5)&YEAR(D5)

How can we take this idea further and make the formula shorter? The trick is to bring in the TEXT function, which can format numbers as text using a variety of special codes. The TEXT function returns a number formatted as text. The format itself is provided as an argument called _format\_text_. Because dates are numbers, we can get a date in the form "mmyyyy" in one step like this:

    =TEXT($B$5,"mmyyyy")

With 1-Oct-2024 in cell B5, TEXT returns the text string "102024", which is exactly what we got with the MONTH and YEAR function in the previous formula. This means we can remove YEAR and MONTH altogether and use only the [TEXT function](https://exceljet.net/functions/text-function)
 like this:

    =TEXT($B$5,"mmyyyy")=TEXT(D5,"mmyyyy")

This formula evaluates the same way as before:

    TEXT($B$5,"mmyyyy")=TEXT(D5,"mmyyyy")
    ="102024"="102024"
    =TRUE

The final formula with the IF function added back in looks like this:

    =IF(TEXT($B$5,"mmyyyy")=TEXT(D5,"mmyyyy"),"x","")

This is a significant improvement. We've reduced function calls by more than half. The reworked formula is more compact, easier to read, and easier to extend, due to the flexibility of the TEXT function.

> The date format could be provided as "mmyyyy" or "yyyymm" with the same result. If you are working with dates that will always be in the same century, you could abbreviate the format to "mmyy" or "yymm". For more information on number formats, see [Excel Custom Number Formats](https://exceljet.net/articles/custom-number-formats)
> .

### Summary

This article explains three formulas to check if two dates share the same month and year, beginning with a traditional long-form solution and ending with a more elegant short-form solution based on the TEXT function. By switching from separate YEAR and MONTH function calls to TEXT with a date format like "mmyyyy", we were able to cut the total number of function calls in half:

1.  Long-form (6 function calls): IF, AND, YEAR(2), and MONTH(2)
2.  Medium form (5 function calls): IF, YEAR(2) and MONTH(2)
3.  Short form (3 function calls): IF and TEXT(2)

Each method is a bit more compact and efficient than the previous one. This problem is a good example of how a better understanding of Excel's functions can lead to simpler, more elegant formulas. It's also a great demonstration of the versatility of the [TEXT function](https://exceljet.net/functions/text-function)
.

Related formulas
----------------

[![Excel formula: Date is same month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Date%20is%20same%20month.png "Excel formula: Date is same month")](https://exceljet.net/formulas/date-is-same-month)

### [Date is same month](https://exceljet.net/formulas/date-is-same-month)

In this case, Excel extracts the month from the date in cell B6 as a number, and the month in the cell C6 as a number, then tests for equivalency using the equal sign. Both dates are in January, so the formula is solved as follows and returns TRUE. =MONTH(B6)=MONTH(C6) =1=1 =TRUE Same month as...

[![Excel formula: Highlight dates in same month and year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20in%20same%20month%20and%20year.png "Excel formula: Highlight dates in same month and year")](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)

### [Highlight dates in same month and year](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)

This formula uses the TEXT function to concatenate the month and year of each date. Then, the two dates are tested for equality. TEXT is a useful function that allows you to convert a number to text in the text format of your choice. In this case the format is the custom date format "myyyy", which...

[![Excel formula: Get same date next month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20same%20date%20next%20month.png "Excel formula: Get same date next month")](https://exceljet.net/formulas/get-same-date-next-month)

### [Get same date next month](https://exceljet.net/formulas/get-same-date-next-month)

The EDATE function returns a date on the same day of the month, n months in the past or future. You can use EDATE to calculate expiration dates, maturity dates, and other due dates. When 1 is given for months , EDATE returns the same date in the next month. Notice that EDATE automatically handles...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Date is same month](https://exceljet.net/formulas/date-is-same-month)
    
*   [Highlight dates in same month and year](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)
    
*   [Get same date next month](https://exceljet.net/formulas/get-same-date-next-month)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    

### Articles

*   [Excel custom number formats](https://exceljet.net/articles/custom-number-formats)
    

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