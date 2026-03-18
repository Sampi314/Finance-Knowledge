# How to Convert Seconds to Minutes in Excel (Easy Formula)

**Source:** https://trumpexcel.com/convert-seconds-to-minutes-excel

---

[Skip to content](https://trumpexcel.com/convert-seconds-to-minutes-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-seconds-to-minutes-excel/#below-title)

If you want to convert seconds values to minutes in Excel, it is not as straightforward as dividing it by 60.

This is because Excel has a specific way of storing date and time values in Excel. While a full day is stored as a whole number in Excel, time values are stored as fractions/decimals.

For example, 44927 represents the date 01 January 2023, and 44927.25 represents _01 January 2023 06:00 AM_.

Here, 0.25 is the fraction that represents the time. Since a day has 24 hours, 0.25 part of the day would mean 6 hours (24\*0.25)

This is why, if you have a value of 150 seconds in a cell, and you divided by 60, it gives you 2.5. While this does mean that 150 seconds is equal to 2.5 minutes, in Excel, this would represent two and a half days.

So, if you want to convert seconds into minutes and seconds, You need to do it a little differently.

In this tutorial, I will show you everything you need to know about **converting seconds into minutes and seconds** using a simple formula and some number formatting magic.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/convert-seconds-to-minutes-excel/#)

Convert Second to Minutes Using Custom Formatting
-------------------------------------------------

Below is a data set of some students who competed in a race along with their completion time.

I have the names of these students in column A, and their completion time in seconds in column B, and I want to convert this time in seconds into minutes and seconds.

![Time dataset with values in seconds](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20590%20266'%3E%3C/svg%3E)

As of now, the value we have are whole numbers that represent the seconds took to complete the race. For example, in cell B2, we have 103, which indicates that 103 seconds were taken to complete the race.

But as I mentioned earlier, Excel stores days as whole numbers, and time values as fractions of that day, so we need to convert these values in seconds into the fraction of the day, so that we can show these in any time value format we want.

Below are the steps to convert the values in seconds as a fraction of the day:

1.  In cell C2, enter the below formula

\=B2/(24\*60\*60)

![Enter the formula in cell B2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20589%20317'%3E%3C/svg%3E)

2.  Copy it for all the cells in the column. You can do a simple copy-paste or double-click on the [Fill handle](https://trumpexcel.com/how-to-use-fill-handle-in-excel/)
     to fill the same formula in the remaining cells

![Copy the formula for all cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20266'%3E%3C/svg%3E)

3.  Select all the resulting values in column C, click the ‘Home’ tab, and within the ‘Number’ group, click on the dialog box launcher icon (you can also use the [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
     Control + 1)

![Click on the dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20783%20248'%3E%3C/svg%3E)

4.  In the ‘Format Cells’ dialog box, within the ‘Number’ tab click on the ‘Custom’ option in the ‘Category’ list

![Click the Custom option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)

5.  In the ‘Type:’ field, enter **mm:ss**

![Enter mmss in the field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)

6.  Click OK

The above steps would convert the values in seconds in column B into minutes and seconds (as shown below).

![Result shown in minutes and seconds](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20587%20266'%3E%3C/svg%3E)

Let me quickly explain how it works.

In the above steps, we did two things:

*   Used the formula to convert the values in seconds into a value that represents it as a fraction of the day. To do this, we have divided the values in seconds by the total number of seconds in a day (which is 24\*60\*60)
*   Formatting the decimal value that we got using [custom number formatting](https://trumpexcel.com/excel-custom-number-formatting/)
     to show it as minutes and seconds

If you are wondering why we did all these steps instead of simply dividing the values in seconds by 60, it’s because doing the above steps have converted our second’s values into a number that Excel recognizes as a time value. With these values, you can format it to show in different ways (such as showing it in hh:mm:ss format) and can also use these in calculations.

Convert Second to Minutes Using Formula
---------------------------------------

In the above method, I first converted the values in seconds into the fraction of the day, and then use custom number formatting to show them in the mm:ss format.

Now let me show you some formula methods to do this.

### Using TEXT Formula

The [TEXT function in Excel](https://trumpexcel.com/excel-text-function/)
 allows you to calculate a value and then specify the format in which you want to show that value right within the formula.

Below I have a data set where I have the values in seconds in column B and I want to show them in minutes and seconds instead.

![Time dataset with values in seconds](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20590%20266'%3E%3C/svg%3E)

Here is the formula that will do this:

\=TEXT(B2/(24\*60\*60),"mm:ss")

Enter the formula in cell C2, and then copy it for all the other cells in the column.

![TEXT formula to convert seconds into minutes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20560%20315'%3E%3C/svg%3E)

The above value first converts the seconds’ values into the fraction of the day and then formatted it to show it in the minutes and seconds format.

One thing you should remember about this method is that the result that you get would be in the text format, so you won’t be able to use these values in further calculations.

### Using INT and MOD Formula

In the methods covered so far, we have first converted the seconds’ values by dividing these by 24\*60\*60, so that they represent a fraction of a whole day.

We did this so that we can get the value in the right format so that it can be displayed using the inbuilt custom formats in Excel.

If all you want to do is convert the seconds’ values to minutes and show them in a cell, you can also use a slightly different approach.

Below I have a data set where I have the time in seconds in column B, and I want to show this time in minutes and seconds in column C.

![Time dataset with values in seconds](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20590%20266'%3E%3C/svg%3E)

Below is the formula you can use to do this:

\=INT(B2/60)&" Minutes "&MOD(B2,60)&" Seconds"

Enter the formula in cell C2, and then copy it for all the other cells in the column.

![INT MOD formula to convert seconds into minutes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20314'%3E%3C/svg%3E)

In the formula, we first divided the seconds’ value by 60 to get how many minutes it represents and then used the [INT function](https://trumpexcel.com/excel-int-function/)
 to give us only the integer portion of the value.

This gives us the total number of completed minutes represented by the seconds’ value.

We then [concatenated it](https://trumpexcel.com/concatenate-excel-ranges/)
 with the result of the [MOD function](https://trumpexcel.com/excel-mod-function/)
, which gives us the seconds remaining after we have taken away all the full minutes from the value.

In the above formula, I have added the words “Minutes” and “Seconds”. you can use the formula as is or you can modify it to show whatever format you want.

For example, if you do not show the words ‘Minutes’ and ‘Seconds’, you can use the below formula:

\=INT(B2/60)&":"&MOD(B2,60)

So these are methods you can use to **convert seconds to minutes in Excel**.

The right way to do this is by converting the seconds to a value that represents the fraction of the day, and then formatting it using Custom Number Formatting.

Alternatively, you can also use the TEXT formula or the INT/MOD formula to get the result as a text value (Which can’t be used in calculations further).

I hope you found this Excel tutorial useful.

**Other Excel tutorials you may also like:**

*   [Convert Time to Decimal Numbers in Excel (Hours, Minutes, Seconds)](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [Calculate Time in Excel (Time Difference, Hours Worked, Add/ Subtract)](https://trumpexcel.com/calculate-time-in-excel/)
    
*   [How to Remove Time from Date/Timestamp in Excel](https://trumpexcel.com/remove-time-from-date-in-excel/)
    
*   [How to Insert Date and Timestamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    
*   [How to Display Numbers as Fractions in Excel (Write Fractions in Excel)](https://trumpexcel.com/display-numbers-as-fractions-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-seconds-to-minutes-excel/#respond)

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