# Get Today's Date in Power Query (Easy Formula)

**Source:** https://trumpexcel.com/power-query/todays-date

---

[Skip to content](https://trumpexcel.com/power-query/todays-date/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/power-query/todays-date/#below-title)

[Power Query](https://trumpexcel.com/power-query/)
 doesn’t have a [_TODAY()_ function](https://trumpexcel.com/excel-today-function/)
 like Excel does. But there’s a formula that works the same way.

In this article, I’ll show you how to use it to get today’s date in Power Query, and then how to use it to calculate how many days have passed since a given date.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/power-query/todays-date/#)

Using the DateTime.LocalNow() Formula
-------------------------------------

Just like the TODAY function in Excel, Power Query has the _DateTime.LocalNow()_ that works the same way.

So if you use this formula, it is going to give you the current date based on your system’s date and time settings.

Let me show you how it works.

Below, I have a dataset where I have the start date in column C, and I want to get the current date in a new column.

![Dataset in Power Query to Get current date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20771%20264'%3E%3C/svg%3E)

Here’s how to add a Current Date column:

1.  Go to the **Add Column** tab and click **Custom Column**.

![Click on Custom Column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20473%20210'%3E%3C/svg%3E)

2.  Rename the column to **Current Date**.
3.  Enter the formula below in the Custom Column dialog box

\= DateTime.Date(DateTime.LocalNow())

    = DateTime.Date(DateTime.LocalNow())

![Enter the formula in the custom column dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201050%20658'%3E%3C/svg%3E)

4.  Click **OK**:

This will add a new column that will show you the current date (as shown below).

![Current date column is added](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201021%20269'%3E%3C/svg%3E)

**How does the formula work?**

_DateTime.LocalNow()_ returns the current date and time from your system. But we just want the date and not the time. I have wrapped this formula within the _DateTime.Date_

This only gives us the date without the time component.

**Note:** You can skip using the _DateTime.Date()_ and just use _DateTime.LocalNow()_ on its own. But this will add a column that would have the date as well as the time. So you’d need an extra step to change the column type to Date, which removes the time part.

Calculating Days Elapsed Between Two Dates in Power Query
---------------------------------------------------------

A common thing people want to do with today’s date is figure out how many days have passed since a certain date.

Let’s see how to do that.

### **Option 1: Using the Current Date column**

Let’s suppose you already have the current date column as shown below.

![Dataset in Power Query to Get current date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20771%20264'%3E%3C/svg%3E)

Here are the steps to get another column that will show the number of days elapsed between the start date and the current date.

1.  Go to **Add Column** and click **Custom Column**.
2.  Name the column **Days Elapsed**.
3.  Enter this formula and click **OK**:

\= \[Current Date\] - \[Start Date\]

    = [Current Date] - [Start Date]

![Formula to get days elapsed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201050%20658'%3E%3C/svg%3E)

4.  The result will show as a Duration type. Right-click the column header, go to **Change Type**, and select **Whole Number**.

![Change type to whole number](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20658%20505'%3E%3C/svg%3E)

That gives you the number of days between the start date and today.

![Days elapsed column added](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201139%20259'%3E%3C/svg%3E)

Now, if you do not want to show the current date column, you can remove it.

### **Option 2: Calculate directly (no Current Date column needed)**

You can also use the full formula in the custom column dialog box that will give you the number of days between the start date and the current date.

This method doesn’t require you to first have a column that has the current date.

Let’s suppose you have a dataset as shown below.

![Dataset in Power Query to Get current date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20771%20264'%3E%3C/svg%3E)

Here are the steps to get the column with the number of days lapsed:

1.  Go to **Add Column** and click **Custom Column**.
2.  Name the column **Days Elapsed**.
3.  Enter this formula and click **OK**:

\= DateTime.Date(DateTime.LocalNow()) - \[Start Date\]

    = DateTime.Date(DateTime.LocalNow()) - [Start Date]

![Formula to get days elapsed from given date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201050%20658'%3E%3C/svg%3E)

4.  Right-click the column header, go to **Change Type**, and select **Whole Number**.

Same result, but without the extra column. Use this one if you only need the final number.

![Days elapsed column from one formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201017%20262'%3E%3C/svg%3E)

Things to Keep in Mind
----------------------

*   **Always include the parentheses.** If you type _DateTime.LocalNow_ without the (), Power Query returns the function name instead of the date. Think of it like TODAY() in Excel. No arguments, but the parentheses still need to be there.
*   **Subtracting two dates gives a Duration, not a number.** When you subtract dates in Power Query, the result is a Duration type. Change the column type to Whole Number to get an actual day count.
*   **Convert your source date columns to Date type first.** If your Start Date column has both a date and a time in it, convert it to Date before subtracting. Mixed types can give you unexpected results.

In this article, I showed you how to get today’s date in Power Query using a simple built-in function.

I hope you found this article helpful.

**Other Power Query articles you may also like:**

*   [Combine CSV Files When Column Headers Don’t Match](https://trumpexcel.com/power-query/combine-csv-inconsistent-headers/)
    
*   [Power Query Functions](https://trumpexcel.com/power-query/functions/)
    
*   [Create All Possible Combinations from Lists](https://trumpexcel.com/create-all-combinations-from-lists-excel/)
    
*   [Free Power Query Course](https://trumpexcel.com/power-query-course/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

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