# Calculate Interquartile Range (IQR) in Excel

**Source:** https://trumpexcel.com/interquartile-range-iqr-excel

---

[Skip to content](https://trumpexcel.com/interquartile-range-iqr-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/interquartile-range-iqr-excel/#below-title)

Interquartile Range (IQR) is often used in statistics to identify outliers and understand the spread of the middle 50% of the data set.

Interquartile Range allows you to analyze data without it getting skewed by outliers and extreme values. This helps us get a better view of the variability of the data as compared to other similar metrics, such as range or [standard deviation](https://trumpexcel.com/standard-deviation/)
.

While there is no dedicated formula in Excel to calculate the interquartile range, there is a formula to calculate Quartiles, which can easily be used to calculate the IQR.

Before I show you how to calculate the Interquartile Range in Excel, let me quickly explain the concept of quartiles and how we can use them to calculate IQR.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/interquartile-range-iqr-excel/#)

What are Quartiles and InterQuartile Range?
-------------------------------------------

In statistics, a population or a dataset can be divided into four parts, and each part is called a quartile (called Q1, Q2, Q3, and Q4).

For the sake of explanation, let’s say I have a series of numbers as shown below in ascending order. Let’s assume that these are scores of students in a test.

0, 1, 2, 3, 4, 5, 6, 7 8, 9, 10

If I calculate the first quartile from this range, it will give me a number below which the first 25 percentile of the scores lies.

In this range, that value would be 2.5 (which means that if you score 2.5 or below, then you would be at the bottom 25% according to this dataset)

Similarly, Quartile 2 would be 5, Quartile 3 would be 7.5, and Quartile 4 would be 10.

Now, once you have the Quartile values, you can calculate the interquartile range by using the below formula:

IQR = Quartile 3 - Quartile 1

So, in our example, the IQR would be:

IQR = 7.5 - 2.5

**Note**: I have shown you a series of numbers in ascending order just for simplicity to explain the concept of IQR. In reality, these numbers could be anything and may not be in an ascending or descending order (as shown in the example next).

Also read: [How to Calculate PERCENTILE in Excel](https://trumpexcel.com/percentile-excel/)

Calculating Interquartile Range (IQR) in Excel
----------------------------------------------

Now, let’s see how to calculate IQR in Excel using in-built formulas.

As I mentioned, Excel does not have an inbuilt function to calculate the Interquartile Range. However, it does have the **Quartile function** that we can use for this purpose.

Below is a dataset of scores of students in a class, and I want to calculate the IQR for this dataset.

![Dataset to calculate interquartile range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20507%20476'%3E%3C/svg%3E)

To calculate the Interquartile Range, we would first have to calculate Quartile 1 and Quartile 3 values.

Enter the below formula in cell E2 to get the Quartile 1 Value:

\=QUARTILE.INC(B2:B16,1)

![Quartile 1 formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20568%20526'%3E%3C/svg%3E)

_The QUARTILE.INC function takes two arguments – the range that has the numbers and the Quart value we want to get. In this case, since we wanted the first-quart value, we used 1 as the second argument._

Now, enter the below formula in cell E3 to get the Quartile 2 Value:

\=QUARTILE.INC(B2:B16,3)

![Quartile 3 formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20570%20523'%3E%3C/svg%3E)

Now use the below formula in cell E4 to get the IQR value:

\=E3-E2

![interquartile range IQR formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20508%20525'%3E%3C/svg%3E)

If you don’t want to do it in parts, you can get the IQR directly with this single formula:

\=QUARTILE.INC(B2:B16,3)-QUARTILE.INC(B2:B16,1)

So, this is a simple formula you can use to calculate IQR in Excel.

Excel has three Quartile functions – QUARTILE, QUARTILE.INC, and QUARTILE.EXC.

*   _QUARTILE_ function is kept for compatibility reasons, so you should not be using it.
*   _QUARTILE.INC_ includes the 0 and 100 percentile values when doing the calculation, and
*   _QUARTILE.EXC_ excludes the 0 and 100 percentile values when doing the calculation

Also read: [How to Find Range in Excel](https://trumpexcel.com/find-range-in-excel/)

### **How to Interprent Interquartile Range Value?**

The IQR tells us how spread out the middle half of your data is (which is the range between the 25th and the 75th percentile value).

A high IQR value indicates a greater spread of the middle data points, while a lower IQR value suggests that these points are closer together.

So, if I take an example of scores of students in a class, a low IQR value tells me that students have scored consistently, and there is not a huge difference in the scores of students in the bottom 25 percentile and top 25 percentile.

On the other hand, if the IQR value is high, it tells me that the variability is high, and there is a large difference between the scores of students who scored in the bottom 25 percentile and the ones who scored in the top 25 percentile.

Since the IQR uses quartiles and not mean/average, it is a better measure to learn about the variability of datasets (especially when you have skewed distributions).

In Excel, IQR is best represented by using Box Plots charts (as it shows the data distributions based on the quartiles)

Also read: [How to Make a Bell Curve in Excel](https://trumpexcel.com/bell-curve/)

IQR\*1.5 Rule to Find Outliers
------------------------------

There is a 1.5\*IQR rule that helps you [identify outliers in your dataset](https://trumpexcel.com/find-outliers-excel/)
.

This is quite useful in statistics when you have large datasets and you want a basis to identify outliers.

According to this rule, outliers are those values that fall below **Q1 – 1.5 \* IQR** or above **Q3 + 1.5 \* IQR**

So, this is how you can use a simple formula to calculate the Interquartile Range (IQR) in Microsoft Excel.

I hope you found this Excel article useful

**Other Excel articles you may also like:**

*   [Calculate the Coefficient of Variation (CV) in Excel](https://trumpexcel.com/calculate-coefficient-of-variation-excel/)
    
*   [Calculate Correlation Coefficient in Excel](https://trumpexcel.com/correlation-coefficient-excel/)
    
*   [Calculate P-value in Excel](https://trumpexcel.com/p-value-excel/)
    
*   [How to Find Slope in Excel?](https://trumpexcel.com/find-slope-excel/)
    
*   [How to Get Descriptive Statistics in Excel?](https://trumpexcel.com/descriptive-statistics-excel/)
    
*   [Calculating Weighted Average in Excel](https://trumpexcel.com/weighted-average-in-excel/)
    
*   [Calculate Chi-Square in Excel](https://trumpexcel.com/chi-square-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/interquartile-range-iqr-excel/#respond)

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