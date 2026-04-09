# The A to Z of DAX Functions – CROSSJOIN

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-crossjoin/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CROSSJOIN

*   November 29, 2022

The A to Z of DAX Functions – CROSSJOIN
=======================================

Power Pivot Principles: The A to Z of DAX Functions – CROSSJOIN
===============================================================

29 November 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **CROSSJOIN**._

**_The CROSSJOIN function_**

The DAX function **CROSSJOIN** returns a table that contains the Cartesian product of all rows from all tables in the arguments. Translating this into English, imagine you had two sets, **A** {x, y, z} and **B** {1, 2, 3}. Named after the French philosopher and mathematician René Descartes, the Cartesian product, **A x B**, would be the set of all ordered pairs from (x, 1) to (z, 3), _viz_.

![](https://sumproduct.com/wp-content/uploads/2025/06/9e14e2043906cab4ce72def31ff68c5d.jpg)

This can be very useful when we want to analyse all possible combinations from two or more sets – or in this case, tables.

Therefore, **CROSSJOIN** is a powerful DAX function that joins the contents from different tables to obtain desired lookup parameters. The columns in the new table are all the columns in all the argument tables. It has the following syntax:

**CROSSJOIN(table, table\[, table\]…)**

where:

*   **table** is any DAX expression that returns a **table** of data.

This function returns a table that contains the Cartesian product of all rows from all tables in the arguments. It should be noted that column names from table arguments must all be different in all tables or an error is returned.

Let’s look at one simple example. Consider the following two tables:

![](https://sumproduct.com/wp-content/uploads/2025/06/0be56c229829d2849f6d59acf0f2e0a6.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/06/ac34a8235bb7f875899e1940a6a71914.jpg)

The first table contains the value of year (2019, 2020 and 2021) and the second table contains the value from 1 to 12.

The result we want is something like (not fully displayed):

![](<Base64-Image-Removed>)

In total, there would be 36 rows, since there are three years, 12 months and 3 x 12 = 36. The **Year** table is cross joined with **Month** table with each individual value.

In order to cross join two tables above, we can evaluate the measure in DAX editor:

![](<Base64-Image-Removed>)

The expression here is:

**Evaluate  
CROSSJOIN(MonthTable, YearTable)**

The DAX editor evaluates the syntax and generate the result table directly in the worksheet and the result would be:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-crossjoin/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-crossjoin/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-crossjoin/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-crossjoin/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-crossjoin/#0 "close")

top