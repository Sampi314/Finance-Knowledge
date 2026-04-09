# The A to Z of DAX Functions – EARLIER

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-earlier/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – EARLIER

*   July 4, 2023

The A to Z of DAX Functions – EARLIER
=====================================

Power Pivot Principles: The A to Z of DAX Functions – EARLIER
=============================================================

4 July 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **EARLIER**._

**_The_** _**EARLIER**_ **_function_**

The **EARLIER** function is one of the filter functions in DAX where it returns the current value of the specific column in an outer evaluation pass of the mentioned column (a nice and clear definition for you!). The **EARLIER** function is quite useful for nested calculations where you want to use a certain value as an input and produce calculation using data from the entire table. The **EARLIER** function is mostly used in the context of calculated columns. It employs a very simple syntax:

**EARLIER(column, \[number\])**

where:

*   **column**: this is required and, represents a column or expression that results in a column
*   **number**: this is optional and, represents a positive number to be outer evaluation pass. The next evaluation level out is represented by one \[1\], two levels out is represented by two \[2\] and so on. When **number** is omitted, it will return the default value of one \[1\].

It should be noted:

*   if there is a row context before the table scan starts, the **EARLIER** function is successful; otherwise, an error is returned
*   the performance of the **EARLIER** function may be slow since, in theory, it may need to execute close to the whole number of rows (in the column) times the same number of operations (depending upon the syntax of the expression). For instance, if the column has 10 rows, then 100 operations may be necessary; if the column contains 100 rows, then close to 10,000 operations may be necessary
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

To illustrate the use of the **EARLIER** function, consider the following example:

![](https://sumproduct.com/wp-content/uploads/2025/06/50cc9ab6eae4bf525aa973992cfa1006.jpg)

Here, we have the following **Sales** table. First, we will create an aggregation measure for **SalesAmount** then we will use this aggregation along with the **EARLIER** function to create a cumulative amount for each date:

![](https://sumproduct.com/wp-content/uploads/2025/06/a8dcb76682113fca488ed94b848bbe9c.jpg)

Next, we move to the Power Pivot data model to create a calculated column with the following DAX code:

![](https://sumproduct.com/wp-content/uploads/2025/06/f1d2bb50a995aa9b8eb9be2785b7294a.jpg)

**EARLIER\_Example:=CALCULATE(\[SalesAmount\],FILTER(Sales,Sales\[OrderDate\]<=EARLIER(Sales\[OrderDate\])))**

This DAX code will return a cumulative **SalesAmount** by date:

![](https://sumproduct.com/wp-content/uploads/2025/06/b7ee63c8ba119a26565c4ace048e1722.jpg)

The following steps describe the method of calculation in more detail.

*   the **EARLIER** function gets the value of **Sales\[OrderDate\]** for the current row in the table
*   in this case, because the process is starting, it is the first row in the table
*   **EARLIER(Sales\[OrderDate\])** evaluates to 1 January 2013, the current row in the outer loop
*   the **FILTER** function now returns a table where all rows have an order date less than 1 January 2013 (which is the current value for **EARLIER**)
*   the **CALCULATE** function then sums the **SalesAmount**
*   the calculated column formula moves to the next row and repeats the above steps
*   these steps are repeated until the end of the table is reached.

The **EARLIER** function will always get the value of the column prior to the current table operation. If you need to get a value from the loop before that, set the second argument to two \[2\].

Assuming you have wrapped your head around this, let’s move on. If we use the same code in the calculated column to create a new measure, we will now get an error message:

![](<Base64-Image-Removed>)

There is a workaround if you want to create a measure instead of calculated column for an **EARLIER** function:

![](<Base64-Image-Removed>)

**\=CALCULATE(**

      **SUM(Sales\[SalesAmount\]),**

      **FILTER(ALL(Sales),**

  **SUMX(FILTER(Sales,EARLIER(Sales\[OrderDate\])<=Sales\[OrderDate\]),Sales\[SalesAmount\])**

      **)**

      **)**

This DAX code help us replicate the same result we have in the previous example using calculated column for our measure. You can create a Pivot Table to view the result of the measure:

![](<Base64-Image-Removed>)

As we can see the result here is identical to the result using the calculated column in Power Pivot.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-earlier/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-earlier/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-earlier/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-earlier/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-earlier/#0 "close")

top