# The A to Z of DAX Functions – ADDMISSINGITEMS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-addmissingitems/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ADDMISSINGITEMS

*   July 27, 2021

The A to Z of DAX Functions – ADDMISSINGITEMS
=============================================

Power Pivot Principles: The A to Z of DAX Functions – ADDMISSINGITEMS
=====================================================================

27 July 2021

_In our long-established Power Pivot Principles articles, we are starting a new series on the A to Z of Data Analysis eXpression (DAX) functions. This week we look to add back missing items…_

**_The ADDMISSINGITEMS function_**

The **ADDMISSINGITEMS** function adds rows with empty values to a table returned by the DAX function **SUMMARIZECOLUMNS**.

The syntax is given by

**ADDMISSINGITEMS(\[showAll\_columnName\[, showAll\_columnName\[, … \] \] \], table\[, groupBy\_columnName\[, \[filterTable\]\[, groupBy\_columnName\[, \[filterTable\] \[, … \] \] \] \] \] \] )**

Well that looks wonderful! The arguments are as follows:

*   **showAll\_columnName**_(optional)_: a column for which to return items with no data for the measures used; if not specified, all columns are returned
*   **table**: a **SUMMARIZECOLUMNS** table
*   **groupBy\_columnName** _(optional)_: a column to group by in the supplied table argument
*   **filterTable** _(optional)_: a table expression that defines which rows are returned.

This will then return a table with one or more columns.

It should be noted that this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

If this all seems a little confusing, it’s perhaps easier to explain with a simple example. Consider the following **Sales** table in Power BI Desktop:

![](https://sumproduct.com/wp-content/uploads/2025/06/f32e5a15e2cf9c3e4d2d058458ce054d-7.jpg)

This has monthly sales data for the divisions Alpha, Bravo, Charlie and Delta, with Echo and Foxtrot seemingly added as a bit of an afterthought.

If you wanted to formulaically summarise this table’s sales for each division, this could be performed in DAX using the **SUMMARIZECOLUMNS** function. To do this, on the ‘Table tools’ tab, click on ‘New table’

and then in the formula bar enter the following formula:

**Summarised Table =**

**SUMMARIZECOLUMNS(Sales\[Division\],”Total Sales”,SUM(Sales\[Sales\]))**

This will create the following table called **Summarised Table**:

![](https://sumproduct.com/wp-content/uploads/2025/06/72aa864d2854c6fefb1083fba0ab5792-5.jpg)

Note that only date for Alpha, Bravo, Charlie and Delta is incorporated because there is no (_null_) data for Echo or Foxtrot divisions.

If we want to “force” Echo and Bravo’s results onto this **SUMMARIZECOLUMNS** table, we should add another new table and this time use the following formula:

**Full Summarised Table =**

**ADDMISSINGITEMS(**

    **Sales\[Division\],**

    **SUMMARIZECOLUMNS(Sales\[Division\],”Total Sales”,SUM(Sales\[Sales\])**

    **),**

    **Sales\[Division\]**

**)**

Here, **ADDMISSINGITEMS** “wraps” the previously constructed formula. This does exactly what it says on the tin and **ADDSMISSINGITEMS**, in particular, the additional **Division** data from the **Sales** table:

![](<Base64-Image-Removed>)

This can be useful when you need to highlight all elements have been considered.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ _[here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
__._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-addmissingitems/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-addmissingitems/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-addmissingitems/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-addmissingitems/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-addmissingitems/#0 "close")

top