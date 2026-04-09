# Power Pivot Principles: Introducing the SUMMARIZE Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-summarize-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the SUMMARIZE Function

*   October 21, 2019

Power Pivot Principles: Introducing the SUMMARIZE Function
==========================================================

Power Pivot Principles: Introducing the SUMMARIZE Function
==========================================================

22 October 2019

_Welcome back to the Power Pivot Principles blog. This week, we are going to look at the SUMMARIZE function._

The **SUMMARIZE** function returns a summary table for the requested totals over a set of groups. For example, we can use this function to summarise the sales for a specific year and month and return a summary table.

Consider the data table shown below (not displayed in full):

![](<Base64-Image-Removed>)

This data table contains the sales amount for a specific date. We want to summarise the total sales based on a specific year and month by using **SUMMARIZE** function.

The **SUMMARIZE** function uses the following syntax to operate:

**SUMMARIZE(<table>, <groupBy\_columnName>, \[<groupBy\_columnName>\]…\[<name>, <expression>\]…)**

*   The **<table>** parameter can be table reference or any DAX expression that returns a table of data
*   The <**groupBy\_columnName**\> parameter is optional. It indicates the qualified name of an existing column to be used to create summary groups
*   The <**name**\> parameter is the name given to a total or summarised column, enclosed in double quotes
*   The <**expression**\> parameter is any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row / context).

In this case, we create a measure, **tableSummary**, as shown below:

![](<Base64-Image-Removed>)

We use a nested function in this case. The **SUMMARIZE** function returns a table, which evaluates the sum of sales based on the attribute of **Year** and **Month**. Since it returns a table, we need to use another function to turn it into a scalar value. In this case, we use **COUNTROWS** to obtain the number of rows for the table calculated.

In order to obtain the result table, we import the table from existing connections, as shown below:

![](<Base64-Image-Removed>)

Then, we use the feature of **Edit DAX** in table attribute to input the formula as shown below:

![](<Base64-Image-Removed>)

We use expression **Evaluate** to obtain the table result from the expression below and the result table would be:

![](<Base64-Image-Removed>)

The result shows that **Monthly Sales** are calculated base on the attributes **Year** and **Month**.

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-summarize-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-summarize-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-summarize-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-summarize-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-summarize-function/#0 "close")

top