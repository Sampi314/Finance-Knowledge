# Power Pivot Principles: Introducing the ADDCOLUMNS Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-addcolumns-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the ADDCOLUMNS Function

*   December 30, 2019

Power Pivot Principles: Introducing the ADDCOLUMNS Function
===========================================================

Power Pivot Principles: Introducing the ADDCOLUMNS Function
===========================================================

31 December 2019

_Welcome back to the Power Pivot Principles blog. This week, we are going to look at the ADDCOLUMNS function._

We introduced the **SUMMARIZE** function in a previous blog. This function returns a summary table for the requested totals over a set of groups. The **SUMMARIZE** function can add columns with calculated values. This week, we are going to create extend this idea by using the functions **ADDCOLUMNS** and **SUMMARIZE**.

The **ADDCOLUMNS** function adds calculated columns to the given table or table expression. It uses the following syntax to operate:

**ADDCOLUMNS(<table>, <name>, <expression>\[, <name>, <expression>\]…)**

*   The **<table>** is any DAX expression that returns a table of data
*   The **<name>** is a name given to the column, enclosed in double quotes
*   The **<expression>** is any DAX expression that returns a scalar expression, evaluated for each row of the table.

Consider the following data table (not displayed in full):

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-299.jpg)

This data table contains the sales amount for a specific date. We also create another calendar table in PowerPivot by using the method introduced [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-a-calendar-table)
:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-304-1.jpg)

The two tables may be linked:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-264.jpg)

We create the measure using **SUMMARIZE** function with the “extended” column, **Monthly Sales**.

![](<Base64-Image-Removed>)

The formula **SUMMARIZE** above, summarize the table **SalesData** at the **Year** and **Month** level. The value aggregated is the sum of **SalesAmount** and the column name is defined as **Monthly Sales**.

We will evaluate the expression in table attribute **Edit DAX** as introduced [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-summarize-function)
. The result would be (not displayed in full):

![](<Base64-Image-Removed>)

We can achieve a similar result by using the **ADDCOLUMNS** function. The syntax operates as:

![](<Base64-Image-Removed>)

**ADDCOLUMNS** works like **SUMMARIZE**. In the case above, it took each combination of **Year** and **Month** as a coordinated filter context and used the table returned from **SUMMARIZE** as the base for **Monthly Sales** calculation. The result would be the same:

![](<Base64-Image-Removed>)

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-addcolumns-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-addcolumns-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-addcolumns-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-addcolumns-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-addcolumns-function/#0 "close")

top