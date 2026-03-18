# The A to Z of DAX Functions – DISTINCT(table)

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-distincttable/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – DISTINCT(table)

*   May 16, 2023

The A to Z of DAX Functions – DISTINCT(table)
=============================================

Power Pivot Principles: The A to Z of DAX Functions – DISTINCT(table)
=====================================================================

16 May 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **DISTINCT (table)**._

**_The DISTINCT (_**_**table**_**_) function_**

The **DISTINCT(**_**table)**_ function is one of the table manipulations functions that returns a table containing only the distinct rows. This means that the duplicate rows are removed, and only unique rows are returned. It has the following syntax:

**DISTINCT(table)**

It has just the one \[1\] argument:

*   **table**: this is required and represents the **table** from which unique rows are to be returned or an expression that returns a table.

Here are a few remarks about this function:

*   the current filter context has an impact on the results of the **DISTINCT(**_**table)**_ function
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules
*   there is another version of the **DISTINCT(**_**table)**_ function which is the **[DISTINCT(column)](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-distinct-column)
    **function. The latter function removes the duplicate value for a column or expression that resulted in column.

For example, we can create a simple table using the **[DATATABLE](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-datatable)
**function in DAX:

![](<Base64-Image-Removed>)

It should return the follow table in Excel:

![](<Base64-Image-Removed>)

Then we can use the **DISTINCT(table)** function to wrap around the DAX code to remove duplicate row for this table:

![](<Base64-Image-Removed>)

Hence, the code above will result in the following table:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-distincttable/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-distincttable/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-distincttable/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-distincttable/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-distincttable/#0 "close")

top