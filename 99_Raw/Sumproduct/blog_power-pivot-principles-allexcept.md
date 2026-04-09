# Power Pivot Principles: ALLEXCEPT

**Source:** https://sumproduct.com/blog/power-pivot-principles-allexcept/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: ALLEXCEPT

*   June 18, 2018

Power Pivot Principles: ALLEXCEPT
=================================

Power Pivot Principles: ALLEXCEPT
=================================

19 June 2018

_Welcome back to our Power Pivot blog. Today we discuss how to use the ALLEXCEPT function in DAX._

In our [previous blog](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-all)
 we talked about using the **ALL** function together with the **CALCULATE** function to sum values up that will not be affected by a filter. Here, we turn the idea on its head with the **ALLEXCEPT** function.

As a refresher, the **ALL** function used in conjunction with the **CALCULATE** function:

![](https://sumproduct.com/wp-content/uploads/2025/05/701129649b8f4dcf09ae882df8c255af.jpg)

This will result in a column that always sums the total sales of the product category, no matter what filter is applied to this field. If we wish to subject other fields: _e.g._**ProductKey** and **CustomerKey**, to the **ALL** function we can use a function like this:

**\=CALCULATE(\[Sales\],ALL(Sales\[OrderDate (Month)\],ALL(Sales\[ProductKey\]),ALL(Sales\[CustomerKey\])).**

It’s pretty simple, but the formula may get unnecessarily long quite quickly. This function will ensure that the order date, the product key and the customer key will not be knocked affected by filters on these fields.

But what if we have a table with 30 fields and we don’t want 29 of the fields to be knocked off instead of just three? We would have to write up a formula with 29 **ALL** functions!

This is where we can use the **ALLEXCEPT** function. Consider our **Sales** table once more:

![](https://sumproduct.com/wp-content/uploads/2025/05/964c32d440b0151f3ea2fdf6257c3a7e.jpg)

Let’s say we don’t want to filter any of the fields except for **OrderDate**. We can use the following **CALCULATE** and **ALLEXCEPT** combination:

![](https://sumproduct.com/wp-content/uploads/2025/05/e0904f3edd8f306b93ce77dc4f8a2009.jpg)

This measure will then allow us to filter all of the other fields, except for the Order Date field in the **Sales** table. Do note the difference in syntax, where the **ALLEXCEPT** function requires us to specify the table first before the field:

**ALLEXCEPT(_Table_, _Table\[Field\]_)**

If you think about it, this makes sense. If we are saying we want to only except certain fields we need to specify the set of fields we are talking about – that is, the table.

That’s it for this week, stay tuned to our [blog](https://www.sumproduct.com/blog)
 for more on Power Pivot. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-allexcept/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-allexcept/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-allexcept/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-allexcept/#0)

[](https://sumproduct.com/blog/power-pivot-principles-allexcept/#0 "close")

top