# How to Add Week to Date in Excel? Easy Formulas!

**Source:** https://trumpexcel.com/add-week-to-date-excel

---

[Skip to content](https://trumpexcel.com/add-week-to-date-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/add-week-to-date-excel/#below-title)

It’s a common requirement to calculate the date after a specific number of weeks from the current date or any other given date.

This is especially helpful while planning a project where you have a tentative idea of how much time a task would take and want to know when it will be completed (by adding the specified number of weeks the project is going to take to the start date of the project/task)

Doing this in Excel confuses many people because Excel has a specific way of dealing with date and time values.

In this tutorial, I will show you simple ways to quickly **add weeks to a date in Excel** using simple formulas.

I’ll also explain how dates work in Excel so that you have a solid understanding and won’t struggle with dates in the future.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/add-week-to-date-excel/#)

Add Week to Date in Excel Using Formulas
----------------------------------------

The easiest way to quickly add weeks to a given date in Excel is by using formulas.

While there is no dedicated formula to do this, since the number of days in a week will always be 7, this can easily be done using a simple addition arithmetic operator or a SUM function.

Let me show you a couple of examples of how to do this.

### Adding a Fixed Number of Weeks to a Date

Below I have a data set where I have some dates in column A, and I want to add one week to each of these dates and get the resulting dates in column B.

![Dates Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20441%20341'%3E%3C/svg%3E)

This can be done using the below formula:

 =A2+7

Enter this formula in cell B2 and then copy it for all the remaining cells in the column to get the result for all the other dates.

![Formula to add week to date in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20461%20388'%3E%3C/svg%3E)

In this example, since I only have to add one week, I’ve added 7 to the existing date (as one week has seven days).

In case you want to add more weeks (say 3), you can use the below formula:

\=A2+7\*3

In the above formula, I multiplied the number of weeks by 7 to give me the total number of days in those weeks and then added those days to the given date.

**Note**: Since we have used a formula here, in case you change the original date and column A, the resulting date in column B will automatically update. In case you do not want the formula and only want the resulting date value, you can copy the cells that have the formula result and then only paste the values so that the [formulas are removed](https://trumpexcel.com/convert-formulas-to-values-excel/)

Also read: [Calculate Number of Weeks Between Two Dates in Excel](https://trumpexcel.com/weeks-between-two-dates-excel/)

### Adding Given Number of Weeks to a Date

Below I have a data set where I have dates in column A and the number of weeks that needs to be added to each date in column B.

![Date with weeks to add in separate column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20570%20341'%3E%3C/svg%3E)

Below is the formula that will add the given number of weeks to the date and give the resulting date:

\=A2+B2\*7

![Formula to add week in a column to date in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20385'%3E%3C/svg%3E)

In the above formula, I first calculated the total number of days that need to be added (by multiplying 7 with the number of weeks value) and then added it to the date and column A.

**Note**: You can use the above formulas even if you have the week number value (that you need to add to the date) as a decimal. For example, if you need to add 4.5 weeks to a given date, you can still use the above formulas, and it will give you the result accordingly

Add Week to Date in Excel Using Paste Special
---------------------------------------------

Another way to add weeks to a date in Excel is by using the Paste Special option.

Paste Special allows you to copy a cell that has a value and then add it to a range of selected cells using the ‘Add’ Operator in Paste Special.

Let me show you how it works.

Below I have some dates in column A, and I want to add a week to these dates.

![Dates Dataset to add a week](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20361%20397'%3E%3C/svg%3E)

Here are the steps to do this:

1.  In any blank cell in your worksheet, enter the value 7. Since we only want to add one week, I am using the value 7 (as there are seven days in a week). In case you want to add any other number of weeks, you need to use the corresponding number of days (for example, 21 for three weeks or 35 for five weeks)

![Enter week to add in a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20510%20386'%3E%3C/svg%3E)

2.  Copy this cell in which you entered the value. You can right-click on the cell and then click on copy, or use the keyboard shortcut Control + C
3.  Select the range of cells that have the dates
4.  Right-click on the selected cells and then click on Paste Special.

![Click on Paste special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20506%20397'%3E%3C/svg%3E)

5.  In the Paste Special dialog box, select the **Value** option (in the Paste options), and the **Add** option in the Operation options

![Select Values and Add option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20414'%3E%3C/svg%3E)

6.  Click OK

The above steps would instantly change your original data set and give you the dates where one week has been added.

![Dates have been changed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20349%20397'%3E%3C/svg%3E)

In case you want to show the start date as well as the resulting date after the weeks have been added, copy the dates in a separate column and then use Paste Special on the copied data.

Also, if you may need the original data in the future, it’s a good idea to make a backup copy of your workbook, or copy the dates data in a separate column and then use Paste Special to add a week to the date.

**Note**: One limitation of this Paste Special method is that you will only be able to add one given week value to all the given dates. In case you want to add different week values to different dates, you will have to use the formula method only

So these are two easy ways you can use to quickly add a week (or any given number of weeks) to a date in Excel.

While I have covered the examples that show how to add weeks to a date in Excel, you can use the same methods to subtract weeks from a date as well.

I hope you found this Excel tutorial useful.

**Other Excel tutorials you may also like:**

*   [How to Add or Subtract Days to a Date in Excel (Shortcut + Formula)](https://trumpexcel.com/add-days-to-date-in-excel/)
    
*   [How to Add Months to Date in Excel (Easy Formula)](https://trumpexcel.com/add-months-to-date-excel/)
    
*   [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    
*   [How to SUM values between two dates (using SUMIFS formula)](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)
    
*   [Add Years to Date in Excel](https://trumpexcel.com/add-years-to-date-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/add-week-to-date-excel/#respond)

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