# Get Day Name from Date in Excel (Easy Formulas)

**Source:** https://trumpexcel.com/get-day-name-from-date-excel

---

[Skip to content](https://trumpexcel.com/get-day-name-from-date-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/get-day-name-from-date-excel/#below-title)

When working with dates in Excel, sometimes you may want to know what day the date is (whether it’s a Monday or a Tuesday, or any other weekday).

This could especially be useful in project planning, where some days could be for a specific task (such as having a project meeting or sending the progress report), or where you need to know what days the working days are and what days are the weekends.

In this tutorial, I will show you a couple of ways you can use to **convert dates into the day of the week and get its name in Excel**.

So let’s get to it!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/get-day-name-from-date-excel/#)

Get the Day Name Using Custom Number Formats
--------------------------------------------

One of the best methods to convert a date into the day name is by [changing the format of the cell that has the date](https://trumpexcel.com/change-date-format-excel/)
.

The good thing about this method is that while you see the day name in the cell, in the back end, it still continues to be the date. This way, you can still use the dates in calculations.

Suppose you have a data set as shown below, where I have some dates in column A for which I want to know the name of the day.

![Dates Data to convert to day names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20224%20445'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the dates in column A
2.  Click the Home tab

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20223'%3E%3C/svg%3E)

3.  In the Number group, click on the dialog box launcher (the tilted arrow at the bottom right part of the group in the ribbon)

![Click the Number group dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20522%20206'%3E%3C/svg%3E)

4.  In the Format Cells dialog box, click on the Custom category option

![Select Custom option in the format cells dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)

5.  In the Type field, enter **dddd**

![Enter dddd as the custom code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)

6.  Click Ok

The above steps would convert the dates in the cells in column A and give you the name of the day for those dates.

![Dates are now shown as day names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20208%20421'%3E%3C/svg%3E)

And as I mentioned, doing, this would only change the way the dates are being displayed in the cells. In the back end, the cells still contain the dates that can be used in calculations.

![Cell still has the date in the backend](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20375%20478'%3E%3C/svg%3E)

When I use the custom code dddd, it tells Excel that I want to show only the day name from the date, and hide the month and the year value.

Below are the formats you can use when you working with dates in Excel:

*   **d** – shows the day value from the date. If the day value is less than 10, only one digit is shown and if it’s 10 or more than 10, then two digits are shown.
*   **dd** – shows the day value from the date in two digits. If the day value is less than 10, a [leading zero](https://trumpexcel.com/add-leading-zeroes-excel/)
     is added to the number. For example, 5 would become 05
*   **ddd** – this will show you the day name in the short format. If it’s Monday it would show you Mon, for Tuesday it will show Tue, and so on.
*   **dddd** – when you use this custom format, it will show you the entire day name (such as Monday or Tuesday)

Note: For this method to work, you need to make sure that the dates are in a format that Excel understands as a date. For example, if you use Jan 21 2021, then it wouldn’t be converted into the day name as Excel doesn’t recognize this as a valid date format.

Get the Day Name Using TEXT Formula
-----------------------------------

You can also use the text formula in excel to convert a date into the name of the day.

However, unlike the above custom number format method, the result of the text formula would be a text string. This means that you would not be able to use the result of the text formula in calculations as a numeric or date value.

Let me show you how this method works.

Suppose I have a dates dataset as shown below and I want the name of the days in column B.

![Data with dates and column for day names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20362%20420'%3E%3C/svg%3E)

Below is the formula I can use to do this:

\=TEXT(A2,"dddd")

The above formula will give you the full name of the day (such as Monday or Tuesday).

![TEXT formula to get the day name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20477'%3E%3C/svg%3E)

All the custom number formats that are covered in the above section can also be used in the text formula. Just make sure that the format is within double quotes (as the one shown in the formula above).

Now, you must be wondering why you would ever use the TEXT formula when the custom formatting method (covered before this method) gives you the same result and seems easier to use.

Let me show you in what situation using the [TEXT formula](https://trumpexcel.com/excel-text-function/)
 to get day names can be useful.

Suppose I have the same data set as shown below, but now instead of getting the day name, I want to get an entire sentence where I have some text below or after the date name.

Let’s say I want to get the result as ‘Due Date – Monday’ (i.e., I want to add some text before the day name)

I can use the below formula to do this:

\="Due Date: "&TEXT(A2,"dddd")

![Day name with text added at the beginning](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20521%20474'%3E%3C/svg%3E)

Or, another example could be where you want to show whether the day is Weekday or Weekend followed by the day name. This can be done using the below formula:

\=IF(WEEKDAY(A2,2)>5,"Weekend: ","Weekday: ")&TEXT(A2,"dddd")

![Getting Day Name along with weekday or weekend](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20432'%3E%3C/svg%3E)

I’m sure you get the idea.

The benefit of using the TEXT formula is that you can combine the result of that formula with other formulas (such as [IF function](https://trumpexcel.com/excel-if-function/)
 or [AND](https://trumpexcel.com/excel-and-function/)
/[OR function](https://trumpexcel.com/excel-or-function/)
).

Also read: [Calculate Number of Weeks Between Two Dates in Excel](https://trumpexcel.com/weeks-between-two-dates-excel/)

Get the Day Name Using CHOOSE and WORKDAY formula
-------------------------------------------------

And lastly, let me show you how to get the denim using a combination of CHOOSE and WORKDAY formulas.

Below I have the data set where I have the dates in column A for which I want to get the day name.

![Data with dates and column for day names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20362%20420'%3E%3C/svg%3E)

Here is the formula that will do this:

\=CHOOSE(WEEKDAY(A2,2),"Mon","Tue","Wed","Thu","Fri","Sat","Sun")

![CHOOSE formula to get the day name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20798%20472'%3E%3C/svg%3E)

In the above formula, I have used the [WEEKDAY formula](https://trumpexcel.com/excel-weekday-function/)
 to get the weekday number of any given date.

Since I’ve specified the second argument of the weekday formula as 2, it would give me 1 for Monday, 2 for Tuesday, and so on.

This value is then used within the CHOOSE formula to get the day name (which is something that I have already specified in the formula).

This is definitely bigger and more complex than the TEXT formula we used in the previous section.

But there is one scenario where using this formula can be useful – when you want to get something specific to that day instead of getting the day name.

For example, below is the same formula where I have changed the day name with specific activities that need to be done on those days.

\=CHOOSE(WEEKDAY(A2,2),"Townhall","Proj Update Call","Buffer day","Support","Weekly Checkin","Weekend","Weekend")

![CHOOSE formula to get day specific text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20760%20492'%3E%3C/svg%3E)

In the above formula, instead of using the day names, I have used the name of the activities that need to be done on those days.

So these are three easy and simple ways you can use to convert a date value into the day name in Excel.

I hope you found this tutorial helpful!

**Other Excel tutorials you may also like:**

*   [How to Get the First Day of the Month in Excel (Easy Formulas)](https://trumpexcel.com/first-day-of-month-excel/)
    
*   [How to Add or Subtract Days to a Date in Excel](https://trumpexcel.com/add-days-to-date-in-excel/)
    
*   [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    
*   [How to Group Dates in Pivot Tables in Excel (by Years, Months, Weeks)](https://trumpexcel.com/group-dates-in-pivot-tables-excel/)
    
*   [How to Calculate Age in Excel using Formulas + FREE Calculator Template](https://trumpexcel.com/calculate-age-in-excel/)
    
*   [Check IF a Date is Between Two Given Dates in Excel](https://trumpexcel.com/check-if-date-is-between-two-dates/)
    
*   [How to Autofill Only Weekday Dates in Excel (Formula)](https://trumpexcel.com/autofill-only-weekday-dates-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/get-day-name-from-date-excel/#respond)

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