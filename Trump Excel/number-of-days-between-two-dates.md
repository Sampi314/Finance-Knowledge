# How to Calculate the Number of Days Between Two Dates in Excel

**Source:** https://trumpexcel.com/number-of-days-between-two-dates

---

[Skip to content](https://trumpexcel.com/number-of-days-between-two-dates/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/number-of-days-between-two-dates/#below-title)

**Watch Video – Calculate the Number of Workdays Between Two Dates**

Excel has some powerful functions to calculate the number of days between two dates in Excel. These are especially useful when you’re creating [Gantt charts](https://trumpexcel.com/gantt-chart-in-excel/)
 or [timelines](https://trumpexcel.com/milestone-chart-in-excel/)
 for a proposal/project.

In this tutorial, you’ll learn how to calculate the number of days between two dates (in various scenarios):

This Tutorial Covers:

[Toggle](https://trumpexcel.com/number-of-days-between-two-dates/#)

Calculating the Total Number of Days Between Two Dates in Excel
---------------------------------------------------------------

Excel has multiple ways to calculate the days between two dates.

### Using the DAYS Function

Excel DAYS function can be used to calculate the total number of days when you have the start and the end date.

You need to specify the ‘Start Date’ and the ‘End Date’ in the Days function, and it will give you the total number of days between the two specified dates.

For example, suppose you have the start date is in cell B1 and End Date is in cell B2 (as shown below):

![Start date and end date in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20441%20131'%3E%3C/svg%3E)

The following formula will give you the total number of days between the two dates:

\=DAYS(B2,B1)

![DAYS Formula to get the Number of Days](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20439%20258'%3E%3C/svg%3E)

Note that you can also manually specify the dates in the Days function by putting it in double-quotes. Just make sure these dates in double-quotes is in an accepted date format in Excel.

Days function gives you the number of days between two dates. This means that if the dates are 1 Dec 2017 and 2 Dec 2017, it will return 1. If you want both the days to be counted, you need to add 1 to the result of Days function. You can read more about the Days function [here](https://support.office.com/en-us/article/DAYS-function-57740535-d549-4395-8728-0f07bff0b9df?ui=en-US&rs=en-US&ad=US&fromAR=1)
.

### Using the DATEDIF Function

DATEDIF function (derived from **Date Dif**ference) also allows you to quickly get the number of days between two dates. But unlike the DAYS function, it can do more than that.

You can also use the DATEDIF function to [calculate the number of months](https://trumpexcel.com/calculate-months-between-two-dates/)
 or years that have elapsed in the two given dates.

Suppose you have the below dataset and you want to get the number of days between these two dates:

![Start date and end date in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20441%20131'%3E%3C/svg%3E)

You can use the below DATEDIF formula to do this:

\=DATEDIF(B1,B2,"D")

The above DATEDIF formula takes three arguments:

*   The start date – B1 in this example
*   The end date – B2 in this example
*   “D” – the text string that tells the DATEDIF function what needs to be calculated.

Also note that unline the other Excel functions, when you type the DATEDIF function in Excel, it will not show the IntelliSense (the autocomplete option that helps you with the formula arguments).

If you only want to calculate the number of days between two given dates, then it’s better to use the DAYS function. DATEDIF is more suited when you want to calculate the total number of years or months that have passed in between two dates.

For example, the below formula would give you the total number of months between the two dates (in B1 and B2)

\=DATEDIF(B1,B2,"M")

Similarly, the below formula will give you the total number of years between the two dates:

\=DATEDIF(B1,B2,"Y")

You can read more about the [DATEDIF function](https://trumpexcel.com/excel-datedif-function/)
 here. One of the common uses of this function is when you need to [calculate age in Excel](https://trumpexcel.com/calculate-age-in-excel/)
.

Also read: [How To Calculate Time In Excel](https://trumpexcel.com/calculate-time-in-excel/)

Number of Working Days Between Two Dates in Excel
-------------------------------------------------

Excel has two functions that will give you the total number of working days between two dates and will automatically account for weekends and specified holidays.

*   [Excel NETWORKDAYS function](https://trumpexcel.com/excel-networkdays-function/)
     – you should use this when the weekend days are Saturday and Sunday.
*   [Excel NETWORKDAYS INTERNATIONAL function](https://trumpexcel.com/excel-networkdays-intl-function/)
     – use this when the weekend days are not Saturday and Sunday.

Let’s first quickly have a look at NETWORKDAYS Function syntax and arguments.

**Excel NETWORKDAYS Function – Syntax & Arguments**

\=NETWORKDAYS(start\_date, end\_date, \[holidays\])

*   start\_date – a date value that represents the start date.
*   end\_date – a date value that represents the end date.
*   \[holidays\] – (Optional) It is a range of dates that are excluded from the calculation. For example, these could be national/public holidays. This could be entered as a reference to a range of cells that contains the dates, an array of serial numbers that represent the dates, or a [named range](https://trumpexcel.com/named-ranges-in-excel/)
    .

Let’s first look at an example where you want to calculate the number of working days (business days) between two dates with Saturday and Sunday as weekends.

![Dates data set where days needs to be calculated between two dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20616%20211'%3E%3C/svg%3E)

To calculate the number of working days (Column D) – when the start date, end date, and holidays are specified – use the below formula in D3 and copy for all cells:

\=NETWORKDAYS(B2,C2,$F$2:$F$6)

![networkdays formula result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20617%20261'%3E%3C/svg%3E)

This function works great in most cases, except the ones where the weekends are days other than Saturday and Sunday.

For example, in middle-eastern countries, the weekend is Friday and Saturday, or in some jobs, people may have a six-day workweek.

To tackle such cases, Excel has another function – NETWORKDAYS.INTL (introduced in Excel 2010).

Before I take you through the example, let’s quickly learn about the syntax and arguments of Excel NETWORKDAY INTERNATIONAL function

**Excel NETWORKDAYS INTERNATIONAL Function – Syntax & Arguments**

\=NETWORKDAYS.INTL(start\_date, end\_date, \[weekend\], \[holidays\])

*   **start\_date –** a date value that represents the start date.
*   **end\_date** – a date value that represents the end date.
*   **\[weekend\] –** (Optional) Here, you can specify the weekend, which could be any two days or any single day. If this is omitted, Saturday and Sunday are taken as the weekend.![Networkdays International formula syntax and weekend options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20257'%3E%3C/svg%3E)
*   **\[holidays\]** – (Optional) It is a range of dates that are excluded from the calculations. For example, these could be national/public holidays. This could be entered as a reference to a range of cells that contains the dates or could be an array of serial numbers that represent the dates.

Now let’s see an example of calculating the number of working days between two dates where the weekend days are Friday and Saturday.

Suppose you have a dataset as shown below:

![networkdays function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20616%20211'%3E%3C/svg%3E)

To calculate the number of working days (Column D) with the weekend as Friday and Saturday, use the following formula:

\=NETWORKDAYS.INTL(B2,C2,7,$F$2:$F$6)

The third argument in this formula (the number 7) tells the formula to consider Friday and Saturday as the weekend.

![networkdays intl formula result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20615%20256'%3E%3C/svg%3E)

Also read: [Calculate Number of Weeks Between Two Dates in Excel](https://trumpexcel.com/weeks-between-two-dates-excel/)

Number of Weekends Between Two Dates in Excel
---------------------------------------------

We can use the NETWORKDAYS function to calculate the number of weekends between two dates.

While the Networkdays function calculates the number of working days, we can also use to get the number of weekend days between two dates.

Suppose we have a dataset as shown below:

![Dataset to calculate the number of weekend days in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20502%20211'%3E%3C/svg%3E)

Here is the formula that will give you the total number of weekends days between the two dates:

\=DAYS(C2,B2)+1-NETWORKDAYS(B2,C2)

![weekend formula - to give the number of weekend days between two dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20510%20257'%3E%3C/svg%3E)

Also read: [Convert Days to Months in Excel](https://trumpexcel.com/convert-days-to-months-excel/)

Number of Work Days in a Part-time Job
--------------------------------------

You can use Excel NETWORKDAYS.INTL function to calculate the number of workdays in a part-time job as well.

Let’s take an example where you are involved in a project where you have to work part-time (Tuesday and Thursday only).

![Calculate part time working days in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20543%20209'%3E%3C/svg%3E)

Here is the formula that will get this done:

\=NETWORKDAYS.INTL($B$3,$C$3,**"1010111"**,$E$3:$E$7)

![NETWORKDAYS International formula to get the part time working days](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20541%20257'%3E%3C/svg%3E)

Note that instead of choosing the weekend from the drop-down that’s inbuilt in the function, we have used **“1010111”** _(in double quotes)._

*   0 indicates a working day
*   1 indicates a non-working day

The first number of this series represents Monday and the last number represents Sunday.

So “0000011_“_ would mean that Monday to Friday are working days and Saturday and Sunday are non-working (weekend).

With the same logic, **“1010111”** indicates that only Tuesday and Thursday are working, and rest 5 days are non-working.

In case you have holidays (which you don’t want to get counted in the result), you can specify these holidays as the fourth argument.

Number of Mondays Between Two Dates
-----------------------------------

To find the number of Mondays between two dates (or any other day), we can use the same logic as used above in calculating part-time jobs.

Suppose you have a dataset as shown below:

![Start date and end date to get the number of Mondays](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20470%20211'%3E%3C/svg%3E)

Here is the formula that will give you the number of Mondays between the two dates:

\=NETWORKDAYS.INTL(B2,C2,"0111111")

![Using Networkdays INTL function to get the number of Mondays](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20513%20257'%3E%3C/svg%3E)

In this formula, ‘0’ means a working day and ‘1’ means a non-working day.

This formula gives us the total number of working days considering that Monday is the only working day of the week.

Similarly, you can also calculate the number of any day between two given dates.

**You May Also Like the Following Tutorials:**

*   [Excel Timesheet Calculator Template](https://trumpexcel.com/excel-timesheet-calculator-template/)
    .
*   [Convert Date to Text in Excel](https://trumpexcel.com/convert-date-to-text-excel/)
    .
*   [How to Group Dates in Pivot Tables in Excel](https://trumpexcel.com/group-dates-in-pivot-tables-excel/)
    .
*   [How to Automatically Insert Date and Time Stamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    .
*   [Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [How to SUM values between two dates in Excel](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)
    
*   [Get Day Name from Date in Excel](https://trumpexcel.com/get-day-name-from-date-excel/)
    
*   [Check IF a Date is Between Two Given Dates in Excel](https://trumpexcel.com/check-if-date-is-between-two-dates/)
    
*   [How to Add Week to Date in Excel?](https://trumpexcel.com/add-week-to-date-excel/)
    
*   [Days Between Dates Calculator](https://trumpexcel.com/calculator/days-between-dates/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

13 thoughts on “How to Calculate the Number of Days Between Two Dates in Excel”
-------------------------------------------------------------------------------

1.  Guys!!! Please tell me some one days calculator for android mobiles and iphone mobiles.
    
    [Reply](https://trumpexcel.com/number-of-days-between-two-dates/#comment-10986)
    
2.  Please tell me some android application names for days calculator.
    
    [Reply](https://trumpexcel.com/number-of-days-between-two-dates/#comment-10985)
    
3.  [https://uploads.disquscdn.com/images/2aceda413b6251203844e8115b328a44b0b73d3dd2a761e26870bad04ac8e809.png](https://uploads.disquscdn.com/images/2aceda413b6251203844e8115b328a44b0b73d3dd2a761e26870bad04ac8e809.png)
    
    I would like to calculate the number of months in the attached table. Can anyone help me?
    
    [Reply](https://trumpexcel.com/number-of-days-between-two-dates/#comment-9692)
    
4.  Hi Sumit, Very informative. Thank you. Especially the use of the binary day-of-week parameter. That could be handy.
    
    [Reply](https://trumpexcel.com/number-of-days-between-two-dates/#comment-9388)
    
5.  I have a excel sheet and i want to send alert mail as a list of customers whose Software LIC are going to expire on so and so date.
    
    [Reply](https://trumpexcel.com/number-of-days-between-two-dates/#comment-9330)
    
6.  Thanks for sharing the informative post. Keep it up.
    
    [Reply](https://trumpexcel.com/number-of-days-between-two-dates/#comment-9304)
    
7.  Dear Sumit  
    Good Day!
    
    very nice your concept for me
    
    [Reply](https://trumpexcel.com/number-of-days-between-two-dates/#comment-9299)
    
8.  Hi Sumit, thanks for the tutorial, very informative. How do I calculate time in hours between dates. If you want to calculate the working hours from 15.00 in afternoon until 09’00 the next morning? If your working hours is 08h00 to 17h00, the working hours would be 3 hours in total ( 2 from previous day nd 1h for present day). Any formula to calculate the total working time between dates?
    
    [Reply](https://trumpexcel.com/number-of-days-between-two-dates/#comment-9296)
    
    *   Hey.. when you have days changing, you need to use the date as well as time to make the entry. Once you have two dates with time, just subtract first from the later.
        
        [Reply](https://trumpexcel.com/number-of-days-between-two-dates/#comment-9301)
        
9.  I need to calculate the # of days between 2 dates, but excluding Sundays, so only 7 days in a week, Including Holidays.
    
    [Reply](https://trumpexcel.com/number-of-days-between-two-dates/#comment-8806)
    
    *   you can use the NETWORKDAYS.INTL funtion and select Sunday as weekend.
        
        [Reply](https://trumpexcel.com/number-of-days-between-two-dates/#comment-9279)
        
10.  Hello  
    I need to calculate the # of days between 2 dates, but excluding Sundays, so only 6 days in a week. Anyone know a function/formula that can accomplish this?  
    Thank you
    
    [Reply](https://trumpexcel.com/number-of-days-between-two-dates/#comment-3602)
    
    *   Hello Mary.. You can use the below formula:  
        \=NETWORKDAYS.INTL(start date,end date,11)
        
        [Reply](https://trumpexcel.com/number-of-days-between-two-dates/#comment-7985)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/number-of-days-between-two-dates/#respond)

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