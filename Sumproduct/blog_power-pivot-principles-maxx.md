# Power Pivot Principles: MAXX

**Source:** https://sumproduct.com/blog/power-pivot-principles-maxx/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: MAXX

*   April 22, 2019

Power Pivot Principles: MAXX
============================

Power Pivot Principles: MAXX
============================

23 April 2019

_Welcome back to our Power Pivot blog. Today, we discuss how to use the MAXX function._

The **MAXX** function evaluates an expression for each row in a table and returns the largest numeric value as a decimal number. The syntax of this function is:

**MAXX** ( <table> , <expression> )

This means it is useful when you are trying to avoid creating an additional column in a Table to calculate the interim calculations.

For our example, let’s look at the following Table:

![](<Base64-Image-Removed>)

To demonstrate, let’s create a measure using the **MAXX** function to calculate the greatest amount spent on apples. The expression here is a simple multiplication of **‘Apple Sales'\[Price\]** and **‘Apple Sales'\[Purchase Volume\]**:

\=MAXX(

‘Apple Sales’,

‘Apple Sales'\[Price\]\*’Apple Sales'\[Purchase Volume\]

)

In other words, for each row, it is calculating the product of the price and the purchase volume, and then deducing which row creates the highest multiplicative total – _all without having to create an extra column for the interim calculation._

![](<Base64-Image-Removed>)

Exporting this to a PivotTable we shall see…:

![](<Base64-Image-Removed>)

The greatest amount spent on apples is $690.00.

If we drag in the Customer field into the ‘Rows’ area of the Pivot Table:

![](<Base64-Image-Removed>)

We can see that Frank spent the most on apples.

That’s it for this week, tune in next week for more on the **MAXX** function. Happy Pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-maxx/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-maxx/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-maxx/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-maxx/#0)

[](https://sumproduct.com/blog/power-pivot-principles-maxx/#0 "close")

top