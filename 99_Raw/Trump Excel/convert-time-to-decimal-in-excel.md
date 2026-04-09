# Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)

**Source:** https://trumpexcel.com/convert-time-to-decimal-in-excel

---

[Skip to content](https://trumpexcel.com/convert-time-to-decimal-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-time-to-decimal-in-excel/#below-title)

By default, date and time are saved as numbers/decimals in Excel. But you often see it in different formats because of the way the cells have been formatted.

For example, in the below example, the value in column A and B is the same, but these are displayed differently because of the format.

![Same value but different formats of time in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20390%20157'%3E%3C/svg%3E)

And one of the things many people need in Excel is to **convert the time to decimal** (such as hours or minutes or seconds).

For example, instead of having the date and time as **_01-01-2020 6:30 AM_**, you may want the get:

*   Number of hours as 6
*   Number of minutes as 30

Thankfully Excel has some awesome formulas, you can easily convert time to decimal values.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/convert-time-to-decimal-in-excel/#)

How to Convert Time to Decimal Numbers in Excel
-----------------------------------------------

In this tutorial, I will show you some examples of converting time to a decimal using formulas (i.e, converting time to hours, minutes, and seconds).

There are multiple ways to **convert time to decimal in Excel**:

*   Using arithmetic operation is the easiest way to convert time to decimal numbers. For example:
    *   To convert time to hours, multiply the time value with **24**
    *   To convert time to minutes, multiply the time value with **24\*60**
    *   To convert time to seconds, multiply the time value with **24\*60\*60**
*   You can also use Excel in-built formulas such as **CONVERT** or **HOUR/MINUTE/SECOND**

In the sections that follow, I will show you examples of how to convert Excel time to decimal values using these methods.

So let’s get started!

### Convert Time to Hours in Excel

In this section, I cover three different ways to convert time to hours in Excel.

#### Using Simple Multiplication to Get the Hour Value

Suppose you have the time in a cell as 6:00 PM  (in cell A2) and you want to convert it into hours.

You can simply multiply it by 24 and it will give you how many hours have elapsed till that time.

\=A2\*24

![Convert Time to Hours using simple multiplication](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20160'%3E%3C/svg%3E)

This works because of the fact that Excel stores dates and times as numbers. A full day (24 hours) is stored as 1 in Excel. This means that each hour is stored as 1/24.

So while you see the value 6:00 PM, in the backend, it is stored as the value 0.75 (indicating that 18 hours out of the 24 hours have already passed). So, when you multiply it with 24, it gives you the number of hours that have passed.

In case you have a value such as 6:32 PM, using the above formula will give you the result as 18.53 (where the minutes/seconds part is shown in decimals and full/complete hours as integers). In this example, the numeric value of 32 minutes in Excel would be 0.53 hours.

Note: In case you get the hour value that has the decimals (such as 18.53), make you sure you have formatted it to show the decimals as well. In case you haven’t, you may see the result as 19, as Excel shows you the rounded off integer value. However, this wouldn’t change the value in the cell, which will continue to be 18.53

In case you only want the complete/full hour value and ignore the minutes part, use the below formula using INT.

\=INT(A2\*24)

![Use INT formula to get full hour value only](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20433%20158'%3E%3C/svg%3E)

INT only gives you the integer part and you don’t have to worry about any extra minutes.

#### Using Excel Functions (HOUR, MINUTE, and SECOND)

If you don’t like the manual multiplication method, another really easy way to convert time to hours is by using the inbuilt time-related  functions ([HOUR](https://trumpexcel.com/excel-hour-function/)
, [MINUTE](https://trumpexcel.com/excel-minute-function/)
, and [SECOND](https://trumpexcel.com/excel-second-function/)
)

Suppose, you have the times as shown below and you want to know how many hours have elapsed in the day.

![Time to Convert to Hour Value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20165'%3E%3C/svg%3E)

Below is the formula to convert the time into hours

\=HOUR(A2)+MINUTE(A2)/60+SECOND(A2)/(60\*60)

![Convert Time to Decimal with Hour Minute Second Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20703%20212'%3E%3C/svg%3E)

The HOUR function simply returns the number of hours that have elapsed in the given time, and so does the MINUTE and SECOND function.

But since we need the final value in hours, we need to divide the minute value by 60 (to convert it into hours) and the second value by 60\*60 (again to convert it into hours).

#### Using the Convert Function

Another really easy (probably the easiest of the three methods), is to use the CONVERT function.

This function takes a numerical value (which would be the time in this case) and can convert it into hours (or minutes/seconds).

Below is the formula that will convert time into hours:

\=CONVERT(A2,"day","hr")

![Convert Time to Decimal using the CONVERT function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20514%20214'%3E%3C/svg%3E)

The second argument is to tell the function of the existing data format and the third argument is the format to which you want to convert.

**Note**: Sometimes the results may look different than expected. This could be due to the cell format which may show the result in a date format instead of decimal format. You can easily change this by going to the Home tab and setting the format from the format drop-down (it’s in the Number group)

_In practice, you’re more likely to get date and time together (instead of just the time as I have shown in the examples above). You can still use the methods shown above, but you first need to split the date and time value and then use the methods shown above on only the time part. Later in this tutorial, I also cover two methods to separate date and time in Excel using formulas._

You can also use these same methods covered above to convert time to minutes and seconds.

Let’s quickly have a look at those examples as well.

### Convert Time to Minutes in Excel

In this section, I cover three different ways to convert time to minutes in Excel.

#### Using Simple Multiplication to Get the Minute Value

In a day, there are 1440 minutes (24\*60).

So, to convert time to minutes, you can simply multiply the time value with 1440.

Suppose you have the time in a cell as 6:00 PM  (in cell A2) and you want to convert it into minutes.

Below is the formula to do this:

\=A2\*1440

![Convert time to minutes with simple multiplication](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20414%20213'%3E%3C/svg%3E)

This will give you the total number of minutes that have elapsed on that day in the given time.

Note: Remember that in case you have seconds as well in the time, these will be converted into minutes and be shown as the decimal part. For these to be visible in the result, you need to format the resulting cells to show results up to 2/3 decimal places.

In case you only want the minute value and ignore the seconds part, use the below formula using INT.

\=INT(A2\*1440)

![Convert time to minute and only get full minutes and not seconds](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20445%20215'%3E%3C/svg%3E)

#### Using Excel Functions (HOUR, MINUTE, and SECOND)

Just like we used these functions to get the hour value, you can also use these to convert time to minutes.

Below is the formula that will convert time to minutes using these functions:

\=HOUR(A2)\*60+MINUTE(A2)+SECOND(A2)/60

![Convert time to minutes using formulas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20665%20212'%3E%3C/svg%3E)

Since the aim here to get all the parts in minutes (hours, minutes, and seconds), we multiply 60 with hours to get the minutes value in it and we divide seconds by 60 to get the minute value.

#### Using the Convert Function

Again, definitely the easiest way to convert time to minutes is by using the convert formula.

The below formula takes the time value and converts it into minutes;

\=CONVERT(A2,"day","mn")

![Convert time to minute using the CONVERT function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20527%20212'%3E%3C/svg%3E)

The second argument tells the function that the value in cell A2 is in day format and the third argument (“mn”) tells it to convert it into minutes.

### Convert Time to Seconds in Excel

In this section, I cover three different ways to convert time to seconds in Excel.

#### Using Simple Multiplication to Get the Seconds Value

In a day, there are 86400 seconds (24\*60\*60).

So, to convert time to seconds, you can simply multiply the time value with 86400.

Suppose you have the time in a cell as 6:32:30 PM  (in cell A2) and you want to convert it into seconds.

Below is the formula to do this:

\=A2\*86400

![Convert Time to seconds with simple arithmetic multiplication](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20424%20217'%3E%3C/svg%3E)

This will give you the total number of seconds that have elapsed on that day in the given time.

#### Using Excel Functions (HOUR, MINUTE, and SECOND)

Below is the formula that will convert time to minutes using these functions:

\=HOUR(A2)\*60\*60+MINUTE(A2)\*60+SECOND(A2)

![Convert time to minutes using HOUR MINUTE SECOND formulas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20694%20212'%3E%3C/svg%3E)

Since the aim here to get all the parts (hours, minutes, and seconds) in seconds, we multiply 60\*60 with hours to get the seconds value in it and we multiply minutes by 60 to get the seconds value.

Split Date and Time and Then Convert Time to Decimal
----------------------------------------------------

So far, we have seen examples where we only have the time and we wanted to convert that time into hours, minutes or seconds.

But what if you have the date as well as the time?

In that case, you can not use the above methods directly. You will first have to split the date and time and then convert the time to decimals.

Since date and time are stored as numbers in Excel, separating these gets easier.

A full day is stored as an integer and the time part is stored as a decimal value. So if you want to separate date and time, you simply need to separate the integer part and the decimal part.

Let’s have a look at a couple of really easy ways to split the date and time in Excel.

### Split Date and Time using INT Formula

Suppose you have the dataset as shown below and you want to split the date and time.

![Date and time that needs to be split](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20156'%3E%3C/svg%3E)

To do this, enter the following formula in cell B2:

\=A2-INT(A2)

![Split date and time using INT function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20218'%3E%3C/svg%3E)

The above formula removes the integer part and gives you the decimal part of the date.

Now you can use any of the three methods covered above (using arithmetic multiplication, using HOUR/MINUTE/SECOND formula, or using the CONVERT formula) to convert the time to decimal.

**Also read:** [How to Convert Seconds to Minutes in Excel (Easy Formula)](https://trumpexcel.com/convert-seconds-to-minutes-excel/)

### Split Date and Time using the MOD Formula

Another way to do this can be by using the MOD function.

Suppose you have the dataset as shown below and you want to split the date and time.

To do this, enter the following formula in cell B2:

\=MOD(A2,1)

![Split Date and Time using MOD function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20482%20213'%3E%3C/svg%3E)

This would give you the decimal part right away and then you can use any of the three methods covered above to convert time to decimal numbers (hours, minutes, or seconds).

**You may also like the following Excel tutorials:**

*   [Calculate Time in Excel (Time Difference, Hours Worked, Add/ Subtract)](https://trumpexcel.com/calculate-time-in-excel/)
    
*   [How to Remove Time from Date/Timestamp in Excel](https://trumpexcel.com/remove-time-from-date-in-excel/)
    
*   [How to Insert Date and Timestamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    
*   [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    
*   [Convert Date to Text in Excel](https://trumpexcel.com/convert-date-to-text-excel/)
    
*   [How to Stop Excel from Changing Numbers to Dates](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/)
    
*   [How to Stop Excel from Rounding Numbers (Decimals/Fractions)](https://trumpexcel.com/stop-excel-from-rounding-numbers/)
    
*   [How to Display Numbers as Fractions in Excel (Write Fractions in Excel)](https://trumpexcel.com/display-numbers-as-fractions-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)”
--------------------------------------------------------------------------------

1.  I am using “YearFrac” for months, but the two dates added together don’t equal a year?  
    using YEARFRAC(B2,B3)\*12.  
    Jan 01, 2024 to Jun 30, 2024 – results 5.967.  
    Jul 01, 2024 to Dec 31, 2024 – result 6.00.  
    5.967 + 6.00 do not = 12 months.  
    YearFrac is supposed to accommodate Leap Year.
    
    [Reply](https://trumpexcel.com/convert-time-to-decimal-in-excel/#comment-30986)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-time-to-decimal-in-excel/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK