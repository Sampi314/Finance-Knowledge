# The A to Z of DAX Functions – ISINSCOPE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isinscope/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISINSCOPE

*   November 11, 2025

The A to Z of DAX Functions – ISINSCOPE
=======================================

____In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **_**ISINSCOPE**_**.____

**_**_**_The_** _**_**ISINSCOPE**_**_ **_function_**_**_**

![](https://sumproduct.com/wp-content/uploads/2025/10/image-194.png)

The **ISINSCOPE** function is one of the information functions that returns TRUE when the specified column is the current level in a hierarchy of levels:

> ****ISINSCOPE(columnName)****

There is one \[1\] main argument in this function:

*   **columnName**: this is the name of an existing column, using standard DAX syntax.  It cannot be an expression.

It helps identify the level of aggregation or grouping within a visual’s hierarchy.  It is often used in conjunction with conditional logic (_e.g_. **IF** statements) to modify and / or measure behaviour based upon the current context.

A common use case is to control the display of totals or subtotals, allowing for different calculations or blank values at different levels of a hierarchy.  It can also be used to calculate percentages over a parent level within a hierarchy.

It is often confused with **HASONEVALUE**.  Whilst **ISINSCOPE** and **HASONEVALUE** may both be used to detect single values in a column, their underlying mechanisms differ:

*   **ISINSCOPE** specifically relates to whether a column is part of the grouping context
*   **HASONEVALUE** checks for the presence of a single distinct value in the current filter context.

**ISINSCOPE** can return TRUE even if **HASONEVALUE** returns FALSE in certain scenarios, particularly with **SUMMARIZECOLUMNS** and empty intersections.

Here are a few remarks about the **ISINSCOPE** function:

*   it is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Let’s consider the following table called **Products**:

![](https://sumproduct.com/wp-content/uploads/2025/10/image-195.png)

We will write this simple code in DAX query view:

**EVALUATE**

**SUMMARIZECOLUMNS(**

 **Products\[Brand\], Products\[Qty\],**

 **“Is In Scope 1”, ISINSCOPE(Products\[Brand\]),**

 **“Is In Scope 2”, ISINSCOPE(Products\[Product\])**

**)**

It will return us wil the following table:

![](https://sumproduct.com/wp-content/uploads/2025/10/image-196.png)

In the **SUMMARIZECOLUMNS** function, we include the **Brand** and **Qty** columns, whilst excluding the **Product** column.  Hence, the **Is** **In** **Scope** **1** field return TRUE but **Is** **In** **Scope** **2** returns FALSE.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isinscope/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isinscope/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isinscope/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isinscope/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isinscope/#0 "close")

top