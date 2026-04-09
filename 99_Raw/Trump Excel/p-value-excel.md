# How to Calculate P-Value in Excel (2 Easy Ways)

**Source:** https://trumpexcel.com/p-value-excel

---

[Skip to content](https://trumpexcel.com/p-value-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/p-value-excel/#below-title)

The P-value is an important concept in statistics that is often used in hypothesis testing and decision-making.

Since Excel is a widely used tool for many statistics calculations, it would be useful to know how to calculate the P-value in Excel.

Excel already has some built-in functions and even an add-in that makes it really easy to calculate P-value.

In this article, I will show you how to do this using a very simple yet practical example.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/p-value-excel/#)

What is the P-value? An Easy Overview
-------------------------------------

Before I get into how to calculate P-value in Excel, let me quickly explain what it is and how it works.

The P-value helps us determine if their results are statistically significant or just due to chance. This helps us make informed decisions (or an idea of whether something needs to be looked into more or not).

Let me explain with a practical example.

Let’s say you want to know if an Excel training course actually improves employees’ productivity.

You have two groups of employees:

*   Group A: Attended the Excel training (let’s say my [Free Online Excel Training](https://trumpexcel.com/learn-excel/)
    )
*   Group B: Didn’t attend the training

After a month, you measure how many reports/tasks each group completes per day. You notice that Group A seems to complete more tasks, but you’re not sure if it’s because of the training or just by chance.

This is where the P-value comes in handy!

The P-value answers this question: “What are the chances we’d see this difference in task completion if the Excel training didn’t actually have any effect?”

If the P-value is small (usually less than 0.05), it suggests the difference is probably not just random luck. You might conclude, “Hey, this Excel training seems to be making a real difference!”

If the P-value is large, it’s like saying, “Well, we can’t be sure if this difference is because of the training or just by chance.”

Think of the P-value as your “coincidence detector.” The smaller it is, the less likely the results are just a coincidence.

But remember, the P-value doesn’t tell you if your hypothesis is true or how important your results are. It’s just a tool to help you decide whether your results are worth getting excited about or if they might just be a fluke.

In the next sections, I’ll show you how to calculate P-value in Excel. It’s simpler than you might expect, and soon, you’ll be crunching these numbers like a pro!

Also read: [How to Make a Bell Curve in Excel](https://trumpexcel.com/bell-curve/)

Calculating P-value in Excel
----------------------------

Now, let’s look at how we can calculate P-value in Excel.

### Using the T.TEST Function

Excel’s T.TEST function can be used to calculate the P-value.

Below, I have a data set where I have the time taken by two groups (Group A and Group B) for an Excel task.

![Dataset to calculate P Value in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20295%20495'%3E%3C/svg%3E)

Group A includes employees who have undergone Excel training, and employees in Group B have not.

Now, I need to check whether taking the Excel training has had any impact on the performance of these groups or not.

In this example, our _Null Hypothesis_ is that Excel training had no impact on the performance of the employees in either group and the _Alternative Hypothesis_ is that Excel training improved the performance of people in group A

This is where calculating the P-value can be helpful.

Here is the formula that will calculate the P-value in this scenario:

\=T.TEST(A2:A16,B2:B16,2,2)

![T TEST Formula to calculate p value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20561%20601'%3E%3C/svg%3E)

The above formula gives us the P-value as .000368.

Since this value is less than 0.05, we can reject the null hypothesis as it suggests the difference is probably not just random luck. You might conclude, “Hey, this Excel training seems to be making a real difference!”

Had this value been more than 0.05, we wouldn’t have been able to conclude that the training had any measurable impact on the performance of the people in Group A.

Think of the P-value as your “coincidence detector.” The smaller it is, the less likely the results are just a coincidence.

Important – In this above formula, I have chosen the third argument as 2 (which means it would be a two-tailed distribution) and the fourth argument as 2 (which means it would be a sample Equal Variance case).

If you are interested in learning what these options are, I have them covered.

#### One-Tailed Distribution vs Two-Tailed Distribution

One-tailed distribution is your choice when you’re predicting an effect in a specific direction.

Imagine you’re testing if a new Excel training boosts productivity – you’re only interested in an increase. Here, you focus on one end of the distribution curve.

It’s more powerful for detecting effects, but you might miss impacts in the opposite direction.

Two-tailed distribution, on the other hand, is perfect when you’re unsure of the effect’s direction.

This means that you’re open to the possibility that the Excel training may increase or decrease productivity. This approach watches both ends of the distribution curve. It’s like casting a wider net – you can catch effects either way, but it’s more conservative.

In our Excel T.TEST example, we used a two-tailed distribution (argument set to 2). This means we considered both positive and negative impacts of the training. It’s cautious but ensures we don’t overlook unexpected outcomes.

If you’re unsure, it’s better to choose the two-tailed distribution option. That’s what I did in the T.TEST formula.

#### Paired vs. Two-Sample Equal Variance vs. Two-Sample Unequal Variance

**Paired tests** are your go-to when you’re dealing with before-and-after scenarios. Imagine you’re measuring the [Excel skills](https://trumpexcel.com/excel-skills/)
 of employees before and after a training course. Each ‘before’ score is naturally paired with an ‘after’ score for the same person. This test looks at the differences within these pairs.

**Two-sample Equal Variance tests** come into play when you’re comparing two independent groups that you believe have **similar variability**. Think of comparing Excel skills between two departments that have similar work environments. This test assumes the spread of scores in both groups is roughly the same.

Two-sample Unequal Variance tests, also known as Welch’s t-test, are your best bet when you’re unsure if the two groups have similar variability. Maybe you’re comparing Excel skills between a tech-savvy marketing team and a less tech-oriented sales team. This test doesn’t assume equal spread, making it more flexible but slightly less powerful.

In our Excel example, I chose the Two-Sample Equal Variance option (the fourth argument set to 2). This means I assumed the variability in Excel skills was similar between our trained and untrained groups.

Also read: [How to Get Descriptive Statistics in Excel?](https://trumpexcel.com/descriptive-statistics-excel/)

### Using Analysis Toolpak

Another method to calculate the P value in Excel is the Analysis Toolpak.

This is an [add-in](https://trumpexcel.com/excel-add-in/)
 that is available by default in your Excel application; however, it may not have been enabled already.

So we first need to enable this Analysis Toolpak add-in, and then we will use it to calculate the P-value in Excel.

#### Enabling Analysis Toolpak Add-in

Below are the steps to enable the Analysis Toolpak add-in Excel

1.  Click the File tab in the ribbon

![Click the File tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20505%20222'%3E%3C/svg%3E)

2.  Click on Options
3.  In the Excel Options dialog box that opens, click on Add-ins

![Click on Add-ins](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201032%20809'%3E%3C/svg%3E)

4.  At the bottom of the dialog box, select _Excel Add-ins_ from the Manage drop-down and then click on Go

![Select Excel Add-in in Manage](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20761%20463'%3E%3C/svg%3E)

5.  In the Add-ins dialog box, check the Analysis Toopak option

![Check the Analysis Toolpak option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20365%20536'%3E%3C/svg%3E)

The above steps would enable the Analysis Toolpak, and you will be able to see a new option in the Data tab called _Data Analysis_

#### Calculating P-Value using Analysis Toolpak

Now, let’s see how to calculate the P-value using the Analysis ToolPak we have just enabled.

Below, I have a data set where I have the time taken by two groups (Group A and Group B) for an Excel task.

![Dataset to calculate P Value in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20295%20495'%3E%3C/svg%3E)

Group A includes employees who have undergone Excel training, and employees in Group B have not.

Now, I need to check whether taking the Excel training has had any impact on the performance of these groups (using the P-value).

Here are the steps to calculate the P-value:

1.  Click the _Data_ tab

![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20581%20223'%3E%3C/svg%3E)

2.  In the _Analysis_ group, click on the _Data Analysis_ option

![Click on Data Analysis](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20598%20223'%3E%3C/svg%3E)

3.  In the Data Analysis dialog box, select _t-Test Two-Sample Assuming Equal Variances_ option

![Select T Test Two sample assuming equal variance](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20514%20274'%3E%3C/svg%3E)

4.  Click OK. This will open a dialog box
5.  For _Variable 1 Range_, select A1:A16 (which are all the employee’s performance in group A, including the header)
6.  For _Variable 2 Range_, select B1:B16 (which are all the employee’s performance in group B, including the header)

![Select ranges for Variable 1 and Variable 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20391'%3E%3C/svg%3E)

7.  Check the Labels dialog box (as our dataset has headers)

![Check the Labels check box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20549%20391'%3E%3C/svg%3E)

8.  Click on the Output Range option
9.  Select a cell in the worksheet where you want the result. In this case, I will select cell D1.

![Select the output location in the sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20391'%3E%3C/svg%3E)

10.  Click Ok

The above steps would give you the result as shown below, where it calculates and gives you some statistics, including the P-value (one-tail as well as two-tail)

![Analysis Toolpak Result giving P value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201091%20502'%3E%3C/svg%3E)

You can also cross-check and see that the result we get from Analysis Toolpak for the P-value two-tail scenario is the same that we got when we used the T.TEST function.

Note: The table that you get as an output of Analysis Toolpak is not dynamic. So, if any of the values in our original data set changes, you will have to rerun this to get the new result.

So, these are two methods you can use to calculate the P-value in Excel.

I hope you found this article helpful. If you have any questions or suggestions for me, please let me know in the comments section.

**Other Excel articles you may also like:**

*   [Calculate the Coefficient of Variation (CV) in Excel](https://trumpexcel.com/calculate-coefficient-of-variation-excel/)
    
*   [How to Calculate Correlation Coefficient in Excel (2 Easy Ways)](https://trumpexcel.com/correlation-coefficient-excel/)
    
*   [Calculate Interquartile Range (IQR) in Excel](https://trumpexcel.com/interquartile-range-iqr-excel/)
    
*   [How to Calculate Standard Deviation in Excel](https://trumpexcel.com/standard-deviation/)
    
*   [Calculate MEDIAN IF in Excel](https://trumpexcel.com/median-if-excel/)
    
*   [Calculating Moving Average in Excel \[Simple, Weighted, & Exponential\]](https://trumpexcel.com/moving-average-excel/)
    
*   [Calculate Chi-Square in Excel](https://trumpexcel.com/chi-square-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/p-value-excel/#respond)

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