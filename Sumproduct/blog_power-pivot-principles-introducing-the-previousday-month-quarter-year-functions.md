# Power Pivot Principles: Introducing the PREVIOUSDAY / MONTH / QUARTER / YEAR Functions

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-previousday-month-quarter-year-functions/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the PREVIOUSDAY / MONTH / QUARTER / YEAR Functions

*   July 6, 2020

Power Pivot Principles: Introducing the PREVIOUSDAY / MONTH / QUARTER / YEAR Functions
======================================================================================

Power Pivot Principles: Introducing the PREVIOUSDAY / MONTH / QUARTER / YEAR Functions
======================================================================================

7 July 2020

_Welcome back to the Power Pivot Principles blog. This week, we will talk about the group of PREVIOUSDAY / MONTH / QUARTER / YEAR functions in DAX._

Previously, we have talked about the [**SAMEPERIODLASTYEAR**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-sameperiodlastyear-function)
 function, which returns a table that contains a column of dates shifted one year back in time from the dates referred to in the specified dates column, given the current context. What if we want a value of one day back, one month or one quarter back? It’s also good to know about the **PREVIOUSDAY**, **PREVIOUSMONTH**, **PREVIOUSQUARTER** and even the **PREVIOUSYEAR** functions.

With the same logic, the **PREVIOUSDAY** function returns a table that contains a column of all dates representing the previous day (funnily enough), in the current context. The **PREVIOUSMONTH** and **PREVIOUSQUARTER** functions also return a table that contains a column of all dates from the previous month or quarter respectively, based upon the first date in the dates column, whilst **PREVIOUSYEAR** returns data from the previous year.

These functions follow the syntax:

**PREVIOUSDAY(dates)**

**PREVIOUSMONTH(dates)**

**PREVIOUSQUARTER(dates)**

**PREVIOUSYEAR(dates)**

One thing we should note is that this function determines the first date in the input parameter, and then returns all dates corresponding to the day previous to that first date. For example, if the first date in the **dates** argument refers to June 10, 2020; this function returns all dates equal to June 9, 2020.

The **dates** argument may be a reference to a date / time column, a table expression that returns a single column of a date / time values, or a Boolean expression that defines a single-column table of date / time values.

Let’s consider an example. Below is \[truncated\] daily sales data from 2016 to 2019 of a store:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-187-1.jpg)

We want to compare sales by each previous date, month, quarter and year.

To do this, we will load the data to the Power Pivot Data Model, by highlighting the whole data, going to the ‘Power Pivot’ tab on the Ribbon and clicking ‘Add to Data Model’. We then rename the tables as **Sales**. We also add a [Calendar Table](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-a-calendar-table)
, which will later be used in our PivotTable, and name it **Calendar**. We will also define the relationships between **Sales** and **Calendar** by switching to ‘Diagram View’ in the Home tab and dragging the **Date** field to connect the two tables.

Going back to Excel, we create a PivotTable in a new worksheet. Here, we drag **Date Hierarchy** from the **Calendar** table into Rows field and **Sales** into the Values field. Thus, we have a PivotTable showing **Sales** over time:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-176-1.jpg)

Now, we navigate to the ‘Power Pivot’ tab on the Ribbon, click **Measures -> ‘New Measure…’**, in order to create a ‘**Previous Day Sales**‘ measure:

**\=CALCULATE(SUM(\[Sales Amount\]),PREVIOUSDAY(‘Calendar'\[Date\]))**

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-172-1.jpg)

We click OK and come back to our PivotTable and drag the ‘**Previous Day Sales**‘ to the Values field. We now have a ‘**Previous Day Sales**‘ column to compare with **Sales**. Please note that the Subtotal of the months in **Sales** column sums all sales in a particular month, while in the ‘**Previous Day Sales**‘ column it shows the sales of the last previous date (_e.g._ $15 in in August 2016 is actually sales of date 31/7/2016):

![](<Base64-Image-Removed>)

Similarly, we will create measure for ‘**Previous Month Sales**‘:

**\=CALCULATE(SUM(\[Sales Amount\]),PREVIOUSMONTH(‘Calendar'\[Date\]))**

The ‘**Previous Month Sales**‘ reflects sales of the previous month:

![](<Base64-Image-Removed>)

For **‘Previous Quarter Sales’**:

**\=CALCULATE(SUM(\[Sales Amount\]),PREVIOUSQUARTER(‘Calendar'\[Date\]))**

![](<Base64-Image-Removed>)

And for **‘Previous Year Sales’**:

**\=CALCULATE(SUM(\[Sales Amount\]),PREVIOUSYEAR(‘Calendar'\[Date\]))**

![](<Base64-Image-Removed>)

To take a step further, we want to see the sales growth by creating a measure ‘**%YoY Change**‘:

**\=DIVIDE(SUM(Sales\[Sales Amount\])-\[Previous Year Sales\],\[Previous Year Sales\])**

![](<Base64-Image-Removed>)

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-previousday-month-quarter-year-functions/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-previousday-month-quarter-year-functions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-previousday-month-quarter-year-functions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-previousday-month-quarter-year-functions/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-previousday-month-quarter-year-functions/#0 "close")

top