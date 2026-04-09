# Power Pivot Principles: Power Pivot Principle: Introducing the RELATEDTABLE function

**Source:** https://sumproduct.com/blog/power-pivot-principles-power-pivot-principle-introducing-the-relatedtable-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Power Pivot Principle: Introducing the RELATEDTABLE function

*   June 1, 2020

Power Pivot Principles: Power Pivot Principle: Introducing the RELATEDTABLE function
====================================================================================

Power Pivot Principles: Power Pivot Principle: Introducing the RELATEDTABLE function
====================================================================================

2 June 2020

_Welcome back to the Power Pivot Principles blog. This week, we consider the RELATEDTABLE function in DAX._

The **RELATEDTABLE** function evaluates a table expression in a context, modified by the given filters and returns a table of values. This function is a shortcut for the [**CALCULATETABLE**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-calculatetable-function)
 function, but with no logical expression. It follows the syntax:

**RELATEDTABLE(tableName)**

Now, let’s dive in with an example. We have data regarding the daily sales of a few product types in a supermarket throughout 2019:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-208-1.jpg)

In another worksheet, we have the data for the price per unit of these products:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-199-1.jpg)

We want to calculate the revenue for each product in this year, equal to

**Quantity Sold x Average Price per Unit.**

Therefore, in the second table, we need to get total quantity sold for each product in 2019, in order to calculate this revenue.

We will load the data to Power Pivot Data Model, by highlighting the whole data, going to the ‘Power Pivot’ tab on the Ribbon and clicking ‘Add to Data Model’. We rename the tables as ‘**Sales Quantity**‘ and ‘**Product Price**‘ respectively. We also add a [Calendar Table](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-a-calendar-table)
, which will later be used in our PivotTable.

We need to define the relationships between our data tables. By switching to ‘Diagram View’ in the Home tab, we drag the ‘**Product Type**‘ field to connect two tables, ‘**Sales Quantity**‘ and ‘**Product Price**‘, simultaneously, as well as the ‘**Date**‘ field for ‘**Sales Quantity**‘ and ‘**Calendar**‘:

![](<Base64-Image-Removed>)

Then, switch back to the ‘Data view’, and in the ‘**Product Price**‘ table, we apply the **RELATEDTABLE** function to get the ‘**Quantity Sold**‘…but we get an error!

![](<Base64-Image-Removed>)

The reason is, we can’t take a table, then drop it into this cell in our data model. We need to get a count, or sum, in here. As we want to know the total number of units sold in the year, we will use the **SUMX** function to cover the **RELATEDTABLE** function thus:

**\=SUMX(RELATEDTABLE(‘Sales Quantity’),\[Quantity Sold\])**

The **RELATEDTABLE** function will return the ‘**Sales Quantity**‘ table, then the **SUMX** function will add up related data in the ‘**Quantity Sold’** column:

![](<Base64-Image-Removed>)

Now that we have both ‘**Average Price per Unit**‘ and ‘**Quantity Sold**‘ in one table, we can calculate **Revenue**:

**\=’Product Price'\[Average Price per Unit\]\*’Product Price'\[Quantity Sold\]**

![](<Base64-Image-Removed>)

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-power-pivot-principle-introducing-the-relatedtable-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-power-pivot-principle-introducing-the-relatedtable-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-power-pivot-principle-introducing-the-relatedtable-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-power-pivot-principle-introducing-the-relatedtable-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-power-pivot-principle-introducing-the-relatedtable-function/#0 "close")

top