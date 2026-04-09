# Calculate days open - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-days-open

---

[Skip to main content](https://exceljet.net/formulas/calculate-days-open#main-content)

[](https://exceljet.net/formulas/calculate-days-open#)

*   [Previous](https://exceljet.net/formulas/calculate-date-overlap-in-days)
    
*   [Next](https://exceljet.net/formulas/calculate-days-remaining)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Calculate days open
===================

by Dave Bruns · Updated 9 Aug 2024

Related functions 
------------------

[TODAY](https://exceljet.net/functions/today-function)

[IF](https://exceljet.net/functions/if-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6587/download?token=-BfHBl8i)
 (14.86 KB)

![Excel formula: Calculate days open](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate%20days%20open.png "Excel formula: Calculate days open")

Summary
-------

To calculate the number of days a ticket/case/issue has been "open" (i.e. not resolved) you can use a formula based on the [IF function](https://exceljet.net/functions/if-function)
, with help from the [TODAY](https://exceljet.net/functions/today-function)
 and [ISBLANK](https://exceljet.net/functions/isblank-function)
 functions. In the example shown, the formula in cell E5 is:

    =IF(ISBLANK(D5),TODAY()-C5,D5-C5)
    

When a ticket is open, the result is the number of days since it was opened using the "Opened" date in column C. When a ticket is closed, the result is the number of days between the "Opened" and "Closed" dates.

_Note: this example was updated on August 9, 2024, so the calculations seen in the screen above are relative to that date._

Generic formula
---------------

    =IF(ISBLANK(closed),TODAY()-opened,closed-opened)

Explanation 
------------

In this example, the goal is to calculate the number of days a ticket/case/issue has been open. We start counting on the date a ticket was opened and stop counting on the date a ticket was closed. If there is no closed date, the ticket is still open. Because [dates in Excel are just serial numbers](https://exceljet.net/glossary/excel-date)
, the math is quite simple. We can simply subtract the "Opened" date from the date today, which we calculate with the TODAY function. However, when a ticket is closed, we need a way to stop this calculation so that the "Days open" number doesn't keep increasing.

### Calculating days open with IF

The core operation of this formula is controlled by the [IF function](https://exceljet.net/functions/if-function)
. In pseudo-code, we can write something like this:

    =IF(ticketIsOpen,daysSinceOpened,daysSinceClosed)
    

After we translate this into a proper Excel formula, the formula in cell E5, copied down, is:

    =IF(ISBLANK(D5),TODAY()-C5,D5-C5)
    

To check if a ticket is open, we use the [ISBLANK function](https://exceljet.net/functions/isblank-function)
:

    ISBLANK(D5) // is date closed empty?
    

This is a [logical test](https://exceljet.net/glossary/logical-test)
 that returns either TRUE or FALSE. If the result is TRUE, the ticket is still open. In that case, we run a calculation based on the [TODAY function](https://exceljet.net/functions/today-function)
 to calculate the number of days the ticket has been open:

    TODAY()-C5 // days since opened
    

TODAY returns the current date from which we subtract the date opened. [Both dates are serial numbers](https://exceljet.net/glossary/excel-date)
. As long as the date opened is past, it will be a smaller number. The number of days open will keep increasing as time goes on because the TODAY function will continue to return larger numbers.

If the result from ISBLANK is FALSE, the ticket is closed. In that case, we run a calculation to figure out how many days the ticket was open before being closed:

    D5-C5 // days open before closed
    

Here, we subtract the date opened from the date closed. Once an issue is closed, the result is always the same and doesn't change.

### Simplification

One thing you might notice is that we subtract the open date regardless of whether we use today's date, or the date closed. In other words, -C5 appears in both arguments. This means we can make a slight simplification and use a formula like this:

    =IF(ISBLANK(D5),TODAY(),D5)-C5
    

In this version, we use the IF function only to return the date to start with, _then_ subtract the start date in C5. We can even go further, and replace the IF function altogether with the [MIN function](https://exceljet.net/functions/min-function)
:

    =MIN(D5,TODAY())-C5
    

Here we use MIN to get the smaller of two values: the closed date, or the date today. If the closed date is empty, its value is zero, so the date today will be used. If the closed date is not empty, it's smaller (or equal) to today, and the close date will be used.

Both simplifications are a good example of how formulas in Excel can be often adjusted to reduce length and redundancy, at the risk of becoming more cryptic and less intuitive to the average user.

_Note: The result in column E is formatted in the "General" [number format](https://exceljet.net/shortcuts/apply-number-format)
 to display a number and not a date._

### Conditional formatting for open tickets

The workbook also has one conditional formatting rule applied to highlight rows where tickets have not been closed. The formatting is applied with this formula:

    =ISBLANK($D5)

Notice that because we want to highlight the entire row, we need to lock the reference to column D. To create a rule like this:

1.  Select the range B5:E16.
2.  Home > Conditional Formatting > New rule.
3.  Use a formula to determine which cells to format.
4.  Enter the formula "=ISBLANK($D5)" in the input area.
5.  Select the formatting of your choice.
6.  Click OK to save the rule.

> Video: [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

Related formulas
----------------

[![Excel formula: Get workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workdays%20between%20dates.png "Excel formula: Get workdays between dates")](https://exceljet.net/formulas/get-workdays-between-dates)

### [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can optionally exclude a list of holidays supplied as dates. For example, in the screenshot shown, the formula in D6 is: =NETWORKDAYS(B6,C6...

[![Excel formula: Calculate days remaining](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20days%20remaining.png "Excel formula: Calculate days remaining")](https://exceljet.net/formulas/calculate-days-remaining)

### [Calculate days remaining](https://exceljet.net/formulas/calculate-days-remaining)

Dates in Excel are just serial numbers that begin on January 1, 1900. If you enter 1/1/1900 in Excel, and format the result with the "General" number format , you'll see the number 1. This means that you can easily calculate the days between two dates by subtracting the earlier date from the later...

[![Excel formula: If cell is not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_not_blank_0.png "Excel formula: If cell is not blank")](https://exceljet.net/formulas/if-cell-is-not-blank)

### [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)

The goal is to create a formula that returns "Done" in column E when a cell in column D is not blank (i.e., contains a value). In the worksheet shown, column D records the date a task is completed. If column D contains a date (i.e. is not empty), we can assume the task is complete. This problem can...

[![Excel formula: Due date by category](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/due%20date%20by%20category.png "Excel formula: Due date by category")](https://exceljet.net/formulas/due-date-by-category)

### [Due date by category](https://exceljet.net/formulas/due-date-by-category)

In this example, the goal is to create a due date based on category, where each category has a different number of days allocated to complete a given task, issue, project, etc. The amount of time available to resolve each category is shown in column H, and categories is the named range G5:H7. The...

[![Excel formula: Time since start in day ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/time%20since%20start%20in%20day%20ranges.png "Excel formula: Time since start in day ranges")](https://exceljet.net/formulas/time-since-start-in-day-ranges)

### [Time since start in day ranges](https://exceljet.net/formulas/time-since-start-in-day-ranges)

In this example, the goal is to calculate durations in "days" starting from the start date and time in cell G5 and ending at the dates and times shown in column B. The twist is that we want to classify the durations using the custom labels shown in column E, starting with "Day 0" for the first 24...

[![Excel formula: Time duration with days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/time%20duration%20with%20days.png "Excel formula: Time duration with days")](https://exceljet.net/formulas/time-duration-with-days)

### [Time duration with days](https://exceljet.net/formulas/time-duration-with-days)

In the example shown, the goal is to enter a valid time based on days, hours, and minutes, then display the result as total hours. The key is to understand that time in Excel is just a number. 1 day = 24 hours , and 1 hour = 0.0412 (1/24). That means 12 hours = 0.5, 6 hours = 0.25, and so on...

[![Excel formula: Conditional formatting date past due](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20formatting%20date%20past%20due.png "Excel formula: Conditional formatting date past due")](https://exceljet.net/formulas/conditional-formatting-date-past-due)

### [Conditional formatting date past due](https://exceljet.net/formulas/conditional-formatting-date-past-due)

In this example, we want to apply three different colors, depending on how much the original date varies from the current date: Green if the variance is less than 3 days Yellow if the variance is between 3 and 10 days Red if the variance is greater than 10 days For each rule, we calculate a...

Related functions
-----------------

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")](https://exceljet.net/functions/isblank-function)

### [ISBLANK Function](https://exceljet.net/functions/isblank-function)

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)
    
*   [Calculate days remaining](https://exceljet.net/formulas/calculate-days-remaining)
    
*   [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)
    
*   [Due date by category](https://exceljet.net/formulas/due-date-by-category)
    
*   [Time since start in day ranges](https://exceljet.net/formulas/time-since-start-in-day-ranges)
    
*   [Time duration with days](https://exceljet.net/formulas/time-duration-with-days)
    
*   [Conditional formatting date past due](https://exceljet.net/formulas/conditional-formatting-date-past-due)
    

### Functions

*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    
*   [Replace ugly IFs with MAX or MIN](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
    

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