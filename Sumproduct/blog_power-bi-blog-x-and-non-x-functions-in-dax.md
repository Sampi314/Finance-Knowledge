# Power BI Blog: “X” and “Non-X” functions in DAX

**Source:** https://sumproduct.com/blog/power-bi-blog-x-and-non-x-functions-in-dax/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: “X” and “Non-X” functions in DAX

*   September 29, 2021

Power BI Blog: “X” and “Non-X” functions in DAX
===============================================

Power BI Blog: “X” and “Non-X” functions in DAX
===============================================

30 September 2021

_Welcome back to this week’s edition of the Power BI blog series. This week, we discuss the difference between “X” and “Non-X” functions in DAX._

**DAX** in both PowerPivot and Power BI includes numerous aggregation and statistical functions that are similar to formulas in Excel. Some of them end with an “**X**“. For example:

![](https://sumproduct.com/wp-content/uploads/2025/05/405adaa2ca45a09cad0810919ec98687.jpg)

You may wonder how and when we can apply each of them. It’s simple:

*   **“Non-X” functions:** only use a single column as a parameter. The syntax is as follows:

**\=****_FunctionName_****(column)**

*   **“X” functions:** specify a table, evaluate expressions for each row of that table (_i.e_. each record) and generate a result based on the set of values. The syntax is as follows:

**\=****_FunctionName_****(table, expression)**

Therefore, if you already have a column with a set of values to calculate the result on, you can use “non-**X**” functions. For example:

**Total Sales = SUM(Sales\[Amount\])**

On the other hand, you should use “**X**” functions when you need to create a new set of values based on existing data. For instance:

**Total Profit = SUMX(****Sales,** **Sales\[Revenue\] – Sales\[Cost\])**

You may also use them to apply some conditions before calculating. For example:

**Total Profit of Product 1 = SUMX(****FILTER(Sales,** **Sales\[ProductID\] = 1),** **Sales\[Revenue\] – Sales\[Cost\])**

In this example, the **[SUMX](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-sumx-function)
** function will store the calculated values of each row on a virtual column and then take the **[SUM](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-revisiting-the-sum-function)
** of all rows in that column.

_Check back next week for more Power BI tips and tricks!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-x-and-non-x-functions-in-dax/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-x-and-non-x-functions-in-dax/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-x-and-non-x-functions-in-dax/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-x-and-non-x-functions-in-dax/#0)

[](https://sumproduct.com/blog/power-bi-blog-x-and-non-x-functions-in-dax/#0 "close")

top