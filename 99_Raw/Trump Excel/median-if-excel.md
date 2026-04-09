# Calculate MEDIAN IF in Excel

**Source:** https://trumpexcel.com/median-if-excel

---

[Skip to content](https://trumpexcel.com/median-if-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/median-if-excel/#below-title)

Excel has an in-built MEDIAN function, but there is no MEDIANIF function.

But that’s not an issue.

In this article, I will show you how you can create your own MEDIAN IF function by combining the MEDIAN and the IF function. I will also show you how to do the same using PERCENT.INC function.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/median-if-excel/#)

MEDIAN IF Function
------------------

MEDIAN function in Excel allows us to find the median value in a dataset.

With the Median IF function, the aim is to find the median value of only those values that satisfy a given criteria.

For example, you might want to find the median salary of employees in a particular department or the median price of products in a specific category. The “IF” part allows you to set these conditions, while the “median” calculation provides the middle value of the resulting subset.

Let’s see how to do this in Excel.

### Using MEDIAN and IF Function

The most straightforward approach to calculating a conditional median in Excel is to combine the MEDIAN and IF functions.

Below, I have a data set where I have the employee name in column A, their department in column B, and the salaries in column C.

![Dataset to calculate Median IF](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20434%20346'%3E%3C/svg%3E)

Now I want to find out the median salary for only those employees who work in the sales department.

I can do this using the below formula:

\=MEDIAN(IF(B2:B11="Sales",C2:C11))

![MEDIAN and IF formula for Median if](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20641%20459'%3E%3C/svg%3E)

The above formula uses the [IF function](https://trumpexcel.com/excel-if-function/)
 to check the department and only gives us the salary value for those people who work in the Sales department.

Important Note: If you’re using an [older version of Excel](https://trumpexcel.com/excel-version/)
 that does not have dynamic arrays, you need to enter it by pressing Ctrl+Shift+Enter instead of just Enter. This tells Excel to treat the formula as an array formula. In newer versions of Excel (365 and later), this step is often unnecessary, as Excel can recognize and handle array formulas automatically.

If you want to check for multiple conditions, you do that within the IF function itself.

For example, if I want to know the median salary in the Sales department, but only for those people whose salary is more than 200K, I can use the below formula:

 =MEDIAN(IF((B2:B11="Sales")\*(C2:C11>200000),C2:C11))

_Note: In case there are errors in your data set, you’ll have to use the [IFERROR function](https://trumpexcel.com/excel-iferror-function/)
 to handle it_

Also read: [Calculating Weighted Average in Excel](https://trumpexcel.com/weighted-average-in-excel/)

### Using PERCENT.INC and IF Function

Another workaround to create a MEDIAN IF function in Excel is by using the PERCENTILE.INC function.

Below, I have a data set with the employee name in column A, their department in column B, and their salaries in column C.

![Dataset to calculate Median IF](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20434%20346'%3E%3C/svg%3E)

Now I want to find out the median salary for only those employees who work in the sales department.

Below is the formula that would give me the median value while satisfying the condition:

\=PERCENTILE.INC(IF(B2:B11="Sales",C2:C11),0.5)

![PERCENTILE and IF function to create Median if function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20754%20458'%3E%3C/svg%3E)

In the above PERCENTILE.INC formula, I have used 0.5 as the second argument, which gives me the 50% [percentile value](https://trumpexcel.com/percentile-excel/)
 (which is also the median value).

The advantage of this method is that you can use the same formula with a minor tweak to get the 30 percentile value or 75 percentile value. Just change the value from 0.5 to whatever percentile value you want.

In this article, I showed you how to create a MEDIANIF function using a combination of existing functions in Excel. You can do this by using a combination of MEDIAN and IF functions, and if you need more control, then you can try using PERCENT.INC with IF function.

I hope you found this article helpful.

If you have any questions or suggestions for me, please let me know in the comments section.

**Other Excel articles you may also like:**

*   [Calculate Interquartile Range (IQR) in Excel](https://trumpexcel.com/interquartile-range-iqr-excel/)
    
*   [Calculate Average Annual Growth Rate (AAGR) in Excel](https://trumpexcel.com/calculate-average-annual-growth-rate-excel/)
    
*   [Calculate Compound Annual Growth Rate (CAGR) in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    
*   [Calculating Moving Average in Excel \[Simple, Weighted, & Exponential\]](https://trumpexcel.com/moving-average-excel/)
    
*   [Count Unique Values in Excel Using COUNTIF Function](https://trumpexcel.com/count-unique-values-in-excel-countif/)
    
*   [Calculate Running Total in Excel (Cumulative Sum)](https://trumpexcel.com/running-total-excel/)
    
*   [Calculate P-value in Excel](https://trumpexcel.com/p-value-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/median-if-excel/#respond)

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