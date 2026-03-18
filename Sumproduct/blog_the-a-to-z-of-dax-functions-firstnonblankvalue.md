# The A to Z of DAX Functions – FIRSTNONBLANKVALUE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstnonblankvalue/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – FIRSTNONBLANKVALUE

*   December 12, 2023

The A to Z of DAX Functions – FIRSTNONBLANKVALUE
================================================

Power Pivot Principles: The A to Z of DAX Functions – FIRSTNONBLANKVALUE
========================================================================

12 December 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **FIRSTNONBLANKVALUE**._

**_The_** _**FIRSTNONBLANKVALUE**_ **_function_**

The _**FIRSTNONBLANKVALUE**_ functionis one of the time intelligence functions which returns the first value in the column that the expression has a non-blank value. It has the following syntax:

_**FIRSTNONBLANKVALUE**_**(column, expression)**

*   **column**: this is required which is a column expression. The **column** argument may be either of the following:
    *   a reference to any column
    *   a table with a single column
*   **expression**: this is also required, and is an expression evaluated for each value of **column**.

It should be further noted that:

*   the difference between the **[FIRSTNONBLANK](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-firstnonblank)
    **function and the **FIRSTNONBLANKVALUE** function is that the **column** argument of **FIRSTNONBLANKVALUE** is addedto thefilter context for the evaluation of **expression**
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Since the _**FIRSTNONBLANKVALUE**_ function is a time intelligence function, it should be noted that:

*   all dates need to be present for the years required. All the days in this span, from January 1 to December 31, must be included in the **Date** table. The date table must include all dates from commencement to the last day of a fiscal year if the report solely refers to fiscal years
*   a column with a DateTime or Date data type and unique values is required. Typically, this column is known as **Date**. Although it is common practice, this is not necessary when defining associations with other tables. However, the ‘mark as Date Table’ feature should relate to the **Date** column, which must have distinct values
*   the **Date** table must be designated as a date table in the model in case the relationship between the **Date** table and any other table is not dependent on the **Date**.

Let’s consider the following example, where we have the following **TB\_Sales** table in Power BI:

![](<Base64-Image-Removed>)

We will write a measure to get the first non-blank value for a selected date:

**FIRSTNONBLANKVALUE\_Example  
\= FIRSTNONBLANKVALUE(TB\_Sales\[OrderDate\],SUM(TB\_Sales\[SalesAmount\]))**

![](<Base64-Image-Removed>)

If we drag and drop this measure and then create a slicer for selecting a date range, we may obtain something similar to the following:

![](<Base64-Image-Removed>)

It will show the first non-blank value for the selected date range.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstnonblankvalue/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstnonblankvalue/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstnonblankvalue/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstnonblankvalue/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstnonblankvalue/#0 "close")

top