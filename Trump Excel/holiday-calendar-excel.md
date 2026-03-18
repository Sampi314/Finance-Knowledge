# Excel Holiday Calendar Template 2026 and Beyond (FREE Download)

**Source:** https://trumpexcel.com/holiday-calendar-excel

---

[Skip to content](https://trumpexcel.com/holiday-calendar-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/holiday-calendar-excel/#below-title)

The last few weeks have been really hectic for me at work. Weekdays are crazy and the weekends are never enough.

Early this week, I was going through our annual holiday calendar to check for the next holiday, and plan a vacation if possible.

And that gave me the idea for this Excel holiday calendar template.

In this tutorial, I will show you how to calculate the date of a given holiday (such as Labor Day).

And you can also get an awesome **Excel holiday list template** (free download) at the end of this blog.

[**Click here to download the template**](https://www.dropbox.com/s/uraw5nvqj0iwa8j/Holiday%20Calendar%20Template%20Excel%202021.xlsx?dl=1)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/holiday-calendar-excel/#)

Formula to Calculate Holidays in Excel (Labor Day)
--------------------------------------------------

Here is the formula to get the date for Labor Day in 2022 (which is the 1st Monday in September)

\=DATE(2023,9,1)+IF(WEEKDAY(DATE(2023,9,1),2)>1,7-WEEKDAY(DATE(2023,9,1),2)+1,1-WEEKDAY(DATE(2023,9,1),2))

It returns the date as 04 September 2023, which is the date of labor day in 2023.

This formula can easily be tweaked to get the date of holidays that fall on a given weekday of the month (such as President’s Day or Memorial Day).

### How the Formula Works

Since we know that Labor day is the 1st Monday of September, we start with the first of September 2023.

The following formula would give us the serial number of September 1, 2023:

\=DATE(2023,9,1)

Now we need to check whether the first day of September is a Monday or not. We do this using the following condition in the IF function:

WEEKDAY(DATE(2023,9,1),2)>1

WEEKDAY function gives a number based on what day of the week it is. Since I have used 2 as the second argument, it would return 1 for Monday, 2 for Tuesday, 3 for Wednesday, and so on.

If 1st day of September is not a Monday, the above IF condition would be TRUE and it would return the value given by the following part of the formula:

7-WEEKDAY(DATE(2023,9,1),2)+1

The above part simply subtracts the weekday number from 7 and adds 1, hence giving us the value that we should add to September 1, 2023, to get the first Monday.

And in case September 1, 2023, is a Monday, the following formula makes sure that the result of IF function is 0:

1-WEEKDAY(DATE(2023,9,1)

Below is an infographic that shows the same explanation (created using 2014 instead of 2023).

![Holiday Calendar - Date calculation in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20768%20260'%3E%3C/svg%3E)

Along similar lines, if you need to calculate other holidays. For example, the Presidents’ Day, which is held on the third Monday in February, can be calculated using the below formula:

\=DATE(B2,2,1)+IF(WEEKDAY(DATE(B2,2,1),2)>1,7-WEEKDAY(DATE(B2,2,1),2)+1,1-WEEKDAY(DATE(B2,2,1),2))+((3-1)\*7)

In the above formula, B2 refers to the year value.

Note: [Easter](https://en.wikipedia.org/wiki/Easter)
 is one holiday that is difficult to calculate. I Googled and found a formula that seems to be working. However, I have no idea how it works 🙂

BONUS EXCEL HOLIDAY CALENDAR TEMPLATE
-------------------------------------

Here is a FREE Excel Holiday Calendar template that gives you:

*   The list of holidays (in the selected year).
*   The number of days to go for the next holiday (number in the blue box). This works only for the current year.
*   The number of days to go for the next long weekend (number in the gray box). This works only for the current year.

All you need to do is select the year from the drop-down and it will automatically show you the list of holidays in the selected year.

![Excel Holiday Calendar 2020](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20773%20525'%3E%3C/svg%3E)

I have created this for the [holidays in the US, as it occurs on fixed dates or days in a month](https://trumpexcel.com/days-in-month-excel/)
.

In India (where I live), many holidays depend on the position of the moon (and many other factors), and hence it’s difficult to come up with such a holiday template.

**_Download Excel Holiday Calendar Template  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/uraw5nvqj0iwa8j/Holiday%20Calendar%20Template%20Excel%202022.xlsx?dl=1)
_**

_[Excel Functions](https://trumpexcel.com/excel-functions/)
 used to create this holiday calendar template: –>_ [WEEKDAY](https://trumpexcel.com/excel-weekday-function/)
 | [DATE](https://trumpexcel.com/excel-date-function/)
 | [IF](https://trumpexcel.com/excel-if-function/)
.

If you’re interested in learning how this holiday calendar template is created, you can unhide columns H-J in the template sheet and see the formulas.

You can also unhide Sheet1, where I have kept data used for the year [drop-down](https://trumpexcel.com/excel-drop-down-list/)
.

**You May Also Like the Following Excel Templates/Articles:**

*   [FREE Monthly & Yearly Excel Calendar Template.](https://trumpexcel.com/calendar-template/)
    
*   [Vacation Itinerary & Packing List Template.](https://trumpexcel.com/vacation-itinerary-packing-list-template/)
    
*   [Employee Leave/Vacation Tracker Template](https://trumpexcel.com/excel-leave-tracker/)
    .
*   [Calendar Integrated with a To-Do List Template](https://trumpexcel.com/calendar-to-do-list-template/)
    .
*   [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    
*   [How to Make Dynamic Monthly and Yearly Calendar in Excel?](https://trumpexcel.com/interactive-calendar-excel/)
    
*   [Free Printable Calendar Generator](https://trumpexcel.com/tools/printable-calendar-generator/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

15 thoughts on “Excel Holiday Calendar Template (FREE Download)”
----------------------------------------------------------------

1.  Sumit, what if the holiday falls on a Saturday? How do you figure the Observed date?
    
    [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-13169)
    
2.  Hi Sumit, thanks for the calendar! I have added in a column to include half days, is there a way to change the formula so instead of calculating a full day (i.e. 1) it will calculate as .5 instead?
    
    [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-12466)
    
3.  Thank you so much for this, I was wondering how to extend the years to go further than 2020
    
    [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-11549)
    
4.  Hi,  
    Thank you for the help, I would like to know how can I CREATE A SPREASHEET LIKE THIS MY SELF ?  
    tHE EMPLOYES HAVE A DIFERETN AMOUNT OF ANUAL LEAVE HOW CAN I GET THET SHOW IN THE bALANCE ?
    
    [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-10822)
    
5.  HI Sumit,
    
    This is really excellent task but could you please share the video of this task so that I can understand more as I have tried a lot but still unable to understand.
    
    \=DATE(A2,2,1)+IF(WEEKDAY(DATE(A2,2,1),2)>1,7-WEEKDAY(DATE(A2,2,1),2)+1,1-WEEKDAY(DATE(A2,2,1),2))+((3-1)\*7)
    
    At the end why r u substracting the (3-1) and multiply from 7 no idea.
    
    [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-10530)
    
6.  Hi,  
    May I know how to change the row of Monday to Sunday for year 2018.
    
    Many thanks!
    
    Choi
    
    [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-9848)
    
7.  Sumit – Very useful! Thank you for making the downloadable template! Quick question, how can I tweak the formulas, for say Independence Day, to show the holiday as the day before or the day after? For example, if 7/4 is a Saturday, the holiday “day off” is Friday 7/3. And if 7/4 is a Sunday, the day off is Monday 7/5.  
    Thank you!
    
    [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-3415)
    
    *   Hey Frank.. In such a case, you can create an additional column and use the following formula: =IF(\[@Weekday\]=”Saturday”,\[@Date\]-1,IF(\[@Weekday\]=”Sunday”,\[@Date\]+1,\[@Date\]))
        
        [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-3436)
        
8.  Wow this is great! Any chance you have a dashboard for Public Holidays in India?
    
    [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-2847)
    
    *   Hello Lauren.. A lot of Public holidays in India vary year on year. It makes almost impossible to get a formula that can track it.
        
        [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-2867)
        
    *   Hey Lauren.. Public holidays in India are not on fixed dates or days, so it’s almost impossible to create a formula that can return the correct date for every year.
        
        [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-3435)
        
9.  I too was searching for a holiday calendar suitable for US Federal offices (observing the 10 standard holidays) and ended up hacking together the attached version, which is printable as well. Feel free to share!
    
    [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-1505)
    
    *   Glad you found this useful 🙂
        
        [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-1507)
        
10.  Very creative little dashboard! My only recommendation would be to put the data inside an Excel table so it is easy to add/subtract holidays based on the year without messing up the lookup formulas. Great job!
    
    [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-1405)
    
    *   Thanks Chris.. And your are right, table is the right way to go. Will make that change in the download file
        
        [Reply](https://trumpexcel.com/holiday-calendar-excel/#comment-1406)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/holiday-calendar-excel/#respond)

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