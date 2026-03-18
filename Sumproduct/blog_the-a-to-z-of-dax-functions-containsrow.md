# The A to Z of DAX Functions – CONTAINSROW

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-containsrow/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CONTAINSROW

*   July 5, 2022

The A to Z of DAX Functions – CONTAINSROW
=========================================

Power Pivot Principles: The A to Z of DAX Functions – CONTAINSROW
=================================================================

5 July 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **CONTAINSROW**._

**_The CONTAINSROW function_**

Similar to the **[CONTAINS](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-contains)
**function, **CONTAINSROW** returns TRUE if there is at least one row in a given **table** where all columns have specified values. Where **CONTAINS** requires only certain field(s) to be specified, **CONTAINSROW** requires you to specify the values in order for all fields in the **table**.

The **CONTAINSROW** function employs the following syntax to operate:

**CONTAINSROW(table, value1\[, value2, …\])**

*   **table:** this is required. This represents any DAX expression that returns a **table** of data
*   **value1, value2, …:** the first **value** is required, the rest are optional. This is any DAX expression that returns a single scalar value that is to be sought for each field in the **table**.

It should be further noted that:

*   **CONTAINSROW** and the **IN** operator are functionally equivalent. Many prefer the latter, as it is often regarded as a simpler syntax
*   The syntax for **IN** is as follows:

**scalar expression IN table expression**

**(scalar expression1, scalar expression2, …) IN table expression**

*   The number of **scalar expression** values must match the number of columns in the **table**
*   **NOT IN** is not an operator in DAX. To perform the logical negation of the **IN** operator, put NOT in front of the entire expression, _e.g._

**NOT \[Colour\] IN { “Red”, “Yellow”, “Blue” }**

*   Unlike the equals (**\=**) operator, the **IN** operator and the **CONTAINSROW** function perform strict comparisons. For example, the **BLANK** value does not match zero \[0\].

Consider the following example, using the Table **Data**:

![](https://sumproduct.com/wp-content/uploads/2025/06/55afba2c4ee05bafdb70862ff93dec7a.jpg)

The following DAX function

**\=CONTAINSROW(Data,  
“Sum”, “Product”)**

![](https://sumproduct.com/wp-content/uploads/2025/06/d2a31e7541c9f741b84c1cee28b827ff.jpg)

will provide the value TRUE:

![](https://sumproduct.com/wp-content/uploads/2025/06/9005efaafa4f8a55223dd5dd3b8ea5b2.jpg)

This is because “Sum” is in the first field and “Product” is in the second field for one of the rows of the Table.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/blog/power-pivot-principles)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-containsrow/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-containsrow/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-containsrow/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-containsrow/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-containsrow/#0 "close")

top