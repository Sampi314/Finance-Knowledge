# How to SUM Values Between Two Dates (using SUMIFS formula)

**Source:** https://trumpexcel.com/sum-between-two-dates-sumifs-excel

---

[Skip to content](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/#below-title)

When you’re working with datasets that have dates, you would often find yourself trying to do calculations based on the dates.

For example, if you have the sales data for a month, you may want to know the total sales that have happened between two given dates or the total sales made on weekends vs weekdays.

One of the ways to quickly get these answers is by using the [SUMIFS function](https://trumpexcel.com/excel-sumifs-function/)
.

SUMIFS (as the name suggests), allows you to sum a range based on criteria. Within SUMIFs, you can specify multiple conditions and it will sum only those cells/values that meet all the conditions.

In this tutorial, I will show you how to **sum values between two dates using the SUMIFS function**.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/#)

SUM all values between two dates
--------------------------------

Suppose you have a dataset as shown below and you want to know the sales that have come in during 1-Jan-2020 and 31-Jan-2020 (I am using the DD-MM-YYYY format for the date here)

![Data where where you need to sum values between two dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20354%20436'%3E%3C/svg%3E)

Below is the formula that will give you the sum of sales between these two dates:

\=SUMIFS(C2:C15,A2:A15,">=1-1-2020",$A$2:$A$15,"<=31-01-2020")

![SUMIFs formula to get sum of values between two dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20631%20579'%3E%3C/svg%3E)

The above SUMIF function uses five arguments (this can change based on the number of conditions you have):

*   The first argument (C2:C15) is the range that has the values that we want to add
*   The second and third argument is for the first condition, which is that the date should be more than or equal to 01-01-2020. For each condition, you need to specify the criteria range and the criteria
*   The fourth and fifth arguments are for the second condition – criteria and the criteria range.

In the above formula, I have hard coded the dates. You can also have the dates in a cell and use the cell reference instead. Also, when your condition involves using an operator (such as = or <>), you need to put the operator in the double quotes.

**Note**: In the formula, you can use any valid date format in the formula, For example, in the cells, I have used the date as 01-01-2020, but in the formula, I can use any format that still refers to this date. For example, I can use 01 Jan, 2020 or 01 January 2020 or 1-Jan-2020. As long as the date format is valid, Excel will be able to use it to calculate the sum between the two given dates.

For example, if you have the start date and end date in cells (as shown below), you can use the following formula to get the sum of sales in the given date range.

\=SUMIFS(C2:C15,A2:A15,">="&F1,$A$2:$A$15,"<="&F2)

![Formula to sum between dates using cell references](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20751%20492'%3E%3C/svg%3E)

Remember that the operator needs to be in double quotes, and the [cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 needs to be out of double quotes.

Also read: [Calculate Days Between Two Dates Excel](https://trumpexcel.com/number-of-days-between-two-dates/)

SUM all values between two dates for a specific product
-------------------------------------------------------

Since the SUMIFS function allows you to use [multiple conditions](https://trumpexcel.com/excel-ifs-function/)
, you can also add more criteria in the same formula.

For example, suppose you have the same dataset (as shown below), but this time, you want to know the total sales of Printers that happened between the two given dates (01 Jan and 31 Jan).

![Data where where you need to sum values between two dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20354%20436'%3E%3C/svg%3E)

You can do that by adding another condition to the formula where apart from checking for the date, it also checks whether the product is Printer or not. It will then give you the result that matches all the given conditions

Below is the formula that will do this:

\=SUMIFS(C2:C15,A2:A15,">=1-1-2020",$A$2:$A$15,"<=31-01-2020",$B$2:$B$15,"Printer")

![Sum values between dates for a specific product](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20705%20585'%3E%3C/svg%3E)

The above formula checks for the dates as well as whether the product is a Printer or not. It would only sum a value when all three conditions are met.

Similarly, you can also get the sum of values between dates where you want to exclude a specific product.

For example, if you want to sum values between 1 and 31 Jan for all the product except the Scanner, then you can use the below formula:

 =SUMIFS(C2:C15,A2:A15,">=1-1-2020",$A$2:$A$15,"<=31-01-2020",$B$2:$B$15,"<>Scanner")

![Sum values between dates excluding a specific product](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20735%20588'%3E%3C/svg%3E)

In the above formula, I have used the not-equal-to-operator (<>) to exclude getting the values for Scanner in the result.

And just to reiterate, I have hard-coded the data values in the formula, but if you have these dates in a cell, you can refer to that cell in the formula.

These are some examples where you can sum values between two dates, and you can tweak the formula to add more conditions if you want.

Hope you found this tutorial useful.

**You may also like the following Excel tutorials:**

*   [How to Sum a Column in Excel](https://trumpexcel.com/sum-column-excel/)
    
*   [How to Sum Colored Cells in Excel (Formula & VBA)](https://trumpexcel.com/sum-by-color-excel/)
    
*   [Count Between Two Numbers in Excel](https://trumpexcel.com/count-between-two-numbers-excel/)
    
*   [How to Sum Positive or Negative Numbers in Excel](https://trumpexcel.com/sum-positive-numbers-excel/)
    
*   [How to SUM values between two dates (using SUMIFS formula)](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)
    
*   [Count Unique Values in Excel Using COUNTIF Function](https://trumpexcel.com/count-unique-values-in-excel-countif/)
    
*   [How to Use Multiple Criteria in Excel COUNTIF and COUNTIFS Function](https://trumpexcel.com/multiple-criteria-in-excel-countif/)
    
*   [How to Add or Subtract Days to a Date in Excel](https://trumpexcel.com/add-days-to-date-in-excel/)
    
*   [Check IF a Date is Between Two Given Dates in Excel](https://trumpexcel.com/check-if-date-is-between-two-dates/)
    
*   [How to Add Week to Date in Excel?](https://trumpexcel.com/add-week-to-date-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/#respond)

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