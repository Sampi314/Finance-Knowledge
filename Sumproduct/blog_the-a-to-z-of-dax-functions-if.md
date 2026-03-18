# The A to Z of DAX Functions – IF

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-if/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – IF

*   March 26, 2024

The A to Z of DAX Functions – IF
================================

Power Pivot Principles: The A to Z of DAX Functions – IF
========================================================

26 March 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **IF**._

**_The_** _**IF**_ **_function_**

![](<Base64-Image-Removed>)

The **IF** function is one of the logical functions, returning different values based upon whether a specified condition is TRUE or FALSE. It employs the following syntax:

**IF(logical\_test, value\_if\_true \[,  \
value\_if\_false\])**

This function has three \[3\] arguments:

*   **logical\_test**: this is required and represents any logical expression that evaluates to either TRUE or FALSE
*   **value\_if\_true**: this is required and represents the value to return if the condition is true
*   **value\_if\_false**: this is an optional argument that is returned if the logical test is FALSE. If omitted, **BLANK** is returned.

How it works:

*   the **IF** function evaluates the condition
*   if the condition is TRUE, it returns **value\_if\_true**
*   if the condition is FALSE, it returns **value\_if\_false** (or **BLANK** if not specified).

It should be noted that:

*   the **IF** function can handle different data types for **value\_if\_true** and **value\_if\_false**, but it will try to return a single data type if possible
*   for multiple conditional branches, consider using the **SWITCH** function for cleaner code
*   the **IF** function is often used with other DAX functions like [**AND**](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-and/)
    , **OR**, **NOT**, and **ISERROR** for complex logic.

Let’s consider the following Table call **tbl\_grades**:

![](<Base64-Image-Removed>)

We may create DAX to determine whether the students completed their final examinations with a score of five \[5\] or higher:

**EVALUATE**

**  
ADDCOLUMNS (tbl\_grades,”Final Result”,**

               **IF(tbl\_grades\[Grade\]>  
5,”Passed”, “Failed”))**

![](<Base64-Image-Removed>)

In the [**EVALUATE**](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-evaluate)
 statement, we construct the following:

*   the [**ADDCOLUMNS**](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-addcolumns/)
     function is used to add a new column named **Final Result**
*   the first argument in this function is the table **tbl\_grades** to which you want to add a new column
*   the second argument is a list of expressions that define the new column to be added. Each expression has two \[2\] parts:
    *   the name of the new column (_e.g_. **Final Result**)
    *   the **IF** function that evaluates whether the Grade column is bigger than five \[5\]
        *   if the result is TRUE the result will display “Passed”
        *   if the result is FALSE the result will display “Failed”.

In the [**EVALUATE**](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-evaluate)
 statement, we summarised the **IF** result values in the new **Final Result** column:

![](<Base64-Image-Removed>)

Important notes:

*   the **IF** function can be used in calculated columns, measures and table filters
*   it is important to consider the data types of the values you’re working with to ensure reliable results
*   indenting nested **IF** functions may improve readability, but you should consider alternative feedback where possible.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-if/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-if/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-if/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-if/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-if/#0 "close")

top