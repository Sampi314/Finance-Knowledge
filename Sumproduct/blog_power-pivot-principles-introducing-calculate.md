# Power Pivot Principles: Introducing CALCULATE

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-calculate/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing CALCULATE

*   May 21, 2018

Power Pivot Principles: Introducing CALCULATE
=============================================

Power Pivot Principles: Introducing CALCULATE
=============================================

22 May 2018

_Welcome back to our Power Pivot blog series. Today we discuss a function that we can use in developing measures._

Any avid Excel user will know the sheer utility you get from the SUMIF function, unfortunately, SUMIF does not work with Power Pivot! Good thing for us there is an alternative – and it is actually _more_ powerful.

The **CALCULATE** function evaluates an expression in a context that is modified by filters. Sounding similar to a famous Excel function namely **SUMIF**? **SUMIF** is not recognised in the Power Pivot programming language (Data Analysis eXpressions, DAX), hence we use the **CALCULATE** function instead.

Similar to **SUMIF**, the syntax for **CALCULATE** is:

**CALCULATE (<expression>, <filter1>, <filter2>, …)**

The filters can be located in any table imported to Power Pivot, as long as the tables have had proper relationships established. The really powerful thing? **CALCULATE** is not “context specific” (_i.e._ the data used does not need to pertain to the row or column headers of the PivotTable) and filters used do not need to be included in the PivotTable either! You can read more about establishing table relationships in this blog [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-relationships)
.

**_Example_**

Let’s create a measure that retrieves the sale for the year of 2014:

![](https://sumproduct.com/wp-content/uploads/2025/05/dbce47720d1f42372c49bb68c1023574.jpg)

We can check that our Calculate filter is working correctly by creating the following PivotTable:

![](https://sumproduct.com/wp-content/uploads/2025/05/ee835934c25d9e928de320331f231ad3.jpg)

As you can see, no matter what the year in each row of the PivotTable the **CALCULATE**\-based measure always relates to 2014 data. We can also apply multiple filters:

![](<Base64-Image-Removed>)

Do note that we are not limited to filter the Calendar Year or Product Category, we can also filter based on Product Types, Weeks, Months, or even Sales Region. Furthermore, applying filters through this method may not be very transparent, so if you wish to apply multiple filters it is recommended that you use filters (but more on this anon).

That’s it for this week, stay tuned to our [blog](https://www.sumproduct.com/blog)
 for more on Power Pivot. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-calculate/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-calculate/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-calculate/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-calculate/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-calculate/#0 "close")

top