# How to Highlight Weekend Dates in Excel?

**Source:** https://trumpexcel.com/highlight-weekend-dates-excel

---

[Skip to content](https://trumpexcel.com/highlight-weekend-dates-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/highlight-weekend-dates-excel/#below-title)

When working with dates in Excel, you may sometimes have a need to highlight only specific days of the week.

For example, you may have a list of dates where you want to **highlight all the weekend dates**.

This can easily be done using Conditional Formatting with a little bit of formula know-how.

In this tutorial, I will show you how to highlight the weekend dates in a date data set. The method covered here can also be used to highlight any kind of dates (say Mondays or Tuesdays or alternate days)

So let’s get to it!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/highlight-weekend-dates-excel/#)

Highlight Weekend Dates Using Conditional Formatting
----------------------------------------------------

Conditional Formatting in Excel allows you to assess the value in a cell and then apply it to format if the specified condition is met.

We can use Conditional Formatting to analyze the date in a range of cells, and if the date lies on a weekend, highlight it.

Below I have a dates dataset where I want to highlight all the dates that occur on a Saturday or a Sunday.

![Date Dataset to highlight weekend dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20407%20464'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the cells that contain the dates

![Select the cells that have the dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20406%20465'%3E%3C/svg%3E)

2.  Click the Home tab

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20603%20223'%3E%3C/svg%3E)

3.  In the Styles group, click on Conditional Formatting icon

![Click on Conditional Formatting icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20679%20223'%3E%3C/svg%3E)

4.  In the options that appear, click on ‘New Rule’ option

![Click on New Rule option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20327%20618'%3E%3C/svg%3E)

5.  In the ‘New Formatting Rule’ dialog box, click on ‘Use a formula to determine which cells to format’

![Select Use a formula to determine what cells to format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

6.  Enter the following formula in the formula field: **\=WEEKDAY(B2,2)>5**

![Enter the formula for Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

7.  Click the Format button

![Click the Format button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

8.  Specify the formatting (I will go with the Yellow [fill color)](https://trumpexcel.com/shortcuts-fill-color-excel/)
    

![Select the color for conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20498'%3E%3C/svg%3E)

9.  Click OK
10.  Click OK

The above steps would highlight those dates that are either a Saturday or a Sunday.

![Dataset where weekends are highlighted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20407%20465'%3E%3C/svg%3E)

**How does this work?**

I have used a formula in [Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
 that checks each cell in the selected range against that formula.

If the result of that formula is TRUE, then the cell is highlighted in the specified color (yellow in this example), and if the result of the formula is FALSE, then nothing happens.

I had used the [WEEKDAY formula](https://trumpexcel.com/excel-weekday-function/)
 that takes the date as the input and returns a value that tells me what day of the week that date represents.

For example, if it is a Monday it would return 1 and if it is a Tuesday it would return 2, and so on. For Saturday and Sunday, it returns 6 and 7 respectively.

And since I have the formula, =WEEKDAY(B2,2)>5, it checks whether the weekday value for a date is more than 5 or not. This would only return TRUE for those dates that occur on a Saturday or Sunday.

So, only those dates that occur on weekends (Sat or Sun) are highlighted.

The same steps (covered above) with a slight change in formula can also be used to highlight only Sunday dates or any specific day of the week.

### Highlight Only Sunday Dates

Use the below formula in Conditional Formatting to only highlight dates that occur on Sunday:

 =WEEKDAY(B2,2)>6

### Highlight Specific Days of the Week

In case you want to highlight specific days of the week, you can do that using a simple OR formula with the WEEKDAY formula in conditional formatting.

Below is the formula that will highlight only those dates that occur on a Tuesday or a Thursday:

   =OR(WEEKDAY(B2,2)=2, WEEKDAY(B2,2)=4)

The above OR formula checks whether the WEEKDAY formula for the date returns 2 or 4 (where 2 is for Tuesday and 4 is for Thursday).

And in case any of these two WEEKDAY formulas return a TRUE, the OR formula also returns a TRUE.

So this is how you can use a simple formula in Conditional Formatting to **highlight weekend dates** (or specific weekdays) in Excel.

I hope you found this tutorial useful!

**Other Excel tutorials you may also like:**

*   [Get Day Name from Date in Excel](https://trumpexcel.com/get-day-name-from-date-excel/)
    
*   [How to Add or Subtract Days to a Date in Excel (Shortcut + Formula)](https://trumpexcel.com/add-days-to-date-in-excel/)
    
*   [Highlight Rows Based on a Cell Value in Excel (Conditional Formatting)](https://trumpexcel.com/highlight-rows-based-on-cell-value/)
    
*   [How to Highlight Blank Cells in Excel](https://trumpexcel.com/highlight-blank-cells-in-excel/)
    
*   [Highlight the Active Row and Column in a Data Range in Excel](https://trumpexcel.com/highlight-active-row-column-excel/)
    
*   [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    
*   [How to Autofill Only Weekday Dates in Excel (Formula)](https://trumpexcel.com/autofill-only-weekday-dates-excel/)
    
*   [Highlight Dates Before Today in Excel](https://trumpexcel.com/highlight-dates-before-today-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Highlight Weekend Dates in Excel?”
-------------------------------------------------------

1.  Unfortunately, this does not work for me because in Excel Sunday = 1 and Saturday = 7
    
    [Reply](https://trumpexcel.com/highlight-weekend-dates-excel/#comment-37858)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/highlight-weekend-dates-excel/#respond)

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