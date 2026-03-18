# Power Pivot Principles: Introducing the Function PARALLELPERIOD

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-parallelperiod/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the Function PARALLELPERIOD

*   February 10, 2020

Power Pivot Principles: Introducing the Function PARALLELPERIOD
===============================================================

Power Pivot Principles: Introducing the Function PARALLELPERIOD
===============================================================

11 February 2020

_Welcome back to the Power Pivot Principles blog. This week, we are going to learn a new DAX function, PARALLELPERIOD._

In our previous blogs, we have introduced different methods to calculate the value for last month/year. This week we are going to introduce another new DAX function, **PARALLELPERIOD**, to calculate previous period value. The DAX function **PARALLELPERIOD** returns a parallel period of dates by the given set of dates and a specified interval. It has following syntax to operate:

**PARALLELPERIOD ( <Dates>, <NumberOfIntervals>, <Interval> )**

where:

*   <**Dates**\> is the name of a column containing dates or a one column table containing dates
*   <**NumberOfIntervals**\> is the number of the intervals
*   <**Interval**\> is the parameter from one of: **MONTH**, **QUARTER**, **YEAR**.

Let’s look at one simple example. Consider the following data table (not displayed in full):

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-277.jpg)

It is a simple table containing the column of Date and Sales Amount. We want to create a Pivot Table to compare current month sales to previous month. In order to get the measure required, we import the **Sales** table into the PowerPivot interface.

We also create a **Calendar** table as described in previous [blog](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-a-calendar-table)
 and the result would be:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-280-1.jpg)

The **Calendar** table and **Sales** table have the following one-to-many relationship on the attribute **Date**.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-264-1.jpg)

We write the **PARALLELPERIOD** measure as:

![](<Base64-Image-Removed>)

**\=CALCULATE(SUM(Sales\[Sales Amount\]),PARALLELPERIOD(‘Calendar'\[Date\],-1,MONTH))**

This measure calculates the total of sales amount in **Sales** table with the filter defined as the **PARALLELPERIOD** expression, which filters the **Date** context to the previous month.

We export the result to a PivotTable with **Date** as the row and **Sum of Sales Amount** and **PreviousMonthSales** as the columns:

![](<Base64-Image-Removed>)

As indicated by the table above, the **PreviousMonthSales** shows the amount for the previous month for different years.

It should be noted that **PARALLELPERIOD** differs from **[DATEADD](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-dateadd-function)
** in that **PARALLELPERIOD** always returns full periods at the given granularity level instead of the partial periods that **DATEADD** returns. For example, if you have a selection of dates that starts at March 10 and finishes at March 21 of the same year, and you want to shift that selection forward by one month then the **PARALLELPERIOD** function will return all dates from the next month (April 1 to April 30) whereas, if **DATEADD** is used instead, the result will include only dates from April 10 to April 21.

It should also be noted that this DAX function is not supported for use in what is known as DirectQuery mode.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-parallelperiod/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-parallelperiod/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-parallelperiod/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-parallelperiod/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-parallelperiod/#0 "close")

top