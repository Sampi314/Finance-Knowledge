# Power BI Blog: Labelling Growth on a Line Chart – Part 1

**Source:** https://sumproduct.com/blog/power-bi-blog-labelling-growth-on-a-line-chart-part-1/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Labelling Growth on a Line Chart – Part 1

*   October 18, 2023

Power BI Blog: Labelling Growth on a Line Chart – Part 1
========================================================

Power BI Blog: Labelling Growth on a Line Chart – Part 1
========================================================

19 October 2023

_Welcome back to this week’s edition of the Power BI blog series. This week, we start looking at a method of labelling growth on a chart._

Power BI visuals are an excellent tool when it comes to telling stories with our data. When we are analysing quantitative data, we often need to compare percentage differences. The most common example of this would probably be, “How much did the stock change today?”. However, how do we highlight that percentage change on a Power BI visual, _e.g._ on a stock price Line chart?

![](<Base64-Image-Removed>)

Above, we have created a custom visual to show cumulative profit, focussing on a specified interval. We have created a label to display the growth of cumulative profit and the current selection is from April to July. We can change the interval shown, by choosing an end month, and then specifying how many months to look back. The visual will not only display a label showing the growth, but it will also change colour automatically depending on whether the growth is positive or negative!

We will be using the **Financials** sample dataset in Power BI Desktop, and you can download our demonstration file with this [link](https://www.sumproduct.com/assets/blog-pictures/2022/PBI/298/sp-growth-label.pbix)
.

First, we prepare to create our visual by making a copy of the **Calendar** table.

**_Create a copy of Calendar_**

The figure used for demonstration here is a cumulative measure of **Profit** from the sample dataset, which we created using the following **DAX** formula:

**Cum  
Profit = CALCULATE(SUM(Financials\[Profit\]), ‘Calendar'\[Date\] <=  
MAX(Financials\[Date\]))**

To be able to select and compare different periods on the visual without applying filters to the background Line chart, we need to make an unconnected copy of the **Calendar** Table, which we’ve named **YearMonth Copy**. Here, we are comparing values from different months, so we will be using **Year** and **Month** for matching and sorting. In**YearMonth Copy**, we create a label **Year Month**, where:

**Year  
Month = FORMAT(‘YearMonth Copy'\[Date\], “mmm-yyyy”)**

and also an index **YM Index**:

**YM Index = YEAR(‘YearMonth Copy'\[Date\]) &  
UNICHAR(MONTH(‘YearMonth Copy'\[Date\]) + 64)**

We have used the **UNICHAR** function to convert the month numbers to capital letters so that we can sort the **Year Month** label.

![](<Base64-Image-Removed>)

We also create, using the same formula, a calculated column **Year Month** in the original **Calendar** Table.

To be able to choose how many months we want to look back, we create a Table **Period Selection** by clicking **New table** and then entering in the Formula bar:

**Period  
Selection = GENERATESERIES(1, 12, 1)**

Thus, we have created the options one \[1\] to 12, and then we create a measure **Period Length**:

**Period  
Length = SELECTEDVALUE(‘Period Selection'\[Period\]) + 1**

When we select three \[3\] months to look back, the measure **Period Length** will be four \[4\], _i.e._ length of the whole comparison period.

So far, we have created the options to choose from, _i.e._ the month to analyse and the number of months to look back. Next, we will define the assisting measures for plotting.

That’s it for this week, next time we show how to create the chart measures that we need.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-labelling-growth-on-a-line-chart-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-labelling-growth-on-a-line-chart-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-labelling-growth-on-a-line-chart-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-labelling-growth-on-a-line-chart-part-1/#0)

[](https://sumproduct.com/blog/power-bi-blog-labelling-growth-on-a-line-chart-part-1/#0 "close")

top