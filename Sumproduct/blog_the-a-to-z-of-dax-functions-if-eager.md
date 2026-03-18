# The A to Z of DAX Functions – IF.EAGER

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-if-eager/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – IF.EAGER

*   April 2, 2024

The A to Z of DAX Functions – IF.EAGER
======================================

Power Pivot Principles: The A to Z of DAX Functions – IF.EAGER
==============================================================

2 April 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **IF**_._**EAGER**__._

**_The_** _**IF.EAGER function**_

![](https://sumproduct.com/wp-content/uploads/2025/06/ae7c49ff09efb8de8a3df8da4b7317bd.jpg)

The **IF.EAGER** function is one of the logical functions and is similar to the **[IF](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-if)
** function. It returns different values based upon whether a specified condition is TRUE or FALSE. It employs the following syntax:

**IF.EAGER (logical\_test,  
value\_if\_true \[, value\_if\_false\])**

This function has three \[3\] arguments:

*   **logical\_test**: this is required and represents any expression that evaluates to either TRUE or FALSE
*   **value\_if\_true**:this is required and the value to return if the condition is true
*   **value\_if\_false**: optional argument that’s returned if the logical test is FALSE. If omitted, BLANK is returned.

The key differences between the DAX functions **IF** and **IF.EAGER** lie in their evaluation plans and the impact upon performance:

*   the**IF.EAGER** function uses an eager execution plan, where both **value\_if\_true** and **value\_if\_false** expressions are always evaluated, regardless of the **logical\_test** outcome. This might be preferable when:
    *   both branches need to be calculated regardless of the condition (_e.g_. side effects within expressions)
    *   the performance difference between the branches is minimal or unknown.

**IF** uses a lazy evaluation plan, where only the expression associated with the TRUE result is evaluated (potentially improving performance if one branch is much more expensive than the other). Furthermore, it is generally preferred for performance optimisation when one branch is significantly more expensive than the other. Lazy evaluation avoids unnecessary calculations.  
It has the same execution plan as the following DAX expression:

**VAR \_value\_if\_true =  
<value\_if\_true>**

**VAR \_value\_if\_false =  
<value\_if\_false>**

**RETURN**

**IF (<logical\_test>,  
\_value\_if\_true, \_value\_if\_false)**

How it works:

*   the **IF.EAGER** function evaluates the condition
*   if the **logical\_test** is TRUE, it returns **value\_if\_true**
*   if the **logical\_test** is FALSE, it returns **value\_if\_false** (or **BLANK** if not specified).

It should be noted that:

*   it can return a variant data type if **value\_if\_true** and**value\_if\_false** have different data types. Attempts to return a single data type if both are numeric (implicit conversion applies)
*   in scenarios where one branch evaluation is significantly more expensive than the other, **IF** might be more efficient due to lazy evaluation
*   **IF.EAGER** function can be useful when both branch evaluations are necessary regardless of the condition, or when side effects within the expressions are desired
*   you should be mindful of potential performance implications if both branches involve complex calculations or database interactions
*   **IF.EAGER** function is not compatible with Excel and is currently only compatible with Power BI.

Let’s consider the following table call **tbl\_financials**:

![](<Base64-Image-Removed>)

We may create a DAX to determine whether the **Units Sold** were higher than the total **Average Units Sold**:

**Evaluation =**

 **IF.EAGER(\[Units Sold\] > \[Average Units  \
Sold\]**

 **, “** **Sales Above  
Average”**

 **, “** **Sales Below  
Average”**

**)**

![](<Base64-Image-Removed>)

In the **DAX** statement, we summarised the **IF** result values to the new **Evaluation** column:

![](<Base64-Image-Removed>)

Do remember that the **IF.EAGER** has the same functional behaviour as the [**IF**](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-if)
 function, but performance may differ due to differences in execution plans.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-if-eager/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-if-eager/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-if-eager/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-if-eager/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-if-eager/#0 "close")

top