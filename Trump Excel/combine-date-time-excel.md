# Combine Date and Time in Excel (Easy Formula)

**Source:** https://trumpexcel.com/combine-date-time-excel

---

[Skip to content](https://trumpexcel.com/combine-date-time-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/combine-date-time-excel/#below-title)

Sometimes you may have dates in one column and time values in another column and you want to combine these to get one single date and time value in a cell.

And if you’re thinking that you can do that by easily combining the two cells by using the concatenate formula or the & sign, you’ll find out that it doesn’t work.

I have tried to use the & sign to [combine the cells](https://trumpexcel.com/combine-cells-in-excel/)
 that contain date and time, and the resulting value is not in the expected format.

In this tutorial, I will show you a couple of ways to quickly **combine date and time values in Excel**.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/combine-date-time-excel/#)

Combine Date and Time with a Simple Addition
--------------------------------------------

Excel stores date and time values as numbers in the back end.

For example, 44197.375 in Excel represents 01-01-2021 09:00 AM

The integer part of the above number represents a date (which is 01 Jan 2021), and the decimal part of the number represents a time (which is 9 AM)

So, if you have dates in one column and time in another column, the easiest way to combine these and get the date and time in one single cell would be to simply add these two cells.

Suppose you have a data set as shown below and you want to combine the date and time in column C.

![Date and Time in separate columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20340'%3E%3C/svg%3E)

Below is the formula that will do that:

\=A2+B2

![Simple addition to combine date and time](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20520%20395'%3E%3C/svg%3E)

All this formula to all the cells in the column to get the combined date and time values.

It automatically picks up the format from the cells and shows you the result that has the date portion and the time portion.

As I mentioned, dates and times are stored as numbers in Excel. The combined date and time that you see in the cells in column C are also decimal numbers in the back end.

In case you want to show that result in a different format, you can do that using the format cells dialog box (where you can specify the custom code to show the date and time in a specific way).

In most cases, Excel will take care of the [formatting](https://trumpexcel.com/excel-formatting-shortcuts/)
 and you will see the date as well as the time as shown above. In case it doesn’t, you will have to change the [cell formatting](https://trumpexcel.com/remove-cell-formatting-in-excel/)
 to show the combined date and time.

Combine Date and Time with a TEXT Function
------------------------------------------

Another quick way to combine date and time in Excel is by using the CONCAT formula with the [TEXT function](https://trumpexcel.com/excel-text-function/)
.

Suppose you have a dataset as shown below and you want to combine the date and time and get the result in column C.

![Date and Time in separate columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20340'%3E%3C/svg%3E)

Below is the formula that can do this:

\=CONCAT(TEXT(A2,"dd-mm-yyy")," ",TEXT(B2,"hh:mm:ss"))

![Formula to combine date and time](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20760%20389'%3E%3C/svg%3E)

The TEXT function allows you to take any value as the input and show it in the specified format.

In our example, I have used two TEXT functions, the first one takes the date value and displays it as a date and the second one takes the time value and displays it as the time.

And since I want both of these in the same cell, I have used the CONCAT formula with space as the separator in between the date and time.

Since we have used the TEXT function to specify the format for the date and the time, it does not matter how the input values are displayed in the cell.

For example, even if I have the numerical values instead of the date and the time, this formula would still give me the right result.

Another big benefit of using the text function is that you can combine other text strings with the result of this formula.

To give you an example, let’s say I don’t want just the date and the time, I want the result in the following format – Date: 01 Jan 2021, Time: 09:00 AM

To do this, you can use the below formula:

\=CONCAT("Date: "&TEXT(A2,"dd-mm-yyy"),", ","Time: "&TEXT(B2,"hh:mm:ss AM/PM"))

![Formula to combine date and time with custom text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20746%20417'%3E%3C/svg%3E)

Since the result of the TEXT function is a text string, we can easily combine it with the other text strings using the ampersand operator (&) or CONCAT formula.

So these are two simple ways you can use to **combine date and time in Excel**.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [Calculate Time in Excel (Time Difference, Hours Worked, Add/ Subtract)](https://trumpexcel.com/calculate-time-in-excel/)
    
*   [Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [How to Remove Time from Date/Timestamp in Excel](https://trumpexcel.com/remove-time-from-date-in-excel/)
    
*   [How to Quickly Insert Date and Timestamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    
*   [How to Change Date Format In Excel?](https://trumpexcel.com/change-date-format-excel/)
    
*   [How to Add Months to Date in Excel](https://trumpexcel.com/add-months-to-date-excel/)
    
*   [How to Compare Dates in Excel (Greater/Less Than, Mismatches)](https://trumpexcel.com/compare-dates-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “Combine Date and Time in Excel (Easy Formula)”
-------------------------------------------------------------

1.  Easy to Use Formula, Thanks sir
    
    [Reply](https://trumpexcel.com/combine-date-time-excel/#comment-40964)
    
2.  None of that worked. I mean, it SHOULD have worked, but I was trying to to figure out the amount of time worked during a day, and if I tried to subtract 06/18/2024 07:30 from 06-17-2024 19:30 it would give me 12:00 (12 hours). BUT if I changed my start time to 16:30 it would give me 12:01 ; and if I changed to to the same day, saying that I worked from 7:30 AM to 7:30 PM, it would give me 0 hours. I finally found a formula that hit the nail on the head, but I don’t understand it, it seems a bit backwards: Date = A1, Start Time B1, End Time = C1, =IF(B1>TIMEVALUE(“8:00”),C1+1,C1)-B1 (I don’t know why I am adding a day to the OLDER time in this formula, but it works PERFECTLY! Though when I transposed it, I went with my gut feeling and used subtraction for that day, and found it working in reverse (giving me more hours for less time, and less hours for more time–that’s when I realized that I had it backwards, because even now it looks incorrect–but it does work!)
    
    [Reply](https://trumpexcel.com/combine-date-time-excel/#comment-35648)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/combine-date-time-excel/#respond)

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