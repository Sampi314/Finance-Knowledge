# The A to Z of DAX Functions – DATESQTD

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datesqtd/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – DATESQTD

*   February 28, 2023

The A to Z of DAX Functions – DATESQTD
======================================

Power Pivot Principles: The A to Z of DAX Functions – DATESQTD
==============================================================

28 February 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **DATESQTD**._

**_The_** _**DATESQTD**_ **_function_**

The **DATESQTD** functionis one of the time intelligence functions. Like the **[DATESMTD](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-datesmtd)
**function, the **DATESQTD** function return a set of dates in the quarter up to the last date visible in the filter context. It operates under the following syntax:

**DATESQTD(dates)**

There is one \[1\] argument for the **DATESQTD** function:

*   **dates:** this argument is required, and it is the name of a column or one column table containing dates. This can be any of the following:
    *   a reference to a date / time column
    *   a table expression that returns a single column of date / time values
    *   a BOOLEAN expression that defines a single-column table of date / time values.

The resulting table includes only dates that exist within the **dates** argument.

Since the **DATESQTD** is a time intelligence function, there are few key notes you should consider when using it (or any time intelligence function):

*   all dates need to be present for the years required. All the days in this span, from January 1 to December 31, must be included in the **Date** table. The date table must include all dates from commencement to the last day of a fiscal year if the report solely refers to fiscal years
*   a column with a DateTime or Date data type and unique values is required. Typically, this column is known as **Date**. Although it is common practice, this is not necessary when defining associations with other tables. However, the ‘mark as Date Table’ feature should relate to the **Date** column, which must have distinct values
*   the **Date** table must be designated as a date table in the model in case the relationship between the **Date** table and any other table is not dependent upon the **Date**.

Consider the following example: we have a table named **Date\_Table** that contains dates ranging from 1 January 2020 to 15 May 2021:

![](<Base64-Image-Removed>)

Using the **DATESQTD** functionon this tableas follows will yield a table containing all of the days of the latest quarter within the data:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

As the latest date within the data was 15 May 2021, this resulting table contains the dates of the quarter starting April 2021 up to the final date defined.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datesqtd/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datesqtd/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datesqtd/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datesqtd/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datesqtd/#0 "close")

top