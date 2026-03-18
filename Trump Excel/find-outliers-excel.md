# How to Find Outliers in Excel (and how to handle these)

**Source:** https://trumpexcel.com/find-outliers-excel

---

[Skip to content](https://trumpexcel.com/find-outliers-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/find-outliers-excel/#below-title)

When working with data in Excel, you’ll often have the issues of handling outliers in your data set.

Having outliers is quite common in all kinds of data, and it’s important to identify and treat these outliers to make sure that your analysis is correct and more meaningful.

In this tutorial, I’ll show you **how to find outliers in Excel**, and some of the techniques that I have used in my work to handle these outliers.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/find-outliers-excel/#)

What are Outliers and Why is it Important to Find these?
--------------------------------------------------------

An outlier is a data point that is way beyond the other data points in the data set. When you have an outlier in the data, it can skew your data which can lead to incorrect inferences.

Let me give you a simple example.

Let’s say 30 people are traveling in a bus from destination A to destination B. All the people are in a similar weight group and income group. For the purpose of this tutorial, let’s consider the average weight to be 220 pounds and the average yearly income to be $70,000.

Now somewhere in the middle of our route, the bus stops, and Bill Gates hops in.

Now, what do you think this would do to the average weight and the average income of the people on the bus.

While the average weight is not likely to change much, the average income of the people on the bus is going to skyrocket heavily.

That’s because Bill Gates’s income is an outlier in our group, and that gives us a wrong interpretation of the data. The average income for each person on the bus would be a few billion dollars, which is way beyond the actual value.

When working with actual datasets in Excel, you can have outliers in any direction (i.e., a positive outlier or a negative outlier).

And to make sure that your analysis is correct, you somehow need to identify these outliers and then decide how to best treat them.

Now let’s see a couple of ways to find outliers in Excel.

Also read: [How to Calculate Percentile in Excel](https://trumpexcel.com/percentile-excel/)

Find Outliers by Sorting the Data
---------------------------------

With small datasets, a quick way to identify outliers is to simply [sort the data](https://trumpexcel.com/sort-excel/)
 and manually go through some of the values at the top of this sorted data.

And since there could be outliers in both directions, make sure you first sort the data in ascending order and then in descending order and then go through the top values.

Let me show you an example.

Below I have a dataset where I have call durations (in seconds) for 15 customer service calls.

![Data with outliers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20331%20408'%3E%3C/svg%3E)

Below are the steps to sort this data so that we can identify the outliers in the dataset:

1.  Select the Column Header of the column you want to sort (cell B1 in this example)
2.  Click the Home tab![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20438%20198'%3E%3C/svg%3E)
3.  In the Editing group, click on the Sort & Filter icon.![Click on Sort and Filter icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20439%20158'%3E%3C/svg%3E)
4.  Click on Custom Sort![Click on Custom Sort](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20273%20421'%3E%3C/svg%3E)
5.  In the Sort dialog box, select ‘Duration’ in the Sort by drop-down and ‘Largest to Smallest’ in the Order drop-down ![Make selection to sort the data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20336'%3E%3C/svg%3E)
6.  Click Ok

The above steps would sort the call duration column with the highest values at the top. Now you can manually scan the data and see if there are any outliers.

![Outliers in the sorted data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20336%20412'%3E%3C/svg%3E)

In our example, I can see that the first two values are way higher than the rest of the values (and the bottom two are way lower).

_Note: This method works with small datasets where you can manually scan the data. It’s not a scientific method but works well_

Finding Outliers Using the Quartile Functions
---------------------------------------------

Now let’s talk about a more scientific solution that can help you identify whether there are any outliers or not.

In statistics, a quartile is one-fourth of the data set. For example, if you have 12 data points, then the first quartile would be the bottom three data points, the second quartile would be the next three data points, and so on.

Below is the data set where I want to find the outliers. To do this, I will have to calculate the 1st and the 3rd quartile, and then using it calculate the upper and the lower limit.

![Data set to find outliers using quartile method](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20630%20416'%3E%3C/svg%3E)

Below is the formula to calculate the first quartile in cell E2:

\=QUARTILE.INC($B$2:$B$15,1)

![First quartile formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20635%20512'%3E%3C/svg%3E)

and here is the one to calculate the third quartile in cell E3:

\=QUARTILE.INC($B$2:$B$15,3)

![Second Quartile formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20640%20666'%3E%3C/svg%3E)

Now, I can use the above two calculations to [get the Interquartile Range](https://trumpexcel.com/interquartile-range-iqr-excel/)
 (which is 50% of our data within the 1st and the 3rd quartile)

\=F3-F2

![Inter quartile range formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20635%20518'%3E%3C/svg%3E)

Now, we will use the interquartile range to find the lower and upper limit which would contain most of our data.

Anything which is out of these lower and upper limits would then be considered outliers.

Below is the formula to calculate the lower limit:

\=Quartile1 - 1.5\*(Inter Quartile Range)

which in our example becomes:

\=F2-1.5\*F4

![Lower Limit formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20641%20540'%3E%3C/svg%3E)

And the formula to calculate the upper limit is:

\=Quartile3 + 1.5\*(Inter Quartile Range)

which in our example becomes:

\=F3+1.5\*F4

![Upper Limit formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20633%20514'%3E%3C/svg%3E)

Now that we have the upper and lower limit in our data set, we can go back to the original data and quickly identify those values that do not lie in this range.

A quick way to do this would be to check every value and return a TRUE or FALSE in a new column.

I have used the below [OR formula](https://trumpexcel.com/excel-or-function/)
 to get TRUE for those values that are outliers.

\=OR(B2<$F$5,B2>$F$6)

![OR formula to show Outliers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20630%20492'%3E%3C/svg%3E)

Now you can filter the Outlier column and only show the records where the value is TRUE.

Alternatively, you can also use [conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
 to highlight all the cells where the value is TRUE

**Note:** While this is a more accepted method to find outliers in statistics. I find this method a bit unusable in real-life scenarios. In the above example, the lower limit calculated by the formula is -103, while the dataset we have can only be positive. So this method can help us find outliers in one direction (high values), it’s useless in identifying outliers in the other direction.

Finding the Outliers Using the LARGE/SMALL functions
----------------------------------------------------

If you work with a lot of data (values in multiple columns), you can extract the largest and the smallest 5 or 7 values and see if there are any outliers in it.

If there are any outliers, you will be able to identify them without having to go through all the data in both directions.

Suppose we have the below dataset and we want to know if there are any outliers.

![Data with outliers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20331%20408'%3E%3C/svg%3E)

Below is the formula that will give you the largest value in the dataset:

\=LARGE($B$2:$B$16,1)

Similarly, the second largest value will be given by

\=LARGE($B$2:$B$16,1)

If you’re not using Microsoft 365, which has dynamic arrays, you can use the below formula and it will give you the five largest values from the dataset with one single formula:

\=LARGE($B$2:$B$16,ROW($1:5))

![Large Formula to find outliers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20606%20509'%3E%3C/svg%3E)

Similarly, if you want the smallest 5 values, use the below formula:

\=SMALL($B$2:$B$16,ROW($1:5))

or the following in case you don’t have dynamic arrays:

\=SMALL($B$2:$B$16,1)

Once you have these values, it’s really easy to find out any outliers in the dataset.

While I have chosen to extract the largest and smallest 5 values, you can choose to get 7 or 10 based on how big your dataset is.

I am not sure if this is an acceptable method for finding outliers in Excel or not, but this is the method that I used when I had to work with a lot of financial data in my job a few years ago. Compared to all the other methods covered in this tutorial, I found this one to be the most effective.

How to Handle Outliers the Right Way
------------------------------------

So far, we have seen the methods that will help us find the outliers in our data set. But what to do once you know that there are outliers.

Here are a couple of methods that you can use to handle outliers so that your data analysis is correct.

### Delete the Outliers

The easiest way to remove outliers from your data set is to simply delete them. This way it won’t skew your analysis.

It’s a more viable solution when you have large datasets and deleting a couple of outliers won’t impact the overall analysis. And of course, before deleting the data make sure you create a copy and delve into what’s causing these outliers.

### Normalize the Outliers (Adjust the Value)

Normalizing the outliers is what I used to do when I was in my full-time job. For all the outlier values, I would simply change them to a value that is slightly higher than the maximum value in the data set.

This made sure that I’m not deleting the data but at the same time I’m not letting it skew my data.

To give you a real-life example, if you’re analyzing the net profit margin of companies, where most of the companies lie within -10% to 30%, and there are a couple of values that are upward of 100%, I would simply change these outlier values to 30% or 35%.

So these are some of the methods that you can use in **Excel to find outliers**.

Once you have identified the outliers, you can delve into the data and look for what’s causing these, at the same time pick one of the techniques to handle these outliers (which could be removing these or normalizing these by adjusting the value)

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [How to Find Range in Excel (Easy Formulas)](https://trumpexcel.com/find-range-in-excel/)
    
*   [Calculating Moving Average in Excel \[Simple, Weighted, & Exponential\]](https://trumpexcel.com/moving-average-excel/)
    
*   [How to Calculate Standard Deviation in Excel](https://trumpexcel.com/standard-deviation/)
    
*   [Standard Deviation Bell Curve](https://trumpexcel.com/bell-curve/)
    
*   [Calculate Chi-Square in Excel](https://trumpexcel.com/chi-square-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/find-outliers-excel/#respond)

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