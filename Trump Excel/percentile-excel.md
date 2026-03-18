# How to Calculate PERCENTILE in Excel (Easy Formula + Examples)

**Source:** https://trumpexcel.com/percentile-excel

---

[Skip to content](https://trumpexcel.com/percentile-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/percentile-excel/#below-title)

Percentile is a statistics metric is that is often used when working with data.

It gives you an idea of where a value lies in the dataset (i.e., its position/rank in the dataset).

In practical life, I have seen the percentile value being used in competitive exams, where on the given score, you get the percentile value. This tells you where you stand in comparison to all the other people who appeared for that exam.

In this tutorial, I will explain everything you need to know about the percentile function in Excel, and show you examples of how to **calculate the 90th percentile or 50th percentile in Excel**.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/percentile-excel/#)

What is Percentile? An Easy Explanation!
----------------------------------------

Percentile value tells you the relative position of a data point in the whole dataset.

For example, if I have the scores of 100 students and I tell you that the 90th percentile score is 84, it means that if anyone scores 84, then their score would be above 90% of the students.

Similarly, if the 50th percentile value for a dataset is 60, it means that anyone who got a score of 60 has about 50% of the people with better scores and about 50% of the people with a lesser score.

This is a preferred method as it’s more meaningful than just giving the score.

For example, if I tell you that your score is 90, it doesn’t tell you where you stand relative to the others. But if I tell you that your score’s percentile is 90th, you immediately know that you have done better than 90% of the people who took the exam.

Calculating the percentile value in Excel is very easy as it has some inbuilt functions to do this.

PERCENTILE Functions in Excel
-----------------------------

There are three variations of the percentile function available in Excel. If you’re using Excel 2010 or versions after that, you will have access to all these three functions.

*   **PERCENTILE** – this is old function that is now kept for backward compatibility purposes. You can use this, but it’s best to use the new ones (if you have those in your version of Excel). The result of this function is a value between 0 and 1
*   **PERCENTILE.INC** – this is the new formula (which works exactly like the PERCENTILE function). In most cases, this is the function you would need to use. The result of this function is a value between 0 and 1
*   **PERCENTILE.EXC** – this also works like the PERCENTILE.INC function with one difference – the result of this function will be a value between 0 and 1, but excludes K values between 0 to 1/(N+1) as well as N/(N+1) to 1 (where N is the size of the sample)

To put it simply, use PERCENTILE.INC in most cases (and if you are using Excel 2007 or prior versions, use PERCENTILE function)

Below is the syntax of the PERCENTILE.INC function in Excel:

 =PERCENTILE.INC(array,k)

Where:

1.  **array** is the range of cells where you have the values for which you want to find out the K-th percentile
2.  **k** is the value between 0 and 1, and gives you the k-th percentile value. For example, if you want to calculate the 90th percentile value, this would be 0.9 or 90%, and for the 50th percentile value, this would be 0.5 or 50%

The syntax remains the same for the PERCENTILE and PERCENTILE.EXC functions.

Also read: [Calculate Interquartile Range (IQR) in Excel](https://trumpexcel.com/interquartile-range-iqr-excel/)

Calculating 90th Percentile in Excel (or 50th Percentile)
---------------------------------------------------------

Suppose you have a dataset as shown below and you want to know the 90th percentile value for this dataset.

![Dataset for calculating Percentile](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20360%20335'%3E%3C/svg%3E)

Below is the formula that will give you the 90th Percentile:

\=PERCENTILE.INC(A2:A21,90%)

![Formula to calculate 90th Percentlle](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20522%20381'%3E%3C/svg%3E)

In the above formula, I have used 90% as the k value. You can also use 0.9 to get the 90th percentile.

The result of this formula tells me that 90% of the values in this dataset lies below 95.3

Also, note that you don’t need to have the data sorted for this formula to work. Sorting and giving you the final result is something PERCENTILE function automatically does in the backend.

Similarly. in case you want to calculate the 50th percentile, you can use the formula below:

\=PERCENTILE.INC(A2:A21,50%)

PERCENTILE.INC vs PERCENTILE.EXC – What’s the Difference?
---------------------------------------------------------

Now, if you’re wondering why there are two separate percentile functions in Excel, let me try and explain.

When you use PERCENTILE.INC function, it would calculate the result while including the first and last value in the dataset. And if you want to exclude the first and the last value from the calculation, you need to use the PERCENTILE.EXC function.

In most cases, you will be required to use the PERCENTILE.INC function only.

But since we are talking about the difference between the two functions, let me try and show you the difference with an example.

Suppose you have the dataset as shown below where I have calculated different percentile values (in column C) using both PERCENTILE.INC and PERCENTILE.EXC.

![Percentile INC vs EXC](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20656%20337'%3E%3C/svg%3E)

As you can see, apart from getting different results, the PERCENTILE.EXC function would return a #NUM! error when I try to calculate the percentile value for 0 or 100%

In fact, PERCENTILE.EXC would give you an error for any value between:

*   0 and 1/(N+1)
*   N/(N+1) and 1

where N is the total number of data points in the dataset (10 in this example)

So it would give the NUM error for any Kth values that lie between 0 and 1/11 or 10/11 and 1.

So it’s good to have the PERCENTILE.EXC function, but in most cases, you can just go ahead and use the PERCENTILE or the PERCENTILE.INC function.

I hope you found this tutorial useful!

**Other Excel tutorials you may also like:**

*   [Calculate Percentage Change in Excel (% Increase/Decrease Formula)](https://trumpexcel.com/percentage-change-excel/)
    
*   [How to Make a Bell Curve in Excel (Step-by-step Guide)](https://trumpexcel.com/bell-curve/)
    
*   [How to Calculate and Format Percentages in Excel](https://trumpexcel.com/calculate-percentages-excel/)
    
*   [How to Calculate Standard Deviation in Excel (Step-by-Step)](https://trumpexcel.com/standard-deviation/)
    
*   [How to Rank within Groups in Excel](https://trumpexcel.com/rank-within-groups-excel/)
    
*   [How to Get Descriptive Statistics in Excel?](https://trumpexcel.com/descriptive-statistics-excel/)
    
*   [Calculate MEDIAN IF in Excel](https://trumpexcel.com/median-if-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/percentile-excel/#respond)

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