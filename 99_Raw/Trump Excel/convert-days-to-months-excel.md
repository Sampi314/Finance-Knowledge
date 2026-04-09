# Convert Days to Months in Excel (2 Easy Formulas)

**Source:** https://trumpexcel.com/convert-days-to-months-excel

---

[Skip to content](https://trumpexcel.com/convert-days-to-months-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-days-to-months-excel/#below-title)

In this article, I will show you how to convert days to months in Excel using a couple of simple formulas.

This could be useful when you are creating a project plan that has a start and an end date, and you want to know how many months there are between the start and the end date.

Let’s see how to do this using a simple example.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/convert-days-to-months-excel/#)

Convert Days to Months Using DATEDIF Function
---------------------------------------------

Below is a data set with employee names in column A, their start date (or joining date) in column B, and their end date (resignation date) in column C.

![Dataset to convert days to months](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20687%20453'%3E%3C/svg%3E)

Using this data, I want to know how many months a person has been employed in the company.

This can be done easily using the [DATEDIF function](https://trumpexcel.com/excel-datedif-function/)
.

### Convert Days to Completed Months

Here is the formula that will do this:

\=DATEDIF(B2,C2,"M")

Enter this formula in cell D2 and then copy it for all the other cells.

![DATEDIF formula to convert days to month](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20685%20513'%3E%3C/svg%3E)

Note that this formula only gives me the total number of completed months between the two dates, and ignores any other additional days after the completed month.

The above DATEDIF formula takes three arguments:

*   **Start\_Date** – This is the start date that we have in cell B2
*   **End\_Date** – This is the end date that we have in cell C2
*   **Code** – This is a code that tells the function what calculation needs to be done for the given number of calculated days between the start date and the end date. Here I have used “M” which will give me the total number of completed months in between the two given dates.

### Convert Days to Completed Months and Days

If you want to know the total number of completed months as well as the days after the completed months, you can use the below formula:

\=DATEDIF(B2,C2,"M")&" M "&DATEDIF(B2,C2,"MD")&" D"

![Formula to convert days to month and days](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20538'%3E%3C/svg%3E)

The above formula gives you the result as a text string and uses the DATEDIF formula two times – first to calculate the total [number of months in between](https://trumpexcel.com/calculate-months-between-two-dates/)
 the given dates and then the total number of remaining dates after the months have been counted

Here are the two formulas I have used:

*   **DATEDIF(B2,C2,”M”)** – Here, I have used “M” as the third argument, which gives me the total number of completed months between the two dates
*   **DATEDIF(B2,C2,”MD”)** – Here, I have used “MD” as the third argument, which gives me the number of days left after the total number of completed months is removed

Note: DATEDIF has been kept for compatibility purposes with Lotus 123. Microsoft recommends using this function with caution, as it can give you [incorrect results in some scenarios](https://support.microsoft.com/en-us/office/datedif-function-25dba1a4-2812-480b-84dd-8b32a451b35c)
.

Also read: [Calculate Number of Weeks Between Two Dates](https://trumpexcel.com/weeks-between-two-dates-excel/)

Convert Days to Months Using Simple Division
--------------------------------------------

If you do not want to use the DATEDIF function for some reason, let me show you another way to do this.

In this method, we will be dividing the total number of days by an approximate number of month values.

Since there are 365 days in a year (assuming a non-leap year) and 12 months in a year, we can get an average number of days per month by dividing 365 by 12.

We can then use this value as the criteria to convert a given number of days into two months.

Below I have a data set where I have the start date in column B and end date in column C, and I want to calculate the total number of months in between the two dates.

![Dataset to convert days to months](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20687%20453'%3E%3C/svg%3E)

Here is the formula that will do this:

\=(C2-B2)/(365/12)

Enter this formula in cell D2 and then copy it for all the cells in the column.

![Formula to convert days to months INT Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20509'%3E%3C/svg%3E)

This gives us the month value with a decimal portion that denotes the remaining number of days.

For example, 4.8 tells us that there were four completed months and 0.8 portions of the remaining month in between the dates.

If you only want the number of months without the decimal portion, you can use the below formula:

\=INT((C2-B2)/(365/12))

One obvious drawback of this method is that it considers every month to be ~30.41 days long and ignores the fact that there could be 28, 29, 30, or 31 days in months.

If you want more accuracy, then you’re better off using the DATEDIF function method.

In this article, I showed you how to convert days into months in Excel using two simple formulas.

I hope you found this article helpful. If you know of any other method to do this or you have any feedback for me, please leave them in the comment section below.

**Other Excel articles you may also like:**

*   [How to Get the Number of Days in a Month in Excel?](https://trumpexcel.com/days-in-month-excel/)
    
*   [How to Add or Subtract Days to a Date in Excel](https://trumpexcel.com/add-days-to-date-in-excel/)
    
*   [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    
*   [How to Get Month Name from Date in Excel](https://trumpexcel.com/get-month-name-from-date-excel/)
    
*   [Check IF a Date is Between Two Given Dates in Excel](https://trumpexcel.com/check-if-date-is-between-two-dates/)
    
*   [Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [Convert Month Name to Number in Excel](https://trumpexcel.com/convert-month-name-to-number-excel/)
    
*   [Days Between Dates Calculator](https://trumpexcel.com/calculator/days-between-dates/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-days-to-months-excel/#respond)

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