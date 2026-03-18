# Count Between Two Numbers in Excel (COUNTIF / COUNTIFS)

**Source:** https://trumpexcel.com/count-between-two-numbers-excel

---

[Skip to content](https://trumpexcel.com/count-between-two-numbers-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/count-between-two-numbers-excel/#below-title)

Excel has multiple count-related functions that allow you to quickly analyze large data sets.

A common task for many people Is to count cells that contain a value in between two specific numbers.

For example, if you are analyzing sales data for different Sales Reps in your company, you may want to know the number of people whose sales are between $100K and $500K.

In this tutorial, I will show you a couple of different methods you can use to count between two numbers in Excel using formulas such as COUNTIF, COUNTIFS, and SUM.

**[Click here to download the example Excel file](https://www.dropbox.com/s/af89gsm0lk494ty/Count%20Between%20Two%20Numbers.xlsx?dl=1)
**

This Tutorial Covers:

[Toggle](https://trumpexcel.com/count-between-two-numbers-excel/#)

COUNTIFS Formula to Count Between Two Numbers
---------------------------------------------

The easiest way to count between two numbers is by using the [COUNTIFS function](https://trumpexcel.com/excel-countifs-function/)
. This function is available in Excel 2010 and higher versions.

Let me show you how it works.

Below I have a data set where I have student names in column A and their scores in column B, and I want to know the number of students who have scored more than 35 but less than 75 (i.e., between 35 and 75).

![Data set to count cells in between two numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20328%20386'%3E%3C/svg%3E)

Below is the COUNTIFS formula that will do this:

\=COUNTIFS(B2:B15,">35",B2:B15,"<75") 

![Countifs function to count cells in between two numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20629%20432'%3E%3C/svg%3E)

The syntax of the COUNTIFS function is _COUNTIFS(criteria\_range1, criteria1, \[criteria\_range2, criteria2\]…)_

In our formula, the COUNTIFS function takes four arguments:

*   _criteria\_range1_ – This is the range that has the numbers
*   _criteria1_ – This is the first criterion (“>35”), that the scores should be greater than 35
*   _criteria\_range2 –_ This is again the same range that has the numbers
*   _criteria_2 – This is the second criterion (“<75”), that the scores should be less than 75

COUNTIFS function gives us only that count that satisfies both pairs of conditions (i.e., numbers that are more than 35 and less than 75)

**Note**: Make sure that your criteria are always in double quotes (as in “<35”). Also, in this case, we excluded counting the cells that have the values 35 and 75. In case you want them to be counted, you can use “<=35” and “<=75” as the criteria.

In case you’re using an older version of Excel that does not have the COUNTIFS function, or you need to share your file with someone who’s working on an older version, you can use the next two methods I’ve covered in this article.

Also read: [Check IF a Date is Between Two Given Dates in Excel](https://trumpexcel.com/check-if-date-is-between-two-dates/)

COUNTIF Formula to Count Between Two Numbers
--------------------------------------------

Below I have the same data set where I have the students’ names in column A and the scores in column B, and I want to find out the total number of students who have scored between 35 and 75.

![Data set to count cells in between two numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20328%20386'%3E%3C/svg%3E)

Here is the [COUNTIF formula](https://trumpexcel.com/excel-countif-function/)
 that will give us the result:

\=COUNTIF(B2:B15,">35")-COUNTIF(B2:B15,">75")

![Countif function to count cells in between 2 numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20687%20436'%3E%3C/svg%3E)

The above formula uses two COUNTIF functions:

*   The first COUNTIF function gives us the count of all the cells where the score is more than 35. These would also include cells where the score is more than 75
*   The second COUNTIF function gives us the count of only those cells where the value is more than 75

Subtracting the value we get from the second COUNTIF from the value that we get from the first COUNTIF would give us the right result.

**[Click here to download the example Excel file](https://www.dropbox.com/s/af89gsm0lk494ty/Count%20Between%20Two%20Numbers.xlsx?dl=1)
**

Also read: [SUM Values Between Two Dates (using SUMIFS formula)](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)

SUM Formula to Count Between Two Numbers
----------------------------------------

While in most cases, you’re better off using the COUNTIFS function or the COUNTIF function, let me show you another smart way to use a simple SUM formula to count between two numbers.

The good thing about this method is that it is going to work in every version of Excel.

Below I have the same data set where I want to calculate the number of cells with scores between 35 and 75.

![Data set to count cells in between two numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20328%20386'%3E%3C/svg%3E)

Here is the SUM formula that will do this for us:

\=SUM((B2:B15>35)-(B2:B15>75))

![SUM formula to count cells between two numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20564%20434'%3E%3C/svg%3E)

The above formula uses (B2:B15>35) to get an array of TRUE and FALSE where we would get a TRUE in case the score in the cell is more than 35, and FALSE in case the score is less than or equal to 35.

In the back end, Excel considers TRUE as 1 and False as 0, so when we compute (B2:B15>35)-(B2:B15>75), it gives us an array of TRUEs and FALSEs (or 1s and 0s), where we would get 1 only if the cell has a value that is more than 35 and less than 75.

This array is then wrapped up within the [SUM function](https://trumpexcel.com/excel-sum-function/)
 that simply counts the total number of 1s and gives us the result.

**Note**: In case you’re using an older version of Excel that does not have dynamic arrays when you have entered the formula, you should use Control + Shift + Enter instead of Enter (i.e., hold the Control and the Shift key and then press the Enter key)

So these are three simple formulas that you can use to count between two numbers in Excel.

The easiest way would be to use the COUNTIFS function. But in case you do not have it or you don’t want to use it because of compatibility reasons, you can also use the COUNTIF or the SUM function method.

I hope you found this Excel tutorial useful.

**Other Excel articles you may also like:**

*   [Calculate the Number of Months Between Two Dates in Excel](https://trumpexcel.com/calculate-months-between-two-dates/)
    
*   [Count Unique Values in Excel Using COUNTIF Function](https://trumpexcel.com/count-unique-values-in-excel-countif/)
    
*   [Count Cells Less than a Value in Excel (COUNTIF Less Than)](https://trumpexcel.com/countif-less-than/)
    
*   [How to Use Multiple Criteria in Excel COUNTIF and COUNTIFS Function](https://trumpexcel.com/multiple-criteria-in-excel-countif/)
    
*   [How to Count Cells that Contain Text Strings](https://trumpexcel.com/count-cells-that-contain-text/)
    
*   [How to Count Filtered Rows in Excel?](https://trumpexcel.com/count-filtered-rows-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/count-between-two-numbers-excel/#respond)

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