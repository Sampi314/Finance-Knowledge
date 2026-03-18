# Power Pivot Principles: MAXX with Filter Criteria

**Source:** https://sumproduct.com/blog/power-pivot-principles-maxx-with-filter-criteria/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: MAXX with Filter Criteria

*   April 29, 2019

Power Pivot Principles: MAXX with Filter Criteria
=================================================

Power Pivot Principles: MAXX with Filter Criteria
=================================================

30 April 2019

_Welcome back to our Power Pivot blog. Today, we discuss how to include filters in the MAXX function._

Last week we covered how the **MAXX** functions works, you can read more about it [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-maxx)
.

This week we’d like to expand on the **MAXX** function a little, and how you how we can use other functions that return with a table to alter the **MAXX** function’s results.

For this example, let’s look at the following Table (the capitalisation is deliberate):

![](<Base64-Image-Removed>)

As a quick refresher, the following measure calculates the greatest amount spent on apples:

\=MAXX(

‘AppleSalesCustType’,

‘AppleSalesCustType'\[Price\] \* AppleSalesCustType\[Purchase Volume\]

)

![](<Base64-Image-Removed>)

This measure returns with the value of $690.00, which is the greatest amount spent on apples without any filters.

What we did not cover last week is that the **MAXX** function can work with other functions too. We can use the **FILTER** function to filter out customers that do not fulfil the criterion ‘Customer Type’ = 1.

\=MAXX(

FILTER(

‘AppleSalesCustType’,\[Customer Type\]=1

),

‘AppleSalesCustType'\[Price\] \* AppleSalesCustType\[Purchase Volume\]

)

![](<Base64-Image-Removed>)

The **FILTER** function returns with a **<table>** (quoting the **MAXX** syntax from last week), therefore we are able to use these two functions together. Exporting this to a PivotTable yields the following result:

![](<Base64-Image-Removed>)

The greatest amount spent on apples by customers who fall in the ‘1’ category is $480.00.

That’s it for this week, until next time. Happy Pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-maxx-with-filter-criteria/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-maxx-with-filter-criteria/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-maxx-with-filter-criteria/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-maxx-with-filter-criteria/#0)

[](https://sumproduct.com/blog/power-pivot-principles-maxx-with-filter-criteria/#0 "close")

top