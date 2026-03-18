# Calculate the Coefficient of Variation (CV) in Excel - Easy Formula!

**Source:** https://trumpexcel.com/calculate-coefficient-of-variation-excel

---

[Skip to content](https://trumpexcel.com/calculate-coefficient-of-variation-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/calculate-coefficient-of-variation-excel/#below-title)

Coefficient of Variation (CV) is a common statistical metric used to understand the variability in your data set.

While there is no inbuilt formula to calculate the coefficient of variation in Excel, it can easily be done by first calculating the mean and the [standard deviation of the data set](https://trumpexcel.com/standard-deviation/)
 separately and then calculating the coefficient of variation using these values.

In this short tutorial, I will show you **how to calculate the coefficient of variation in Excel** using a simple data set.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/calculate-coefficient-of-variation-excel/#)

What is the Coefficient of Variation?
-------------------------------------

The Coefficient of Variation is a value (shown as a percentage) that tells us a measure of variation in our data set.

If this value is high, it indicates a high variation in our data set compared to the mean of the data set (i.e., some values are far higher or lower the mean of the dataset).

And if this value is low, it indicates a low variation in our data set, and most values lie closer to the mean.

For example, if we have a data set of heights of different students in a class, a high CV value would mean that the height of the class varies a lot (i.e., there are some students that are short and some that are long).

And if the coefficient of variation value is low, it indicates that most of the students in the class have a similar height which lies closer to the mean height of the group.

Also read: [Calculate P-value in Excel](https://trumpexcel.com/p-value-excel/)

Calculating Coefficient of Variation in Excel
---------------------------------------------

To calculate the coefficient of variation in Excel, we would first have to calculate the standard deviation and the mean of the data set and then use it to calculate the coefficient of variation value.

Let me show you how by using a simple example.

Below I have a data set where I have the height values (in cm) for some students in a class, and I want to calculate the coefficient of variation value for this data set.

![Dataset to calculate coefficient of variation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20355%20345'%3E%3C/svg%3E)

### Step 1 – Calculating the Mean of the Dataset

The first step is to calculate the mean of the given data set, and we will do that using the AVERAGE function in Excel.

Below is the formula that would give us the average of the heights in our data set:

\=AVERAGE(B2:B10)

![Calculating mean of the dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20465%20513'%3E%3C/svg%3E)

### Step 2 – Calculating the Standard Deviation of the Dataset

The second step is to calculate the standard deviation of this data set.

This can be done using the inbuilt STDEV.P and STDEV.S functions in Excel (where STDEV.P calculates the standard deviation of the population and STDEV.S calculate the standard deviation of the sample).

For this tutorial, I will go ahead with the STDEV.P function.

Below is the formula that will give us the standard deviation of this data set:

\=STDEV.P(B2:B10)

![Standard Deviation of the dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20460%20518'%3E%3C/svg%3E)

### Step 3 – Calculating the Coefficient of Variation

And now, we can calculate the coefficient of variation by dividing the standard deviation value by the mean of the dataset.

Below is the formula that would give us the coefficient of variation value for this data:

\=(B13/B12)

![Coefficient of Variation calculation Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20397%20519'%3E%3C/svg%3E)

If you get the Coefficient of Variation value as a decimal, you can [change that to a percentage](https://trumpexcel.com/calculate-percentages-excel/)
.

To do this, select the cell that has the CV value, click on the Home tab, and then click on the percentage icon (it’s in the Number group)

![Convert decimal value to percentage](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20698%20145'%3E%3C/svg%3E)

While I’ve broken down the calculation into three different steps, you do not need to mean and the standard deviation value in separate cells to calculate the coefficient of variation.

You can use the single below formula to get the same result:

\=STDEV.P(B2:B10)/AVERAGE(B2:B10)

Coefficient of Variation of Population vs. Sample
-------------------------------------------------

While calculating the standard deviation in step in step 2, I mentioned that you could either use the STDEV.P function or the STDEV.S function.

If you use the STDEV.P function to calculate the CV value, it would be the CV value for the population, and if you use STDEV.S function, the CV value will be for the sample.

While I’m not going to go too deep into the difference between the population and the sample, the general idea is that if you are calculating the standard deviation for an entire population, the value is considered to be more accurate, and when you are calculating it for a sample, it is considered to be slightly less accurate as it is only for a part of the population.

So if you know whether your data set is the entire population or the sample, you can calculate the coefficient of variation accordingly using the right standard deviation function.

In this tutorial, I showed you how to calculate the coefficient of variation in Excel. It can be done by dividing the standard deviation of the data set by the mean of the data set (both of which can easily be calculated using the inbuilt functions in Excel).

**Other Excel articles you may also like:**

*   [How to Calculate Correlation Coefficient in Excel](https://trumpexcel.com/correlation-coefficient-excel/)
    
*   [Calculating Weighted Average in Excel](https://trumpexcel.com/weighted-average-in-excel/)
    
*   [Percent Increase Formula in Excel](https://trumpexcel.com/percentage-change-excel/)
    
*   [How to Get Descriptive Statistics in Excel?](https://trumpexcel.com/descriptive-statistics-excel/)
    
*   [How to Calculate PERCENTILE in Excel](https://trumpexcel.com/percentile-excel/)
    
*   [How to Find Slope in Excel? Using Formula and Chart](https://trumpexcel.com/find-slope-excel/)
    
*   [Calculate Chi-Square in Excel](https://trumpexcel.com/chi-square-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/calculate-coefficient-of-variation-excel/#respond)

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