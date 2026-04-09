# The A to Z of DAX Functions – FIRSTNONBLANK

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstnonblank/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – FIRSTNONBLANK

*   December 5, 2023

The A to Z of DAX Functions – FIRSTNONBLANK
===========================================

Power Pivot Principles: The A to Z of DAX Functions – FIRSTNONBLANK
===================================================================

5 December 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **FIRSTNONBLANK**._

**_The_** _**FIRSTNONBLANK**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/bee5b9988f70c2f28de6874854803933.jpg)

The _**FIRSTNONBLANK**_ functionis one of the time intelligence functions, it returns the first value in the column where the expression has a non-blank value. It has the following syntax:

_**FIRSTNONBLANK**_**(column, expression)**

*   **column**: this is required and is a column expression. The **column** argument can be any of the following:
    *   a reference to any column
    *   a table with a single column
*   **expression**: this is also required and is an expression evaluated for blanks for each value of column.

It should be noted that:

*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Since the _**FIRSTNONBLANK**_ function is a time intelligence function, it should be noted that:

*   all dates need to be present for the years required. It is suggested that all the days in this span, from January 1 to December 31, must be included in the **Date** table. The date table must include all dates from commencement to the last day of a fiscal year if the report solely refers to fiscal years
*   a column with a DateTime or Date data type and unique values is required. Typically, this column is known as **Date**. Although it is common practice, this is not necessary when defining associations with other tables. However, the ‘mark as Date Table’ feature should relate to the **Date** column, which must have distinct values
*   the **Date** table must be designated as a date table in the model in case the relationship between the **Date** table and any other table is not dependent on the **Date**.

Let’s consider the following example, where we have the **Sales** table:

![](<Base64-Image-Removed>)

Firstly, we will create a simple measure called **Sales\_Amount** to be our expression:

![](<Base64-Image-Removed>)

**Sales\_Amount  
\= SUM(Sales\[Sales Amount\])**

Then, we will create our **FIRSTNONBLANK** measure to grab the first date we make a sale in the **Date** column of the **Sales** table:

![](<Base64-Image-Removed>)

**FIRSTNONBLANK\_Example\_1  
\= FIRSTNONBLANK(Sales\[Date\], \[Sales\_Amount\])**

We then put it in the ‘Values’ section of the PivotTable Fields pane, _viz._

![](<Base64-Image-Removed>)

Since in our data we make the first sale on 3rd January 2020, the measure will display 3/01/2020.

Let’s consider another example:

![](<Base64-Image-Removed>)

**FIRSTNONBLANK\_Example\_2  
\= FIRSTNONBLANK(Sales\[Sales Amount\], \[Sales Amount\])**

This measure identifies the lowest value in the **Sales Amount** column as the first value, hence it displays 90,000:

![](<Base64-Image-Removed>)

Alternatively, we can put zero \[0\] in the **expression** argument to get the same result here:

![](<Base64-Image-Removed>)

**FIRSTNONBLANK\_Example\_3  
\= FIRSTNONBLANK(Sales\[Sales Amount\], 0)**

This will produce the following result:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstnonblank/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstnonblank/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstnonblank/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstnonblank/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstnonblank/#0 "close")

top