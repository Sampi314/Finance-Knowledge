# Power Pivot Principles: Is there anything RELATED?

**Source:** https://sumproduct.com/blog/power-pivot-principles-is-there-anything-related/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Is there anything RELATED?

*   May 18, 2020

Power Pivot Principles: Is there anything RELATED?
==================================================

Power Pivot Principles: Is there anything RELATED?
==================================================

19 May 2020

_Welcome back to the Power Pivot Principles blog. This week, let’s talk about the RELATED function._

The **RELATED** function in DAX returns a single value that is _related_ to the current row, similar to the **LOOKUP** function in Excel. When the **RELATED** function performs a lookup, it examines all values in the specified table regardless of any filters that may have been applied. The **RELATED** function needs a row context; therefore, it may only be used in a calculated column expression and follows the syntax:

**RELATED(<column>)**

The **RELATED** function requires that a relationship exists between the current table and the table with related information. You specify the column that contains the data that you want, and the function follows an existing many-to-one relationship to fetch the value from the specified column in the related table.

For example, we have a data about daily quantity sales of several products in a supermarket over three years as shown below:

![](<Base64-Image-Removed>)

In another worksheet, we have the data for the price per unit of those products:

![](<Base64-Image-Removed>)

To facilitate analysis, we need to figure out the revenue, which equals

**Quantity Sold x Average Price per Unit.**

These two fields, unfortunately, lie in two different places, and we need to bring them into one table.

To do this, first, we will load the data to Power Pivot Data Model, by highlighting the whole data, going to ‘Power Pivot’ tab on the Ribbon and clicking ‘Add to Data Model’. We rename the tables as ‘**Sales Quantity**‘ and ‘**Product Price**‘ respectively. We also add a [Calendar Table](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-a-calendar-table)
, which will later be used in our PivotTable.

We need to define the relationships amongst our data tables. By switching to ‘Diagram View’ in the Home tab, we drag the ‘**Product Type**‘ field to connect two tables, ‘**Sales Quantity**‘ and ‘**Product Price**‘, simultaneously, as well as the ‘**Date**‘ field of ‘**Sales Quantity**‘ and ‘**Calendar**‘:

![](<Base64-Image-Removed>)

Switching back to ‘Data View’, we add a new column, ‘Average Price per Unit’ and define the following **RELATED** function in the formula bar:

**\=RELATED(‘Product Price'\[Average Price per Unit\])**

This will look up the average price per unit in the ‘Product Price’ table to match the ‘Product Type’:

![](<Base64-Image-Removed>)

Now that we have both **Quantity Sold** and **Average Price per Unit**, it is straightforward to calculate **Revenue**:

**\=’Sales Quantity'\[Quantity Sold\]\*’Sales Quantity'\[Average Price per Unit\]**

![](<Base64-Image-Removed>)

With all necessary fields ready, we can create a PivotTable to see **Revenue** by month / year:

![](<Base64-Image-Removed>)

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-is-there-anything-related/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-is-there-anything-related/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-is-there-anything-related/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-is-there-anything-related/#0)

[](https://sumproduct.com/blog/power-pivot-principles-is-there-anything-related/#0 "close")

top