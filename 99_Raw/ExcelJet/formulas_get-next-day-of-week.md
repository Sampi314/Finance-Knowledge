# Get next day of week - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-next-day-of-week

---

[Skip to main content](https://exceljet.net/formulas/get-next-day-of-week#main-content)

[](https://exceljet.net/formulas/get-next-day-of-week#)

*   [Previous](https://exceljet.net/formulas/get-most-recent-day-of-week)
    
*   [Next](https://exceljet.net/formulas/get-next-scheduled-event)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get next day of week
====================

by Dave Bruns · Updated 13 Mar 2024

Related functions 
------------------

[MATCH](https://exceljet.net/functions/match-function)

[TEXT](https://exceljet.net/functions/text-function)

[WEEKDAY](https://exceljet.net/functions/weekday-function)

![Excel formula: Get next day of week](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_next_day_of_week.png "Excel formula: Get next day of week")

Summary
-------

To get the next specified weekday (i.e. the next Monday, the next Tuesday, the next Wednesday, etc.) starting from a given start date, you can use a formula based on the [MATCH function](https://exceljet.net/functions/match-function)
 and the [TEXT function](https://exceljet.net/functions/text-function)
. In the example shown, the formula in E5 is:

    =B5+MATCH(C5,TEXT(B5+{0,1,2,3,4,5,6},"ddd"),0)-1

Where B5 contains a start date, and C5 contains the target weekday, given as the 3-letter abbreviation "Mon". The result is Monday, October 2, 2023 — the first Monday after Friday, September 29, 2023. 

Generic formula
---------------

    =A1+MATCH("Mon",TEXT(A1+{0,1,2,3,4,5,6},"ddd"),0)-1

Explanation 
------------

In this example, the goal is to get the next specified weekday, starting on a given start date. So for example, with a valid start date in column B, we want to be able to ask for the next Monday, the next Tuesday, the next Wednesday, and so on. This article describes two different ways of solving this problem. The first way, which appears in the worksheet shown above, is based on the TEXT function and the MATCH function. This method is flexible and intuitive since you can simply ask for the desired day of the week by name. The second method is based on the WEEKDAY function. This is the "traditional approach", although I find it harder to understand. Both approaches are explained below, and both work equally well.

> _I've now added a third option to solve this problem with the WORKDAY.INTL function below. This last approach is the simplest option, but it does involve using some cryptic custom codes. Also, note that the first two options will return the start date if it is already the target day of the week. The last option will always advance to the next target day of the week, even if the start date is already the target day of the week._

### MATCH + TEXT option

One way to solve this problem is with the [MATCH function](https://exceljet.net/functions/match-function)
 and the [TEXT function](https://exceljet.net/functions/text-function)
 using a generic formula like this:

    =A1+MATCH("Mon",TEXT(A1+{0,1,2,3,4,5,6},"ddd"),0)-1

In this formula, we assume the start date is in cell A1, and that our target day of the week is Monday, abbreviated "Mon". Here's how this formula works, working from the inside out:

1.  **A1+{0,1,2,3,4,5,6}**: This creates an [array](https://exceljet.net/glossary/array)
     of dates that includes the start date plus the next six days.
2.  **TEXT(A1+{0,1,2,3,4,5,6},"ddd")**: This converts each date in the array to a text string representing the abbreviated day of the week (e.g., "Sun", "Mon", "Tue", etc.).
3.  **MATCH("Mon",TEXT(A1+{0,1,2,3,4,5,6},"ddd"),0)**: This searches for the position of the specified day ("Mon" for Monday) in the array of abbreviated day names. The position becomes the number of days to add to the original date in A1 to reach the next specified weekday.
4.  **\-1**: Since the array includes the current day, we subtract 1 to adjust the position to the correct number of days to add.
5.  **A1 +** : Finally, the number of days calculated above is added to the original date in A1 to get the date of the next specified weekday.

The main trick in this formula is this: TEXT(A1+{0,1,2,3,4,5,6},"ddd"). Excel evaluates this part of the formula in E5 as follows:

    =TEXT(B5+{0,1,2,3,4,5,6},"ddd")
    =TEXT(45198+{0,1,2,3,4,5,6},"ddd")
    =TEXT({45198,45199,45200,45201,45202,45203,45204},"ddd")
    ={"Fri","Sat","Sun","Mon","Tue","Wed","Thu"}

What we see above is that the date in cell B5 (September 29, 2023) is serial number 45198 in [Excel's date system](https://exceljet.net/glossary/excel-date)
. When we add the array constant {0,1,2,3,4,5,6} to this number, we get an array that represents Sep. 29 plus the next 6 days. The text string "ddd" is a [custom number format](https://exceljet.net/articles/custom-number-formats)
 for a 3-letter abbreviation for weekday names. TEXT runs on all seven dates and returns their abbreviated names in an array like this:

    {"Fri","Sat","Sun","Mon","Tue","Wed","Thu"}

When we drop this array back into the original formula, we get the following:

    =B5+MATCH(C5,{"Fri","Sat","Sun","Mon","Tue","Wed","Thu"},0)-1
    =B5+MATCH("Mon",{"Fri","Sat","Sun","Mon","Tue","Wed","Thu"},0)-1
    =B5+4-1
    =45198+4-1
    =45201

With "Mon" in cell C5, MATCH returns 4, and the final result is 45201, which is Monday, October 2, 2023.

This formula is intuitive and flexible since you can easily change the target day by replacing "Mon" with the abbreviation of another day of the week. It will return the original date in A1 if it is already the specified weekday, and the next occurrence of the specified weekday otherwise. There is no need to know the numeric values for each day, as with the WEEKDAY formula below.

### WEEKDAY option

Another more traditional way to solve this problem is with the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
. The WEEKDAY function takes a date and returns a number between 1-7 representing the day of the week. By default, WEEKDAY uses a scheme where Sunday =1, Monday=2, Tuesday=3, Wednesday=4, Thursday=5, Friday=6, and Saturday=7. So, for example, WEEKDAY returns 6 for September 29, 2023, which is a Friday:

    =WEEKDAY("29-Sep-2023") // returns 6

We can use this behavior to create a formula that returns the next given weekday with a generic formula like this:

    =A1+7-WEEKDAY(A1+7-n)

Where A1 contains the start date, and n represents the day number of the weekday you want. So for example, in the first formula below n is 7 to get the next Saturday while in the second formula n is 2 to get the next Monday:

    =A1+7-WEEKDAY(A1+7-7) // next Saturday
    =A1+7-WEEKDAY(A1+7-2) // next Monday

You can see this approach used in the worksheet below, where start dates appear in column B, and the target weekday is specified with a day number in column C:

![WEEKDAY option for getting the next specified day of week](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/get_next_day_of_week_weekday_option.png "WEEKDAY option for getting the next specified day of week")

_Notes: (1) The table in G5:H11 is a key for day numbers, provided for reference only. (2) When the given date is already the desired day of week, the original date is returned._

This formula is more difficult to understand than the first formula. The gist is that it first rolls the date forward by 7 days, then steps back to the correct date by subtracting the result of a calculation that uses the WEEKDAY function. Working from the inside out, here are the steps

1.  **A1 + 7**: Moves forward 7 days to the same weekday of the _next week_.
2.  **A1 + 7 - n**: Shifts back by n days to a "reference day". The result depends on the weekday provided as n.
3.  **WEEKDAY(A1 + 7 - n)**: Calculates the weekday number of the reference day.
4.  **A1 + 7 - WEEKDAY(A1 + 7 - n)**: Subtracts the weekday number of the reference day from the date calculated in step 1.

The key is the reference day calculated by A1 + 7 - n. This reference day is always in the same week as the original date A1. By calculating the WEEKDAY of the reference day and subtracting it from A1 + 7, we are essentially finding the next occurrence of the desired weekday in the current week. For example, assume A1 contains the date Sep 29, 2023 (which is a Friday), and n is given as 2 (for Monday):

1.  **A1 + 7**: Sep 29, 2023 + 7 days = Oct 6, 2023 (a Friday).
2.  **A1 + 7 - n**: Oct 6, 2023 - 2 (since n is 2 for Monday) = Oct 4, 2023 (a Wednesday).
3.  **WEEKDAY(A1 + 7 - n)**: WEEKDAY(Oct 4, 2023) = 4 (Wednesday is 4 in the default scheme).
4.  **A1 + 7 - WEEKDAY(A1 + 7 - n**): Oct 6, 2023 - 4  = Oct 2, 2023 (a Monday).

The final result is Oct 2, 2023, the next Monday after the given date.

### Next day of week from today

To get the next day of week starting with the current date, you can use the TODAY function in place of a date in A1 like so:

    =TODAY()+7-WEEKDAY(TODAY()+7-n)
    

### WORKDAY.INTL option

Many months after I wrote the article above, I ran into another way to solve this problem with the [WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)
 function and a generic formula like this:

    =WORKDAY.INTL(start_date, 1, "custom_code")

WORKDAY.INTL calculates the "next" working day n days in the past or future, taking into non-working days and (optionally) holidays. In the formula above, _start\_date_ is the date to start from, and 1 is _days -_ the number of days to move forward. The tricky part is the "custom\_code" provided for the _weekend_ argument, which involves "hacking" a hidden feature of WORKDAY.INTL.

The third argument in WORKDAY.INTL is _weekend_, which specifies which days of the week should be treated as weekends. Normally provided as a [numeric code](https://exceljet.net/functions/workday.intl-function#weekend_codes)
, weekday can also be provided as a 7-digit binary code that covers all seven days of the week, Monday through Saturday. In this scheme, a 1 indicates a weekend (non-working) day, and a 0 indicates a workday. For example, to get the next regular workday Monday through Friday, you can use the code "0000011" like this:

    =WORKDAY.INTL(A1,1,"0000011") // next workday, Mon-Fri

_Note: Zeros are "workdays" and the 1s are "weekends"._

By carefully creating a code that only allows one day of the week, we can hijack this feature and use the WORKDAY.INTL function to find the next target day of the week like this:

    =WORKDAY.INTL(A1,1,"0111111") // next Monday
    =WORKDAY.INTL(A1,1,"1011111") // next Tuesday
    =WORKDAY.INTL(A1,1,"1101111") // next Wednesday
    =WORKDAY.INTL(A1,1,"1110111") // next Thursday
    =WORKDAY.INTL(A1,1,"1111011") // next Friday
    =WORKDAY.INTL(A1,1,"1111101") // next Saturday
    =WORKDAY.INTL(A1,1,"1111110") // next Sunday

This formula is simpler than either of the two formulas above, but there is one key difference: it will always advance to the next target day of week, even if the start date is already the target day of the week. 

Related formulas
----------------

[![Excel formula: Get Monday of the week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20monday%20of%20the%20week.png "Excel formula: Get Monday of the week")](https://exceljet.net/formulas/get-monday-of-the-week)

### [Get Monday of the week](https://exceljet.net/formulas/get-monday-of-the-week)

Imagine you have a random date and want to find the Monday of the week in which the date appears. You can see you will need to "roll back" a specific number of days, depending on what day of the week the given date is. If the date is a Wednesday, you need to roll back 2 days, if the date is a...

[![Excel formula: If Monday, roll back to Friday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20Monday%20roll%20back%20to%20Friday_0.png "Excel formula: If Monday, roll back to Friday")](https://exceljet.net/formulas/if-monday-roll-back-to-friday)

### [If Monday, roll back to Friday](https://exceljet.net/formulas/if-monday-roll-back-to-friday)

The WEEKDAY function returns a number, 1-7, that corresponds to particular days of the week. By default, WEEKDAY assumes a Sunday-based week, and assigns 1 to Sunday, 2 to Monday, and so on, with 7 assigned to Saturday. In this case, we only want to take action if the date in question is Monday. To...

[![Excel formula: Get most recent day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_most_recent_day_of_week.png "Excel formula: Get most recent day of week")](https://exceljet.net/formulas/get-most-recent-day-of-week)

### [Get most recent day of week](https://exceljet.net/formulas/get-most-recent-day-of-week)

In this example, the goal is to create a formula that will return the most recent day of the week, given a date and a target day of the week, abbreviated as "dow" in the generic formula. Excel tracks the day of the week internally as a specific number for each of the seven days. By default, Excel...

Related functions
-----------------

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

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
    
*   [Get most recent day of week](https://exceljet.net/formulas/get-most-recent-day-of-week)
    

### Functions

*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    
*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    

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