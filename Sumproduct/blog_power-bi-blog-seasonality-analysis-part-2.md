# Power BI Blog Seasonality Analysis Part 2

**Source:** https://sumproduct.com/blog/power-bi-blog-seasonality-analysis-part-2/

---

[Home](https://sumproduct.com/)

\> Power BI Blog Seasonality Analysis Part 2

*   October 23, 2025

Power BI Blog Seasonality Analysis Part 2
=========================================

_Welcome back to this week’s edition of the Power BI blog series._  _This week, we add slicers to the report._

Seasonality plays a key role in business, especially retail, shaping when and how customers buy products.  By analysing sales patterns across months and years, retailers can identify which items are seasonal, such as coats in winter or sandals in summer, and which remain steady throughout the year.  Let’s use a simple fashion retail dataset to explore how to detect seasonality and apply these insights to smarter business decisions. The Power BI Desktop file, both for practice and with solutions, may be downloaded [here](https://sumproduct0.sharepoint.com/:f:/s/SumProductTeam/EqlMpZqagmZGsQ-pVSHO2K8Bc_gXQfFomt68Z9c_QX4ZKA?e=VX2z9n)
.

It’s a straightforward fashion retail dataset containing several dimensional tables such as **dCustomers**, **dProducts** and **dStores**, along with a fact table called **fSales**.  The **Calendar** table is generated automatically based upon the earliest and latest transaction dates in **fSales**.  In addition, the model includes a **Sales Plan** table, which provides projected sales by store, month and year.

The task here will be to understand what seasonality means and how to identify it in product sales.  Seasonality refers to the influence of recurring annual or monthly fluctuations on sales.  The stronger these fluctuations, the more seasonal a product is considered; its sales vary noticeably from month to month or season to season.  To analyse this, we’ll make small adjustments to our calendar, focusing on months rather than the full year-month format, since seasonality is typically observed at the monthly level.

[Last week](https://sumproduct.com/blog/power-bi-blog-seasonality-analysis-part-1/)
, we created  a column that extracts the month from each date in the calendar, which allows us to focus purely on month-based seasonality. 

![](<Base64-Image-Removed>)

Next, we built a histogram of sales by month. 

![](<Base64-Image-Removed>)

At first glance, the chart appeared to highlight a noticeable decline in the fourth quarter.  However, in 2018 there were no sales records for Q4.  As a result, the seasonal pattern appears distorted. Whilst the visual may look convincing, missing data may mislead the analysis.  Seasonality must always be checked against actual transaction dates to ensure accuracy.

This time, to make our analysis more flexible, we will add slicers to the report. 

Using the **Year** column from the **Calenda**r table, we can quickly filter sales by specific years.  This way, we may check whether seasonal patterns repeat consistently across different years or if certain anomalies (like missing data in 2018) are affecting the results.

![](<Base64-Image-Removed>)

Before moving further, it’s important to ask:

*   where does this data come from? 
*   who collects it?
*   how is it collected? 

Data quality directly impacts seasonality analysis.  To keep our experiment clean, let’s focus only on 2016 and 2017, since these are complete years with full transaction data.  Immediately, we see a quite different picture compared to the incomplete years.  This confirms that seasonality should always be measured on closed, full periods to avoid distortion.

Now, how do we define seasonality in formula terms?  Seasonality may be expressed as the deviation of sales in a particular month from the average monthly sales of the year.  To calculate this, we first need the average monthly sales for the year.  Let’s create a measure for that:

> **Sales Monthly Average =  
> AVERAGEX(DISTINCT(‘Calendar'\[MonthNumbers\]), \[Sales Revenue\])**

For each month, we calculate total sales and then compare it with the average monthly sales.  By adding our measure to a table visual, we can now see both values side by side-monthly sales and the annual monthly average:

![](<Base64-Image-Removed>)

When calculating the **Sales Monthly Average**, clearly, we need to remove the current filter context.  Otherwise, the calculation would only consider the selected month instead of the entire year.  To achieve this, we use the **CALCULATE** function together with **ALL**, which resets the context and ensures the average is based on all months of the selected year. 

> **Average Monthly Sales = CALCULATE(AVERAGEX(DISTINCT(‘Calendar'\[MonthNumbers\]), \[Sales Revenue\]),ALL(‘Calendar'\[MonthNumbers\]))**

With this adjustment, the average monthly sales line becomes stable and consistent, giving us a reliable baseline for analysing fluctuations in individual months.

![](<Base64-Image-Removed>)

Now that we have the average monthly sales,  next time we will measure how each month deviates from this baseline. 

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/training)
.  If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
. 

*   [Log in](https://sumproduct.com/blog/power-bi-blog-seasonality-analysis-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-seasonality-analysis-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-seasonality-analysis-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-seasonality-analysis-part-2/#0)

[](https://sumproduct.com/blog/power-bi-blog-seasonality-analysis-part-2/#0 "close")

top