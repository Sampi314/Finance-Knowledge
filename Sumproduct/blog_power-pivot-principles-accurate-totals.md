# Power Pivot Principles: Accurate Totals

**Source:** https://sumproduct.com/blog/power-pivot-principles-accurate-totals/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Accurate Totals

*   May 4, 2020

Power Pivot Principles: Accurate Totals
=======================================

Power Pivot Principles: Accurate Totals
=======================================

5 May 2020

_Welcome back to the Power Pivot Principles blog. This week, we are going to use DAX measure to obtain an accurate total._

When using DAX measures to obtain total amounts, the expression may sometimes be wrong with incorrect calculations produced. However, DAX expressions, when written properly, can be very useful. Let’s have a look at one simple example.

Suppose we have the following **Sales** table (not displayed in full):

![](<Base64-Image-Removed>)

We load this table into Power Pivot and add a **Calendar** table, starting from 1 Jan 2020 to 31 Mar 2020. The two tables have the following relationship:

![](<Base64-Image-Removed>)

Firstly, we add a calculated column in the Power Pivot interface using the following formula:

![](<Base64-Image-Removed>)

**\=IF(Sales\[Sales\]>30,1,0)**

If we export the data as PivotTable based on the fields **Date**, **Sales** and **Higher Sales**, the result would be (not displayed in full):

![](<Base64-Image-Removed>)

According to the result, if the sales for individual day is greater than 30, then the column returns one (1), otherwise zero (0). The result could be replicated by a DAX expression as well. We can use the expression:

![](<Base64-Image-Removed>)

We use **SUMX** to evaluate the **Sales** table with the filter on sales amount. With this new measure, the result would be:

![](<Base64-Image-Removed>)

The result is same as calculated column. However, if we want to calculate if the month has any sales that are greater than 30, the result would be incorrect:

![](<Base64-Image-Removed>)

Obviously, the higher sales for January should be one (1), not 12. In order to get the correct result, we need to revise the DAX expression to the following:

![](<Base64-Image-Removed>)

In the DAX expression, we transform the month in **Calendar** table using **VALUES** function to return the unique month value as a table expression. Then, the table is evaluated with **SUMX** with filter of sales amount. The result table would be:

![](<Base64-Image-Removed>)

In this case, we can see that the value for each month is correctly calculated.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-accurate-totals/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-accurate-totals/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-accurate-totals/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-accurate-totals/#0)

[](https://sumproduct.com/blog/power-pivot-principles-accurate-totals/#0 "close")

top