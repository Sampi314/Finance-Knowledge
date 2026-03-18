# How to Autofill Only Weekday Dates in Excel (Formula)

**Source:** https://trumpexcel.com/autofill-only-weekday-dates-excel

---

[Skip to content](https://trumpexcel.com/autofill-only-weekday-dates-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/autofill-only-weekday-dates-excel/#below-title)

While working with dates in Excel, you may have a need to fill a column only with the dates that occur on a weekday.

This is usually needed when you’re creating a project plan, where only the weekday dates can be used, and the weekend dates are holidays.

In this short tutorial, I am going to show you two simple ways to quickly autofill weekday dates in a column in Excel.

We’ll first look at an inbuilt feature in excel that can quickly do this value, and then we will also learn about a formula that you can use to get only the weekday dates.

Let’s dive in!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/autofill-only-weekday-dates-excel/#)

Using the ‘Fill Weekday’ Option in Autofill
-------------------------------------------

Microsoft Excel has an inbuilt auto-fill option called “Fill Weekdays” that allows you to quickly fill a sequence of weekday dates only.

Let me show you how it works.

Below I have a date in cell A1, and I want to fill the cells below A1 with only the weekday dates (i.e. Monday to Friday).

![Date in cell A1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20335%20541'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select cell A1
2.  Place the mouse cursor at the bottom right of the selection. you will notice that the cursor changes into a plus icon. This is called a [Fill Handle](https://trumpexcel.com/how-to-use-fill-handle-in-excel/)
    

![Plus icon when cursor placed at the bottom right of the cell selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20317%20520'%3E%3C/svg%3E)

3.  Hold the left mouse key and drag the fill handle down to auto-populate the cells in the column
4.  Click on the Auto Fill option icon that appears at the bottom right of the selected cells

![Autofill Options icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20291%20556'%3E%3C/svg%3E)

5.  Click on the ‘Fill Weekdays’ option

![Fill Weekday option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20317%20551'%3E%3C/svg%3E)

The above steps would instantly fill the column with a sequence of dates and occur on weekdays only.

![Column filled with weekdays only](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20345%20538'%3E%3C/svg%3E)

_If you do not see the Auto Fill icon, you can also get the same thing done by selecting the cells, going to the Home tab, in the Editing group clicking on the Fill option, and then clicking on the Series option. This will open the Series dialog box where you can select the Weekdays option to fill the entire column with the weekday dates only._

While this is a quick and easy way to quickly fill a column with only the weekday dates, remember that **it will consider Monday to Friday as the weekday dates, and Saturday and Sunday as the weekend dates**.

It does not give you the flexibility to choose the days you want to consider weekdays.

For example, if you want the weekdays to be dates that occur from Monday to Saturday, and only Sunday as the weekend date, then you can not use this method.

In that case, you’re better off using the formula method covered later in this tutorial.

### Fill Handle Not Showing – How to Fix?

When I shared this trick on my YouTube channel, some people reported that they cannot see the fill handle when they select a cell (i.e., when they place the cursor at the bottom right of the cell selection, their cursor does not change into a plus icon).

If you’re facing the same problem, here is how to fix it:

1.  Click the File option in the ribbon

![Click the File option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20603%20224'%3E%3C/svg%3E)

2.  Click on Options. This will open the options dialog box
3.  Select the Advanced option in the left pane of the [Excel Options dialog box](https://trumpexcel.com/excel-options-hacks/)
    

![Click on the Advanced option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20735%20491'%3E%3C/svg%3E)

4.  Check the option – “Enable fill handle and cell drag and drop”

![Enable fill handle and cell drag and drop option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20664%20471'%3E%3C/svg%3E)

6.  Click Ok

The fill handle should now be available to use in the worksheet.

Also read: [Excel Calculate Days Between Two Dates](https://trumpexcel.com/number-of-days-between-two-dates/)

Using Formula to Get Weekday Dates Only
---------------------------------------

If you want to fill a column with the dates that occur on specific days, you can easily do that using the WORKDAY.INTL function.

WORKDAY.INTL function returns the date after a specified number of days, and it also allows you to choose the days in the week that are acceptable.

Let me first show you how it works and then I’ll explain the formula in detail.

Below I have a date in column A1 and I want to fill the column with dates that occur on weekdays only (where we give would be Monday to Friday).

![Date in cell A1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20335%20541'%3E%3C/svg%3E)

Here is a formula that will do this for me:

\=WORKDAY.INTL(A2,1,"0000011")

![Formula to get weekdays only in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20565%20551'%3E%3C/svg%3E)

Once I have this formula in cell A2, I can copy it for all the other cells in the column.

**How does this formula work?**

[WORKDAY.INTL](https://trumpexcel.com/excel-workdayintl-function/)
 function takes 3 arguments:

1.  The start date – which is the date that I have in cell A1
2.  The number of days after which I want the date. in this case, since I need a sequence of days one after the other, I have kept this as one
3.  The Weekend – this is where I can specify the days that should be considered as weekdays and weekends

The magic happens in the third argument where I have used “0000011”

There are 7 digits in the double quotes, where each digit specify whether that day should be considered a weekday or a weekend. 0 means that it would be a weekday and 1 means it would be a weekend.

0000011 means that the first five days of the week (which would be Monday to Friday) would be considered weekdays, and the last two days of the week (which would be Saturday and Sunday) would be considered weekend days.

So when the WORKDAY.INTL function is giving me the next date, it makes sure that only the working days are returned, and weekends are not.

The best thing about this formula is that you can specify any day as a working day or a non-working day.

So if you want to fill a column with dates that occur only on Monday, Wednesday, and Friday, you can modify the third argument in the formula as shown below:

\=WORKDAY.INTL(A2,1,"0101011")

You can also modify the above formula to give you only the weekend dates as well. to do that, you will have to change the third argument to make the first five days as non-working, and make the last two days as working.

\=WORKDAY.INTL(A2,1,"1111100")

So these are two simple ways you can use to quickly auto-fill a sequence of weekday dates only. if you’re looking for a super quick and easy solution, you can use the inbuilt Fill Weekdays option in Autofill.

And if you need more control over what days should be considered working and what days should be considered weekend days, you can use the formula method.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [Check IF a Date is Between Two Given Dates in Excel](https://trumpexcel.com/check-if-date-is-between-two-dates/)
    
*   [Excel WEEKDAY Function](https://trumpexcel.com/excel-weekday-function/)
    
*   [How to Highlight Weekend Dates in Excel?](https://trumpexcel.com/highlight-weekend-dates-excel/)
    
*   [Get Day Name from Date in Excel (Easy Formulas)](https://trumpexcel.com/get-day-name-from-date-excel/)
    
*   [How to Get the First Day of the Month in Excel](https://trumpexcel.com/first-day-of-month-excel/)
    
*   [How to Add or Subtract Days to a Date in Excel](https://trumpexcel.com/add-days-to-date-in-excel/)
    
*   [How to Quickly Insert Date and Timestamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    
*   [How to Quickly Fill Numbers in Cells without Dragging](https://trumpexcel.com/fill-numbers-in-cells-without-dragging/)
    
*   [Highlight Dates Before Today in Excel (An Easy Guide)](https://trumpexcel.com/highlight-dates-before-today-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Autofill Only Weekday Dates in Excel (Formula)”
---------------------------------------------------------------------

1.  Thank you for this tutorial. I have been able to successfully implement this is my spreadsheet. I am encountering blank cells where the Saturday and Sunday dates are being skipped. How can I remove, or hide the blanks and still keep the dynamic nature of the formula?
    
    [Reply](https://trumpexcel.com/autofill-only-weekday-dates-excel/#comment-45693)
    
2.  Thank you so much for this tutorial. I read several others and I just couldn’t figure it out. No one else explained that the 0s and 1s in the “magical” part of the formula stood for each day of the week. When I saw your explanation it all suddenly clicked! Now I feel like and Excel wiz!
    
    [Reply](https://trumpexcel.com/autofill-only-weekday-dates-excel/#comment-44093)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/autofill-only-weekday-dates-excel/#respond)

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