# Power Pivot Principles: Finding the Top N Values in a Dataset

**Source:** https://sumproduct.com/blog/power-pivot-principles-finding-the-top-n-values-in-a-dataset/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Finding the Top N Values in a Dataset

*   April 20, 2020

Power Pivot Principles: Finding the Top N Values in a Dataset
=============================================================

Power Pivot Principles: Finding the Top N Values in a Dataset
=============================================================

21 April 2020

_Welcome back to the Power Pivot Principles blog. This week, we are going to learn a method of finding the top N value in a dataset._

In business cases, one important metric in sales performance analysis is to understand which customer groups or customer orders have contributed most to the company. There are several DAX functions and methods could help us to determine the amount. The DAX function, **TOPN**, is one such example. This function returns the top **N** rows of the specified table. It uses the following syntax to operate

**TOPN (n\_value, table, orderBy\_expression, \[order\[, orderBy\_expression, \[order\]\]…\]))**

where:

*   **n\_value** represents the number of rows to return. It is any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row / context)
*   **table** represents any DAX expression that returns a table of data from where to extract the top **N** rows
*   **orderBy\_expression** represents any DAX expression where the result value is used to sort the table, and it is evaluated for each row of table
*   **order** indicates an optional value that specifies how to sort **orderBy\_expression** values, ascending or descending.

Let’s look at a simple example. Suppose we have following two tables, the **Product** table and **Sales** table (the **Sales** table is not displayed in full):

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

They have the following relationship (one-to-many relationship based on the **ProductKey** field):

![](<Base64-Image-Removed>)

Next, suppose we want to obtain the top sales value (_i.e._ “top 1 value”) in the **Sales** table. We may write the DAX syntax as following:

![](<Base64-Image-Removed>)

**\=CALCULATE(SUM(Sales\[Sum of Sales\]),TOPN(1,Sales,Sales\[Sum of Sales\],DESC))**

We calculate the sum of sales and apply the filter by using the **TOPN** function. In the **TOPN** function, we specify the top one (1) row to be returned in descending order. Then, we export the result as a PivotTable and choose the **ProductKey**, **Product Name** and **Top 1 Sales** as fields. The result would be:

![](<Base64-Image-Removed>)

In this scenario, we can see the top one (1) sale for each product. This result can be confirmed further by the raw data below:

![](<Base64-Image-Removed>)

We may implement another measure which calculates the top five (5) sales values in same way.

![](<Base64-Image-Removed>)

**\=CALCULATE(SUM(Sales\[Sum of Sales\]),TOPN(5,Sales,Sales\[Sum of Sales\],DESC))**

The resulting PivotTable would be:

![](<Base64-Image-Removed>)

Let’s compare the result in the PivotTable with the raw data:

![](<Base64-Image-Removed>)

We can see that for product 1, the total of the top five (5) records is 351 (allowing for roundings), which is the same result shown in the PivotTable above. The measure ‘**Top 5 Sales**‘ summarises the amount of the first five records in descending order.

Finally, we may write another measure which calculates the top three (3) sales values. This time, we want to create a chart to identify the trend for different top **N** measures.

![](<Base64-Image-Removed>)

**\=CALCULATE(SUM(Sales\[Sum of Sales\]),TOPN(3,Sales,Sales\[Sum of Sales\],DESC))**

Then, we may create the following PivotChart:

![](<Base64-Image-Removed>)

We list the top **N** values according to different product names. Thus, we can see different growth rates for each product.

  
That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-finding-the-top-n-values-in-a-dataset/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-finding-the-top-n-values-in-a-dataset/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-finding-the-top-n-values-in-a-dataset/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-finding-the-top-n-values-in-a-dataset/#0)

[](https://sumproduct.com/blog/power-pivot-principles-finding-the-top-n-values-in-a-dataset/#0 "close")

top