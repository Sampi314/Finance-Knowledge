# Year is a leap year - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/year-is-a-leap-year

---

[Skip to main content](https://exceljet.net/formulas/year-is-a-leap-year#main-content)

[](https://exceljet.net/formulas/year-is-a-leap-year#)

*   [Previous](https://exceljet.net/formulas/working-days-left-in-month)
    
*   [Next](https://exceljet.net/formulas/biweekly-pay-schedule)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Year is a leap year
===================

by Dave Bruns · Updated 18 Apr 2024

Related functions 
------------------

[DATE](https://exceljet.net/functions/date-function)

[YEAR](https://exceljet.net/functions/year-function)

[MONTH](https://exceljet.net/functions/month-function)

[MOD](https://exceljet.net/functions/mod-function)

[AND](https://exceljet.net/functions/and-function)

[OR](https://exceljet.net/functions/or-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8270/download?token=3CmAUf-J)
 (22.49 KB)

![Excel formula: Year is a leap year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/year_is_leap_year.png "Excel formula: Year is a leap year")

Summary
-------

To test whether the year of a certain date is a leap year, you can use a formula that uses the [MONTH](https://exceljet.net/functions/month-function)
, [YEAR](https://exceljet.net/functions/year-function)
, and [DATE](https://exceljet.net/functions/date-function)
 functions. In the example shown, the formula in cell C5 is:

    =MONTH(DATE(YEAR(B5),2,29))=2
    

As the formula is copied down, it returns TRUE if the year in column B is a leap year and FALSE if not.

_Note: This formula works fine for dates after 1900, but will fail on earlier dates. See below for a full explanation and a more robust formula that will work for earlier years._

Generic formula
---------------

    =MONTH(DATE(YEAR(date),2,29))=2

Explanation 
------------

In this example, the goal is to write a formula that will return TRUE if a year is a leap year and FALSE if not. This is a surprisingly challenging problem in Excel for two reasons: (1) Excel thinks 1900 is a leap year due to a long-standing bug inherited from Lotus 1-2-3 and (2) The logic for testing a leap year is not intuitive and requires some understanding of the history of the Gregorian calendar system we use today. Both topics are discussed in more detail below.

### Quick and dirty solution

In the worksheet shown above, we use a quick and dirty formula to check for leap years. The core of this formula is the [DATE function](https://exceljet.net/functions/date-function)
, which will automatically adjust to month and year values that are out of range. In the formula, the year is extracted with the [YEAR function](https://exceljet.net/functions/year-function)
. Then it is passed into the DATE function, along with 2 for the month (February) and 29 for the day:

    DATE(YEAR(B5),2,29)

Then we wrap the [MONTH function](https://exceljet.net/functions/month-function)
 around that formula and check if the month is 3:

    =MONTH(DATE(YEAR(B5),2,29))=2 // returns TRUE or FALSE

What's going on here? The answer depends on a subtle behavior in Excel's date system. In a leap year, February has 29 days, so the DATE function will simply return the date February 29 in the given year. For example, when the year is 1960, DATE returns the valid date 29-Feb-1960:

    DATE(1960,2,29) // returns "29-Feb-1960"

However, in a _non-leap year_, DATE will return March 1 in the given year, because _there is no 29th day in February_. In other words, the DATE function rolls the date forward to the next valid date. For example, if we change the year to 1961, we get the date 1-Mar-1961:

    DATE(1961,2,29) // returns "1-Mar-1961"

The MONTH function then extracts the month from the date and checks if the month number is 2. If the result is TRUE, we have a leap year. If the result is FALSE (the month is 3), the year is not a leap year.

### Testing the year only

In the worksheet shown, we are extracting the year from a date with the YEAR function before testing for a leap year. To test a year value only, just remove the YEAR function from the formula:

    =MONTH(DATE(year,2,29))=2
    

In this version, we don't extract a year value from a date, we pass a year value (i.e. 1960) directly to the DATE function.

### Limitations

Although the formulas above are clever and efficient, they have two limitations you should be aware of:

1.  They incorrectly report 1900 as a leap year (see below for details).
2.  They only work with dates/years after January 1, 1900.

These limitations arise because the formulas are built directly on Excel's date system. The first limitation is easy to work around, as explained in the next section. The second limitation is more fundamental and requires a different approach.

### Excel's 1900 problem

[Excel erroneously treats 1900 as a leap year](https://learn.microsoft.com/en-us/office/troubleshoot/excel/wrongly-assumes-1900-is-leap-year)
. This is due to a legacy bug from compatibility with Lotus 1-2-3, an older spreadsheet application that _also_ erroneously treated 1900 as a leap year. Unfortunately, this means the formulas above will incorrectly return TRUE if you are testing for a leap year with dates in 1900. You can guard against this problem with a simple hack like this:

    =AND(MONTH(DATE(YEAR(B5),2,29))=2,YEAR(B5)<>1900)

This version of the formula enforces two conditions with the [AND function](https://exceljet.net/functions/and-function)
:

1.  The month of the adjusted date must be 2.
2.  The year must not be equal to 1900.

Both conditions must be TRUE or else the formula will return FALSE. This is a simple way to avoid classifying 1900 as a leap year. However, to test year values earlier than 1900, we need a new approach, because Excel's date functions will only work with dates beginning with January 1, 1900. However, before we look at a solution, I need to introduce the Julian and Gregorian calendars.

### The Julian and Gregorian calendars

The formulas below don't make sense unless you know a little about the history of the [Julian and Gregorian Calendars](https://www.nottingham.ac.uk/manuscriptsandspecialcollections/researchguidance/datingdocuments/juliangregorian.aspx#:~:text=The%20Julian%20Calendar%20was%20the,not%20a%20straight%20365%20days.)
. The Julian Calendar was a system of dates instituted by Julius Caesar in 46 BC. This calendar added one extra day every four years, based on the calculation that it takes 365.25 days for the earth to travel around the sun, not exactly 365 days. The idea was to account for an extra day every four years, creating a "leap year". However, it turns out this calculation is not correct. The sun's trip around the sun is not exactly 365.25 days but 365.24237 days, approximately 11 minutes less. As a result, the Julian Calendar was over-correcting by about 8 days every 1000 years. 

Further study in the 16th century resulted in a better solution. The idea was that centenary years would not be leap years _unless they were divisible by 400_. This meant three out of four centenary years _would not_ be leap years. In other words, every 400 years there would be 97 leap years instead of 100 leap years. In 1582, Pope Gregory ruled that the new date system (called the "Gregorian Calendar" thereafter) should replace the Julian Calendar. In simple language, [the rule for leap years](https://www.rmg.co.uk/stories/topics/which-years-are-leap-years-can-you-have-leap-seconds)
 is as follows:

_To be a leap year, the year number must be divisible by four – except for end-of-century years, which must be divisible by 400. This means that 2000 is a leap year, but 1700, 1800, and 1900 are not leap years._

The long-form formula below is meant to follow this logic.

### Classic leap year formula

Now that we understand the basic history of leap years in our calendar system, we can look at how to implement a leap year rule in Excel. To handle years before 1900, we need a math-based formula that doesn't require Excel's date functions. The classic long-form formula to test for a leap year looks like this:

    =IF(MOD(A1,400)=0,TRUE,IF(MOD(A1,100)=0,FALSE,IF(MOD(A1,4)=0,TRUE,FALSE)))

Here, A1 contains a year value like 1985, 2005, etc. This formula uses the [MOD function](https://exceljet.net/functions/mod-function)
 to test if the year is evenly divisible by 400, 100, and 4 and applies this logic to determine if the year is a leap year:

1.  If the year is divisible by 400, it's a leap year (TRUE).
2.  If the year is not divisible by 400 but is divisible by 100, it is _not_ a leap year (FALSE)
3.  If the year is not divisible by 100 but is divisible by 4, it's a leap year (TRUE).

The same logic can be condensed by replacing the nested IF construction above with the AND and OR functions like this:

    =OR(MOD(A1,400)=0,AND(MOD(A1,4)=0,MOD(A1,100)<>0))

1.  If the year is divisible by 400, it's a leap year (TRUE).
2.  Or if the year is divisible by 4 and not divisible by 100, it's a leap year (TRUE)
3.  Otherwise, the year is not a leap year (FALSE).

Both formulas above work well, and both correctly report 1900 as a non-leap year. The formulas are a bit longer and less intuitive, but both formulas can be used to test year values _before_ 1900. By contrast, the original "short" formulas at the top of this page depend on Excel's date engine and won't handle dates or years before 1900.

Related formulas
----------------

[![Excel formula: Sequence of leap years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_leap_years.png "Excel formula: Sequence of leap years")](https://exceljet.net/formulas/sequence-of-leap-years)

### [Sequence of leap years](https://exceljet.net/formulas/sequence-of-leap-years)

In this example, the goal is to generate a list of leap years between a given start year and end year. The worksheet is set up so that the start year is an input in cell B5 and the end year is an input in cell B8. If either value changes, the formula should generate a new list of leap years. In the...

Related functions
-----------------

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sequence of leap years](https://exceljet.net/formulas/sequence-of-leap-years)
    

### Functions

*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [OR Function](https://exceljet.net/functions/or-function)
    

### Links

*   [Excel Bible (John Walkenbach)](http://spreadsheetpage.com/)
    
*   [Lots of ways to test for leap year (Chandoo)](http://chandoo.org/wp/2012/02/29/check-leap-year-using-excel/)
    

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