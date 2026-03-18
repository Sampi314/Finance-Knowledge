# Power BI Blog Seasonality Analysis Part 1

**Source:** https://sumproduct.com/blog/power-bi-blog-seasonality-analysis-part-1/

---

[Home](https://sumproduct.com/)

\> Power BI Blog Seasonality Analysis Part 1

*   October 16, 2025

Power BI Blog Seasonality Analysis Part 1
=========================================

_Welcome back to this week’s edition of the Power BI blog series._  _This week, we look at seasonality analysis in Power BI._

Seasonality plays a key role in business, especially retail, shaping when and how customers buy products.  By analysing sales patterns across months and years, retailers can identify which items are seasonal, such as coats in winter or sandals in summer, and which remain steady throughout the year.  Let’s use a simple fashion retail dataset to explore how to detect seasonality and apply these insights to smarter business decisions.

The Power BI Desktop file, both for practice and with solutions, may be downloaded [here](https://sumproduct0.sharepoint.com/:f:/s/SumProductTeam/EqlMpZqagmZGsQ-pVSHO2K8Bc_gXQfFomt68Z9c_QX4ZKA?e=VX2z9n)
.

Before diving into the analysis, let’s briefly review the dataset.  It’s a straightforward fashion retail dataset containing several dimensional tables such as **dCustomers**, **dProducts** and **dStores**, along with a fact table called **fSales**.  The **Calendar** table is generated automatically based upon the earliest and latest transaction dates in **fSales**.  In addition, the model includes a **Sales Plan** table, which provides projected sales by store, month and year.

The task here will be to understand what seasonality means and how to identify it in product sales.  Seasonality refers to the influence of recurring annual or monthly fluctuations on sales.  The stronger these fluctuations, the more seasonal a product is considered; its sales vary noticeably from month to month or season to season.  To analyse this, we’ll make small adjustments to our calendar, focusing on months rather than the full year-month format, since seasonality is typically observed at the monthly level.

To begin our analysis, we need a column that extracts the month from each date in the calendar.  This will allow us to focus purely on month-based seasonality.  We can create it with a simple **DAX** expression:

> **MonthNumbers = MONTH(‘Calendar'\[Date\])**

This new column will assign each date its corresponding month number (1 for January, 2 for February, _etc._).

![](<Base64-Image-Removed>)

With this new column in place, we now have a clear list of months extracted from our **Calendar** table.  This gives us a straightforward way to align sales data with monthly periods for seasonality analysis.

Next, we will build a histogram of sales by month.  To make the visualisation clearer, let’s set the axis type to categorical and sort the values in ascending order by **MonthNumber**.  This allows us to see sales distributed across months.

At first glance, the chart highlights a noticeable decline in the fourth quarter.  However, when we look closer at the underlying dates, we discover that in 2018 there were no sales records for Q4.  As a result, the seasonal pattern appears distorted.

This reminds us to be cautious.  Whilst the visual may look convincing, missing data may mislead the analysis.  Seasonality must always be checked against actual transaction dates to ensure accuracy.

![](<Base64-Image-Removed>)

Next time, to make our analysis more flexible, we will add slicers to the report.  

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/training)
.  If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
. 

*   [Log in](https://sumproduct.com/blog/power-bi-blog-seasonality-analysis-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-seasonality-analysis-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-seasonality-analysis-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-seasonality-analysis-part-1/#0)

[](https://sumproduct.com/blog/power-bi-blog-seasonality-analysis-part-1/#0 "close")

top