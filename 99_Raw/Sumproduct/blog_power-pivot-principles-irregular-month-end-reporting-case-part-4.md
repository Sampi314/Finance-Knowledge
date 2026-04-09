# Power Pivot Principles: Irregular Month-End Reporting Case – Part 4

**Source:** https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-4/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Irregular Month-End Reporting Case – Part 4

*   September 7, 2020

Power Pivot Principles: Irregular Month-End Reporting Case – Part 4
===================================================================

Power Pivot Principles: Irregular Month-End Reporting Case – Part 4
===================================================================

8 September 2020

_Welcome back to the Power Pivot Principles blog. This week, we still continue with our irregular month-end reporting case study._

To recap, we have a sales data set of four product lines in a supermarket over four years. This supermarket has a rule for month-end reporting, which is the reporting end of month day is the final Thursday of a month, regardless of whether it matches the end of the calendar month.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-149-1.jpg)

By using the **EOMONTH** and the **WEEKDAY** functions to [compare the logic](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-irregular-month-end-reporting-case-part-1)
 or by using ‘[Fill Up’ calculations](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-irregular-month-end-reporting-case-part-2)
 , we worked out the ‘**Reporting End of Month**‘. From there, in [Part 3](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-irregular-month-end-report-part-3)
, we created a ‘**Current Month Sales**‘ measure and a PivotTable, displaying sales by month ending on the final Thursday of the month.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-137-1.jpg)

This week, we want to compare the ‘**Current Month Sales**‘ with the sales of previous month, next month and of the same month last year.

To get the ‘**Previous Month Sales**‘, we will use the **[PREVIOUSMONTH](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-previousday-month-quarter-year-functions)
** function:

**\=CALCULATE(SUM(\[Total Sales\]), PREVIOUSMONTH(‘Calendar'\[Date\]))**

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-128-1.jpg)

When we drag the ‘**Previous Month Sales**‘ measure into the PivotTable, it appears as below, which doesn’t seem right. This is due to a discrepancy between the Calendar Date and the ‘**Reporting End of Month**‘ defined by the rule of the final Thursday of the month. There is also a _(blank)_ in the Row Labels, because there are a few days in the end of December 2019 that do not belong to any reporting month.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-113-1.jpg)

To fix this, first, we go back to the Power Pivot window, in the Diagram View, adjust the relationship between the two tables by connecting the ‘**Reporting End of Month**‘ in the **Sales** table to the **Date** field in the **Calendar** table:

![](<Base64-Image-Removed>)

Then, we adjust the ‘**Current Month Sales**‘ measure, from

**CALCULATE(SUM(Sales\[Total Sales\]),** **‘Calendar’****\[Reporting End of Month\])**

to

**CALCULATE(SUM(Sales\[Total Sales\]),Sales\[Reporting End of Month\])**

![](<Base64-Image-Removed>)

In the PivotTable, we replace the fields in the Rows to **Year** and **Month** (rather than ‘**Reporting Year**‘ and ‘**Reporting Month**‘). The PivotTable now behaves itself:

![](<Base64-Image-Removed>)

Now, we want to see the ‘**Next Month Sales**‘ where data is available, by using the **NEXTDAY**, **NEXTMONTH**, **NEXTQUARTER** and **NEXTYEAR** functions. The **NEXTDAY** function returns a table that contains a column of all dates representing the next day, based on the first date specified in the **dates** column in the current context. The **NEXTMONTH** and **NEXTQUARTER** functions also return a table that contains a column of all dates from the next month or quarter respectively, whilst **NEXTYEAR** returns data in the next year.

These functions follow the syntax:

**NEXTDAY(dates)**

**NEXTMONTH(dates)**

**NEXTQUARTER(dates)**

**NEXTYEAR(dates)**

One thing we should note is that these functions return all dates from the next day to the first date in the input parameter. For example, if the first date in the **dates** argument refers to August 10, 2020, the **NEXTDAY** function returns all dates equal to August 11, 2020. The **dates** argument can be a reference to a date / time column, a table expression that returns a single column of date / time values or a Boolean expression that defines a single-column table of date / time values.

We will create the ‘**Next Month Sales**‘ measure by the formula:

**\=CALCULATE(SUM(\[Total Sales\]),NEXTMONTH(‘Calendar'\[Date\]))**

![](<Base64-Image-Removed>)

Drag the ‘**Next Month Sales’** measure to Values, our PivotTable looks like the one below:

![](<Base64-Image-Removed>)

Next, we want to compare the ‘**Current Month Sales**‘ with the Sales of same month last year, which can be done by using the **[SAMEPERIODLASTYEAR](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-sameperiodlastyear-function)
** function:

**Same Period Last Year Sales =CALCULATE(SUM(\[Total Sales\]),SAMEPERIODLASTYEAR(‘Calendar'\[Date\]))**

![](<Base64-Image-Removed>)

To compare the Sales changes over year, we will create a ‘**YOY% Sales Changes**‘ using the **[DIVIDE](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-divide-function)
** function:

**\=DIVIDE(Sum(\[Total Sales\])-\[Same Period Last Year Sales\],Sales\[Same Period Last Year Sales\])**

![](<Base64-Image-Removed>)

If we drag the two measures to the PivotTable and we can view the ‘**Current Month Sales**‘ in comparison to sales of different time periods:

![](<Base64-Image-Removed>)

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-4/#0)

[](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-4/#0 "close")

top