# Happy birthday message - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/happy-birthday-message

---

[Skip to main content](https://exceljet.net/formulas/happy-birthday-message#main-content)

[](https://exceljet.net/formulas/happy-birthday-message#)

*   [Previous](https://exceljet.net/formulas/get-year-from-date)
    
*   [Next](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Happy birthday message
======================

by Dave Bruns · Updated 13 May 2022

Related functions 
------------------

[TEXT](https://exceljet.net/functions/text-function)

[TODAY](https://exceljet.net/functions/today-function)

[IF](https://exceljet.net/functions/if-function)

[AND](https://exceljet.net/functions/and-function)

[MONTH](https://exceljet.net/functions/month-function)

[DAY](https://exceljet.net/functions/day-function)

![Excel formula: Happy birthday message](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/happy%20birthday%20message.png "Excel formula: Happy birthday message")

Summary
-------

To display "Happy Birthday" when the current date matches a known birthday, you can use a formula based on the [TEXT function](https://exceljet.net/functions/text-function)
 with help from the [IF function](https://exceljet.net/functions/if-function)
 and the [TODAY function](https://exceljet.net/functions/today-function)
. In the example shown, the formula in E5, copied down, is:

    =IF(TEXT(C5,"mmdd")=TEXT(TODAY(),"mmdd"),"Happy Birthday, "&B5&"!","")
    

As the formula is copied down, it will return a "Happy Birthday!" when a birthday in column C matches the current date. Otherwise, the formula will return [empty string](https://exceljet.net/glossary/empty-string)
 (""), which displays as a blank cell.

Generic formula
---------------

    =IF(TEXT(A1,"mmdd")=TEXT(TODAY(),"mmdd"),"Happy Birthday!","")

Explanation 
------------

In this example, the goal is to display a Happy Birthday message when a birthday in a given cell matches the current date. The core of the problem is to compare the given birthday to the current date while ignoring the year. There are two main ways to approach the problem. The first way is to use the MONTH function and the DAY function to compare the birthday in column C to the current date. This works fine, but the formula is a bit more complex. The second way is to use the TEXT function with a [custom number format](https://exceljet.net/articles/custom-number-formats)
 to compare the birthday in column C to the current date. This solution is a bit more elegant. Both methods are described below.

### The long way

The traditional "long way" solution to this problem is to use a formula like this:

    =IF(AND(MONTH(C5)=MONTH(TODAY()),DAY(C5)=DAY(TODAY())),"Happy Birthday!","")
    

Working from the inside out, the [logical test](https://exceljet.net/glossary/logical-test)
 inside the [IF function](https://exceljet.net/functions/if-function)
 is based on the [AND function](https://exceljet.net/functions/and-function)
:

    AND(MONTH(C5)=MONTH(TODAY()),DAY(C5)=DAY(TODAY()))
    

Inside the AND function, there are two logical expressions, one that checks the month, and one that checks the day:

    MONTH(C5)=MONTH(TODAY()) // check month
    DAY(C5)=DAY(TODAY()) // check day
    

The [MONTH function](https://exceljet.net/functions/month-function)
 returns the month for a given date as a number (i.e. MONTH returns 5 for a date in May) . The [DAY function](https://exceljet.net/functions/day-function)
 returns the day portion of a date. The [TODAY function](https://exceljet.net/functions/today-function)
 returns the current date.  Essentially, the logical expressions inside the AND function check to see if the month and day both match. We purposely ignore the year for birthdays, since the year only matches in the first year of birth.

The AND function will only return TRUE if both the month and the day match, which means we have a birthday that lands on the current date. When AND returns TRUE,the IF function will return "Happy Birthday!" as a result. If either the month or day do not match, AND will return FALSE and the IF function will return an [empty string](https://exceljet.net/glossary/empty-string)
 (""). This formula works fine, but the TEXT function can streamline the formula somewhat, as explained below.

### TEXT function

The [TEXT function](https://exceljet.net/functions/text-function)
 can also be used to solve this problem in a more elegant way. The TEXT function is used to apply [custom number formats](https://exceljet.net/articles/custom-number-formats)
 inside a formula. By using a number format that contains only the month and day, we can check both values at the same time. In the worksheet shown, the formula in E5 is:

    =IF(TEXT(C5,"mmdd")=TEXT(TODAY(),"mmdd"),"Happy Birthday!","")
    

Inside the [IF function,](https://exceljet.net/functions/if-function)
 the logical test is:

    TEXT(C5,"mmdd")=TEXT(TODAY(),"mmdd")
    

Here, the TEXT function is used to apply the [number format](https://exceljet.net/glossary/number-format)
 "mmdd" to both the date in column C and the current date, supplied by the [TODAY function](https://exceljet.net/functions/today-function)
. In the worksheet shown, the date in C5 is January 15, 1999 and the current date is May 13, 2022. With these dates, the TEXT function returns a text string that includes both the month and day like this:

    =TEXT(TODAY(),"mmdd") // returns "0513"
    =TEXT(C6,"mmdd") // returns "0115"
    

These values don't match, so the logical test returns FALSE and the IF function returns an empty string (""). However, in row 12 where the date in C12 is May 13, 1999, we have:

    =TEXT(TODAY(),"mmdd") // returns "0513"
    =TEXT(C12,"mmdd") // returns "0513"
    

Here the text values match. The logical test returns TRUE and the IF function returns "Happy Birthday!" as a result.

### Message with name

To include the first name in the Happy Birthday message, you can [concatenate](https://exceljet.net/glossary/concatenation)
 the name from column B like this :

    =IF(TEXT(C5,"mmdd")=TEXT(TODAY(),"mmdd"),"Happy Birthday, "&B5&"!","")
    

For an overview of concatenation with more formula examples, see: [How to concatenate in Excel](https://exceljet.net/articles/how-to-concatenate-in-excel)
.

Related formulas
----------------

[![Excel formula: Get age from birthday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20age%20from%20birthdate.png "Excel formula: Get age from birthday")](https://exceljet.net/formulas/get-age-from-birthday)

### [Get age from birthday](https://exceljet.net/formulas/get-age-from-birthday)

The DATEDIF function (Date + Dif) is a bit of an anomaly in Excel. A compatibility function that comes originally from Lotus 1-2-3, Excel will not help supply arguments when the function is entered. However, DATEDIF works in all modern versions of Excel and is a useful function for calculating the...

[![Excel formula: Count birthdays by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20birthdays%20by%20month.png "Excel formula: Count birthdays by month")](https://exceljet.net/formulas/count-birthdays-by-month)

### [Count birthdays by month](https://exceljet.net/formulas/count-birthdays-by-month)

You would think you could use the COUNTIF function to count birthdays, but the trouble is COUNTIF only works with ranges , and won't let you use something like MONTH to extract just the month number from dates. So, we use the SUMPRODUCT function with custom logic instead. Inside SUMPRODUCT, we have...

[![Excel formula: Sort birthdays by month and day](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sort%20birthdays%20by%20month%20and%20day.png "Excel formula: Sort birthdays by month and day")](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)

### [Sort birthdays by month and day](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)

In this example, the goal is to sort a list of names and birthdays by month and year. The complication is that the birthdays also include a birth year, so if we try to sort the raw data by birthdays, we'll end up with a list of birthdays sorted first by year. We will actually see the oldest people...

[![Excel formula: List upcoming birthdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20upcoming%20birthdays.png "Excel formula: List upcoming birthdays")](https://exceljet.net/formulas/list-upcoming-birthdays)

### [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)

In this example, the goal is to list the next n upcoming birthdays from a larger set of 25 birthdays based on the current date. The set of birthdays are in an Excel Table named data in the range B5:C29. In the example shown, we are using 7 for n , so the result will be the next 7 upcoming birthdays...

Related functions
-----------------

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

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

[![Excel DAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_day_function.png "Excel DAY function")](https://exceljet.net/functions/day-function)

### [DAY Function](https://exceljet.net/functions/day-function)

The Excel DAY function returns the day of the month as a number between 1 and 31 from a given date. DAY is commonly combined with the [YEAR function](https://exceljet.net/functions/year-function)
 and [MONTH function](https://exceljet.net/functions/month-function)
 to take apart dates for manipulation, and...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get age from birthday](https://exceljet.net/formulas/get-age-from-birthday)
    
*   [Count birthdays by month](https://exceljet.net/formulas/count-birthdays-by-month)
    
*   [Sort birthdays by month and day](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)
    
*   [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)
    

### Functions

*   [TEXT Function](https://exceljet.net/functions/text-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [DAY Function](https://exceljet.net/functions/day-function)
    

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