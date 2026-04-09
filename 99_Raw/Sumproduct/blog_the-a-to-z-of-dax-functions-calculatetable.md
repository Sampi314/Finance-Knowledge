# The A to Z of DAX Functions – CALCULATETABLE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calculatetable/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CALCULATETABLE

*   November 23, 2021

The A to Z of DAX Functions – CALCULATETABLE
============================================

Power Pivot Principles: The A to Z of DAX Functions – CALCULATETABLE
====================================================================

23 November 2021

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at one of the key functions in DAX: **CALCULATETABLE**._

![](https://sumproduct.com/wp-content/uploads/2025/06/139912db22966be62de3aa10e22d3227.jpg)

_Wrong sort – but you know what we mean!!_

This function is similar to [**CALCULATE**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-az-calculate)
, but in this case, it evaluates a table expression in a modified filter context. Its syntax is as follows:

**CALCULATETABLE(table expression \[, filter1 \[, filter2 \[, …\]\]\])**

It has several arguments:

*   **table expression:** this is required and is the **table****expression** to be evaluated
*   **filter1**, _etc_: these are optional Boolean expressions or table expressions that define filters of filter modifier functions.

The **table expression** used as the first parameter _must_ be a model table or a function that returns a table. Filters may be:

*   Boolean filter expressions
*   filter modification functions
*   table filter expressions.

The last filter, a table expression filter, applies a table object as a filter. It could be a reference to a model table, but more likely it’s a function that returns a table object. You can use the **FILTER** function to apply complex filter conditions, including those that cannot be defined by a Boolean filter expression.

When there are multiple filters, they can be evaluated by using the **AND** (**&&**) logical operator, meaning all conditions must be TRUE, or by the **OR** (**||**) logical operator, meaning either condition can be TRUE.

In case you were wondering, a Boolean expression filter is an expression that evaluates to either TRUE or FALSE. Furthermore, there are several rules that they must abide by:

*   they can reference columns from a single table
*   they cannot reference measures
*   they cannot use a nested **CALCULATE** function.

Beginning with the September 2021 release of Power BI Desktop, the following also apply:

*   they cannot use functions that scan or return a table unless they are passed as arguments to aggregation functions
*   however, they _can_ contain an aggregation function that returns a scalar value.

It should be noted that:

*   when filter expressions are provided, the **CALCULATETABLE** function modifies the filter context to evaluate the expression. For each filter expression, there are two possible standard outcomes when the filter expression is not wrapped in the **KEEPFILTERS** function:
    *   if the columns (or tables) aren’t in the filter context, then new filters will be added to the filter context to evaluate the expression
    *   if the columns (or tables) are already in the filter context, the existing filters will be overwritten by the new filters to evaluate the **CALCULATETABLE** expression

*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

**_Example_**

Let’s create a measure that calculates the sales for division 3 in the year 2020:

**\= CALCULATETABLE(**

        **‘Sales Table’, ‘Calendar Table'\[Year\]=2020**

        **)**

Using the **CALCULATETABLE** formula alone will not work, as Power Pivot will return with the error:

![](<Base64-Image-Removed>)

As it stands above, the current **CALCULATETABLE** measure returns with a table looking like this:

![](<Base64-Image-Removed>)

Power Pivot can’t aggregate an entire table into a single cell. We have to specify which expression we want to be evaluated. We have to use the **SUMX** function. The **SUMX** function ‘returns the sum of an expression evaluated for each row in a table’, it requires the following syntax to operate:

\=**SUMX**(**table**, **expression**)

With that in mind we can adjust our previous measure:

**\= SUMX(**

        **CALCULATETABLE(‘Sales Table’, ‘Calendar Table'\[Year\]=2020)**

               **, \[Division 3\]**

        **)**

The resulting PivotTable:

![](<Base64-Image-Removed>)

Of course, this result can be achieved using the **CALCULATE** function:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

As it stands the **CALCULATETABLE** and the **CALCULATE** functions are quite similar. The key difference is their outputs. We would use the **CALCULATETABLE** function when we need to use other functions that expect a table as an expression and **CALCULATE** when we use functions that expect a single value.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ _[here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
__._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calculatetable/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calculatetable/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calculatetable/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calculatetable/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calculatetable/#0 "close")

top