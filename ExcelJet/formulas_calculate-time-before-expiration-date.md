# Calculate time before expiration date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-time-before-expiration-date

---

[Skip to main content](https://exceljet.net/formulas/calculate-time-before-expiration-date#main-content)

[](https://exceljet.net/formulas/calculate-time-before-expiration-date#)

*   [Previous](https://exceljet.net/formulas/calculate-retirement-date)
    
*   [Next](https://exceljet.net/formulas/calculate-years-between-dates)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Calculate time before expiration date
=====================================

by Dave Bruns · Updated 11 Jul 2024

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[DATEDIF](https://exceljet.net/functions/datedif-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8375/download?token=r97ToeRv)
 (22.34 KB)

![Excel formula: Calculate time before expiration date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate_time_before_expiration_date.png "Excel formula: Calculate time before expiration date")

Summary
-------

To calculate the time remaining before a given expiration date, you can use a formula based on the [IF function](https://exceljet.net/functions/if-function)
 and some simple date arithmetic. In the example shown, the formula in E5 is:

    =IF(C5>cdate,C5-cdate&" days","Expired")

In this formula, "cdate" is the [named range](https://exceljet.net/glossary/named-range)
 G5, which contains the current date. As the formula is copied down, it calculates the time before expiration (in days) for each item. See below for an explanation of how to solve this problem with two other approaches, including one that outputs the time in years, months, and days, and one that outputs the remaining time to expiration as a percentage of the total shelf life.

Generic formula
---------------

    ​=IF(A1>date,A1-date&" days","Expired")

Explanation 
------------

In this example, the goal is to calculate the time remaining before an expiration date. There are many ways to do something like this in Excel, and in this article, we'll look at three different approaches:

1.  Calculating the remaining time in days
2.  Calculating the remaining time in years, months, and days
3.  Calculating the percentage of shelf life remaining.

Each approach includes an explanation of how the formula works.

### Important notes

1.  Examples use the named range "cdate", which points to a cell that contains the "current date". This makes it easy to change the date used to calculate the remaining time. This also makes it possible to calculate results based on a future date. For example, you can easily change the date to the first of next month to evaluate expiration dates as of that date.
2.  If you prefer, you can replace the hardcoded date in _cdate_ with the [TODAY function](https://exceljet.net/functions/today-function)
    , so that it always contains the current date. However, be aware that over time more and more items will appear as expired in this particular example.
3.  You should be familiar with the concept of [concatenation in Excel](https://exceljet.net/articles/how-to-concatenate-in-excel)
    , the process of joining values together in text strings.

### How Excel Tracks Time

Excel tracks time using its date system, which is [based on serial numbers](https://exceljet.net/glossary/excel-date)
. Each date is represented as a unique serial number, where January 1, 1900, is serial number 1, January 2, 1900, is serial number 2, and so on. This system allows you to perform date arithmetic easily in Excel. For example, subtracting one date from another yields the number of days between the two dates. Understanding this date system is important for creating and working with date-related formulas in Excel.

### Approach 1: Calculating Time in Days

The simplest approach is to calculate the remaining time in _days_, which takes advantage of Excel's built-in date system and requires no special date functions. In the worksheet below, the formula in cell E5 is:

    =IF(C5>cdate,C5-cdate&" days","Expired")

![Calculating the time before expiration date in days](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/time_before_expiration_date_days_example.png "Calculating the time before expiration date in days")

The logic of the formula works as follows. At a high level, the IF function controls the flow of the formula. Inside IF, the logical test is configured to check if the expiration date (C5) is greater than the current date (_cdate_):

    =IF(C5>cdate,

Excel dates are just serial numbers underneath, so if the expiration date in C5 is larger than the "current" date (cdate) it means the date is still in the future. The logical test will return TRUE and the formula will subtract _cdate_ from C5 and concatenate "days " to the result:

    =IF(C5>cdate,C5-cdate&" days",

Otherwise, the expiration date in C5 is not larger than the current date, which means the expiration has already been reached. In that case, the logical test will return FALSE and the IF function will return "Expired" as a result.

### Approach 2: Calculating Time in Years, Months, and Days

Another approach is to calculate the time remaining in years, months, and days. This requires a more elaborate formula based on the DATEDIF function. In the worksheet below, the formula in cell E5, with line breaks\* added for readability, looks like this:

    =IF(C5>cdate,
    DATEDIF(cdate,C5,"y")&" years, "&
    DATEDIF(cdate,C5,"ym")&" months, " &
    DATEDIF(cdate,C5,"md")&" days",
    "Expired")

![Calculating the time before expiration date in years, months, and days](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/time_before_expiration_date_years_months_days_example.png "Calculating the time before expiration date in years, months, and days")

Here, we calculate the time remaining before the expiration date in a combination of years, months, and days all concatenated together in a text string. The tricky part of the problem is that we need to ensure we are correctly "backing out" the time units we have already accounted for. Luckily, the [DATEDIF function](https://exceljet.net/functions/datedif-function)
 is designed just for this purpose.

At the top level, this formula again uses the IF function to control flow by first testing the expiration date to ensure it is still in the future. If so, we calculate a final result with three separate calls to DATEDIF. If not, we simply return "Expired":

    =IF(C5>cdate,...,"Expired")

When the expiration date is greater than the current date, we call DATEDIF three times like this:

    DATEDIF(cdate,C5,"y")&" years, "&
    DATEDIF(cdate,C5,"ym")&" months, " &
    DATEDIF(cdate,C5,"md")&" days",

*   DATEDIF(cdate,C5,"y") - Calculate the number of complete years between the current date and the expiration date.
*   DATEDIF(cdate,C5,"ym") - Calculate the number of complete months, ignoring the years.
*   DATEDIF(cdate,C5,"md") - Calculate the number of days, ignoring the years and months.

The three results are then concatenated into a single text string, which IF returns as the final result. [See this page](https://exceljet.net/formulas/get-days-months-and-years-between-dates)
 for a more detailed example of this approach, including a simplified formula based on the [LET function](https://exceljet.net/functions/let-function)
.

_\*You can add line breaks to a formula in Excel with the [Keyboard Shortcut](https://exceljet.net/shortcuts)
 Alt + Enter._

### Approach 3: Calculating Percentage of Shelf Life Remaining

In this last approach, we calculate the percentage of the shelf life that remains. Note that this requires us to have a "Packed" or "Manufactured" date to calculate the product's total shelf life. In the worksheet below, the formula in cell F5, copied down, is:

    =(D5-cdate)/(D5-C5)

![Calculating the time before expiration as a percentage of shelf life](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/time_before_expiration_date_shelf_life_percentage_example.png "Calculating the time before expiration as a percentage of shelf life")

One key difference between this formula and the two previous formulas is that we are not using the IF function to control flow. Instead, we are simply calculating a percentage and allowing negative percentage results to pass through. The formula used in the worksheet is:

    =(D5-cdate)/(D5-C5)

*   (D5-cdate) - Calculate the time to expiration in days, by subtracting the current date (cdate) from the packed date (D5).
*   (D5-C5) - Calculate the total shelf life in days, by subtracting packed date (C5) from the expiration date (D5).
*   Divide time to expiration in days by total shelf life in days

The result is a number like 0.338 that must be then [formatted as a percentage](https://exceljet.net/glossary/percentage-number-format)
.

### Creating an expiration date

To create an expiration date based on a given date you can simply add the number of days until expiration. With a date in A1:

    =A1+30 // 30 days in the future
    =A1+90 // 90 days in the future
    

Alternatively, you can use the [EDATE function](https://exceljet.net/functions/edate-function)
 to calculate in months:

    =EDATE(A1,1) // 1 month in the future
    =EDATE(A1,3)  // 3 months in the future
    

Both options above will work fine, but one advantage of EDATE is that it will preserve the day from the original date in A1.

Related formulas
----------------

[![Excel formula: Calculate days remaining](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20days%20remaining.png "Excel formula: Calculate days remaining")](https://exceljet.net/formulas/calculate-days-remaining)

### [Calculate days remaining](https://exceljet.net/formulas/calculate-days-remaining)

Dates in Excel are just serial numbers that begin on January 1, 1900. If you enter 1/1/1900 in Excel, and format the result with the "General" number format , you'll see the number 1. This means that you can easily calculate the days between two dates by subtracting the earlier date from the later...

[![Excel formula: Highlight dates in the next N days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20in%20the%20next%20n%20days.png "Excel formula: Highlight dates in the next N days")](https://exceljet.net/formulas/highlight-dates-in-the-next-n-days)

### [Highlight dates in the next N days](https://exceljet.net/formulas/highlight-dates-in-the-next-n-days)

The AND function takes multiple arguments and returns TRUE only when all arguments return TRUE. The TODAY function returns the current date. Dates in Excel are simply large serial numbers, so you can create a new relative date by adding or subtracting days. TODAY() + 30 creates a new date 30 days...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel DATEDIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_datedif_function_0.png "Excel DATEDIF function")](https://exceljet.net/functions/datedif-function)

### [DATEDIF Function](https://exceljet.net/functions/datedif-function)

The Excel DATEDIF function returns the difference between two date values in years, months, or days. DATEDIF supports six unit codes that let you calculate complete years, complete months, total days, and partial intervals. DATEDIF is a "compatibility" function inherited from Lotus 1-2-3....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20expiration%20dates.png)](https://exceljet.net/videos/how-to-calculate-and-highlight-expiration-dates)

### [How to calculate and highlight expiration dates](https://exceljet.net/videos/how-to-calculate-and-highlight-expiration-dates)

In this video we'll look at how to calculate and highlight expiration dates. Let's say your company has started a membership program of some kind and your boss just sent you a set of data. She's given you a list of 1,000 people that have renewed a membership in the last year or so, and she's...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Calculate days remaining](https://exceljet.net/formulas/calculate-days-remaining)
    
*   [Highlight dates in the next N days](https://exceljet.net/formulas/highlight-dates-in-the-next-n-days)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [DATEDIF Function](https://exceljet.net/functions/datedif-function)
    

### Videos

*   [How to calculate and highlight expiration dates](https://exceljet.net/videos/how-to-calculate-and-highlight-expiration-dates)
    

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