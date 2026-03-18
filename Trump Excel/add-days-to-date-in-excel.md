# How to Add or Subtract Days to a Date in Excel (Shortcut + Formula)

**Source:** https://trumpexcel.com/add-days-to-date-in-excel

---

[Skip to content](https://trumpexcel.com/add-days-to-date-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/add-days-to-date-in-excel/#below-title)

Microsoft Excel stores dates and times as numbers, which allows the user to easily add and subtract days to a date in Excel.

It also makes it really easy when you want to find out the total number of days between two dates, as you can simply subtract one from the other.

In this tutorial, I’ll show you a couple of really easy ways to **add or subtract days to dates in Excel**.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/add-days-to-date-in-excel/#)

Add or Subtract Days to Dates in Excel Using Paste Special
----------------------------------------------------------

Recently, I was working with one of the content writers on one of my projects. I sent her a list of articles with the due dates to the writer (as shown below).

![Dataset where days need to be added](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20501%20378'%3E%3C/svg%3E)

The writer came back to me and asked me to shift all these due dates by 10 days, as she had some urgent stuff to take care of and needed 10 days off.

This is a perfect example where I would need to add a fixed number of days to the due date so that I can get the new date for each task.

Excel has an in-built [Paste Special functionality](https://trumpexcel.com/multiply-in-excel-using-paste-special/)
 that allows you to quickly add or subtract a fixed number from a range of selected cells.

Below are the steps to add 10 days to the existing dates in our data set:

1.  In an empty cell, enter 10 (the number that we want to add to the dates)![Enter the days to add in an emptry cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20785%20388'%3E%3C/svg%3E)
2.  Copy this cell (the one in which we enter the value 10)
3.  Select the cells that have the dates![Select the cells with the dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20786%20426'%3E%3C/svg%3E)
4.  Right-click on the selection
5.  Click on [Paste Special](https://trumpexcel.com/excel-paste-special-shortcuts/)
    . This will open the Paste Special dialog box![Click on Paste Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20623%20390'%3E%3C/svg%3E)
6.  In the Paste option, select ‘Values’![Select Values option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20462%20449'%3E%3C/svg%3E)
7.  In the Operation options, select ‘Add’![Click on Add](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20462%20449'%3E%3C/svg%3E)
8.  Click Ok![Click on OK](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20462%20449'%3E%3C/svg%3E)

That’s it!

The above steps would add 10 to all the dates in the selection.

![Final Result where days are added to dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20377'%3E%3C/svg%3E)

In case you want to subtract from a date, select the Subtract option in Step 7.

Note: It’s important to select the Value option in Step 6 as this makes sure that the format of the dates remains unchanged. If you don’t do this, it would change the formatting of your dates (as it also [copies the formatting](https://trumpexcel.com/excel-format-painter/)
 from the copied cell).

This method is best used when you want to add a fixed number of days to dates. In case you want to add a variable number of days to a date, it’s best to use the formula method (covered next).

Also read: [How to Add Week to Date in Excel?](https://trumpexcel.com/add-week-to-date-excel/)

Add or Subtract Days to Dates Using Formulas
--------------------------------------------

With formulas, you get a lot of flexibility while adding or subtracting dates.

For example, you can add a different number of days to date by just having that number in an additional column.

You can also only add the weekdays (while ignoring the weekends).

Let’s see a couple of examples that will make these scenarios easy to understand.

### Adding Fixed Number of Days to a Date

Suppose you have a data set as shown below and you want to add a fixed number of days to each of these dates.

![Adding fixed number of dates using formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20725%20378'%3E%3C/svg%3E)

Below is the formula to do this:

\=B2+10

![Formula to add fixed number of days](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20724%20431'%3E%3C/svg%3E)

Since dates are stored as numbers in Excel, all you need to do is add the value by which you want to extend the date.

In this example, I have simply added 10 to the date in each cell to get the date after 10 days.

You can copy and paste the above formula to all the cells in the column to apply it for all the dates.

### Adding Varying Number of Days to a Date

What if you don’t want to add the same number to each date? What if you want to have a variable date added two different existing dates.

For example, in some of these dates, I may want to add 10 days, and in some others, I may want to add 5 days or 15 days.

In such a scenario, it’s best to insert a helper column and have your variable dates in that helper column.

Below I have the example data set where I have a helper column (columns C) it has the days to add.

![Dataset with variable days to add](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20728%20342'%3E%3C/svg%3E)

Below is the formula that I can use to add these days in the helper column to the existing dates:

\=B2+C2

![Formula to add variable number of days](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20770%20395'%3E%3C/svg%3E)

This is pretty straight forward, as we are simply adding two numbers.

And in case you want to subtract days from a date, use the minus sign instead of the plus sign in the above formula.

Note: In some cases, you may see a serial number instead of the date (or the date may be in a different format). If that happens, you simply need to [change the format of the cell](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
 to show it in the expected date format.

But now, what if only want to add weekdays to the existing date (i.e., ignore the weekends – Saturday and Sunday)?

You can do that as well (as covered in the next section).

### Adding Only Weekdays to a Date

Below I have the data set where the dates are in column B and the number of weekdays that I want to add are in column C.

![Dataset with variable days to add](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20728%20342'%3E%3C/svg%3E)

Below is the formula that would give you the date after adding the given number of working days:

\=WORKDAY(B2,C2)

![WorkDay function to only weekdays](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20705%20354'%3E%3C/svg%3E)

[WORKDAY function](https://trumpexcel.com/excel-workday-function/)
 in Excel takes three arguments:

*   The date to which you want to add a specific number of workdays (B2 in our example)
*   The total number of workdays that you want to add (C2 in our example)
*   \[Optional Argument\] List of holidays that should not be counted

In our example, since we do not have the list of holidays, I am only using the first two arguments. This function only counts the weekdays (i.e., Monday to Friday), and ignore the weekends days (i.e., Saturday and Sunday).

In case you want to add weekend days that are different than Saturday and Sunday (say Friday and Saturday or only Sunday), you can do that by using a slightly different formula.

Below is the formula that would give me the final result considering Friday and Saturday as the weekend days

\=WORKDAY.INTL(B2,C2,7)

The [WORKDAY.INTL formula](https://trumpexcel.com/excel-workdayintl-function/)
 is a slight improvement over the WORKDAY function, as it allows you to choose the weekend days.

![Workday International arguments](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20332'%3E%3C/svg%3E)

For example, in the above formula, I have specified the third argument as 7, which indicates that I want to consider Friday and Saturday as the weekend days.

Similarly, you can also choose to only have Sunday as the weekend day. In fact, you can choose to have any single day or combination of two consecutive days as the weekend days within this formula.

Note: In case you want to subtract days instead of adding days, use a negative number as the day value. For example, instead of 10 use -10 in Column c.

These are two simple ways you can use to **add or subtract days from a date in Excel**. If you want to quickly add a fixed number of days, you can use the paste special technique or a simple addition formula.

In case you want to only add the weekdays and ignore the weekends, you can also do that using the WORKDAY or the WORKDAY.INTL formulas.

I hope you found this tutorial useful.

**Other Excel tutorials you may like:**

*   [How to SUM values between two dates (using SUMIFS formula)](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)
    
*   [Calculate the Number of Months Between Two Dates in Excel](https://trumpexcel.com/calculate-months-between-two-dates/)
    
*   [How to Stop Excel from Changing Numbers to Dates Automatically](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/)
    
*   [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    
*   [How to Calculate Age in Excel using Formulas + FREE Calculator Template](https://trumpexcel.com/calculate-age-in-excel/)
    
*   [How to Add Months to Date in Excel](https://trumpexcel.com/add-months-to-date-excel/)
    
*   [How To Subtract In Excel (Subtract Cells, Column, Dates/Time)](https://trumpexcel.com/subtract-in-excel/)
    
*   [Get Day Name from Date in Excel](https://trumpexcel.com/get-day-name-from-date-excel/)
    
*   [How to Autofill Only Weekday Dates in Excel (Formula)](https://trumpexcel.com/autofill-only-weekday-dates-excel/)
    
*   [Convert Days to Months in Excel](https://trumpexcel.com/convert-days-to-months-excel/)
    
*   [Add Years to Date in Excel](https://trumpexcel.com/add-years-to-date-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/add-days-to-date-in-excel/#respond)

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