# The A to Z of DAX Functions – DATESBETWEEN

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datesbetween/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – DATESBETWEEN

*   February 7, 2023

The A to Z of DAX Functions – DATESBETWEEN
==========================================

Power Pivot Principles: The A to Z of DAX Functions – DATESBETWEEN
==================================================================

7 February 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **DATESBETWEEN**__._

**_The_** _**DATESBETWEEN**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/1c92a18fc0040fd13ba979e4879b8e73.jpg)

The **DATESBETWEEN** function is one of the time intelligence functions. This function returns a table with a single column of the dates between two \[2\] given dates. It has the following syntax.

**DATESBETWEEN(Dates,  
StartDate, EndDate)**

There are three \[3\] arguments in this function:

*   **Dates**: this argument is required, and is a column reference containing dates
*   **StartDate**: this a date expression
*   **EndDate**: this is also a date expression.

Because the **DATESBETWEEN** functionis a time intelligence function, there are few key notes you should consider when using it (or any time intelligence function):

*   all dates need to be present for the years required. All the days in this span, from January 1 to December 31, must be included in the **Date** table. The **Date** table must include all dates from commencement to the last day of a fiscal year if the report solely refers to fiscal years
*   a column with a DateTime or Date data type and unique values is required. Typically, this column is known as **Date**. Although it is common practice, this is not necessary when defining associations with other tables. However, the ‘mark as Date Table’ feature should relate to the **Date** column, which must have distinct values
*   the **Date** table must be designated as a date table in the model in case the relationship between the **Date** table and any other table is not dependent upon the **Date**.

Consider this example: we have the following **Date** table that contains dates from 1 January 2008 to 31 December 2008:

![](https://sumproduct.com/wp-content/uploads/2025/06/30a161893a813d0d73f3c826d1c4bde5.jpg)

We can write the following expression in DAX to return the dates contained between two \[2\] specified dates (25 August 2020 and 31 August 2020):

**EVALUATE**

    **VAR StartDate = DATE  
( 2020, 08, 25 )**

    **VAR EndDate   = DATE ( 2020, 08, 31 )**

**RETURN**

    **DATESBETWEEN  
( Date\_Table\[Date\], StartDate, EndDate )**

![](<Base64-Image-Removed>)

This will return the following:

![](<Base64-Image-Removed>)

It should be noted that:

*   if **StartDate** is BLANK, then **StartDate** will be the earliest value present in the **Dates** column
*   if **EndDate** is BLANK, then **EndDate** will be the latest value present in the **Dates** column
*   both **StartDate** and **EndDate** are inclusive, meaning that both **StartDate** and **EndDate** will be included in the resulting table (providing that these dates exist in the **Dates** column)
*   the returned table can only contain dates that are present in the **Dates** column
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datesbetween/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datesbetween/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datesbetween/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datesbetween/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datesbetween/#0 "close")

top