# Calculate the Number of Months Between Two Dates in Excel (Easy Formulas)

**Source:** https://trumpexcel.com/calculate-months-between-two-dates

---

[Skip to content](https://trumpexcel.com/calculate-months-between-two-dates/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/calculate-months-between-two-dates/#below-title)

If you manage multiple projects, you would have a need to know how many months have passed between two dates.

Or, if you’re in the planning phase, you may need to know the same for the start and end date of a project.

There are multiple ways to calculate the number of months between two dates (all using different formulas).

In this tutorial, I will give you some formulas that you can use to get the number of months between two dates.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/calculate-months-between-two-dates/#)

Using DATEDIF Function (Get Number of Completed Months Between Two Dates)
-------------------------------------------------------------------------

It’s unlikely that you will get the dates that have a perfect number of months. It’s more likely to be some number of months and some days that are covered by the two dates.

For example, between 1 Jan 2020 and 15 March 2020, there are 2 months and 15 days.

If you only want to calculate the total number of months between two dates, you can use the DATEDIF function.

Suppose you have a dataset as shown below where you only want to get the total number of months (and not the days).

![Data to calculate months between two dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20321%20307'%3E%3C/svg%3E)

Below is the [DATEDIF formula](https://trumpexcel.com/excel-datedif-function/)
 that will do that:

\=DATEDIF(A2,B2,"M")

![DATEDIF formula to get number of month between dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20492%20365'%3E%3C/svg%3E)

The above formula will give you only the total number of completed months between two dates.

DATEDIF is one of the few undocumented functions in Excel. When you type the =DATEDIF in a cell in Excel, you would not see any IntelliSense or any guidance on what arguments it can take. So, if you’re using DATEDIF in Excel, you need to know the syntax.

In case you want to get the total number of months as well as days between two dates, you can use the below formula:

\=DATEDIF(A2,B2,"M")&"M "&DATEDIF(A2,B2,"MD")&"D"

![Use DATEDIF to get month number as well as the days numbers between dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20744%20363'%3E%3C/svg%3E)

Note: DATEDIF function will exclude the start date when counting the month numbers. For example, if you start a project on 01 Jan and it ends on 31 Jan, the DATEDIF function will give the number of months as 0 (as it doesn’t count the start date and according to it only 30 days in January have been covered)

Also read: [Calculating Time In Excel](https://trumpexcel.com/calculate-time-in-excel/)

Using YEARFRAC Function (Get Total Months Between Two Dates)
------------------------------------------------------------

Another method to get the number of months between two specified dates is by using the YEARFRAC function.

The YEARFRAC function will take a start date and end date as input arguments and it will give you the number of years that have passed during these two dates.

Unlike the DATEDIF function, the YEARFRAC function will give you the values in decimal in case a year has not elapsed between the two dates.

For example, if my start date is 01 Jan 2020 and end date is 31 Jan 2020, the result of the YEARFRAC function will be 0.833. Once you have the year value, you can get the month value by multiplying this with 12.

Suppose you have the dataset as shown below and you want to get the number of months between the start and end date.

![Data to calculate months between two dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20321%20307'%3E%3C/svg%3E)

Below is the formula that will do this:

\=YEARFRAC(A2,B2)\*12

This will give you the months in decimals.

![YEARFRAC function to get number of month in decimal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20502%20366'%3E%3C/svg%3E)

In case you only want to get the number of complete months, you can wrap the above formula in INT (as shown below):

\=INT(YEARFRAC(A2,B2)\*12)

Another major difference between the DATEDIF function and YEARFRAC function is that the YEARFRAC function will consider the start date as a part of the month. For example, if the start date is 01 Jan and end date is 31 Jan, the result from the above formula would be 1

Below is a comparison of the results you get from DATEDIF and YEARFRAC.

![Difference between YEARFRAC and DATEDIF function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20652%20310'%3E%3C/svg%3E)

Also read: [Convert Days to Months in Excel](https://trumpexcel.com/convert-days-to-months-excel/)

Using the YEAR and MONTH Formula (Count All Months when the Project was Active)
-------------------------------------------------------------------------------

If you want to know the total months that are covered between the start and end date, then you can use this method.

Suppose you have the dataset as shown below:

![Data to calculate months between two dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20321%20307'%3E%3C/svg%3E)

Below is the formula that will give you the number of months between the two dates:

\=(YEAR(B2)-YEAR(A2))\*12+MONTH(B2)-MONTH(A2)

![using YEAR and MONTH formula to get the month count](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20706%20363'%3E%3C/svg%3E)

This formula uses the YEAR function (which gives you the year number using the date) and the MONTH function (which gives you the month number using the date).

The above formula also completely ignores the month of the start date.

For example, if your project starts on 01 Jan and ends on 20 Feb, the formula shown below will give you the result as 1, as it completely ignores the start date month.

In case you want it to count the month of the start date as well, you can use the below formula:

\=(YEAR(B2)-YEAR(A2))\*12+(MONTH(B2)-MONTH(A2)+1)

You may want to use the above formula when you want to know-how in how many months was this project active (which means that it could count the month even if the project was active for only 2 days in the month).

So these are three different ways to calculate months between two dates in Excel. The method you choose would be based on what you intend to calculate (below is a quick summary):

*   Use the DATEDIF function method if you want to get the total number of completed months in between two dates (it ignores the start date)
*   Use the YEARFRAC method when you want to get the actual value of months elapsed between tow dates. It also gives the result in decimal (where the integer value represents the number of full months and decimal part represents the number of days)
*   Use the YEAR and MONTH method when you want to know how many months are covered in between two dates (even when the duration between the start and the end date is only a few days)

Below is how each formula covered in this tutorial will count the number of months between two dates:

![Difference between YEARFRAC and DATEDIF and YEAR & MONTH function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20783%20323'%3E%3C/svg%3E)

Hope you found this Excel tutorial useful.

**You may also like the following Excel tips and tutorials:**

*   [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    
*   [How to Remove Time from Date/Timestamp in Excel](https://trumpexcel.com/remove-time-from-date-in-excel/)
    
*   [Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [How to Quickly Insert Date and Timestamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    
*   [Convert Date to Text in Excel](https://trumpexcel.com/convert-date-to-text-excel/)
    
*   [How to SUM values between two dates in Excel](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)
    
*   [How to Add Months to Date in Excel](https://trumpexcel.com/add-months-to-date-excel/)
    
*   [How to Calculate Years of Service in Excel (Easy Formulas)](https://trumpexcel.com/calculate-years-of-service-excel/)
    
*   [How to Make an Interactive Calendar in Excel? (FREE Template)](https://trumpexcel.com/interactive-calendar-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/calculate-months-between-two-dates/#respond)

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