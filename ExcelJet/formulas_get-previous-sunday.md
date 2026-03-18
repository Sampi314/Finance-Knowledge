# Get previous Sunday - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-previous-sunday

---

[Skip to main content](https://exceljet.net/formulas/get-previous-sunday#main-content)

[](https://exceljet.net/formulas/get-previous-sunday#)

*   [Previous](https://exceljet.net/formulas/get-percent-of-year-complete)
    
*   [Next](https://exceljet.net/formulas/get-project-end-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get previous Sunday
===================

by Dave Bruns · Updated 16 Jun 2022

Related functions 
------------------

[WEEKDAY](https://exceljet.net/functions/weekday-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

![Excel formula: Get previous Sunday](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20previous%20Sunday.png "Excel formula: Get previous Sunday")

Summary
-------

To roll a given date back to the previous Sunday, you can use a formula based on the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
. In the example shown, the formula in D5 is:

    =B5-WEEKDAY(B5,11)
    

As the formula is copied down, it returns the previous Sunday for each date shown in column B. See below to customize the formula to return different days of the week.

Generic formula
---------------

    =date-WEEKDAY(date,11)

Explanation 
------------

In this example, the goal is to calculate the previous Sunday based on any given date. At a high level, this means we need to subtract some number of days from the given date. For example, if the given date is a Monday, we need to subtract 1 day. If the given date is a Tuesday, we need to subtract 2 days, and so on. The main challenge is to figure out how many days to subtract and for this, we use the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
.

_Note: the formulas below use simple math to adjust the date. This works because [Excel dates are large serial numbers](https://exceljet.net/glossary/excel-date)
._

### WEEKDAY solution

The [WEEKDAY function](https://exceljet.net/functions/weekday-function)
 accepts a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable, based on a second argument called _return\_type_. In this example, because we want to roll back the date to the previous Sunday, we want to set WEEKDAY to return 1 for Monday and 7 for Sunday. To do this, we can use either 2 or 11 for return\_type:

    =WEEKDAY(A1,2) // returns 1 for Monday
    =WEEKDAY(A1,11) // returns 1 for Monday
    

Now that we have WEEKDAY returning 1 for Monday and 7 for Sunday, we can simply subtract the result from the given date:

    =B5-WEEKDAY(B5,11)
    

If the date is a Sunday, WEEKDAY will return 7. Subtracting 7 from the original date in B5 will return the previous Sunday. If the date is a Tuesday, weekday will return 2, moving the date back 2 days to Sunday. The formula works the same way for each day of the week.

### Other previous weekdays

In the above formula, you might wonder why we're using 11 for _return\_type_ instead of 2? This is done for consistency To adapt the formula to return different previous weekdays, _return\_type_ needs to be adjusted Using 11 allows the different values to "line up" logically, as seen below:

    =A1-WEEKDAY(A1,11) // previous Sunday
    =A1-WEEKDAY(A1,12) // previous Monday
    =A1-WEEKDAY(A1,13) // previous Tuesday
    =A1-WEEKDAY(A1,14) // previous Wednesday
    =A1-WEEKDAY(A1,15) // previous Thursday
    =A1-WEEKDAY(A1,16) // previous Friday
    =A1-WEEKDAY(A1,17) // previous Saturday
    

To be clear, using 2 instead of 11 for the previous Sunday will work just fine.

### CHOOSE function alternative

One feature of all formulas above is that they subtract days even when the given date is already the target weekday. In other words, if the date is already a Sunday, the result is the Sunday seven days prior. This isn't always desired behavior. Sometimes, the goal is to leave the date alone if it's already the right day of week. One way to accomplish this is with the [CHOOSE function](https://exceljet.net/functions/choose-function)
.

The CHOOSE function is used to select values by numeric position. For example, if we have the colors "red", "blue", and "green", we can use CHOOSE like this:

    =CHOOSE(1,"red", "blue", "green") // returns "red"
    =CHOOSE(2,"red", "blue", "green") // returns "blue"
    =CHOOSE(3,"red", "blue", "green") // returns "green"
    

The first argument is called _index\_num_ and specified the index of the value to return. We can combine CHOOSE and WEEKDAY to give us the correct "roll back" number like this:

    =CHOOSE(WEEKDAY(date),0,1,2,3,4,5,6) // rollback calculation
    

Here, the _index\_num_ argument is provided by the WEEKDAY function. Note WEEKDAY is in its default mode (no _return\_type_ provided), which returns 1 for Sunday and 7 for Saturday. The values that follow WEEKDAY are the actual rollback numbers. The first value is zero, which is the number of days to roll back if the date is already a Sunday. Putting the entire formula together, we get:

    =B5-CHOOSE(WEEKDAY(B5),0,1,2,3,4,5,6) // previous Sunday
    

This formula will return the previous Sunday unless the date is already a Sunday. In that case, CHOOSE will return zero and the formula itself will return the original date unchanged. To extend this idea to handle other days of the week, you can adjust the rollback numbers as needed for each day of the week like this:

    =date-CHOOSE(WEEKDAY(date),0,1,2,3,4,5,6) // prev Sun
    =date-CHOOSE(WEEKDAY(date),6,0,1,2,3,4,5) // prev Mon
    =date-CHOOSE(WEEKDAY(date),5,6,0,1,2,3,4) // prev Tue
    =date-CHOOSE(WEEKDAY(date),4,5,6,0,1,2,3) // prev Wed
    =date-CHOOSE(WEEKDAY(date),3,4,5,6,0,1,2) // prev Thu
    =date-CHOOSE(WEEKDAY(date),2,3,4,5,6,0,1) // prev Fri
    =date-CHOOSE(WEEKDAY(date),1,2,3,4,5,6,0) // prev Sat
    

Alternately, you can adjust the formula to use a _return\_type_ argument in WEEKDAY and leave the rollback values alone:

    =date-CHOOSE(WEEKDAY(date,17),0,1,2,3,4,5,6) // prev Sun
    =date-CHOOSE(WEEKDAY(date,11),0,1,2,3,4,5,6) // prev Mon
    =date-CHOOSE(WEEKDAY(date,12),0,1,2,3,4,5,6) // prev Tue
    =date-CHOOSE(WEEKDAY(date,13),0,1,2,3,4,5,6) // prev Wed
    =date-CHOOSE(WEEKDAY(date,14),0,1,2,3,4,5,6) // prev Thu
    =date-CHOOSE(WEEKDAY(date,15),0,1,2,3,4,5,6) // prev Fri
    =date-CHOOSE(WEEKDAY(date,16),0,1,2,3,4,5,6) // prev Sat
    

Again, the behavior of these formulas is the same as the original formula above except the rollback _does not occur_ if the given date is _already_ the target day of week.

### Custom number formatting

All dates in the example shown use the following [custom number format](https://exceljet.net/articles/custom-number-formats)
:

    ddd d-mmm-yy
    

This number format displays a weekday abbreviation plus a date to make it easier to check results at a glance. The underlying date is unchanged.

Related formulas
----------------

[![Excel formula: Get Monday of the week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20monday%20of%20the%20week.png "Excel formula: Get Monday of the week")](https://exceljet.net/formulas/get-monday-of-the-week)

### [Get Monday of the week](https://exceljet.net/formulas/get-monday-of-the-week)

Imagine you have a random date and want to find the Monday of the week in which the date appears. You can see you will need to "roll back" a specific number of days, depending on what day of the week the given date is. If the date is a Wednesday, you need to roll back 2 days, if the date is a...

[![Excel formula: If Monday, roll back to Friday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20Monday%20roll%20back%20to%20Friday_0.png "Excel formula: If Monday, roll back to Friday")](https://exceljet.net/formulas/if-monday-roll-back-to-friday)

### [If Monday, roll back to Friday](https://exceljet.net/formulas/if-monday-roll-back-to-friday)

The WEEKDAY function returns a number, 1-7, that corresponds to particular days of the week. By default, WEEKDAY assumes a Sunday-based week, and assigns 1 to Sunday, 2 to Monday, and so on, with 7 assigned to Saturday. In this case, we only want to take action if the date in question is Monday. To...

[![Excel formula: Get next day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_next_day_of_week.png "Excel formula: Get next day of week")](https://exceljet.net/formulas/get-next-day-of-week)

### [Get next day of week](https://exceljet.net/formulas/get-next-day-of-week)

In this example, the goal is to get the next specified weekday, starting on a given start date. So for example, with a valid start date in column B, we want to be able to ask for the next Monday, the next Tuesday, the next Wednesday, and so on. This article describes two different ways of solving...

[![Excel formula: Get last weekday in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20weekday%20in%20month.png "Excel formula: Get last weekday in month")](https://exceljet.net/formulas/get-last-weekday-in-month)

### [Get last weekday in month](https://exceljet.net/formulas/get-last-weekday-in-month)

First, this formula determines the first day of the next month \*after\* a given date. It does this my using EOMONTH to get the last day of the month, then adding one day: =EOMONTH(B5,0)+1 Next, the formula calculates the number of days required to "roll back" to the last requested weekday in the...

[![Excel formula: Get first day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_day_of_month.png "Excel formula: Get first day of month")](https://exceljet.net/formulas/get-first-day-of-month)

### [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)

In this example, the goal is to get the first day of the month based on any valid date. This problem can be solved by combining the EOMONTH function with simple addition. The EOMONTH Function The EOMONTH function returns the last day of the month, a given number of months in the past or future. For...

[![Excel formula: Get last day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_day_of_month.png "Excel formula: Get last day of month")](https://exceljet.net/formulas/get-last-day-of-month)

### [Get last day of month](https://exceljet.net/formulas/get-last-day-of-month)

In this example, the goal is to get the last day of the month based on any valid date. This problem can be solved most easily with the EOMONTH function. However, it can also be solved with the DATE function as explained below. The EOMONTH function The EOMONTH function returns the last day of the...

Related functions
-----------------

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get Monday of the week](https://exceljet.net/formulas/get-monday-of-the-week)
    
*   [If Monday, roll back to Friday](https://exceljet.net/formulas/if-monday-roll-back-to-friday)
    
*   [Get next day of week](https://exceljet.net/formulas/get-next-day-of-week)
    
*   [Get last weekday in month](https://exceljet.net/formulas/get-last-weekday-in-month)
    
*   [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)
    
*   [Get last day of month](https://exceljet.net/formulas/get-last-day-of-month)
    

### Functions

*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    

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