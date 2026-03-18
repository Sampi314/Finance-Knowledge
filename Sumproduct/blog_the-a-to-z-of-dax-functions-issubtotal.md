# The A to Z of DAX Functions – ISSUBTOTAL

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-issubtotal/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISSUBTOTAL

*   February 3, 2026

The A to Z of DAX Functions – ISSUBTOTAL
========================================

__In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **ISSUBTOTAL**.__

**_**_The_** _**ISSUBTOTAL**_ **_function_**_**

![](<Base64-Image-Removed>)

**ISSUBTOTAL** is a function that checks whether the current row in a column is a subtotal or a grand total:

****ISSUBTOTAL(ColumnName)****

There is only one \[1\] argument in this function:

*   **ColumnName**: this is the column you want to test.

Here are a few remarks about the **ISSUBTOTAL** function:

*   it returns TRUE for both subtotal and grand total rows, otherwise, it returns FALSE
*   this function is for use (_i.e._ functional) only within a **SUMMARIZE** function
*   the column that **ISSUBTOTAL** creates must be named before entering in the corresponding **ISSUBTOTAL** function.

To test, a base table, consisting of sales from cities of two \[2\] Australian states, was created:

![](<Base64-Image-Removed>)

**SalesData =**

**DATATABLE(**

    **“State”, STRING,**

    **“City”, STRING,**

    **“Total Sales”, INTEGER,**

    **{**

        **{“NSW”, “Sydney”, 100},**

        **{“NSW”, “Newcastle”, 50},**

        **{“VIC”, “Melbourne”, 120},**

        **{“VIC”, “Geelong”, 30}**

    **}**

**)**

A second table that adds subtotals and subtotal check columns using the **ISSUBTOTAL** function, was also created:

![](<Base64-Image-Removed>)

**SalesWithSubtotals =**

**SUMMARIZE(**

    **SalesData,**

    **ROLLUPGROUP(SalesData\[State\], SalesData\[City\]),**

    **“Total Sales”, SUM(SalesData\[Total Sales\]),**

    **“Is State Subtotal?”, IF(ISSUBTOTAL(SalesData\[State\]), “TRUE”, “FALSE”),**

    **“Is City Subtotal?”, IF(ISSUBTOTAL(SalesData\[City\]), “TRUE”, “FALSE”)**

**)**

There are a few things to note with this formula:

*   the **ISSUBTOTAL** function was put within a **SUMMARIZE** function
*   **ROLLUPGROUP** was used to create subtotal rows for both state and city contexts
*   the subtotal check columns were named before use of **ISSUBTOTAL**.

The results show that **ISSUBTOTAL** has correctly identified summary rows for both city and state.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-issubtotal/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-issubtotal/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-issubtotal/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-issubtotal/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-issubtotal/#0 "close")

top