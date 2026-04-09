# How to Find Range in Excel (Easy Formulas)

**Source:** https://trumpexcel.com/find-range-in-excel

---

[Skip to content](https://trumpexcel.com/find-range-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/find-range-in-excel/#below-title)

Normally, when I use the word range in my tutorials about Excel, it’s a reference to a cell or a collection of cells in the worksheet.

But this tutorial is not about that range.

A ‘Range’ is also a mathematical term that refers to the range in a data set (i.e., the range between the minimum and the maximum value in a given dataset)

In this tutorial, I will show you really simple ways to **calculate the range in Exce**l.

What is a Range?
----------------

In a given data set, the range of that data set would be the spread of values in that data set.

To give you a simple example, if you have a data set of student scores where the minimum score is 15 and the maximum score is 98, then the spread of this data set (also called the range of this data set) would be 73

Range = 98 – 15

‘Range’ is nothing but the difference between the maximum and the minimum value of that data set.

How to Calculate Range in Excel?
--------------------------------

If you have a list of [sorted values](https://trumpexcel.com/sort-excel/)
, you just have to subtract the first value from the last value (assuming that the sorting is in the ascending order).

But in most cases, you would have a random data set where it’s not already sorted.

Finding the range in such a data set is quite straightforward as well.

Excel has the functions to find out the maximum and the minimum value from a range (the [MAX](https://trumpexcel.com/excel-max-function/)
 and the [MIN function](https://trumpexcel.com/excel-min-function/)
).

Suppose you have a data set as shown below, and you want to calculate the range for the data in column B.

![Dataset to find Range in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20411'%3E%3C/svg%3E)

Below is the formula to calculate the range for this data set:

\=MAX(B2:B11)-MIN(B2:B11)

![Formula to calculate range in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20552%20741'%3E%3C/svg%3E)

The above formula finds the maximum and the minimum value and gives us the difference.

Quite straightforward… isn’t it?

Also read: [Calculate Interquartile Range (IQR) in Excel](https://trumpexcel.com/interquartile-range-iqr-excel/)

Calculate Conditional Range in Excel
------------------------------------

In most practical cases, finding the range would not be as simple as just subtracting the minimum value from the maximum value

In real-life scenarios, you might also need to account for some conditions or [outliers](https://trumpexcel.com/find-outliers-excel/)
.

For example, you may have a data set where all the values are below 100, but there is one value that is above 500.

If you calculate arrange for this data set, it would lead to you making misleading interpretations of the data.

Thankfully, Excel has many conditional formulas that can help you sort out some of the anomalies.

Below I have a data set where I need to find the range for the sales values in column B.

![Dataset to find Range in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20411'%3E%3C/svg%3E)

If you look closely at this data, you would notice that there are two stores where the values are quite low (Store 1 and Store 3).

This could be because these are new stores or there were some external factors that impacted the sales for these specific stores.

While calculating the range for this data set, it might make sense to exclude these newer stores and only consider stores where there are substantial sales.

In this example, let’s say I want to ignore all those stores where the sales value is less than 20,000.

Below is the formula that would find the range with the condition:

\=MAX(B2:B11)-MINIFS(B2:B11,B2:B11,">20000")

![Calculating conditional range in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20706%20738'%3E%3C/svg%3E)

In the above formula, instead of using the MIN function, I have used the MINIFS function (it’s a new function in Excel 2019 and Microsoft 365).

This function finds the minimum value if the criteria mentioned in it are met. In the above formula, I specified the criteria to be any value that is more than 20,000.

So, the MINIFS function goes through the entire data set, but only considers those values that are more than 20,000 while calculating the minimum value.

This makes sure that values lower than 20,000 are ignored and the minimum value is always more than 20,000 (hence ignoring the outliers).

Note that the MINIFS is a new function in Excel is **available only in Excel 2019 and Microsoft 365 subscription.** If you’re using prior versions, you would not have this function (and can use the formula covered later in this tutorial)

If you don’t have the MINIF function in your Excel, use the below formula that uses a combination of [IF function](https://trumpexcel.com/excel-if-function/)
 and MIN function to do the same:

\=MAX(B2:B11)-MIN(IF(B2:B11>20000,B2:B11))

Just like I have used the conditional MINIFS function, you can also use the MAXIFS function if you want to avoid data points that are outliers in the other direction (i.e., a couple of large data points that can skew the data)

So, this is how you can quickly **find the range in Excel** using a couple of simple formulas.

I hope you found this tutorial useful.

**Other Excel tutorials you may like:**

*   [How to Calculate Standard Deviation in Excel](https://trumpexcel.com/standard-deviation/)
    
*   [How to Calculate Square Root in Excel](https://trumpexcel.com/calculate-square-root-in-excel/)
    
*   [How to Calculate and Format Percentages in Excel](https://trumpexcel.com/calculate-percentages-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/find-range-in-excel/#respond)

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