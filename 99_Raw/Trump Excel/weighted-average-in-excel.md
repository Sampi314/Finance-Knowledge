# Calculating Weighted Average in Excel (Using Formulas)

**Source:** https://trumpexcel.com/weighted-average-in-excel

---

[Skip to content](https://trumpexcel.com/weighted-average-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/weighted-average-in-excel/#below-title)

When we calculate a simple average of a given set of values, the assumption is that all the values carry an equal weight or importance.

For example, if you appear for exams and all the exams carry a similar weight, then the average of your total marks would also be the weighted average of your scores.

However, in real life, this is hardly the case.

Some tasks are always more important than the others. Some exams are more important than the others.

And that’s where **Weighted Average** comes into the picture.

Here is the textbook definition of Weighted Average:

![Definition of Weighted Average](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20568%20145'%3E%3C/svg%3E)

Now let’s see how to calculate the Weighted Average in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/weighted-average-in-excel/#)

Calculating Weighted Average in Excel
-------------------------------------

In this tutorial, you’ll learn how to calculate the weighted average in Excel:

*   Using the SUMPRODUCT function.
*   Using the SUM function.

So let’s get started.

### Calculating Weighted Average in Excel – SUMPRODUCT Function

There could be various scenarios where you need to calculate the weighted average. Below are three different situations where you can use the SUMPRODUCT function to calculate weighted average in Excel

Below are three different situations where you can use the SUMPRODUCT function to calculate weighted average in Excel

#### Example 1 – When the Weights Add Up to 100%

Suppose you have a dataset with marks scored by a student in different exams along with the weights in percentages (as shown below):

![Dataset of grades for calculating Weighted Average in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20386%20193'%3E%3C/svg%3E)

In the above data, a student gets marks in different evaluations, but in the end, needs to be given a final score or grade. A simple average can not be calculated here as the importance of different evaluations vary.

For example, a quiz, with a weight of 10% carries twice the weight as compared with an assignment, but one-fourth the weight as compared with the Exam.

In such a case, you can use the [SUMPRODUCT function](https://trumpexcel.com/excel-sumproduct-function/)
 to get the weighted average of the score.

Here is the formula that will give you the weighted average in Excel:

\=SUMPRODUCT(B2:B8,C2:C8)

![SUMPRODUCT formula to calculate weighted average when weights are 100 percentage](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20557%20272'%3E%3C/svg%3E)

**Here is how this formula works****:** Excel SUMPRODUCT function multiplies the first element of the first array with the first element of the second array. Then it multiplies the second element of the first array with the second element of the second array. And so on..

And finally, it adds all these values.

Here is an illustration to make it clear.

![Calculate Weighted Average in Excel - Sumproduct explaination](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20668%20420'%3E%3C/svg%3E)

Also read: [How to Calculate Percentile in Excel](https://trumpexcel.com/percentile-excel/)

#### Example 2 – When Weights Don’t Add Up to 100%

In the above case, the weights were assigned in such a way that the total added up to 100%. But in real life scenarios, it may not always be the case.

Let’s have a look at the same example with different weights.

![Calculating weighted average when the weights don't add up to 100%](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20405%20195'%3E%3C/svg%3E)

In the above case, the weights add up to 200%.

If I use the same SUMPRODUCT formula, it will give me the wrong result.

![Calculate Weighted Average in Excel - double result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20573%20250'%3E%3C/svg%3E)

In the above result, I have doubled all the weights, and it returns the weighted average value as 153.2. Now we know a student can’t get more than 100 out of 100, no matter how brilliant he/she is.

The reason for this is that the weights don’t add up to 100%.

Here is the formula that will get this sorted:

\=SUMPRODUCT(B2:B8,C2:C8)/SUM(C2:C8)

In the above formula, the SUMPRODUCT result is divided by the sum of all the weights. Hence, no matter what, the weights would always add up to 100%.

![Normalized weights to calculate weighted average in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20250'%3E%3C/svg%3E)

One practical example of different weights is when businesses calculate the [weighted average cost of capital](https://en.wikipedia.org/wiki/Weighted_average_cost_of_capital)
. For example, if a company has raised capital using debt, equity, and preferred stock, then these will be serviced at a different cost. The company’s accounting team then calculates the weighted average cost of capital that represents the cost of capital for the entire company.

Also read: [How to Calculate Percentage Increase in Excel](https://trumpexcel.com/percentage-change-excel/)

#### Example 3 – When the Weights Need to be Calculated

In the example covered so far, the weights were specified. However, there may be cases, where the weights are not directly available, and you need to calculate the weights first and then calculate the weighted average.

Suppose you are selling three different types of products as mentioned below:

![Using SUMPRODUCT when weights are not in percentages](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20423%20123'%3E%3C/svg%3E)

You can calculate the weighted average price per product by using the SUMPRODUCT function. Here is the formula you can use:

\=SUMPRODUCT(B2:B4,C2:C4)/SUM(B2:B4)

![Calculate Weighted Average in Excel - Sumproduct data normalized](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20656%20186'%3E%3C/svg%3E)

Dividing the SUMPRODUCT result with the SUM of quantities makes sure that the weights (in this case, quantities) add up to 100%.

Also read: [How to Calculate Ratios in Excel?](https://trumpexcel.com/calculate-ratios-excel/)

### Calculating Weighted Average in Excel – SUM Function

While the SUMPRODUCT function is the best way to calculate the weighted average in Excel, you can also use the SUM function.

To calculate the weighted average using the SUM function, you need to multiply each element, with its assigned importance in percentage.

Using the same dataset:

![Calculate Weighted Average in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20386%20193'%3E%3C/svg%3E)

Here the formula that will give you the right result:

\=SUM(B2\*C2,B3\*C3,B4\*C4,B5\*C5,B6\*C6,B7\*C7,B8\*C8)

![Calculate Weighted Average in Excel - sum function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20225'%3E%3C/svg%3E)

This method is alright to use when you have a couple of items. But when you have many items and weights, this method could be cumbersome and error-prone. There is shorter and better way of doing this using the [SUM function](https://trumpexcel.com/excel-sum-function/)
.

Continuing with the same data set, here is the short formula that will give you the weighted average using the SUM function:

\=SUM(B2:B8\*C2:C8)

The trick while using this formula is to use Control + Shift + Enter, instead of just using Enter. Since SUM function can not handle arrays, you need to use Control + Shift + Enter.![Calculate Weighted Average in Excel - sum array](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20519%20249'%3E%3C/svg%3E)

When you hit Control + Shift + Enter, you would see curly brackets appear automatically at the beginning and the end of the formula (see the formula bar in the above image).

Again, make sure the weights add up to 100%. If it does not, you need to divide the result by the sum of the weights (as shown below, taking the product example):

![Normalizing Weights using SUM formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20604%20181'%3E%3C/svg%3E)

**You May Also Like the Following Excel Tutorials:**

*   [How to Calculate CAGR in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    
*   [5 Easy Ways to Calculate Running Total in Excel (Cumulative Sum)](https://trumpexcel.com/running-total-excel/)
    
*   [How to Calculate IRR in Excel](https://trumpexcel.com/calculate-irr-excel/)
    
*   [Calculating Loan Payment Using PMT Function](https://trumpexcel.com/pmt-function/)
    
*   [How to Calculate and Format Percentages in Excel](https://trumpexcel.com/calculate-percentages-excel/)
    
*   [How to Calculate Age in Excel using Formulas](https://trumpexcel.com/calculate-age-in-excel/)
    
*   [Calculating Standard Deviation in Excel](https://trumpexcel.com/standard-deviation/)
    
*   [Calculating Compound Interest in Excel](https://trumpexcel.com/compound-interest-calculator/)
    
*   [Calculating Moving Average in Excel \[Simple, Weighted, & Exponential\]](https://trumpexcel.com/moving-average-excel/)
    
*   [How to Calculate Average Annual Growth Rate (AAGR) in Excel](https://trumpexcel.com/calculate-average-annual-growth-rate-excel/)
    
*   [Interquartile Range in Excel](https://trumpexcel.com/interquartile-range-iqr-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “Calculating Weighted Average in Excel (Using Formulas)”
----------------------------------------------------------------------

1.  i want silver multification  
    2.145 weight  
    44.55 touch  
    2145\*4455=9555  
    exel automatically last 5 come add one number for multification(\*) how to incress last 8 number come Add one number
    
    [Reply](https://trumpexcel.com/weighted-average-in-excel/#comment-13041)
    
2.  I’m trying to weight 4 different column rankings for cumulative of 100%. Trying to figure formula would be 20%, 50%, 15%, 15%.
    
    [Reply](https://trumpexcel.com/weighted-average-in-excel/#comment-11589)
    
3.  u should also mention frequency related weighted average
    
    [Reply](https://trumpexcel.com/weighted-average-in-excel/#comment-10800)
    
4.  Excellent explanation Sumit! I like the modification to the formula when the %s add up to more than 100. I’m going to share this!
    
    [Reply](https://trumpexcel.com/weighted-average-in-excel/#comment-3103)
    
    *   Thanks for commenting Kevin.. Glad you found this useful 🙂
        
        [Reply](https://trumpexcel.com/weighted-average-in-excel/#comment-3131)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/weighted-average-in-excel/#respond)

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