# The A to Z of DAX Functions – ALLEXCEPT

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-allexcept/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ALLEXCEPT

*   August 10, 2021

The A to Z of DAX Functions – ALLEXCEPT
=======================================

Power Pivot Principles: The A to Z of DAX Functions – ALLEXCEPT
===============================================================

10 August 2021

_In our long-established Power Pivot Principles articles, we are starting a new series on the A to Z of Data Analysis eXpression (DAX) functions. This week we look at **ALLEXCEPT**…_

**_The ALLEXCEPT function_**

[Last time](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-az-all)
, we discussed the **ALL** function, together with the **CALCULATE** function, to sum up values that will not be affected by a filter. Here, we turn the idea on its head with the **ALLEXCEPT** function.

As a refresher, the **ALL** function is often used in conjunction with the **CALCULATE** function, _e.g._

![](<Base64-Image-Removed>)

This will result in a column that always sums the total sales of the product category, no matter what filter is applied to this field. If we wish to subject other fields: _e.g._**ProductKey** and **CustomerKey**, to the **ALL** function we can use a function like this:

**\=CALCULATE(\[Sales\],ALL(Sales\[OrderDate (Month)\],ALL(Sales\[ProductKey\]),ALL(Sales\[CustomerKey\])).**

It’s pretty simple, but the formula may get unnecessarily long quite quickly. This function will ensure that the **OrderDate**, the **ProductKey** and the **CustomerKey** will not be knocked affected by filters on these fields.

But what if we have a table with 30 fields and we don’t want 29 of the fields to be knocked off instead of just three? We would have to write up a formula with 29 **ALL** functions!

This is where we can use the **ALLEXCEPT** function. Consider our **Sales** table once more:

![](<Base64-Image-Removed>)

Let’s say we don’t want to filter any of the fields except for **OrderDate**. We can use the following **CALCULATE** and **ALLEXCEPT** combination:

![](<Base64-Image-Removed>)

This measure will then allow us to filter all of the other fields, except for the Order Date field in the **Sales** table. Do note the difference in syntax, where the **ALLEXCEPT** function requires us to specify the table first before the field:

**ALLEXCEPT(Table, Table\[Field\])**

If you think about it, this makes sense. If we are saying we want to only except certain fields we need to specify the set of fields we are talking about – that is, the table.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ _[here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
__._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-allexcept/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-allexcept/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-allexcept/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-allexcept/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-allexcept/#0 "close")

top