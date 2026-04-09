# The A to Z of DAX Functions – FIRSTDATE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstdate/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – FIRSTDATE

*   November 28, 2023

The A to Z of DAX Functions – FIRSTDATE
=======================================

Power Pivot Principles: The A to Z of DAX Functions – FIRSTDATE
===============================================================

28 November 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **FIRSTDATE**._

**_The_** _**FIRSTDATE**_ **_function_**

![](<Base64-Image-Removed>)

The **FIRSTDATE** functionis one of the time intelligence functions, it returns the first non-blank date. It has the following syntax:

**FIRSTDATE(dates)**

*   **dates**: this is required which represents a column that contains dates. This can be any of the following:
    *   a reference to a date / time column
    *   a table expression that returns a single column of date / time values
    *   a Boolean expression that defines a single-column table of date / time values.

It should be further noted:

*   the **FIRSTDATE** and **LASTDATE** functions will return the same day if the currentcontext contains a single value
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Since the **FIRSTDATE** function is a time intelligence function, it should be noted that:

*   all dates need to be present for the years required. It is suggested that all the days in this span, from January 1 to December 31, must be included in the **Date**table. The date table must include all dates from commencement to the last day of a fiscal year if the report solely refers to fiscal years
*   a column / field with a DateTime or Date data type and unique values is required. Typically, this column is known as **Date**. Although it is common practice, this is not necessary when defining associations with other tables. However, the ‘mark as Date Table’ feature should relate to the **Date** column, which must have distinct values
*   the **Date** table must be designated as a date table in the model in case the relationship between the **Date** table and any other table is not dependent on the **Date**.

Let’s consider the following example. We have the following **Sales** table with 60,398 rows of data:

![](<Base64-Image-Removed>)

We will create a PivotTable that grabs the first **OrderDate** of every **ProductKey**. Therefore, we will create the following measure:

![](<Base64-Image-Removed>)

**FIRSTDATE\_Example  
\= FIRSTDATE(Sales\[OrderDate\])**

Then, we insert a PivotTable from the data model and drag the newly created measure and **ProductKey** into the corresponding PivotTable Fields:

![](<Base64-Image-Removed>)

This will return the following PivotTable:

![](<Base64-Image-Removed>)

Since the database data started on the 18th July 2013, the first date for all **ProductKey** values here will be displayed in column **B** as shown.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstdate/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstdate/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstdate/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstdate/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-firstdate/#0 "close")

top