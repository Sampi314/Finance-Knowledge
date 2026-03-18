# The A to Z of DAX Functions – EXCEPT

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-except/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – EXCEPT

*   October 3, 2023

The A to Z of DAX Functions – EXCEPT
====================================

Power Pivot Principles: The A to Z of DAX Functions – EXCEPT
============================================================

3 October 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **EXCEPT**._

**_The_** _**EXCEPT**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/eba61ca2c1ce45551518ec74ba64ee02.jpg)

The **EXCEPT** functionis one of the table manipulation functions that returns the rows of one table which do not appear in another table. It employs the following syntax:

**EXCEPT(table\_expression1, table\_expression2)**

It has two \[2\] arguments:

*   **table\_expression1** and **table\_expression2**: these are both required and represent any DAX expressions that return tables.

Some comments regarding the **EXCEPT** function:

*   if a row appears in both tables, it and its duplicate will not appear in the result set
*   if a row appears only in the **table\_expression1**, it and any duplicate will appear in the result set
*   the column name will match the column names in **table\_expression1**
*   regardless of the lineage of the columns in the second table, the returned table has lineage based upon the columns in **table\_expression1**. For instance, the **EXCEPT** function will decrease the rows depending upon the availability of values in the first column of the second table expression and maintain the lineage on base column **C1** if the first column of the first table expression has lineage to the base column **C1** in the model
*   there must be an equal number of columns in each table
*   positioning and data comparison is used to compare objects without using any type of coercion
*   depending upon how the two expressions are used, a certain set of rows will be returned
*   columns from tables associated with **table\_expression1** are absent from the returned table
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

We can write the following DAX code to test out the **EXCEPT** function:

![](<Base64-Image-Removed>)

**EVALUATE  
VAR DaysofWeek    ={“Monday”,”Tuesday”,”Wednesday”,”Thursday”,”Friday”,”Saturday”,”Sunday”}  
VAR  
WeekendDays    ={“Saturday”,”Sunday”}  
VAR  
WorkingDays    =EXCEPT(DaysofWeek, WeekendDays)  
RETURN  
WorkingDays**

This DAX code essentially declares three \[3\] variables where one is **DaysofWeek** which is all the days in the weeks and another is **WeekendDays** which is the Weekend days. The last variable is **WorkingDays** which is the days of the week except for the weekend. Hence, the **EXCEPT** function is used. We will have the following table:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-except/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-except/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-except/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-except/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-except/#0 "close")

top