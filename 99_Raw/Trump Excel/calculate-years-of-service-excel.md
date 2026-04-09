# How to Calculate Years of Service in Excel (Easy Formulas)

**Source:** https://trumpexcel.com/calculate-years-of-service-excel

---

[Skip to content](https://trumpexcel.com/calculate-years-of-service-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/calculate-years-of-service-excel/#below-title)

Excel can be quite useful when you’re working dates. It has some powerful built-in formulas that allow you to do calculations based on dates.

One common scenario where you have to perform calculations with dates would be to find out how many years or months or dates have elapsed between two given dates.

This could especially be useful if you want to **calculate years of service of employees** in your company (where you have their joining date and the end date).

In this tutorial, I will show you some formula techniques that you can use to calculate the years of service in years (or years and months and days).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/calculate-years-of-service-excel/#)

Calculating Years of Service Using the YEARFRAC Formula
-------------------------------------------------------

If you only want to get the total number of years of service between two dates, you can use the YEARFRAC function.

Below I have a data set where I have the start date and end date for a set of employees, and I want to calculate their years of service in column D.

![Dataset to calculate years of service](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20670%20247'%3E%3C/svg%3E)

You can do that using the below formula:

\=INT(YEARFRAC(B2,C2,1))

![INT and YEARFRAC Formula to get Years of service](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20670%20296'%3E%3C/svg%3E)

The YEARFRAC function gives you the total number of years between two dates (where full years are shown as integers and incomplete years are shown as decimals).

The [INT function](https://trumpexcel.com/excel-int-function/)
 then extracts the integer part from the result of YERAFRAC, which is the total number of years of service between the two given dates.

Also read: [How to Get the Number of Days in a Month in Excel?](https://trumpexcel.com/days-in-month-excel/)

Calculating Years of Service Using the DATEDIF Formula
------------------------------------------------------

If you need to calculate the use of service where you may want to get the number of years as well as the number of months and/or days, then you are better off using the [DATEDIF formula](https://trumpexcel.com/excel-datedif-function/)
 (pronounced as DATE DIF formula)

It’s one of the undocumented functions in Excel, which means that you would not find any help on this function from Microsoft or see this as a part of the IntelliSense when you type it in a cell in Excel.

But when it comes to calculating the total years of service between two dates, this is the best function to use.

### Calculating Only the Years of Service

Below I have a data set where I have the start date and end date for a set of employees, and I want to calculate the total number of years of service for each employee.

![Dataset to calculate years of service](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20670%20247'%3E%3C/svg%3E)

Below is the formula that will do this:

 =DATEDIF(B2,C2,"y")

![DATEDIF formula to get years of service](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20670%20293'%3E%3C/svg%3E)

The DATEDIF formula takes the start and the end date as the first two arguments and gives the total years between the dates (as I have specified Y as the third argument).

### Calculating Service Duration in Years and Months

Below I again have the same data set and I want to calculate the duration of service of each employee in years and months.

![Dataset for year and month](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20672%20248'%3E%3C/svg%3E)

Below is the formula that will do this:

\=DATEDIF(B2,C2,"y")&" Years "&DATEDIF(B2,C2,"ym")&" Months"

![DATEDIF formula to get years and months of service](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20274'%3E%3C/svg%3E)

The above formula contains two DATEDIF functions

*   The first one is used to calculate the total number of completed years between the two dates
*   The second one is used to calculate the total number of months between the two dates, but does not include those months that have completed an year. For example, if the difference between two dates is 14 months, this would only return 2, as the first 12 months completed to become a year.

These DATEDIF functions are combined with the text “Years” and “Months”, so that the result is more meaningful and the user would know how many years and months of service has been completed.

### Calculating Service Duration in Years, Months, and Days

And if you want to get the total service duration in Years, Months as Days, you can use the below formula:

\=DATEDIF(B2,C2,"y")&" Years "&DATEDIF(B2,C2,"ym")&" Months "&DATEDIF(B2,C2,"md")&" Days"

![DATEDIF formula to get service in years months and days](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20275'%3E%3C/svg%3E)

The above formula uses three DATEDIF functions to find out the numbers of years months and days in the total service and then combine these using the & operator.

I have also added the words Years, Months, and Days to make the result easy to comprehend.

### Calculating Service Duration Till Today

If you want to [calculate the total time elapsed](https://trumpexcel.com/calculate-time-in-excel/)
 between a given date and the current date, you can use the same DATEDIF formula, and replace the end date with the TODAY formula.

[TODAY() formula](https://trumpexcel.com/excel-today-function/)
 gives you the current date based on your computer settings. It’s a [volatile formula](https://trumpexcel.com/excel-volatile-formulas/)
, which means that the next time you open the workbook or make a change in the workbook, this formula would be refreshed, and if the date has changed, then the new date would be used.

Below I have a data set where I want to calculate the total years of service for each employee from their joining date till today.

![Dataset to calculate years of service till today](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20523%20248'%3E%3C/svg%3E)

Here’s the formula that will do that:

\=DATEDIF(B2,TODAY(),"y")&" Years "&DATEDIF(B2,TODAY(),"ym")&" Months "&DATEDIF(B2,TODAY(),"md")&" Days"

![DATEDIF formula to get service duration till today](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20761%20317'%3E%3C/svg%3E)

**Note**: You can also use this formula to [calculate the age of a person](https://trumpexcel.com/calculate-age-in-excel/)
 when you have their date of birth

Also read: [Calculate Fiscal Year from Date in Excel](https://trumpexcel.com/fiscal-year-excel/)

Calculate the Date After a Specific Duration of Service
-------------------------------------------------------

Another scenario involving total tenure of service could be when you want the date after a specific number of years in service.

For example, let’s say you’re the HR in a company that offers loyalty bonuses to employees who complete 10 years in service.

You have a list of employees and their joining data shown below, and you need to know on what date their loyalty bonus would be due.

![Date of Bonus dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20224'%3E%3C/svg%3E)

Below is the formula that will give you this date:

\=EDATE(B2,10\*12)

![EDATE formula to calculate date after specific years](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20265'%3E%3C/svg%3E)

The EDATE formula is meant to return the date after or before the specified number of months, but we have hacked it to give us the date after 10 years.

To do this, instead of specifying the number of months as the second argument, we have specified 10\*12, which is the total number of months in 10 years.

So these are some of the ways you can use to calculate the years of service in Excel and get the result in years, years, and months, or years months and days.

I also covered how to get the date after a specific number of years using the EDATE formula.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [Get Day Name from Date in Excel (Easy Formulas)](https://trumpexcel.com/get-day-name-from-date-excel/)
    
*   [How to SUM values between two dates (using SUMIFS formula)](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)
    
*   [Calculate the Number of Months Between Two Dates in Excel](https://trumpexcel.com/calculate-months-between-two-dates/)
    
*   [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    
*   [How to Add Months to Date in Excel (Easy Formula)](https://trumpexcel.com/add-months-to-date-excel/)
    
*   [Check IF a Date is Between Two Given Dates in Excel (Easy Formula)](https://trumpexcel.com/check-if-date-is-between-two-dates/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Calculate Years of Service in Excel (Easy Formulas)”
-------------------------------------------------------------------------

1.  In the examples you have, there are examples with joining dates. But I have birth date, retirement date. In this situation, how can the left of service be taken out?
    
    [Reply](https://trumpexcel.com/calculate-years-of-service-excel/#comment-41560)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/calculate-years-of-service-excel/#respond)

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