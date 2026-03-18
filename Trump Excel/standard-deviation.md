# How to Calculate Standard Deviation in Excel (Step-by-Step)

**Source:** https://trumpexcel.com/standard-deviation

---

[Skip to content](https://trumpexcel.com/standard-deviation/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/standard-deviation/#below-title)

Excel is used extensively for statistics and data analysis. Standard deviation is something that is used quite often in statistical calculations.

In this tutorial, I will show you **how to calculate the standard deviation in Excel** (using simple formulas)

But before getting into, let me quickly give you a brief overview of what standard deviation is and how it’s used.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/standard-deviation/#)

What is Standard Deviation?
---------------------------

A standard deviation value would tell you how much the data set deviates from the mean of the data set.

For example, suppose you have a group of 50 people, and you are recording their weight (in kgs).

In this data set, the average weight is 60 kg, and the standard deviation is 4 kg. It means that most of the people’s weight is within 4 kg of the average weight (which would be 56-64 kg).

Now let’s interpret the standard deviation value:

*   A lower value indicates that the data points tend to be closer to the [average](https://trumpexcel.com/excel-average-function/)
     (mean) value.
*   A higher value indicates that there is widespread variation in the data points. This can also be a case when there are many [outliers in the data set](https://trumpexcel.com/find-outliers-excel/)
    .

![Standard Deviation in Excel- Bell Curve](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20466'%3E%3C/svg%3E)
-----------------------------------------------------------------------------------------------------------------------------------------------------

Calculating Standard Deviation in Excel
---------------------------------------

While it’s easy to calculate the standard deviation, you need to know which formula to use in Excel.

There are six standard deviation formulas in Excel (eight if you consider database functions as well).

![there are eight standard deviation functions in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20103%20169'%3E%3C/svg%3E)

These six formulas can be divided into two groups:

1.  Calculating the sample standard deviation: The formulas in this category are STDEV.S, STDEVA, and STDEV
2.  Calculating the standard deviation for an entire population: The formulas in this category are STDEV.P, STDEVPA, and STDEVP

In almost all of the cases, you will use standard deviation for a sample.

Again in layman terms, you use the term ‘population’ when you want to consider all the datasets in the entire population. On the other hand, you use term ‘sample’ when using a population is not possible (or it’s unrealistic to do so). In such a case, you pick a sample from the population.

You can use the sample data to calculate the standard deviation and infer for the entire population. You can read a great explanation of it [here](https://stats.stackexchange.com/questions/269/what-is-the-difference-between-a-population-and-a-sample)
 (read the first response).

So. this narrows down the number of formulas to three (STDEV.S, STDEVA, and STDEV function)

Now let’s understand these three formulas:

*   STDEV.S – Use this when your data is numeric. It ignores the text and logical values.
*   STDEVA – Use this when you want to include text and logical values in the calculation (along with numbers). Text and FALSE are taken as 0 and TRUE is taken as 1.
*   STDEV – STDEV.S was introduced in Excel 2010. Before it, the STDEV function was used. It is still included for compatibility with prior versions.

So, you can safely assume that in most of the cases, you would have to use STDEV.S function (or STDEV function if you’re using Excel 2007 or prior versions).

So now let’s see how to use it in Excel.

Using STDEV.S Function in Excel
-------------------------------

As mentioned, STDEV.S function uses numerical values but ignores the text and logical values.

Here is the syntax of STDEV.S function:

_STDEV.S(number1,\[number2\],…)_

*   **Number1** – This is a mandatory argument in the formula. The first number argument corresponds to the first element of the sample of a population. You can also use a [named range](https://trumpexcel.com/named-ranges-in-excel/)
    , single array, or a reference to an array instead of arguments separated by commas.
*   **Number2, …** \[Optional argument in the formula\] You can use up to 254 additional arguments. These can refer to a data point, a named range, a single array, or a reference to an array.

Now, let’s have a look at a simple example where we calculate the standard deviation.

Also read: [Calculate Interquartile Range (IQR) in Excel](https://trumpexcel.com/interquartile-range-iqr-excel/)

Example – Calculating the Standard Deviation for Weight Data
------------------------------------------------------------

Suppose you have a data set as shown below:

![Weight Data to Calculate Standard Deviation in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20160%20292'%3E%3C/svg%3E)

To calculate the standard deviation using this data set, use the following formula:

\=STDEV.S(A2:A10)

In case you’re using Excel 2007 or prior versions, you will not have the STDEV.S function. In that case, you can use the below formula:

\=STDEV(D2:D10)

![Using STDEVS function to find deviation in weight](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20497%20336'%3E%3C/svg%3E)

The above formula returns the value of 2.81, which indicates that most of the people in the group would be within the weight range 69.2-2.81 and 69.2+2.81.

Note that when I say ‘most of the people’, it refers to the normal distribution of the sample (that is 68% of the sample population is within one standard deviation from the mean).

Also, note that this is a very small sample set. In reality, you may have to do this for a bigger sample data set where you can observe normal distribution better.

Hope you found this Excel tutorial useful.

**You May Also Like the Following Excel Tutorials:**

*   [Calculating Weighted Average in Excel](https://trumpexcel.com/weighted-average-in-excel/)
    .
*   [Calculating CAGR in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    .
*   [Calculate and Format Percentages in Excel](https://trumpexcel.com/calculate-percentages-excel/)
    .
*   [Calculate Age in Excel using Formulas](https://trumpexcel.com/calculate-age-in-excel/)
    .
*   [Creating a Bell Curve in Excel](https://trumpexcel.com/bell-curve/)
    .
*   [Calculating Compound Interest in Excel](https://trumpexcel.com/compound-interest-calculator/)
    .
*   [How to Calculate Square Root in Excel](https://trumpexcel.com/calculate-square-root-in-excel/)
    
*   [Calculate the Coefficient of Variation (CV) in Excel](https://trumpexcel.com/calculate-coefficient-of-variation-excel/)
    
*   [How to Calculate Correlation Coefficient in Excel](https://trumpexcel.com/correlation-coefficient-excel/)
    
*   [How to Get Descriptive Statistics in Excel?](https://trumpexcel.com/descriptive-statistics-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Calculate Standard Deviation in Excel”
-----------------------------------------------------------

1.  Very useful applications.  
    Thanks.
    
    [Reply](https://trumpexcel.com/standard-deviation/#comment-13037)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/standard-deviation/#respond)

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