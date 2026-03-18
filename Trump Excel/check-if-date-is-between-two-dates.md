# Check IF a Date is Between Two Given Dates in Excel (Easy Formula)

**Source:** https://trumpexcel.com/check-if-date-is-between-two-dates

---

[Skip to content](https://trumpexcel.com/check-if-date-is-between-two-dates/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/check-if-date-is-between-two-dates/#below-title)

Data analysis in Excel often involves working with dates.

A common thing many Excel users need to check when working with dates is whether a date is between two given dates.

A simple use case of this could be when you need to check whether the date of submission of a report was within the given dates or not. Based on this, you can highlight what reports were submitted after the deadline.

In this tutorial, I will show you how to **check if the date is between two given dates or not**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/check-if-date-is-between-two-dates/#)

Using Nested IF Formula
-----------------------

One of the easiest ways to check whether a date is in between two given dates is by using a simple [if formula](https://trumpexcel.com/excel-if-function/)
.

And since we need to check for two conditions, we would need to use two if formulas.

And when you use an IF formula within another IF formula, that is called the nested IF construct.

Below I have a data set where I have the project start date and project end date in column A and column B respectively. And then I have the project submission date in column C.

![Dataset to check if date lies between two dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20613%20307'%3E%3C/svg%3E)

Now I want to check whether the project submission date was between the project start and project end date or not.

This can easily be done using the below nested IF formula:

\=IF(C2>=A2,IF(C2<=B2,"In Range","Out of Range"),"Out of Range")

![Formula to check date in between two dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20330'%3E%3C/svg%3E)

The above formula would return ‘In Range’ if the date lies in between the two given dates, and it would return ‘Out of Range’ in case the date is either before the project started or after the project end date.

Now let me quickly explain how this formula works.

I first used and if formula to check whether the date is after the project start date or not.

Based on these criteria, I need to specify what should the formula do in case this condition is true, and what should the formula do in case the condition is not true.

But since I have two conditions to check, immediately after I checked the first condition, I use the second IF function to check for the other condition (which is whether the date is before the project end date or not).

Since the IF function takes 3 arguments (the condition, value when the condition is True, and value in the condition is False), for the second IF function, I specify ‘In Range’ as the second argument, as it has satisfied both the conditions, and I specify out of range as the third argument, because it satisfies the first if condition, but it fails the second if condition.

And then finally, I specify ‘Out of Range’ as the second argument for the first IF function (which means that the condition in the first IF function failed, and hence it did not go to the second if function and instead returned the second argument of the first IF function).

Since I had only two conditions to check, I have used two if functions where the second function is nested within the first one. In case you have more than two conditions to check you can further nest these if functions (although it tends to get a bit complicated after a few)

Also read: [Avoid Nested IF Function in Excel…VLOOKUP to Rescue](https://trumpexcel.com/avoid-nested-if-function-vlookup/)

Using IF + AND Formula
----------------------

While many Excel users are quite comfortable using the IF formula, when you have multiple conditions to check, I prefer using the combination of IF and AND formula instead.

Within the [AND formula](https://trumpexcel.com/excel-and-function/)
, you can check for multiple conditions, and can specify what result you should get in case all the conditions are true, and the result you should get in case any of these conditions are FALSE.

Let’s again take the same data set where I have the project started and project end date in column A and column B, and I have the project submission date in column C.

![Dataset to check if date lies between two dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20613%20307'%3E%3C/svg%3E)

Below is the formula I can use to check whether the submission date lies between the project start date and project end date or not:

\=IF(AND(C2>=A2,C2<=B2),"In Range","Out of Range")

![IF and AND formula to check in between two dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20358'%3E%3C/svg%3E)

The above formula checks for both the conditions and it would return ‘In Range’ in case the submission date is in between the start and the end date, and it would return ‘Out of Range’ in case the submission date is before the project started or after the project end date.

Note that I have still used an IF function in the above formula, however, I didn’t have the need to use two if functions.

Since I had to check for both the conditions, I did that using the AND function instead.

The AND function would return TRUE if both the conditions are true, and it would return FALSE if any or both the conditions are false.

And since I needed a more descriptive output instead of a simple TRUE or FALSE, I have used an IF function where it would give me ‘In Range’ in case the result is TRUE and ‘Out of Range’ in case the result is FALSE.

Also read: [Count Between Two Numbers in Excel (COUNTIF / COUNTIFS)](https://trumpexcel.com/count-between-two-numbers-excel/)

Check If the Date Occurs on Weekend
-----------------------------------

A common use case when working with dates in project management is to identify whether a date occurs on a weekend or not.

If you’re checking this manually, you would check whether a date is a Saturday or Sunday.

But when working with dates in Excel, you can use the [WEEKDAY function](https://trumpexcel.com/excel-weekday-function/)
 that can easily do this for you.

Below I have a data set where I have some dates in column A, and I want to check whether these dates occur on a weekend or not.

![Check if Date is weekend](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20355%20342'%3E%3C/svg%3E)

For the purpose of this tutorial, I would consider Saturday and Sunday as the weekend days.

Below is the formula that will do this for you:

\=WEEKDAY(A2,2)>5

![WEEKDAY formula to check the date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20430%20386'%3E%3C/svg%3E)

If the date occurs on a Saturday or Sunday, it will give you a TRUE, else it will give a FALSE.

The above WEEKDAY formula checks the [serial number of the date](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
, and returns a number that corresponds to the weekday number for that date. So if it’s a Monday, it would return 1, if it’s a Tuesday it would return 2, and so on.

Since the condition that I’m checking is whether the weekday result is more than 5, it would return TRUE if the date is on a weekend, and it would return FALSE if it’s on a weekday.

If you want the result to be more meaningful, you can use the below if formula, which will return ‘Weekday’ in case the date occurs on a weekday and ‘Weekend’ in case the date occurs on a weekend.

\=IF(WEEKDAY(A2,2)>5,"Weekend","Weekday")

Also read: [Calculating Time In Excel](https://trumpexcel.com/calculate-time-in-excel/)

Issues When Checking Whether a Date is in Between two dates
-----------------------------------------------------------

So far, I’ve shown you a couple of scenarios where you can check whether a date lies between two given dates.

In all the formulas, the underlying principle is to compare the value of the given date with the start and the end date. If the value of the given date, is in between the start and the end date, then it occurs in between these two dates, else it does not.

However, in some cases, you may see some unexpected results.

In this section, I cover some common pitfalls that you need to be aware of when [comparing dates in Excel](https://trumpexcel.com/compare-dates-in-excel/)
:

### Dates Need to Be in the Right Format

Dates and time values are stored as numbers in the back-end in Excel. So when you compare two dates, you’re essentially comparing two numbers.

You may think that the date looks nothing like a number (for example 01 January 2023), but remember that dates are formatted to show up differently in the cell in Excel, while in the back-end these are still numbers.

For example, a cell may show 01 January 2023, but in the backend, the value of this cell would be 44927 (which indicates the total number of days that have elapsed after 01 Jan 1900).

Now, if your dates are in the right format, all is well.

But there is also a possibility that your date is in a format that Excel does not recognize as a date, which means that instead of a number in the back end, it ends up being considered a [text string](https://trumpexcel.com/count-cells-that-contain-text/)
.

For example, Jan 01, 2023, is not a valid date format in Excel.

So if you have this in a cell in excel, it would be considered a text string, and using this to compare it with other dates can give you incorrect results.

_Bottom line – When comparing dates in Excel, make sure that the dates are in the right format_

Also read: [How to Change Date Format In Excel?](https://trumpexcel.com/change-date-format-excel/)

### Dates May have a Time Part that’s Hidden

Just like dates, time values are also stored as numbers in the backend in Excel.

While a whole number would indicate a full day, the decimal part would indicate the portion of the day or the time value for that day.

For example, if you have 01-01-2023 18:00:00 in a cell in Excel, in the backend it would be 44927.75, where 44927 means 01-01-2023 and 0.75 means 18:00:00

Now, here’s the problem that you can encounter when checking whether a date lies in between two given dates.

You may clearly see that the date is in between the two given dates, but Excel may give you a different result.

This can happen because most of the time when people work with dates and times, the time portion is hidden so that you only see the date but you do not see the time value.

Below I have a simple example where I have the same date in cells A1 and B1, but when I compare these two cells, it tells me these are not the same.

![Date look same but are different](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20621%20147'%3E%3C/svg%3E)

While you can clearly see that these dates are exactly the same, what you do not see is that there is a time value in cell A1 that is hidden so you do not see it. But when excel compares these two cells, it considers these as different (which it rightly should).

While this is not such a common scenario, if this happens, it can sometimes stump even advanced Excel users.

In this tutorial, I showed you a couple of simple formulas that you can use to check whether a date is between two given dates or not.

I’ve also mentioned some of the pitfalls you should be aware of when comparing dates and Excel.

I hope you found this Excel tutorial useful.

**Other Excel Tutorials you may also like:**

*   [Calculate the Number of Months Between Two Dates in Excel](https://trumpexcel.com/calculate-months-between-two-dates/)
    
*   [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    
*   [How to Add or Subtract Days to a Date in Excel](https://trumpexcel.com/add-days-to-date-in-excel/)
    
*   [How to Stop Excel from Changing Numbers to Dates Automatically](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/)
    
*   [How to Add Months to Date in Excel](https://trumpexcel.com/add-months-to-date-excel/)
    
*   [How to Get the Number of Days in a Month in Excel?](https://trumpexcel.com/days-in-month-excel/)
    
*   [Get Day Name from Date in Excel](https://trumpexcel.com/get-day-name-from-date-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/check-if-date-is-between-two-dates/#respond)

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