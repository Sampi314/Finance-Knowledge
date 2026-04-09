# The A to Z of DAX Functions – ADDCOLUMNS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-addcolumns/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ADDCOLUMNS

*   July 20, 2020

The A to Z of DAX Functions – ADDCOLUMNS
========================================

Power Pivot Principles: The A to Z of DAX Functions – ADDCOLUMNS
================================================================

20 July 2020

_In our long-established Power Pivot Principles articles, we are starting a new series on the A to Z of Data Analysis eXpression (DAX) functions. This week we’re building on what we have so far…_

**_The ADDCOLUMNS function_**

The **ADDCOLUMNS** function adds calculated columns to a given table or table expression. It uses the following syntax to operate:

**ADDCOLUMNS(table, name, expression\[, name, expression\]…)**

*   **table** is any DAX expression that returns a table of data
*   **name** is a name given to the column, enclosed in double quotes
*   **expression** is any DAX expression that returns a scalar expression, evaluated for each row of the table.

As an example, consider the following data table (not displayed in full):

![](https://sumproduct.com/wp-content/uploads/2025/06/f32e5a15e2cf9c3e4d2d058458ce054d-6.jpg)

This data table contains the sales amount for a specific date. We also create another calendar table in PowerPivot by using the method introduced [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-a-calendar-table)
:

![](https://sumproduct.com/wp-content/uploads/2025/06/f1140ff857fc3b6f5f97a6a24f4a6fc7-6.jpg)

The two tables may be linked:

![](https://sumproduct.com/wp-content/uploads/2025/06/72aa864d2854c6fefb1083fba0ab5792-4.jpg)

We can create a measure using the **ADDCOLUMNS** function:

![](https://sumproduct.com/wp-content/uploads/2025/06/23912d3b1671861e02bebcd5183f1607-1.jpg)

**ADDCOLUMNS** here incorporates **[SUMMARIZE](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-summarize-function)
**. Here, the calculation takes each combination of **Year** and **Month** as a coordinated filter context and uses the table returned from **SUMMARIZE** as the base for **Monthly Sales** calculation:

![](https://sumproduct.com/wp-content/uploads/2025/06/6f49c288a0d88a66b427eaf4ece923d6-1.jpg)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ _[here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
__._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-addcolumns/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-addcolumns/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-addcolumns/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-addcolumns/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-addcolumns/#0 "close")

top