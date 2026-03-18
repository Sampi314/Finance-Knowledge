# The A to Z of DAX Functions – LASTNONBLANK

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-lastnonblank/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – LASTNONBLANK

*   March 3, 2026

The A to Z of DAX Functions – LASTNONBLANK
==========================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions.  This week, we look at **LASTNONBLANK**._ 

**_The_** _**LASTNONBLANK**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2026/02/image-164.png)

The _**LASTNONBLANK**_ function is one of the time intelligence functions which returns the last value in the column that the expression has a non-blank value.  It has the following syntax:

_**LASTNONBLANK**_**(column, expression)**

*   **column**: this is required which is a column expression.  The **column** argument can be any of the following
    
    *   a reference to any column
    
    *   a table with a single column
*   **expression**: this is also required which is an expression evaluated for blanks for each value of column.

It should be noted that:

*   this function is typically used to return the last value of a column for which the expression is not blank.  For example, you could get the last value for which there were sales of a product
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Since the _**LASTNONBLANK**_ function is a time intelligence function, it should be noted that:

*   all dates need to be present for the years required.  All the days in this span, from January 1 to December 31, must be included in the **Date** table.  The date table must include all dates from commencement to the last day of a fiscal year if the report solely refers to fiscal years
*   a column with a DateTime or Date data type and unique values is required.  Typically, this column is known as **Date**.  Although it is common practice, this is not necessary when defining associations with other tables.  However, the ‘mark as Date Table’ feature should relate to the **Date** column, which must have distinct values
*   the **Date** table must be designated as a date table in the model in case the relationship between the **Date** table and any other table is not dependent on the **Date.**

Let’s consider the following example, where we have the **Sales** table:

![](<Base64-Image-Removed>)

Firstly, we will create a simple measure call **Sales\_Amount** to be our **expression**:

![](<Base64-Image-Removed>)

**Sales\_Amount = SUM(Sales\[Sales Amount\])**

Then we will create our **LASTNONBLANK** measure to grab the last date we make a sale in the **Date** column of **Sales** table:

![](<Base64-Image-Removed>)

**LASTNONBLANK\_Example\_1 = LASTNONBLANK(Sales\[Date\], \[Sales\_Amount\])**

We then put it in the Values section of the PivotTable Fields:

![](<Base64-Image-Removed>)

In our data, we made the last sales in our dataset on 12th January 2020, hence the measure displays 12/01/2020. 

Let’s consider another example:

![](<Base64-Image-Removed>)

**LASTNONBLANK\_Example\_2 = LASTNONBLANK(Sales\[Sales Amount\], \[Sales Amount\])**

This time the second measure considers the highest value in the **Sales Amount** column as the first value hence it displays 150,000:

![](<Base64-Image-Removed>)

Alternatively, we can put zero \[0\] in the **expression** arguments to get the same results here:

![](<Base64-Image-Removed>)

**LASTNONBLANK\_Example\_3 = LASTNONBLANK(Sales\[Sales Amount\], 0)**

Which will produce the following result:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-lastnonblank/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-lastnonblank/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-lastnonblank/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-lastnonblank/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-lastnonblank/#0 "close")

top