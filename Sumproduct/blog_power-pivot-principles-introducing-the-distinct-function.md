# Power Pivot Principles: Introducing the DISTINCT function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-distinct-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the DISTINCT function

*   June 8, 2020

Power Pivot Principles: Introducing the DISTINCT function
=========================================================

Power Pivot Principles: Introducing the DISTINCT function
=========================================================

9 June 2020

_Welcome back to the Power Pivot Principles blog. This week, we will talk about the DISTINCT function in DAX._

The **DISTINCT** function returns a one-column table that contains the distinct values from the specified column. In other words, duplicate values are removed and only unique values are returned. This function cannot be used to return values into a cell or column on a worksheet, rather, it is nested within a formula, to get a list of distinct values that can be passed to another function and then counted, summed, or used for other operations. A while ago, we wrote about the [**DISTINCTCOUNT**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-function-distinctcount)
 function, so you could argue that this is another distinction!

The **DISTINCT** function follows the syntax:

**DISTINCT(column)**

Let’s look at an example. Here, we have sales data from 2016 to 2019, for a number of stores, where they track sales by ‘**Product Key**‘ and ‘**Customer Key**‘:

![](<Base64-Image-Removed>)

We want to know the number of unique customers each store gains over time.

To do this, we will load the data to the Power Pivot Data Model, by highlighting the whole data, going to the ‘Power Pivot’ tab on the Ribbon and clicking ‘Add to Data Model’. We rename the tables as **Sales**. We also add a [Calendar Table](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-a-calendar-table)
, which will later be used in our PivotTable, and name it **Calendar**. We will also define the relationships between **Sales** and **Calendar** by switching to ‘Diagram View’ in the Home tab and dragging to connect **Date** between the two tables.

To count the number of unique customers, we will create a measure ‘**Unique Customer**‘ and use the **DISTINCT** function as follows:

**\=COUNTROWS(DISTINCT(Sales\[Customer Key\]))**

In here, we cannot bring the list of values that **DISTINCT** returns directly into a column: there will be a thousand of them. We just want to know a whole number! Therefore, we need to nest the **DISTINCT** function in the **COUNTROWS** function. The measure returns a result of 18,484 unique customers, which makes sense, but is not the end result that we want…

![](<Base64-Image-Removed>)

Going back to Excel, we create a PivotTable in a new worksheet. Here, we drag **Year** from the **Calendar** table into the Rows field, ‘**Store Key’** into the Columns field, and ‘**Unique Customer’** into the Values field. Thus, we have the PivotTable showing the number of unique customers by stores and by years:

![](<Base64-Image-Removed>)

Just to double check, the Grand Total of Grand Totals is 18,484 customers, which coincides with the number generated from our Data Model’s measure!

![](<Base64-Image-Removed>)

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-distinct-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-distinct-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-distinct-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-distinct-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-distinct-function/#0 "close")

top