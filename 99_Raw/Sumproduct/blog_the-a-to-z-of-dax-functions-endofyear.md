# The A to Z of DAX Functions – ENDOFYEAR

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-endofyear/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ENDOFYEAR

*   August 15, 2023

The A to Z of DAX Functions – ENDOFYEAR
=======================================

Power Pivot Principles: The A to Z of DAX Functions – ENDOFYEAR
===============================================================

15 August 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **ENDOFYEAR**._

**_The_** _**ENDOFYEAR**_ **_function_**

![](<Base64-Image-Removed>)

The **ENDOFYEAR** function is one of the time intelligence functions where it returns the end-of-year date. It employs the following syntax:

**ENDOFYEAR(dates\[, year\_end\_date\])**

Unlike its counterparts, the **[ENDOFMONTH](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-endofmonth)
**function and the **[ENDOFQUARTER](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-endofquarter)
**function, the **ENDOFYEAR** function contains two \[2\] arguments:

*   **dates:** this is required which represents a column that contains dates. This can be any of the following:
    *   a reference to a date / time column
    *   a table expression that returns a single column of date / time values
    *   a BOOLEAN expression that defines a single-column table of date / time values
*   **year\_end\_date:** this is an optional, literal string that defines the year-end date. If omitted, the default is 31 December. It may be specified using **\=ENDOFYEAR(Calendar\[Date\], “30 June 1976”)**, for example.

It should be further noted that:

*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Please consider the following example where we have a **Dates** table with a date range from 1 May 2020 to 1 January 2025:

![](<Base64-Image-Removed>)

We can create a simple measure to get the end of the year date for each date in the **Start Date** column:

![](<Base64-Image-Removed>)

Then we can create a PivotTable to view our results:

![](<Base64-Image-Removed>)

All the dates return to the last date of the year for the respective year. However, there is something odd in the PivotTable which is 1 January 2025 is supposed to return 31 December 2025 but in this case, it does not.

Therefore, we should note the following when dealing with the time intelligence function:

*   all dates need to be present for the years required. All the days in this span, from January 1 to December 31, must be included in the **Date** table. The date table must include all dates from commencement to the last day of a fiscal year if the report solely refers to fiscal years
*   a column with a DateTime or Date data type and unique values is required. Typically, this column is known as **Date**. Although it is common practice, this is not necessary when defining associations with other tables. However, the ‘mark as Date Table’ feature should relate to the **Date** column, which must have distinct values
*   the **Date** table must be designated as a date table in the model in case the relationship between the **Date** table and any other table is not dependent on the **Date**.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-endofyear/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-endofyear/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-endofyear/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-endofyear/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-endofyear/#0 "close")

top