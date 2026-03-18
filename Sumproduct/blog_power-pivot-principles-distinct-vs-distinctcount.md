# Power Pivot Principles: DISTINCT vs. DISTINCTCOUNT

**Source:** https://sumproduct.com/blog/power-pivot-principles-distinct-vs-distinctcount/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: DISTINCT vs. DISTINCTCOUNT

*   June 15, 2020

Power Pivot Principles: DISTINCT vs. DISTINCTCOUNT
==================================================

Power Pivot Principles: DISTINCT vs. DISTINCTCOUNT
==================================================

16 June 2020

_Welcome back to the Power Pivot Principles blog. This week, we will consider the differences between the DISTINCT and DISTINCTCOUNT functions in DAX._

Last week, we talked about the [**DISTINCT**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-distinct-function)
 function, which returns a one-column table, that contains the distinct values from the specified column. It has the following syntax:

**DISTINCT(column)**

We have also previously written about the [**DISTINCTCOUNT**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-function-distinctcount)
 function, which counts the number of unique values in a column, and has the following syntax:

**DISTINCTCOUNT(column)**

The two functions look similar for both calculations and syntax. However, the key difference between the **DISTINCT** function and **DISTINCTCOUNT** functions lies in how they work.

The **DISTINCTCOUNT** function already has the built-in ‘**COUNT**‘ which is defined by its name. Meanwhile, the **DISTINCT** function cannot be used to return values into a cell or column on a worksheet. Rather, it is nested within a formula, in order to produce a list of distinct values that may be passed to another function, and then counted, summed, or aggregated in other ways for other operations.

Let’s reuse the example. We have sales data from 2016 to 2019 for a number of stores, where they track sales by ‘**Product Key**‘ and ‘**Customer Key**‘:

![](<Base64-Image-Removed>)

We want to know the number of unique customers each store gains over time.

To do this, let’s load the data to the Power Pivot Data Model, by highlighting the whole data, going to the ‘Power Pivot’ tab on the Ribbon and clicking ‘Add to Data Model’. We rename the table as **Sales**. We also add a [Calendar Table](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-a-calendar-table)
, which will later be used in our PivotTable, and imaginatively name it **Calendar**. We will also define the relationships between **Sales** and **Calendar** by switching to ‘Diagram View’ in the Home tab and dragging **Date** to connect to both tables.

We can use two ways to count the number of unique customers:

*   ‘**Unique Customer DISTINCTCOUNT**‘:

**\=DISTINCTCOUNT(Sales\[Customer Key\]))**

*   ‘**Unique Customer DISTINCT**‘:

**\=COUNTROWS(DISTINCT(Sales\[Customer Key\]))**

We may even create something fancy like this:

**\=CALCULATE(COUNTROWS(DISTINCT(Sales\[Customer Key\])),ALL(Sales\[Date\]))**

The measure returns a result of 18,484 unique customers for each of these methods:

![](<Base64-Image-Removed>)

Going back to Excel, let’s create two PivotTables in a new worksheet. Here, we’ll drag **Yea**r from **Calendar** table into the Rows field, ‘**Store Key’** into the Columns field, and both ‘**Unique Customer DISTINCT**‘ and ‘**Unique Customer DISTINCTCOUNT**‘ into the Values field for two similar PivotTables. We have the PivotTables showing the number of unique customers by stores and by years, which are identical:

![](<Base64-Image-Removed>)

In short, [**DISTINCTCOUNT**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-function-distinctcount)
 function is straightforward to count a distinct number, where [**DISTINCT**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-distinct-function)
 function can be nested into a number of aggregation functions in order to return a combined result related to uniqueness.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-distinct-vs-distinctcount/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-distinct-vs-distinctcount/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-distinct-vs-distinctcount/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-distinct-vs-distinctcount/#0)

[](https://sumproduct.com/blog/power-pivot-principles-distinct-vs-distinctcount/#0 "close")

top