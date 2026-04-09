# Calculate Fiscal Year from Date in Excel (Easy Formulas)

**Source:** https://trumpexcel.com/fiscal-year-excel

---

[Skip to content](https://trumpexcel.com/fiscal-year-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/fiscal-year-excel/#below-title)

I was recently working on a project where I had some dates and had to classify each date into its fiscal year (also sometimes called the financial year).

While Excel does not have a dedicated function to do this, it can quickly be done using a combination of functions.

In this article, I will show you how to **calculate the fiscal year from a date in Excel** using a formula and some variations to use that formula.

**[_Click here to download the example file and follow along_](https://www.dropbox.com/scl/fi/nwoqoqrldo7zfcexaejht/Fiscal-Year.xlsx?rlkey=21urnr824sipmf2faiopougsj&dl=1)
**

This Tutorial Covers:

[Toggle](https://trumpexcel.com/fiscal-year-excel/#)

Get Fiscal Year From Date (same Fiscal Period)
----------------------------------------------

Below is a data set where I have transaction dates in column A, and I want to get the fiscal year value for each date in column B.

![Data set to get the fiscal year from date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20433%20280'%3E%3C/svg%3E)

For this example, I will assume that the new fiscal year for all the dates starts in July.

We can’t just extract the _Year_ value of the date to get the fiscal year (as fiscal year is different from calendar year). In our example, since the fiscal year starts in July, any date before July would be considered in the current year’s fiscal period, and any date in or after July would be considered a part of the next year’s fiscal period.

So, a transaction date of 05-Mar-2025 would be in the fiscal year 2025, while 05-Sep-2025 would be in the fiscal year 2026.

Here is the formula to get the fiscal year using the date:

\=YEAR(A2)+(MONTH(A2)>=7)

Enter this formula in cell B2 and copy it for all the other cells in the column.

![Formula to get the fiscal year value from date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20583%20332'%3E%3C/svg%3E)

In case you see a date in cell B2, you can change the cell format to show the numbers (instead of the date). Here are the steps to do this:

1.  Select the cells that have the result that is showing up as a date instead of numbers.
2.  Click the Home tab.
3.  Click on the formatting dropdown in the Number group.
4.  Select the ‘General’ option.

![Change the cell formatting to general to show numbers instead of dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20518'%3E%3C/svg%3E)

Now, let me explain how this formula works.

In the above formula, we extract the year value from the date using the YEAR function.

However, since a new fiscal year starts from July onwards, we check whether the Month value in the date is more than or equal to 7 or not.

If the month value is seven or more, (MONTH(A2)>=7) would return TRUE, where TRUE has a value of 1 in Excel. This 1 is then added to the year value we extracted from the date to get the fiscal year value.

If the month value is less than 7, (MONTH(A2)>=7) would return FALSE, which has the value of 0 in Excel. This would then give us the fiscal year value, which is the same as the year in the date.

But what if the fiscal year is not between July and June? What if it starts in some other month, say Apr-Mar?

In that case, you need to adjust the formula by using a different month number to compare with.

For example, if the fiscal year is from April to March, then a formula would become:

\=YEAR(A2)+(MONTH(A2)>=4)

In case your fiscal year and calendar year are the same (i.e., Jan-Dec), Then the fiscal year would be the same as the year in the date (Which you can extract using the YEAR function)

Also read: [How to Calculate Years of Service in Excel](https://trumpexcel.com/calculate-years-of-service-excel/)

Get Fiscal Year From Date (different Fiscal Periods)
----------------------------------------------------

In the above example, I assumed that the fiscal period for all the transactions was July to June.

But what if we have different fiscal periods for different transactions?

For example, I have a dataset below with dates in column A and the month in which the fiscal year starts in column B, and I want to get the Fiscal year value in column C.

![Dataset to calculate fiscal year from date with first month of each fiscal year](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20631%20282'%3E%3C/svg%3E)

The formula below works in this case and gives us the fiscal year value:

\=YEAR(A2)+IF(B2<>1, MONTH(A2)>=B2,0)

Enter this formula in cell B2 and copy it for all the other cells in the column.

![Formula to calculate fiscal year from date with different fiscal years](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20696%20325'%3E%3C/svg%3E)

In the above formula, I extract the year value from the date using the YEAR function.

Now, I need to analyze the start month of the fiscal year to determine whether the year value I’ve extracted remains the fiscal year value or it would be the next year.

This is done by the following part of the formula:

_IF(B2<>1, MONTH(A2)>=B2,0)_

Here, the above part of the formula checks for two conditions and does the following:

*   If the month value in the date is more than that of the start date of the first month of the fiscal year, then I need to add 1 to the Year value that I extracted from the date. And if the month value of the date is less than that of the start date of the first month of the fiscal year, I don’t need to change the Year value extracted from the date.
*   In case the fiscal year starts from January itself (which is month 1), The fiscal year would be the same as the year extracted from the date.

Also read: [Calculate Quarter from Date in Excel (Easy Formula)](https://trumpexcel.com/calculate-quarter-from-date-excel/)

Get Fiscal Year Range from Date
-------------------------------

In most cases, a fiscal year is written in the format 2024-2025 (which indicates that the fiscal year started in 2024 and ends in 2025).

So, if you want to get the result in this format, you can adjust the formula to do this.

Below is the data set where I have transaction dates in column A, the fiscal year start month in column B, and I want to get the fiscal dates in column C.

![Dataset to calculate fiscal year from date with first month of each fiscal year](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20631%20282'%3E%3C/svg%3E)

Here is the formula that would give me the result in the desired format:

\=(YEAR(A2)+IF(B2<>1, MONTH(A2)>=B2,1)-1)&"-"&(YEAR(A2)+IF(B2<>1, MONTH(A2)>=B2,0))

Enter this formula in cell B2 and copy it for all the other cells in the column.

![Formula to get the fiscal year value as a range of two years](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20312'%3E%3C/svg%3E)

The above formula works the same way as covered in the previous section, but since we want a range, it uses the ‘&’ to concatenate the year value, which is one less than the fiscal year value (along with the dash in between).

In this article, I covered some simple formulas to get the fiscal year from a date in Excel.

I’ve shown both scenarios where the starting month of the fiscal year is fixed, and you need to get the fiscal year for a set of dates, or where we have a different fiscal year starting month for each date.

Also read: [How to Group Dates in Pivot Tables in Excel (by Years, Months, Weeks)](https://trumpexcel.com/group-dates-in-pivot-tables-excel/)

Fiscal Year vs Financial Year
-----------------------------

The terms “fiscal year” and “financial year” are often used interchangeably, and both refer to a 12-month period used for accounting purposes by businesses and governments.

In the context of companies in the United States, “fiscal year” and “financial year” mean the same thing and refer to the 12 consecutive months used as an accounting period.

The key difference, if any, might be in the usage based on the entity being referred to. For example, “fiscal year” is more commonly used when discussing governmental accounting and budgeting.

Both “fiscal year” and “financial year” are used when referring to businesses, but the term might be chosen based on regional or industry-specific practices.

I hope this article was useful for you. If you know of any other method that can be used to do this, do let me know in the comments section.

**Other Excel articles you may also like:**

*   [How to Get the Number of Days in a Month in Excel?](https://trumpexcel.com/days-in-month-excel/)
    
*   [FREE Monthly & Yearly Excel Calendar Template](https://trumpexcel.com/calendar-template/)
    
*   [How to Change Date Format In Excel?](https://trumpexcel.com/change-date-format-excel/)
    
*   [Last Date of the Year in Excel (Formula)](https://trumpexcel.com/end-of-year-formula-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/fiscal-year-excel/#respond)

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