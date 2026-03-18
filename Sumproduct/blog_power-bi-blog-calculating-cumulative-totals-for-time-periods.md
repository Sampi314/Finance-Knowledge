# Power BI Blog: Calculating Cumulative Totals for Time Periods

**Source:** https://sumproduct.com/blog/power-bi-blog-calculating-cumulative-totals-for-time-periods/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Calculating Cumulative Totals for Time Periods

*   September 23, 2020

Power BI Blog: Calculating Cumulative Totals for Time Periods
=============================================================

Power BI Blog: Calculating Cumulative Totals for Time Periods
=============================================================

24 September 2020

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at how to calculate cumulative totals for time periods in Power BI._

It should be noted that calculating cumulative totals in structured data usually requires an index key (for a Power Query example, please refer to [One Route to a Running Total](https://sumproduct.com/blog/power-query-one-route-to-a-running-total/)
 for more information). However, you can use dates as your index key – which is the idea here.

The first step in calculating a cumulative total for our data is to create a measure that will sum the total sales:

**Total Sales = SUM(Sales\[SalesAmount\])**

It is important to note that before we calculate any measure that involves dates, you should first create a calendar table. If you do not know what a calendar table is, please read this Power Pivot [blog](https://sumproduct.com/thought/power-pivot-principles-creating-a-calendar-table/)
 for more information on calendar tables. You can also find more information on how to create a dynamic calendar table in Power BI [here](https://sumproduct.com/blog/power-bi-blog-creating-a-dynamic-calendar-table/)
.

Plotting this measure on a Table and Clustered Column visualisation we get the following results:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-138-1.jpg)

We have covered how to calculate the cumulative total in our Power Pivot blog series, which you can read about [here](https://sumproduct.com/blog/power-pivot-principles-cumulative-totals-with-the-earlier-function/)
, in that example we used the **EARLIER** function. In this case we can adopt a different approach that does not utilise the **EARLIER** function and write the following measure instead:

**Cumulative Total =**

**CALCULATE(\[Total Sales\],**

    **FILTER(ALL(‘Calendar Table’),**

        **‘Calendar Table'\[Date\] <= MAX(‘Calendar Table'\[Date\])**

        **)**

    **)**

In this measure we use the **ALL** function in the **FILTER** table to remove the filter context. This allows the **CALCULATE** function to look to the earliest date in the dataset and sum the cumulative total sales up to the current date. The current date is calculated with the ‘**MAX**(‘Calendar Table'\[Date\])’ segment of the measure.

Plotting the ‘**Cumulative Total**‘ measure onto our visualisations, we get the following results:

![](<Base64-Image-Removed>)

There you have it, a simple way to calculate the cumulative total for any sales metrics based upon dates.

That’s it for this week. Come back next week for more on Power BI!

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-calculating-cumulative-totals-for-time-periods/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-calculating-cumulative-totals-for-time-periods/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-calculating-cumulative-totals-for-time-periods/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-calculating-cumulative-totals-for-time-periods/#0)

[](https://sumproduct.com/blog/power-bi-blog-calculating-cumulative-totals-for-time-periods/#0 "close")

top