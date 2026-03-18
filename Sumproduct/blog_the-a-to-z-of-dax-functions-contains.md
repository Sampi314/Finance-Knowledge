# The A to Z of DAX Functions – CONTAINS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-contains/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CONTAINS

*   June 28, 2022

The A to Z of DAX Functions – CONTAINS
======================================

Power Pivot Principles: The A to Z of DAX Functions – CONTAINS
==============================================================

28 June 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **CONTAINS**._

**_The CONTAINS function_**

Do you know what **CONTAINS** contains? This function returns TRUE if values for all referred columns exist (concurrently); otherwise, the function returns FALSE.

The **CONTAINS** function employs the following syntax to operate:

**CONTAINS(table, columnname1, value1\[, columnname2,  \
value2, …\])**

*   **table:** this is required. This represents any DAX expression that returns a **table** of data
*   **columnname1, columnname2, …:** the first **columnname** is required; the rest are optional. This is the name of an existing column (field) using standard DAX syntax. It cannot be an expression
*   **value1, value2, …:** again, the first **value** is required, the rest are optional. This is any DAX expression that returns a single scalar value that is to be sought in **columnname**. The expression is to be evaluated exactly once and before it is passed to the argument list.

It should be further noted that:

*   the arguments **columnname** and **value** must come in pairs; otherwise, an error is returned
*   **columnname** must belong to the specified **table**, or to a table that is related to **table**
*   if **columnname** refers to a column in a related table then it must be fully qualified; otherwise, an error is returned. It is probably safest to fully qualify in any case
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Consider the following example, using the Table **Data**:

![](<Base64-Image-Removed>)

The following DAX function

**\=CONTAINS(Data,  
Data\[Function\], “Sum”, Data\[Business Driver\], “Product”)**

![](https://sumproduct.com/wp-content/uploads/2025/06/be8469a40caf316af2b87a31c4406b82.jpg)

will provide the value FALSE:

![](https://sumproduct.com/wp-content/uploads/2025/06/9c5979e548f5e07aaecf7507400f462a.jpg)

This is because although “Sum” is in the **Function** field and “Product” is in the ‘**Business Driver**’ field, they are not in the same row of the Table.

If the Table **Data** were revised so that “Sum” and “Product” are on the same row,

![](https://sumproduct.com/wp-content/uploads/2025/06/3c5c84b6fc3ef6b9092190a6187757a2.jpg)

then the ‘**Contains Example**’measure would be TRUE instead, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/06/6d63f5e6ac7d8be49742e03c85271496.jpg)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/blog/power-pivot-principles)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-contains/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-contains/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-contains/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-contains/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-contains/#0 "close")

top