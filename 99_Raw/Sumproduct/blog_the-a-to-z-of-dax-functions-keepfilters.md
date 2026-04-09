# The A to Z of DAX Functions – KEEPFILTERS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-keepfilters/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – KEEPFILTERS

*   February 17, 2026

The A to Z of DAX Functions – KEEPFILTERS
=========================================

____In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **KEEPFILTERS**.____

**_The_** _**KEEPFILTERS**_ **_function_**

![](<Base64-Image-Removed>)

The **KEEPFILTERS** function is used to modify how filters are applied whilst evaluating a **CALCULATE** or **CALCULATETABLE** function.  It uses the following syntax:

> **KEEPFILTERS(expression)**

There is only one \[1\] argument in this function:

*   **expression**: this argument is required and must be a table expression that defines the filter to apply.

Here are a few remarks about the **KEEPFILTERS** function:

*   **KEEPFILTERS** is use within the context **CALCULATE** and **CALCULATETABLE** functions, to override the standard behaviour of those functions
*   by default, filter arguments in functions such as **CALCULATE** are used as the context for evaluating the expression, and as such, filter arguments for **CALCULATE** replace all existing filters over the same columns.  The new context resulting from the filter argument for **CALCULATE** affects only existing filters on columns mentioned as part of the filter argument.  Filters on columns other than those mentioned in the arguments of **CALCULATE** or other related functions remain in effect and unaltered
*   the **KEEPFILTERS** function allows you to modify this behaviour.  When you use **KEEPFILTERS**, any existing filters in the current context are compared with the columns in the filter arguments, and the intersection of those arguments is used as the context for evaluating the expression.  The net effect over any one column is that both sets of arguments apply: both the filter arguments used in **CALCULATE** and the filters in the arguments of the **KEEPFILTER** function.  In other words, whereas **CALCULATE** filters replace the current context, **KEEPFILTERS** adds filters to the current context
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

As an example, let’s set up a simple Sales table within Power BI:

**Sales =  
DATATABLE (  
 “Product”, STRING,  
** **“Region”, STRING,** **“Amount”, INTEGER,**                           **{**                           **{ “A”, “East”, 100 },**                           **{ “A”, “West”, 50 },**                           **{ “B”, “East”, 80 },**                           **{ “B”, “West”, 20 }**       **}****)**

This code will give you a simple table with three \[3\] columns:

![](<Base64-Image-Removed>)

Then we write two \[2\] separate measure to understand the effect of **KEEPFILTER**S and normal filter context of **CALCULATE** function:

**Sales = (Sales\[Amount\])**

and

**Sales A (KEEPFILTERS) =  
****CALCULATE (  
** **SUM(Sales\[Amount\]),** **KEEPFILTERS ( Sales\[Product\] = “A” )****)**

When we put it in a Card visual, we will have the following:

![](<Base64-Image-Removed>)

This makes sense, since we have 100 sales from product B and 150 sales from product A.  Now let’s added a slicer on this and filter out the product B only:

![](<Base64-Image-Removed>)

The Sales A (**KEEPFILTERS**) became zero \[0\] because right now it has two \[2\] filters applied to it, which filter out Product A only and filter out Product B only.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-keepfilters/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-keepfilters/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-keepfilters/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-keepfilters/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-keepfilters/#0 "close")

top